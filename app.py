import os.path

from aws_cdk.aws_s3_assets import Asset

from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_ecs as ecs,
    core    
)

from aws_cdk.aws_ecr_assets import DockerImageAsset

from aws_cdk.aws_logs import RetentionDays

dirname = os.path.dirname(__file__)


class EC2InstanceStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # VPC
        vpc = ec2.Vpc(self, "VPC",
            nat_gateways=0,
            subnet_configuration=[ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC)]
            )

        # AMI 
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
            )

        # Instance Role and SSM Managed Policy
        role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonEC2RoleforSSM"))

        # Security Group
        security_group = ec2.SecurityGroup(
            self,
            "SecurityGroup",
            vpc=vpc,
            allow_all_outbound=True
        )

        security_group.add_ingress_rule(
            peer=ec2.Peer().ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80)
        )

        # Instance
        instance = ec2.Instance(self, "Instance",
            instance_type=ec2.InstanceType("t3a.micro"),
            machine_image=amzn_linux,
            vpc = vpc,
            role = role,
            security_group = security_group
            )

        # Script in S3 as Asset
        asset = Asset(self, "Asset", path=os.path.join(dirname, "configure.sh"))
        local_path = instance.user_data.add_s3_download_command(
            bucket=asset.bucket,
            bucket_key=asset.s3_object_key
        )

        # Userdata executes script from S3
        instance.user_data.add_execute_file_command(
            file_path=local_path
            )
        asset.grant_read(instance.role)


class JanusCluster(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Janus Image
        janus_asset = DockerImageAsset(self, "JanusBuildImage",
        directory=os.path.join(dirname, "janus-image")
        )

        # VPC
        vpc = ec2.Vpc(self, "VPC",
        nat_gateways=0,
        subnet_configuration=[ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC)]
        )

        # Create an ECS cluster
        cluster = ecs.Cluster(self, "JanusCluster",
        vpc=vpc
        )

        #Task definition
        task_definition = ecs.FargateTaskDefinition(self, 'JanusTask')

        task_definition.add_container("Janus",
        image=ecs.ContainerImage.from_docker_image_asset(janus_asset),
        cpu=256,
        memory_limit_mib=512,
        logging=ecs.LogDriver.aws_logs(
            stream_prefix='JanusTask',
            log_retention=RetentionDays("ONE_DAY")
        ),
        health_check=ecs.HealthCheck(command=[
                "CMD-SHELL", "curl -fs http://localhost:7088/admin | grep error"])
        )

        #Service
        ecs.FargateService(self, 'JanusService',
        cluster=cluster,
        task_definition=task_definition,
        desired_count=1)


app = core.App()
#EC2InstanceStack(app, "ec2-instance")
JanusCluster(app, "janus-cluster")
app.synth()