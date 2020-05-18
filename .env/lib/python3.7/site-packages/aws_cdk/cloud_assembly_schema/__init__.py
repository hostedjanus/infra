"""
## Cloud Assembly Schema

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Cloud Assembly

The *Cloud Assembly* is the output of the synthesis operation. It is produced as part of the
[`cdk synth`](https://github.com/aws/aws-cdk/tree/master/packages/aws-cdk#cdk-synthesize)
command, or the [`app.synth()`](https://github.com/aws/aws-cdk/blob/master/packages/@aws-cdk/core/lib/app.ts#L135) method invocation.

Its essentially a set of files and directories, one of which is the `manifest.json` file. It defines the set of instructions that are
needed in order to deploy the assembly directory.

> For example, when `cdk deploy` is executed, the CLI reads this file and performs its instructions:
>
> * Build container images.
> * Upload assets.
> * Deploy CloudFormation templates.

Therefore, the assembly is how the CDK class library and CDK CLI (or any other consumer) communicate. To ensure compatibility
between the assembly and its consumers, we treat the manifest file as a well defined, versioned schema.

## Schema

This module contains the typescript structs that comprise the `manifest.json` file, as well as the
generated [*json-schema*](./schema/cloud-assembly.schema.json).

## Versioning

The schema version is specified in the [`cloud-assembly.version.json`](./schema/cloud-assembly.schema.json) file, under the `version` property.
It follows semantic versioning, but with a small twist.

When we add instructions to the assembly, they are reflected in the manifest file and the *json-schema* accordingly.
Every such instruction, is crucial for ensuring the correct deployment behavior. This means that to properly deploy a cloud assembly,
consumers must be aware of every such instruction modification.

For this reason, every change to the schema, even though it might not strictly break validation of the *json-schema* format,
is considered `major` version bump.

## How to consume

If you'd like to consume the [schema file](./schema/cloud-assembly.schema.json) in order to do validations on `manifest.json` files,
simply download it from this repo and run it against standard *json-schema* validators, such as [jsonschema](https://www.npmjs.com/package/jsonschema).

Consumers must take into account the `major` version of the schema they are consuming. They should reject cloud assemblies
with a `major` version that is higher than what they expect. While schema validation might pass on such assemblies, the deployment integrity
cannot be guaranteed because some instructions will be ignored.

> For example, if your consumer was built when the schema version was 2.0.0, you should reject deploying cloud assemblies with a
> manifest version of 3.0.0.

## Contributing

See [Contribution Guide](./CONTRIBUTING.md)
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from ._jsii import *


@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.AmiContextQuery", jsii_struct_bases=[], name_mapping={'account': 'account', 'filters': 'filters', 'region': 'region', 'owners': 'owners'})
class AmiContextQuery():
    def __init__(self, *, account: str, filters: typing.Mapping[str, typing.List[str]], region: str, owners: typing.Optional[typing.List[str]]=None) -> None:
        """Query to AMI context provider.

        :param account: Account to query.
        :param filters: Filters to DescribeImages call.
        :param region: Region to query.
        :param owners: Owners to DescribeImages call. Default: - All owners
        """
        self._values = {
            'account': account,
            'filters': filters,
            'region': region,
        }
        if owners is not None: self._values["owners"] = owners

    @builtins.property
    def account(self) -> str:
        """Account to query."""
        return self._values.get('account')

    @builtins.property
    def filters(self) -> typing.Mapping[str, typing.List[str]]:
        """Filters to DescribeImages call."""
        return self._values.get('filters')

    @builtins.property
    def region(self) -> str:
        """Region to query."""
        return self._values.get('region')

    @builtins.property
    def owners(self) -> typing.Optional[typing.List[str]]:
        """Owners to DescribeImages call.

        default
        :default: - All owners
        """
        return self._values.get('owners')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AmiContextQuery(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.ArtifactManifest", jsii_struct_bases=[], name_mapping={'type': 'type', 'dependencies': 'dependencies', 'environment': 'environment', 'metadata': 'metadata', 'properties': 'properties'})
class ArtifactManifest():
    def __init__(self, *, type: "ArtifactType", dependencies: typing.Optional[typing.List[str]]=None, environment: typing.Optional[str]=None, metadata: typing.Optional[typing.Mapping[str, typing.List["MetadataEntry"]]]=None, properties: typing.Optional[typing.Mapping[str, typing.Any]]=None) -> None:
        """A manifest for a single artifact within the cloud assembly.

        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.
        """
        self._values = {
            'type': type,
        }
        if dependencies is not None: self._values["dependencies"] = dependencies
        if environment is not None: self._values["environment"] = environment
        if metadata is not None: self._values["metadata"] = metadata
        if properties is not None: self._values["properties"] = properties

    @builtins.property
    def type(self) -> "ArtifactType":
        """The type of artifact."""
        return self._values.get('type')

    @builtins.property
    def dependencies(self) -> typing.Optional[typing.List[str]]:
        """IDs of artifacts that must be deployed before this artifact.

        default
        :default: - no dependencies.
        """
        return self._values.get('dependencies')

    @builtins.property
    def environment(self) -> typing.Optional[str]:
        """The environment into which this artifact is deployed.

        default
        :default: - no envrionment.
        """
        return self._values.get('environment')

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[str, typing.List["MetadataEntry"]]]:
        """Associated metadata.

        default
        :default: - no metadata.
        """
        return self._values.get('metadata')

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[str, typing.Any]]:
        """The set of properties for this artifact (depends on type).

        default
        :default: - no properties.
        """
        return self._values.get('properties')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ArtifactManifest(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/cloud-assembly-schema.ArtifactMetadataEntryType")
class ArtifactMetadataEntryType(enum.Enum):
    """Type of artifact metadata entry."""
    ASSET = "ASSET"
    """Asset in metadata."""
    INFO = "INFO"
    """Metadata key used to print INFO-level messages by the toolkit when an app is syntheized."""
    WARN = "WARN"
    """Metadata key used to print WARNING-level messages by the toolkit when an app is syntheized."""
    ERROR = "ERROR"
    """Metadata key used to print ERROR-level messages by the toolkit when an app is syntheized."""
    LOGICAL_ID = "LOGICAL_ID"
    """Represents the CloudFormation logical ID of a resource at a certain path."""
    STACK_TAGS = "STACK_TAGS"
    """Represents tags of a stack."""

@jsii.enum(jsii_type="@aws-cdk/cloud-assembly-schema.ArtifactType")
class ArtifactType(enum.Enum):
    """Type of cloud artifact."""
    NONE = "NONE"
    """Stub required because of JSII."""
    AWS_CLOUDFORMATION_STACK = "AWS_CLOUDFORMATION_STACK"
    """The artifact is an AWS CloudFormation stack."""
    CDK_TREE = "CDK_TREE"
    """The artifact contains the CDK application's construct tree."""

@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.AssemblyManifest", jsii_struct_bases=[], name_mapping={'version': 'version', 'artifacts': 'artifacts', 'missing': 'missing', 'runtime': 'runtime'})
class AssemblyManifest():
    def __init__(self, *, version: str, artifacts: typing.Optional[typing.Mapping[str, "ArtifactManifest"]]=None, missing: typing.Optional[typing.List["MissingContext"]]=None, runtime: typing.Optional["RuntimeInfo"]=None) -> None:
        """A manifest which describes the cloud assembly.

        :param version: Protocol version.
        :param artifacts: The set of artifacts in this assembly. Default: - no artifacts.
        :param missing: Missing context information. If this field has values, it means that the cloud assembly is not complete and should not be deployed. Default: - no missing context.
        :param runtime: Runtime information. Default: - no info.
        """
        if isinstance(runtime, dict): runtime = RuntimeInfo(**runtime)
        self._values = {
            'version': version,
        }
        if artifacts is not None: self._values["artifacts"] = artifacts
        if missing is not None: self._values["missing"] = missing
        if runtime is not None: self._values["runtime"] = runtime

    @builtins.property
    def version(self) -> str:
        """Protocol version."""
        return self._values.get('version')

    @builtins.property
    def artifacts(self) -> typing.Optional[typing.Mapping[str, "ArtifactManifest"]]:
        """The set of artifacts in this assembly.

        default
        :default: - no artifacts.
        """
        return self._values.get('artifacts')

    @builtins.property
    def missing(self) -> typing.Optional[typing.List["MissingContext"]]:
        """Missing context information.

        If this field has values, it means that the
        cloud assembly is not complete and should not be deployed.

        default
        :default: - no missing context.
        """
        return self._values.get('missing')

    @builtins.property
    def runtime(self) -> typing.Optional["RuntimeInfo"]:
        """Runtime information.

        default
        :default: - no info.
        """
        return self._values.get('runtime')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AssemblyManifest(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.AvailabilityZonesContextQuery", jsii_struct_bases=[], name_mapping={'account': 'account', 'region': 'region'})
class AvailabilityZonesContextQuery():
    def __init__(self, *, account: str, region: str) -> None:
        """Query to availability zone context provider.

        :param account: Query account.
        :param region: Query region.
        """
        self._values = {
            'account': account,
            'region': region,
        }

    @builtins.property
    def account(self) -> str:
        """Query account."""
        return self._values.get('account')

    @builtins.property
    def region(self) -> str:
        """Query region."""
        return self._values.get('region')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AvailabilityZonesContextQuery(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.ContainerImageAssetMetadataEntry", jsii_struct_bases=[], name_mapping={'id': 'id', 'packaging': 'packaging', 'path': 'path', 'source_hash': 'sourceHash', 'build_args': 'buildArgs', 'file': 'file', 'image_name_parameter': 'imageNameParameter', 'image_tag': 'imageTag', 'repository_name': 'repositoryName', 'target': 'target'})
class ContainerImageAssetMetadataEntry():
    def __init__(self, *, id: str, packaging: str, path: str, source_hash: str, build_args: typing.Optional[typing.Mapping[str, str]]=None, file: typing.Optional[str]=None, image_name_parameter: typing.Optional[str]=None, image_tag: typing.Optional[str]=None, repository_name: typing.Optional[str]=None, target: typing.Optional[str]=None) -> None:
        """Metadata Entry spec for container images.

        :param id: Logical identifier for the asset.
        :param packaging: Type of asset.
        :param path: Path on disk to the asset.
        :param source_hash: The hash of the asset source.
        :param build_args: Build args to pass to the ``docker build`` command. Default: no build args are passed
        :param file: Path to the Dockerfile (relative to the directory). Default: - no file is passed
        :param image_name_parameter: ECR Repository name and repo digest (separated by "@sha256:") where this image is stored. Default: undefined If not specified, ``repositoryName`` and ``imageTag`` are required because otherwise how will the stack know where to find the asset, ha?
        :param image_tag: The docker image tag to use for tagging pushed images. This field is required if ``imageParameterName`` is ommited (otherwise, the app won't be able to find the image). Default: - this parameter is REQUIRED after 1.21.0
        :param repository_name: ECR repository name, if omitted a default name based on the asset's ID is used instead. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - this parameter is REQUIRED after 1.21.0
        :param target: Docker target to build to. Default: no build target
        """
        self._values = {
            'id': id,
            'packaging': packaging,
            'path': path,
            'source_hash': source_hash,
        }
        if build_args is not None: self._values["build_args"] = build_args
        if file is not None: self._values["file"] = file
        if image_name_parameter is not None: self._values["image_name_parameter"] = image_name_parameter
        if image_tag is not None: self._values["image_tag"] = image_tag
        if repository_name is not None: self._values["repository_name"] = repository_name
        if target is not None: self._values["target"] = target

    @builtins.property
    def id(self) -> str:
        """Logical identifier for the asset."""
        return self._values.get('id')

    @builtins.property
    def packaging(self) -> str:
        """Type of asset."""
        return self._values.get('packaging')

    @builtins.property
    def path(self) -> str:
        """Path on disk to the asset."""
        return self._values.get('path')

    @builtins.property
    def source_hash(self) -> str:
        """The hash of the asset source."""
        return self._values.get('source_hash')

    @builtins.property
    def build_args(self) -> typing.Optional[typing.Mapping[str, str]]:
        """Build args to pass to the ``docker build`` command.

        default
        :default: no build args are passed
        """
        return self._values.get('build_args')

    @builtins.property
    def file(self) -> typing.Optional[str]:
        """Path to the Dockerfile (relative to the directory).

        default
        :default: - no file is passed
        """
        return self._values.get('file')

    @builtins.property
    def image_name_parameter(self) -> typing.Optional[str]:
        """ECR Repository name and repo digest (separated by "@sha256:") where this image is stored.

        default
        :default:

        undefined If not specified, ``repositoryName`` and ``imageTag`` are
        required because otherwise how will the stack know where to find the asset,
        ha?

        deprecated
        :deprecated:

        specify ``repositoryName`` and ``imageTag`` instead, and then you
        know where the image will go.

        stability
        :stability: deprecated
        """
        return self._values.get('image_name_parameter')

    @builtins.property
    def image_tag(self) -> typing.Optional[str]:
        """The docker image tag to use for tagging pushed images.

        This field is
        required if ``imageParameterName`` is ommited (otherwise, the app won't be
        able to find the image).

        default
        :default: - this parameter is REQUIRED after 1.21.0
        """
        return self._values.get('image_tag')

    @builtins.property
    def repository_name(self) -> typing.Optional[str]:
        """ECR repository name, if omitted a default name based on the asset's ID is used instead.

        Specify this property if you need to statically address the
        image, e.g. from a Kubernetes Pod. Note, this is only the repository name,
        without the registry and the tag parts.

        default
        :default: - this parameter is REQUIRED after 1.21.0
        """
        return self._values.get('repository_name')

    @builtins.property
    def target(self) -> typing.Optional[str]:
        """Docker target to build to.

        default
        :default: no build target
        """
        return self._values.get('target')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ContainerImageAssetMetadataEntry(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/cloud-assembly-schema.ContextProvider")
class ContextProvider(enum.Enum):
    """Identifier for the context provider."""
    AMI_PROVIDER = "AMI_PROVIDER"
    """AMI provider."""
    AVAILABILITY_ZONE_PROVIDER = "AVAILABILITY_ZONE_PROVIDER"
    """AZ provider."""
    HOSTED_ZONE_PROVIDER = "HOSTED_ZONE_PROVIDER"
    """Route53 Hosted Zone provider."""
    SSM_PARAMETER_PROVIDER = "SSM_PARAMETER_PROVIDER"
    """SSM Parameter Provider."""
    VPC_PROVIDER = "VPC_PROVIDER"
    """VPC Provider."""

@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.FileAssetMetadataEntry", jsii_struct_bases=[], name_mapping={'artifact_hash_parameter': 'artifactHashParameter', 'id': 'id', 'packaging': 'packaging', 'path': 'path', 's3_bucket_parameter': 's3BucketParameter', 's3_key_parameter': 's3KeyParameter', 'source_hash': 'sourceHash'})
class FileAssetMetadataEntry():
    def __init__(self, *, artifact_hash_parameter: str, id: str, packaging: str, path: str, s3_bucket_parameter: str, s3_key_parameter: str, source_hash: str) -> None:
        """Metadata Entry spec for files.

        :param artifact_hash_parameter: The name of the parameter where the hash of the bundled asset should be passed in.
        :param id: Logical identifier for the asset.
        :param packaging: Requested packaging style.
        :param path: Path on disk to the asset.
        :param s3_bucket_parameter: Name of parameter where S3 bucket should be passed in.
        :param s3_key_parameter: Name of parameter where S3 key should be passed in.
        :param source_hash: The hash of the asset source.
        """
        self._values = {
            'artifact_hash_parameter': artifact_hash_parameter,
            'id': id,
            'packaging': packaging,
            'path': path,
            's3_bucket_parameter': s3_bucket_parameter,
            's3_key_parameter': s3_key_parameter,
            'source_hash': source_hash,
        }

    @builtins.property
    def artifact_hash_parameter(self) -> str:
        """The name of the parameter where the hash of the bundled asset should be passed in."""
        return self._values.get('artifact_hash_parameter')

    @builtins.property
    def id(self) -> str:
        """Logical identifier for the asset."""
        return self._values.get('id')

    @builtins.property
    def packaging(self) -> str:
        """Requested packaging style."""
        return self._values.get('packaging')

    @builtins.property
    def path(self) -> str:
        """Path on disk to the asset."""
        return self._values.get('path')

    @builtins.property
    def s3_bucket_parameter(self) -> str:
        """Name of parameter where S3 bucket should be passed in."""
        return self._values.get('s3_bucket_parameter')

    @builtins.property
    def s3_key_parameter(self) -> str:
        """Name of parameter where S3 key should be passed in."""
        return self._values.get('s3_key_parameter')

    @builtins.property
    def source_hash(self) -> str:
        """The hash of the asset source."""
        return self._values.get('source_hash')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'FileAssetMetadataEntry(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.HostedZoneContextQuery", jsii_struct_bases=[], name_mapping={'account': 'account', 'domain_name': 'domainName', 'region': 'region', 'private_zone': 'privateZone', 'vpc_id': 'vpcId'})
class HostedZoneContextQuery():
    def __init__(self, *, account: str, domain_name: str, region: str, private_zone: typing.Optional[bool]=None, vpc_id: typing.Optional[str]=None) -> None:
        """Query to hosted zone context provider.

        :param account: Query account.
        :param domain_name: The domain name e.g. example.com to lookup.
        :param region: Query region.
        :param private_zone: True if the zone you want to find is a private hosted zone. Default: false
        :param vpc_id: The VPC ID to that the private zone must be associated with. If you provide VPC ID and privateZone is false, this will return no results and raise an error. Default: - Required if privateZone=true
        """
        self._values = {
            'account': account,
            'domain_name': domain_name,
            'region': region,
        }
        if private_zone is not None: self._values["private_zone"] = private_zone
        if vpc_id is not None: self._values["vpc_id"] = vpc_id

    @builtins.property
    def account(self) -> str:
        """Query account."""
        return self._values.get('account')

    @builtins.property
    def domain_name(self) -> str:
        """The domain name e.g. example.com to lookup."""
        return self._values.get('domain_name')

    @builtins.property
    def region(self) -> str:
        """Query region."""
        return self._values.get('region')

    @builtins.property
    def private_zone(self) -> typing.Optional[bool]:
        """True if the zone you want to find is a private hosted zone.

        default
        :default: false
        """
        return self._values.get('private_zone')

    @builtins.property
    def vpc_id(self) -> typing.Optional[str]:
        """The VPC ID to that the private zone must be associated with.

        If you provide VPC ID and privateZone is false, this will return no results
        and raise an error.

        default
        :default: - Required if privateZone=true
        """
        return self._values.get('vpc_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'HostedZoneContextQuery(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class Manifest(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/cloud-assembly-schema.Manifest"):
    """Protocol utility class."""
    @jsii.member(jsii_name="load")
    @builtins.classmethod
    def load(cls, file_path: str) -> "AssemblyManifest":
        """Load manifest from file.

        :param file_path: - path to the manifest file.
        """
        return jsii.sinvoke(cls, "load", [file_path])

    @jsii.member(jsii_name="save")
    @builtins.classmethod
    def save(cls, manifest: "AssemblyManifest", file_path: str) -> None:
        """Save manifest to file.

        :param manifest: - manifest.
        :param file_path: -
        """
        return jsii.sinvoke(cls, "save", [manifest, file_path])

    @jsii.member(jsii_name="version")
    @builtins.classmethod
    def version(cls) -> str:
        """Fetch the current schema version number."""
        return jsii.sinvoke(cls, "version", [])


@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.MetadataEntry", jsii_struct_bases=[], name_mapping={'type': 'type', 'data': 'data', 'trace': 'trace'})
class MetadataEntry():
    def __init__(self, *, type: str, data: typing.Optional[typing.Union[typing.Optional[str], typing.Optional["FileAssetMetadataEntry"], typing.Optional["ContainerImageAssetMetadataEntry"], typing.Optional[typing.List["Tag"]]]]=None, trace: typing.Optional[typing.List[str]]=None) -> None:
        """A metadata entry in a cloud assembly artifact.

        :param type: The type of the metadata entry.
        :param data: The data. Default: - no data.
        :param trace: A stack trace for when the entry was created. Default: - no trace.
        """
        self._values = {
            'type': type,
        }
        if data is not None: self._values["data"] = data
        if trace is not None: self._values["trace"] = trace

    @builtins.property
    def type(self) -> str:
        """The type of the metadata entry."""
        return self._values.get('type')

    @builtins.property
    def data(self) -> typing.Optional[typing.Union[typing.Optional[str], typing.Optional["FileAssetMetadataEntry"], typing.Optional["ContainerImageAssetMetadataEntry"], typing.Optional[typing.List["Tag"]]]]:
        """The data.

        default
        :default: - no data.
        """
        return self._values.get('data')

    @builtins.property
    def trace(self) -> typing.Optional[typing.List[str]]:
        """A stack trace for when the entry was created.

        default
        :default: - no trace.
        """
        return self._values.get('trace')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'MetadataEntry(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.MissingContext", jsii_struct_bases=[], name_mapping={'key': 'key', 'props': 'props', 'provider': 'provider'})
class MissingContext():
    def __init__(self, *, key: str, props: typing.Union["AmiContextQuery", "AvailabilityZonesContextQuery", "HostedZoneContextQuery", "SSMParameterContextQuery", "VpcContextQuery"], provider: "ContextProvider") -> None:
        """Represents a missing piece of context.

        :param key: The missing context key.
        :param props: A set of provider-specific options.
        :param provider: The provider from which we expect this context key to be obtained.
        """
        self._values = {
            'key': key,
            'props': props,
            'provider': provider,
        }

    @builtins.property
    def key(self) -> str:
        """The missing context key."""
        return self._values.get('key')

    @builtins.property
    def props(self) -> typing.Union["AmiContextQuery", "AvailabilityZonesContextQuery", "HostedZoneContextQuery", "SSMParameterContextQuery", "VpcContextQuery"]:
        """A set of provider-specific options."""
        return self._values.get('props')

    @builtins.property
    def provider(self) -> "ContextProvider":
        """The provider from which we expect this context key to be obtained."""
        return self._values.get('provider')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'MissingContext(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.RuntimeInfo", jsii_struct_bases=[], name_mapping={'libraries': 'libraries'})
class RuntimeInfo():
    def __init__(self, *, libraries: typing.Mapping[str, str]) -> None:
        """Information about the application's runtime components.

        :param libraries: The list of libraries loaded in the application, associated with their versions.
        """
        self._values = {
            'libraries': libraries,
        }

    @builtins.property
    def libraries(self) -> typing.Mapping[str, str]:
        """The list of libraries loaded in the application, associated with their versions."""
        return self._values.get('libraries')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'RuntimeInfo(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.SSMParameterContextQuery", jsii_struct_bases=[], name_mapping={'account': 'account', 'parameter_name': 'parameterName', 'region': 'region'})
class SSMParameterContextQuery():
    def __init__(self, *, account: str, parameter_name: str, region: str) -> None:
        """Query to SSM Parameter Context Provider.

        :param account: Query account.
        :param parameter_name: Parameter name to query.
        :param region: Query region.
        """
        self._values = {
            'account': account,
            'parameter_name': parameter_name,
            'region': region,
        }

    @builtins.property
    def account(self) -> str:
        """Query account."""
        return self._values.get('account')

    @builtins.property
    def parameter_name(self) -> str:
        """Parameter name to query."""
        return self._values.get('parameter_name')

    @builtins.property
    def region(self) -> str:
        """Query region."""
        return self._values.get('region')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SSMParameterContextQuery(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.Tag", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
class Tag():
    def __init__(self, *, key: str, value: str) -> None:
        """Metadata Entry spec for stack tag.

        :param key: Tag key.
        :param value: Tag value.
        """
        self._values = {
            'key': key,
            'value': value,
        }

    @builtins.property
    def key(self) -> str:
        """Tag key."""
        return self._values.get('key')

    @builtins.property
    def value(self) -> str:
        """Tag value."""
        return self._values.get('value')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'Tag(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cloud-assembly-schema.VpcContextQuery", jsii_struct_bases=[], name_mapping={'account': 'account', 'filter': 'filter', 'region': 'region', 'return_asymmetric_subnets': 'returnAsymmetricSubnets', 'subnet_group_name_tag': 'subnetGroupNameTag'})
class VpcContextQuery():
    def __init__(self, *, account: str, filter: typing.Mapping[str, str], region: str, return_asymmetric_subnets: typing.Optional[bool]=None, subnet_group_name_tag: typing.Optional[str]=None) -> None:
        """Query input for looking up a VPC.

        :param account: Query account.
        :param filter: Filters to apply to the VPC. Filter parameters are the same as passed to DescribeVpcs.
        :param region: Query region.
        :param return_asymmetric_subnets: Whether to populate the subnetGroups field of the {@link VpcContextResponse}, which contains potentially asymmetric subnet groups. Default: false
        :param subnet_group_name_tag: Optional tag for subnet group name. If not provided, we'll look at the aws-cdk:subnet-name tag. If the subnet does not have the specified tag, we'll use its type as the name. Default: 'aws-cdk:subnet-name'
        """
        self._values = {
            'account': account,
            'filter': filter,
            'region': region,
        }
        if return_asymmetric_subnets is not None: self._values["return_asymmetric_subnets"] = return_asymmetric_subnets
        if subnet_group_name_tag is not None: self._values["subnet_group_name_tag"] = subnet_group_name_tag

    @builtins.property
    def account(self) -> str:
        """Query account."""
        return self._values.get('account')

    @builtins.property
    def filter(self) -> typing.Mapping[str, str]:
        """Filters to apply to the VPC.

        Filter parameters are the same as passed to DescribeVpcs.

        see
        :see: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html
        """
        return self._values.get('filter')

    @builtins.property
    def region(self) -> str:
        """Query region."""
        return self._values.get('region')

    @builtins.property
    def return_asymmetric_subnets(self) -> typing.Optional[bool]:
        """Whether to populate the subnetGroups field of the {@link VpcContextResponse}, which contains potentially asymmetric subnet groups.

        default
        :default: false
        """
        return self._values.get('return_asymmetric_subnets')

    @builtins.property
    def subnet_group_name_tag(self) -> typing.Optional[str]:
        """Optional tag for subnet group name.

        If not provided, we'll look at the aws-cdk:subnet-name tag.
        If the subnet does not have the specified tag,
        we'll use its type as the name.

        default
        :default: 'aws-cdk:subnet-name'
        """
        return self._values.get('subnet_group_name_tag')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'VpcContextQuery(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = [
    "AmiContextQuery",
    "ArtifactManifest",
    "ArtifactMetadataEntryType",
    "ArtifactType",
    "AssemblyManifest",
    "AvailabilityZonesContextQuery",
    "ContainerImageAssetMetadataEntry",
    "ContextProvider",
    "FileAssetMetadataEntry",
    "HostedZoneContextQuery",
    "Manifest",
    "MetadataEntry",
    "MissingContext",
    "RuntimeInfo",
    "SSMParameterContextQuery",
    "Tag",
    "VpcContextQuery",
]

publication.publish()
