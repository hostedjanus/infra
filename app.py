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

        # Create a security group
        security_group = ec2.SecurityGroup(self, "JanusSecurityGroup",
        vpc=vpc,
        allow_all_outbound=True
        )

        security_group.add_ingress_rule(peer=ec2.Peer.any_ipv4(), connection=ec2.Port.tcp(8088), description="Janus")

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
        ecs_service = ecs.FargateService(self, 'JanusService',
        cluster=cluster,
        task_definition=task_definition,
        desired_count=1,
        assign_public_ip=True,
        security_group=security_group,
        enable_execute_command=True)


app = core.App()
JanusCluster(app, "janus-cluster")
app.synth()