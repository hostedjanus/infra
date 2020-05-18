"""
## Cloud Executable API

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development. They are subject to non-backward compatible changes or removal in any future version. These are not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be announced in the release notes. This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.cloud_assembly_schema

from ._jsii import *


@jsii.data_type(jsii_type="@aws-cdk/cx-api.AssemblyBuildOptions", jsii_struct_bases=[], name_mapping={'runtime_info': 'runtimeInfo'})
class AssemblyBuildOptions():
    def __init__(self, *, runtime_info: typing.Optional["RuntimeInfo"]=None) -> None:
        """
        :param runtime_info: Include the specified runtime information (module versions) in manifest. Default: - if this option is not specified, runtime info will not be included

        stability
        :stability: experimental
        """
        if isinstance(runtime_info, dict): runtime_info = RuntimeInfo(**runtime_info)
        self._values = {
        }
        if runtime_info is not None: self._values["runtime_info"] = runtime_info

    @builtins.property
    def runtime_info(self) -> typing.Optional["RuntimeInfo"]:
        """Include the specified runtime information (module versions) in manifest.

        default
        :default: - if this option is not specified, runtime info will not be included

        stability
        :stability: experimental
        """
        return self._values.get('runtime_info')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AssemblyBuildOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cx-api.AwsCloudFormationStackProperties", jsii_struct_bases=[], name_mapping={'template_file': 'templateFile', 'parameters': 'parameters', 'stack_name': 'stackName', 'termination_protection': 'terminationProtection'})
class AwsCloudFormationStackProperties():
    def __init__(self, *, template_file: str, parameters: typing.Optional[typing.Mapping[str, str]]=None, stack_name: typing.Optional[str]=None, termination_protection: typing.Optional[bool]=None) -> None:
        """Artifact properties for CloudFormation stacks.

        :param template_file: A file relative to the assembly root which contains the CloudFormation template for this stack.
        :param parameters: Values for CloudFormation stack parameters that should be passed when the stack is deployed.
        :param stack_name: The name to use for the CloudFormation stack. Default: - name derived from artifact ID
        :param termination_protection: Whether to enable termination protection for this stack. Default: false

        stability
        :stability: experimental
        """
        self._values = {
            'template_file': template_file,
        }
        if parameters is not None: self._values["parameters"] = parameters
        if stack_name is not None: self._values["stack_name"] = stack_name
        if termination_protection is not None: self._values["termination_protection"] = termination_protection

    @builtins.property
    def template_file(self) -> str:
        """A file relative to the assembly root which contains the CloudFormation template for this stack.

        stability
        :stability: experimental
        """
        return self._values.get('template_file')

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[str, str]]:
        """Values for CloudFormation stack parameters that should be passed when the stack is deployed.

        stability
        :stability: experimental
        """
        return self._values.get('parameters')

    @builtins.property
    def stack_name(self) -> typing.Optional[str]:
        """The name to use for the CloudFormation stack.

        default
        :default: - name derived from artifact ID

        stability
        :stability: experimental
        """
        return self._values.get('stack_name')

    @builtins.property
    def termination_protection(self) -> typing.Optional[bool]:
        """Whether to enable termination protection for this stack.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get('termination_protection')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AwsCloudFormationStackProperties(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CloudArtifact(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/cx-api.CloudArtifact"):
    """Represents an artifact within a cloud assembly.

    stability
    :stability: experimental
    """
    def __init__(self, assembly: "CloudAssembly", id: str, *, type: aws_cdk.cloud_assembly_schema.ArtifactType, dependencies: typing.Optional[typing.List[str]]=None, environment: typing.Optional[str]=None, metadata: typing.Optional[typing.Mapping[str, typing.List[aws_cdk.cloud_assembly_schema.MetadataEntry]]]=None, properties: typing.Optional[typing.Mapping[str, typing.Any]]=None) -> None:
        """
        :param assembly: -
        :param id: -
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.

        stability
        :stability: experimental
        """
        manifest = aws_cdk.cloud_assembly_schema.ArtifactManifest(type=type, dependencies=dependencies, environment=environment, metadata=metadata, properties=properties)

        jsii.create(CloudArtifact, self, [assembly, id, manifest])

    @jsii.member(jsii_name="fromManifest")
    @builtins.classmethod
    def from_manifest(cls, assembly: "CloudAssembly", id: str, *, type: aws_cdk.cloud_assembly_schema.ArtifactType, dependencies: typing.Optional[typing.List[str]]=None, environment: typing.Optional[str]=None, metadata: typing.Optional[typing.Mapping[str, typing.List[aws_cdk.cloud_assembly_schema.MetadataEntry]]]=None, properties: typing.Optional[typing.Mapping[str, typing.Any]]=None) -> typing.Optional["CloudArtifact"]:
        """Returns a subclass of ``CloudArtifact`` based on the artifact type defined in the artifact manifest.

        :param assembly: The cloud assembly from which to load the artifact.
        :param id: The artifact ID.
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.

        return
        :return: the ``CloudArtifact`` that matches the artifact type or ``undefined`` if it's an artifact type that is unrecognized by this module.

        stability
        :stability: experimental
        """
        artifact = aws_cdk.cloud_assembly_schema.ArtifactManifest(type=type, dependencies=dependencies, environment=environment, metadata=metadata, properties=properties)

        return jsii.sinvoke(cls, "fromManifest", [assembly, id, artifact])

    @jsii.member(jsii_name="findMetadataByType")
    def find_metadata_by_type(self, type: str) -> typing.List["MetadataEntryResult"]:
        """
        :param type: -

        return
        :return: all the metadata entries of a specific type in this artifact.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "findMetadataByType", [type])

    @builtins.property
    @jsii.member(jsii_name="assembly")
    def assembly(self) -> "CloudAssembly":
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "assembly")

    @builtins.property
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.List["CloudArtifact"]:
        """Returns all the artifacts that this artifact depends on.

        stability
        :stability: experimental
        """
        return jsii.get(self, "dependencies")

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "id")

    @builtins.property
    @jsii.member(jsii_name="manifest")
    def manifest(self) -> aws_cdk.cloud_assembly_schema.ArtifactManifest:
        """The artifact's manifest.

        stability
        :stability: experimental
        """
        return jsii.get(self, "manifest")

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(self) -> typing.List["SynthesisMessage"]:
        """The set of messages extracted from the artifact's metadata.

        stability
        :stability: experimental
        """
        return jsii.get(self, "messages")


class CloudAssembly(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/cx-api.CloudAssembly"):
    """Represents a deployable cloud application.

    stability
    :stability: experimental
    """
    def __init__(self, directory: str) -> None:
        """Reads a cloud assembly from the specified directory.

        :param directory: The root directory of the assembly.

        stability
        :stability: experimental
        """
        jsii.create(CloudAssembly, self, [directory])

    @jsii.member(jsii_name="getStack")
    def get_stack(self, stack_name: str) -> "CloudFormationStackArtifact":
        """Returns a CloudFormation stack artifact by name from this assembly.

        :param stack_name: -

        deprecated
        :deprecated: renamed to ``getStackByName`` (or ``getStackArtifact(id)``)

        stability
        :stability: deprecated
        """
        return jsii.invoke(self, "getStack", [stack_name])

    @jsii.member(jsii_name="getStackArtifact")
    def get_stack_artifact(self, artifact_id: str) -> "CloudFormationStackArtifact":
        """Returns a CloudFormation stack artifact from this assembly.

        :param artifact_id: the artifact id of the stack (can be obtained through ``stack.artifactId``).

        return
        :return: a ``CloudFormationStackArtifact`` object.

        stability
        :stability: experimental
        throws:
        :throws:: if there is no stack artifact with that id
        """
        return jsii.invoke(self, "getStackArtifact", [artifact_id])

    @jsii.member(jsii_name="getStackByName")
    def get_stack_by_name(self, stack_name: str) -> "CloudFormationStackArtifact":
        """Returns a CloudFormation stack artifact from this assembly.

        :param stack_name: the name of the CloudFormation stack.

        return
        :return: a ``CloudFormationStackArtifact`` object.

        stability
        :stability: experimental
        throws:
        :throws::

        if there is more than one stack with the same stack name. You can
        use ``getStackArtifact(stack.artifactId)`` instead.
        """
        return jsii.invoke(self, "getStackByName", [stack_name])

    @jsii.member(jsii_name="tree")
    def tree(self) -> typing.Optional["TreeCloudArtifact"]:
        """Returns the tree metadata artifact from this assembly.

        return
        :return: a ``TreeCloudArtifact`` object if there is one defined in the manifest, ``undefined`` otherwise.

        stability
        :stability: experimental
        throws:
        :throws:: if there is no metadata artifact by that name
        """
        return jsii.invoke(self, "tree", [])

    @jsii.member(jsii_name="tryGetArtifact")
    def try_get_artifact(self, id: str) -> typing.Optional["CloudArtifact"]:
        """Attempts to find an artifact with a specific identity.

        :param id: The artifact ID.

        return
        :return: A ``CloudArtifact`` object or ``undefined`` if the artifact does not exist in this assembly.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "tryGetArtifact", [id])

    @builtins.property
    @jsii.member(jsii_name="artifacts")
    def artifacts(self) -> typing.List["CloudArtifact"]:
        """All artifacts included in this assembly.

        stability
        :stability: experimental
        """
        return jsii.get(self, "artifacts")

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> str:
        """The root directory of the cloud assembly.

        stability
        :stability: experimental
        """
        return jsii.get(self, "directory")

    @builtins.property
    @jsii.member(jsii_name="manifest")
    def manifest(self) -> aws_cdk.cloud_assembly_schema.AssemblyManifest:
        """The raw assembly manifest.

        stability
        :stability: experimental
        """
        return jsii.get(self, "manifest")

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> aws_cdk.cloud_assembly_schema.RuntimeInfo:
        """Runtime information such as module versions used to synthesize this assembly.

        stability
        :stability: experimental
        """
        return jsii.get(self, "runtime")

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List["CloudFormationStackArtifact"]:
        """
        return
        :return: all the CloudFormation stack artifacts that are included in this assembly.

        stability
        :stability: experimental
        """
        return jsii.get(self, "stacks")

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> str:
        """The schema version of the assembly manifest.

        stability
        :stability: experimental
        """
        return jsii.get(self, "version")


class CloudAssemblyBuilder(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/cx-api.CloudAssemblyBuilder"):
    """Can be used to build a cloud assembly.

    stability
    :stability: experimental
    """
    def __init__(self, outdir: typing.Optional[str]=None) -> None:
        """Initializes a cloud assembly builder.

        :param outdir: The output directory, uses temporary directory if undefined.

        stability
        :stability: experimental
        """
        jsii.create(CloudAssemblyBuilder, self, [outdir])

    @jsii.member(jsii_name="addArtifact")
    def add_artifact(self, id: str, *, type: aws_cdk.cloud_assembly_schema.ArtifactType, dependencies: typing.Optional[typing.List[str]]=None, environment: typing.Optional[str]=None, metadata: typing.Optional[typing.Mapping[str, typing.List[aws_cdk.cloud_assembly_schema.MetadataEntry]]]=None, properties: typing.Optional[typing.Mapping[str, typing.Any]]=None) -> None:
        """Adds an artifact into the cloud assembly.

        :param id: The ID of the artifact.
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.

        stability
        :stability: experimental
        """
        manifest = aws_cdk.cloud_assembly_schema.ArtifactManifest(type=type, dependencies=dependencies, environment=environment, metadata=metadata, properties=properties)

        return jsii.invoke(self, "addArtifact", [id, manifest])

    @jsii.member(jsii_name="addMissing")
    def add_missing(self, *, key: str, props: typing.Union[aws_cdk.cloud_assembly_schema.AmiContextQuery, aws_cdk.cloud_assembly_schema.AvailabilityZonesContextQuery, aws_cdk.cloud_assembly_schema.HostedZoneContextQuery, aws_cdk.cloud_assembly_schema.SSMParameterContextQuery, aws_cdk.cloud_assembly_schema.VpcContextQuery], provider: aws_cdk.cloud_assembly_schema.ContextProvider) -> None:
        """Reports that some context is missing in order for this cloud assembly to be fully synthesized.

        :param key: The missing context key.
        :param props: A set of provider-specific options.
        :param provider: The provider from which we expect this context key to be obtained.

        stability
        :stability: experimental
        """
        missing = aws_cdk.cloud_assembly_schema.MissingContext(key=key, props=props, provider=provider)

        return jsii.invoke(self, "addMissing", [missing])

    @jsii.member(jsii_name="buildAssembly")
    def build_assembly(self, *, runtime_info: typing.Optional["RuntimeInfo"]=None) -> "CloudAssembly":
        """Finalizes the cloud assembly into the output directory returns a ``CloudAssembly`` object that can be used to inspect the assembly.

        :param runtime_info: Include the specified runtime information (module versions) in manifest. Default: - if this option is not specified, runtime info will not be included

        stability
        :stability: experimental
        """
        options = AssemblyBuildOptions(runtime_info=runtime_info)

        return jsii.invoke(self, "buildAssembly", [options])

    @builtins.property
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> str:
        """The root directory of the resulting cloud assembly.

        stability
        :stability: experimental
        """
        return jsii.get(self, "outdir")


class CloudFormationStackArtifact(CloudArtifact, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/cx-api.CloudFormationStackArtifact"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, assembly: "CloudAssembly", artifact_id: str, *, type: aws_cdk.cloud_assembly_schema.ArtifactType, dependencies: typing.Optional[typing.List[str]]=None, environment: typing.Optional[str]=None, metadata: typing.Optional[typing.Mapping[str, typing.List[aws_cdk.cloud_assembly_schema.MetadataEntry]]]=None, properties: typing.Optional[typing.Mapping[str, typing.Any]]=None) -> None:
        """
        :param assembly: -
        :param artifact_id: -
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.

        stability
        :stability: experimental
        """
        artifact = aws_cdk.cloud_assembly_schema.ArtifactManifest(type=type, dependencies=dependencies, environment=environment, metadata=metadata, properties=properties)

        jsii.create(CloudFormationStackArtifact, self, [assembly, artifact_id, artifact])

    @builtins.property
    @jsii.member(jsii_name="assets")
    def assets(self) -> typing.List[typing.Union[aws_cdk.cloud_assembly_schema.FileAssetMetadataEntry, aws_cdk.cloud_assembly_schema.ContainerImageAssetMetadataEntry]]:
        """Any assets associated with this stack.

        stability
        :stability: experimental
        """
        return jsii.get(self, "assets")

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> str:
        """A string that represents this stack.

        Should only be used in user interfaces.
        If the stackName and artifactId are the same, it will just return that. Otherwise,
        it will return something like " ()"

        stability
        :stability: experimental
        """
        return jsii.get(self, "displayName")

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> "Environment":
        """The environment into which to deploy this artifact.

        stability
        :stability: experimental
        """
        return jsii.get(self, "environment")

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """The physical name of this stack.

        deprecated
        :deprecated: renamed to ``stackName``

        stability
        :stability: deprecated
        """
        return jsii.get(self, "name")

    @builtins.property
    @jsii.member(jsii_name="originalName")
    def original_name(self) -> str:
        """The original name as defined in the CDK app.

        stability
        :stability: experimental
        """
        return jsii.get(self, "originalName")

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[str, str]:
        """CloudFormation parameters to pass to the stack.

        stability
        :stability: experimental
        """
        return jsii.get(self, "parameters")

    @builtins.property
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> str:
        """The physical name of this stack.

        stability
        :stability: experimental
        """
        return jsii.get(self, "stackName")

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> typing.Any:
        """The CloudFormation template for this stack.

        stability
        :stability: experimental
        """
        return jsii.get(self, "template")

    @builtins.property
    @jsii.member(jsii_name="templateFile")
    def template_file(self) -> str:
        """The file name of the template.

        stability
        :stability: experimental
        """
        return jsii.get(self, "templateFile")

    @builtins.property
    @jsii.member(jsii_name="terminationProtection")
    def termination_protection(self) -> typing.Optional[bool]:
        """Whether termination protection is enabled for this stack.

        stability
        :stability: experimental
        """
        return jsii.get(self, "terminationProtection")


@jsii.data_type(jsii_type="@aws-cdk/cx-api.Environment", jsii_struct_bases=[], name_mapping={'account': 'account', 'name': 'name', 'region': 'region'})
class Environment():
    def __init__(self, *, account: str, name: str, region: str) -> None:
        """Models an AWS execution environment, for use within the CDK toolkit.

        :param account: The AWS account this environment deploys into.
        :param name: The arbitrary name of this environment (user-set, or at least user-meaningful).
        :param region: The AWS region name where this environment deploys into.

        stability
        :stability: experimental
        """
        self._values = {
            'account': account,
            'name': name,
            'region': region,
        }

    @builtins.property
    def account(self) -> str:
        """The AWS account this environment deploys into.

        stability
        :stability: experimental
        """
        return self._values.get('account')

    @builtins.property
    def name(self) -> str:
        """The arbitrary name of this environment (user-set, or at least user-meaningful).

        stability
        :stability: experimental
        """
        return self._values.get('name')

    @builtins.property
    def region(self) -> str:
        """The AWS region name where this environment deploys into.

        stability
        :stability: experimental
        """
        return self._values.get('region')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'Environment(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class EnvironmentUtils(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/cx-api.EnvironmentUtils"):
    """
    stability
    :stability: experimental
    """
    def __init__(self) -> None:
        jsii.create(EnvironmentUtils, self, [])

    @jsii.member(jsii_name="format")
    @builtins.classmethod
    def format(cls, account: str, region: str) -> str:
        """Format an environment string from an account and region.

        :param account: -
        :param region: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "format", [account, region])

    @jsii.member(jsii_name="make")
    @builtins.classmethod
    def make(cls, account: str, region: str) -> "Environment":
        """Build an environment object from an account and region.

        :param account: -
        :param region: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "make", [account, region])

    @jsii.member(jsii_name="parse")
    @builtins.classmethod
    def parse(cls, environment: str) -> "Environment":
        """
        :param environment: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "parse", [environment])


@jsii.data_type(jsii_type="@aws-cdk/cx-api.MetadataEntry", jsii_struct_bases=[aws_cdk.cloud_assembly_schema.MetadataEntry], name_mapping={'type': 'type', 'data': 'data', 'trace': 'trace'})
class MetadataEntry(aws_cdk.cloud_assembly_schema.MetadataEntry):
    def __init__(self, *, type: str, data: typing.Optional[typing.Union[typing.Optional[str], typing.Optional[aws_cdk.cloud_assembly_schema.FileAssetMetadataEntry], typing.Optional[aws_cdk.cloud_assembly_schema.ContainerImageAssetMetadataEntry], typing.Optional[typing.List[aws_cdk.cloud_assembly_schema.Tag]]]]=None, trace: typing.Optional[typing.List[str]]=None) -> None:
        """Backwards compatibility for when ``MetadataEntry`` was defined here.

        This is necessary because its used as an input in the stable

        :param type: The type of the metadata entry.
        :param data: The data. Default: - no data.
        :param trace: A stack trace for when the entry was created. Default: - no trace.

        deprecated
        :deprecated: moved to package 'cloud-assembly-schema'

        see
        :see: core.ConstructNode.metadata
        stability
        :stability: deprecated
        aws-cdk:
        :aws-cdk:: /core library.
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
    def data(self) -> typing.Optional[typing.Union[typing.Optional[str], typing.Optional[aws_cdk.cloud_assembly_schema.FileAssetMetadataEntry], typing.Optional[aws_cdk.cloud_assembly_schema.ContainerImageAssetMetadataEntry], typing.Optional[typing.List[aws_cdk.cloud_assembly_schema.Tag]]]]:
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


@jsii.data_type(jsii_type="@aws-cdk/cx-api.MetadataEntryResult", jsii_struct_bases=[aws_cdk.cloud_assembly_schema.MetadataEntry], name_mapping={'type': 'type', 'data': 'data', 'trace': 'trace', 'path': 'path'})
class MetadataEntryResult(aws_cdk.cloud_assembly_schema.MetadataEntry):
    def __init__(self, *, type: str, data: typing.Optional[typing.Union[typing.Optional[str], typing.Optional[aws_cdk.cloud_assembly_schema.FileAssetMetadataEntry], typing.Optional[aws_cdk.cloud_assembly_schema.ContainerImageAssetMetadataEntry], typing.Optional[typing.List[aws_cdk.cloud_assembly_schema.Tag]]]]=None, trace: typing.Optional[typing.List[str]]=None, path: str) -> None:
        """
        :param type: The type of the metadata entry.
        :param data: The data. Default: - no data.
        :param trace: A stack trace for when the entry was created. Default: - no trace.
        :param path: The path in which this entry was defined.

        stability
        :stability: experimental
        """
        self._values = {
            'type': type,
            'path': path,
        }
        if data is not None: self._values["data"] = data
        if trace is not None: self._values["trace"] = trace

    @builtins.property
    def type(self) -> str:
        """The type of the metadata entry."""
        return self._values.get('type')

    @builtins.property
    def data(self) -> typing.Optional[typing.Union[typing.Optional[str], typing.Optional[aws_cdk.cloud_assembly_schema.FileAssetMetadataEntry], typing.Optional[aws_cdk.cloud_assembly_schema.ContainerImageAssetMetadataEntry], typing.Optional[typing.List[aws_cdk.cloud_assembly_schema.Tag]]]]:
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

    @builtins.property
    def path(self) -> str:
        """The path in which this entry was defined.

        stability
        :stability: experimental
        """
        return self._values.get('path')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'MetadataEntryResult(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cx-api.MissingContext", jsii_struct_bases=[], name_mapping={'key': 'key', 'props': 'props', 'provider': 'provider'})
class MissingContext():
    def __init__(self, *, key: str, props: typing.Mapping[str, typing.Any], provider: str) -> None:
        """Backwards compatibility for when ``MissingContext`` was defined here.

        This is necessary because its used as an input in the stable

        :param key: The missing context key.
        :param props: A set of provider-specific options. (This is the old untyped definition, which is necessary for backwards compatibility. See cxschema for a type definition.)
        :param provider: The provider from which we expect this context key to be obtained. (This is the old untyped definition, which is necessary for backwards compatibility. See cxschema for a type definition.)

        deprecated
        :deprecated: moved to package 'cloud-assembly-schema'

        see
        :see: core.Stack.reportMissingContext
        stability
        :stability: deprecated
        aws-cdk:
        :aws-cdk:: /core library.
        """
        self._values = {
            'key': key,
            'props': props,
            'provider': provider,
        }

    @builtins.property
    def key(self) -> str:
        """The missing context key.

        stability
        :stability: deprecated
        """
        return self._values.get('key')

    @builtins.property
    def props(self) -> typing.Mapping[str, typing.Any]:
        """A set of provider-specific options.

        (This is the old untyped definition, which is necessary for backwards compatibility.
        See cxschema for a type definition.)

        stability
        :stability: deprecated
        """
        return self._values.get('props')

    @builtins.property
    def provider(self) -> str:
        """The provider from which we expect this context key to be obtained.

        (This is the old untyped definition, which is necessary for backwards compatibility.
        See cxschema for a type definition.)

        stability
        :stability: deprecated
        """
        return self._values.get('provider')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'MissingContext(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cx-api.RuntimeInfo", jsii_struct_bases=[aws_cdk.cloud_assembly_schema.RuntimeInfo], name_mapping={'libraries': 'libraries'})
class RuntimeInfo(aws_cdk.cloud_assembly_schema.RuntimeInfo):
    def __init__(self, *, libraries: typing.Mapping[str, str]) -> None:
        """Backwards compatibility for when ``RuntimeInfo`` was defined here.

        This is necessary because its used as an input in the stable

        :param libraries: The list of libraries loaded in the application, associated with their versions.

        deprecated
        :deprecated: moved to package 'cloud-assembly-schema'

        see
        :see: core.ConstructNode.synth
        stability
        :stability: deprecated
        aws-cdk:
        :aws-cdk:: /core library.
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


@jsii.data_type(jsii_type="@aws-cdk/cx-api.SynthesisMessage", jsii_struct_bases=[], name_mapping={'entry': 'entry', 'id': 'id', 'level': 'level'})
class SynthesisMessage():
    def __init__(self, *, entry: aws_cdk.cloud_assembly_schema.MetadataEntry, id: str, level: "SynthesisMessageLevel") -> None:
        """
        :param entry: 
        :param id: 
        :param level: 

        stability
        :stability: experimental
        """
        if isinstance(entry, dict): entry = aws_cdk.cloud_assembly_schema.MetadataEntry(**entry)
        self._values = {
            'entry': entry,
            'id': id,
            'level': level,
        }

    @builtins.property
    def entry(self) -> aws_cdk.cloud_assembly_schema.MetadataEntry:
        """
        stability
        :stability: experimental
        """
        return self._values.get('entry')

    @builtins.property
    def id(self) -> str:
        """
        stability
        :stability: experimental
        """
        return self._values.get('id')

    @builtins.property
    def level(self) -> "SynthesisMessageLevel":
        """
        stability
        :stability: experimental
        """
        return self._values.get('level')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SynthesisMessage(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/cx-api.SynthesisMessageLevel")
class SynthesisMessageLevel(enum.Enum):
    """
    stability
    :stability: experimental
    """
    INFO = "INFO"
    """
    stability
    :stability: experimental
    """
    WARNING = "WARNING"
    """
    stability
    :stability: experimental
    """
    ERROR = "ERROR"
    """
    stability
    :stability: experimental
    """

class TreeCloudArtifact(CloudArtifact, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/cx-api.TreeCloudArtifact"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, assembly: "CloudAssembly", name: str, *, type: aws_cdk.cloud_assembly_schema.ArtifactType, dependencies: typing.Optional[typing.List[str]]=None, environment: typing.Optional[str]=None, metadata: typing.Optional[typing.Mapping[str, typing.List[aws_cdk.cloud_assembly_schema.MetadataEntry]]]=None, properties: typing.Optional[typing.Mapping[str, typing.Any]]=None) -> None:
        """
        :param assembly: -
        :param name: -
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.

        stability
        :stability: experimental
        """
        artifact = aws_cdk.cloud_assembly_schema.ArtifactManifest(type=type, dependencies=dependencies, environment=environment, metadata=metadata, properties=properties)

        jsii.create(TreeCloudArtifact, self, [assembly, name, artifact])

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "file")


@jsii.data_type(jsii_type="@aws-cdk/cx-api.VpcContextResponse", jsii_struct_bases=[], name_mapping={'availability_zones': 'availabilityZones', 'vpc_id': 'vpcId', 'isolated_subnet_ids': 'isolatedSubnetIds', 'isolated_subnet_names': 'isolatedSubnetNames', 'isolated_subnet_route_table_ids': 'isolatedSubnetRouteTableIds', 'private_subnet_ids': 'privateSubnetIds', 'private_subnet_names': 'privateSubnetNames', 'private_subnet_route_table_ids': 'privateSubnetRouteTableIds', 'public_subnet_ids': 'publicSubnetIds', 'public_subnet_names': 'publicSubnetNames', 'public_subnet_route_table_ids': 'publicSubnetRouteTableIds', 'subnet_groups': 'subnetGroups', 'vpc_cidr_block': 'vpcCidrBlock', 'vpn_gateway_id': 'vpnGatewayId'})
class VpcContextResponse():
    def __init__(self, *, availability_zones: typing.List[str], vpc_id: str, isolated_subnet_ids: typing.Optional[typing.List[str]]=None, isolated_subnet_names: typing.Optional[typing.List[str]]=None, isolated_subnet_route_table_ids: typing.Optional[typing.List[str]]=None, private_subnet_ids: typing.Optional[typing.List[str]]=None, private_subnet_names: typing.Optional[typing.List[str]]=None, private_subnet_route_table_ids: typing.Optional[typing.List[str]]=None, public_subnet_ids: typing.Optional[typing.List[str]]=None, public_subnet_names: typing.Optional[typing.List[str]]=None, public_subnet_route_table_ids: typing.Optional[typing.List[str]]=None, subnet_groups: typing.Optional[typing.List["VpcSubnetGroup"]]=None, vpc_cidr_block: typing.Optional[str]=None, vpn_gateway_id: typing.Optional[str]=None) -> None:
        """Properties of a discovered VPC.

        :param availability_zones: AZs.
        :param vpc_id: VPC id.
        :param isolated_subnet_ids: IDs of all isolated subnets. Element count: #(availabilityZones) · #(isolatedGroups)
        :param isolated_subnet_names: Name of isolated subnet groups. Element count: #(isolatedGroups)
        :param isolated_subnet_route_table_ids: Route Table IDs of isolated subnet groups. Element count: #(availabilityZones) · #(isolatedGroups)
        :param private_subnet_ids: IDs of all private subnets. Element count: #(availabilityZones) · #(privateGroups)
        :param private_subnet_names: Name of private subnet groups. Element count: #(privateGroups)
        :param private_subnet_route_table_ids: Route Table IDs of private subnet groups. Element count: #(availabilityZones) · #(privateGroups)
        :param public_subnet_ids: IDs of all public subnets. Element count: #(availabilityZones) · #(publicGroups)
        :param public_subnet_names: Name of public subnet groups. Element count: #(publicGroups)
        :param public_subnet_route_table_ids: Route Table IDs of public subnet groups. Element count: #(availabilityZones) · #(publicGroups)
        :param subnet_groups: The subnet groups discovered for the given VPC. Unlike the above properties, this will include asymmetric subnets, if the VPC has any. This property will only be populated if {@link VpcContextQuery.returnAsymmetricSubnets} is true. Default: - no subnet groups will be returned unless {@link VpcContextQuery.returnAsymmetricSubnets} is true
        :param vpc_cidr_block: VPC cidr. Default: - CIDR information not available
        :param vpn_gateway_id: The VPN gateway ID.

        stability
        :stability: experimental
        """
        self._values = {
            'availability_zones': availability_zones,
            'vpc_id': vpc_id,
        }
        if isolated_subnet_ids is not None: self._values["isolated_subnet_ids"] = isolated_subnet_ids
        if isolated_subnet_names is not None: self._values["isolated_subnet_names"] = isolated_subnet_names
        if isolated_subnet_route_table_ids is not None: self._values["isolated_subnet_route_table_ids"] = isolated_subnet_route_table_ids
        if private_subnet_ids is not None: self._values["private_subnet_ids"] = private_subnet_ids
        if private_subnet_names is not None: self._values["private_subnet_names"] = private_subnet_names
        if private_subnet_route_table_ids is not None: self._values["private_subnet_route_table_ids"] = private_subnet_route_table_ids
        if public_subnet_ids is not None: self._values["public_subnet_ids"] = public_subnet_ids
        if public_subnet_names is not None: self._values["public_subnet_names"] = public_subnet_names
        if public_subnet_route_table_ids is not None: self._values["public_subnet_route_table_ids"] = public_subnet_route_table_ids
        if subnet_groups is not None: self._values["subnet_groups"] = subnet_groups
        if vpc_cidr_block is not None: self._values["vpc_cidr_block"] = vpc_cidr_block
        if vpn_gateway_id is not None: self._values["vpn_gateway_id"] = vpn_gateway_id

    @builtins.property
    def availability_zones(self) -> typing.List[str]:
        """AZs.

        stability
        :stability: experimental
        """
        return self._values.get('availability_zones')

    @builtins.property
    def vpc_id(self) -> str:
        """VPC id.

        stability
        :stability: experimental
        """
        return self._values.get('vpc_id')

    @builtins.property
    def isolated_subnet_ids(self) -> typing.Optional[typing.List[str]]:
        """IDs of all isolated subnets.

        Element count: #(availabilityZones) · #(isolatedGroups)

        stability
        :stability: experimental
        """
        return self._values.get('isolated_subnet_ids')

    @builtins.property
    def isolated_subnet_names(self) -> typing.Optional[typing.List[str]]:
        """Name of isolated subnet groups.

        Element count: #(isolatedGroups)

        stability
        :stability: experimental
        """
        return self._values.get('isolated_subnet_names')

    @builtins.property
    def isolated_subnet_route_table_ids(self) -> typing.Optional[typing.List[str]]:
        """Route Table IDs of isolated subnet groups.

        Element count: #(availabilityZones) · #(isolatedGroups)

        stability
        :stability: experimental
        """
        return self._values.get('isolated_subnet_route_table_ids')

    @builtins.property
    def private_subnet_ids(self) -> typing.Optional[typing.List[str]]:
        """IDs of all private subnets.

        Element count: #(availabilityZones) · #(privateGroups)

        stability
        :stability: experimental
        """
        return self._values.get('private_subnet_ids')

    @builtins.property
    def private_subnet_names(self) -> typing.Optional[typing.List[str]]:
        """Name of private subnet groups.

        Element count: #(privateGroups)

        stability
        :stability: experimental
        """
        return self._values.get('private_subnet_names')

    @builtins.property
    def private_subnet_route_table_ids(self) -> typing.Optional[typing.List[str]]:
        """Route Table IDs of private subnet groups.

        Element count: #(availabilityZones) · #(privateGroups)

        stability
        :stability: experimental
        """
        return self._values.get('private_subnet_route_table_ids')

    @builtins.property
    def public_subnet_ids(self) -> typing.Optional[typing.List[str]]:
        """IDs of all public subnets.

        Element count: #(availabilityZones) · #(publicGroups)

        stability
        :stability: experimental
        """
        return self._values.get('public_subnet_ids')

    @builtins.property
    def public_subnet_names(self) -> typing.Optional[typing.List[str]]:
        """Name of public subnet groups.

        Element count: #(publicGroups)

        stability
        :stability: experimental
        """
        return self._values.get('public_subnet_names')

    @builtins.property
    def public_subnet_route_table_ids(self) -> typing.Optional[typing.List[str]]:
        """Route Table IDs of public subnet groups.

        Element count: #(availabilityZones) · #(publicGroups)

        stability
        :stability: experimental
        """
        return self._values.get('public_subnet_route_table_ids')

    @builtins.property
    def subnet_groups(self) -> typing.Optional[typing.List["VpcSubnetGroup"]]:
        """The subnet groups discovered for the given VPC.

        Unlike the above properties, this will include asymmetric subnets,
        if the VPC has any.
        This property will only be populated if {@link VpcContextQuery.returnAsymmetricSubnets}
        is true.

        default
        :default: - no subnet groups will be returned unless {@link VpcContextQuery.returnAsymmetricSubnets} is true

        stability
        :stability: experimental
        """
        return self._values.get('subnet_groups')

    @builtins.property
    def vpc_cidr_block(self) -> typing.Optional[str]:
        """VPC cidr.

        default
        :default: - CIDR information not available

        stability
        :stability: experimental
        """
        return self._values.get('vpc_cidr_block')

    @builtins.property
    def vpn_gateway_id(self) -> typing.Optional[str]:
        """The VPN gateway ID.

        stability
        :stability: experimental
        """
        return self._values.get('vpn_gateway_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'VpcContextResponse(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cx-api.VpcSubnet", jsii_struct_bases=[], name_mapping={'availability_zone': 'availabilityZone', 'route_table_id': 'routeTableId', 'subnet_id': 'subnetId', 'cidr': 'cidr'})
class VpcSubnet():
    def __init__(self, *, availability_zone: str, route_table_id: str, subnet_id: str, cidr: typing.Optional[str]=None) -> None:
        """A subnet representation that the VPC provider uses.

        :param availability_zone: The code of the availability zone this subnet is in (for example, 'us-west-2a').
        :param route_table_id: The identifier of the route table for this subnet.
        :param subnet_id: The identifier of the subnet.
        :param cidr: CIDR range of the subnet. Default: - CIDR information not available

        stability
        :stability: experimental
        """
        self._values = {
            'availability_zone': availability_zone,
            'route_table_id': route_table_id,
            'subnet_id': subnet_id,
        }
        if cidr is not None: self._values["cidr"] = cidr

    @builtins.property
    def availability_zone(self) -> str:
        """The code of the availability zone this subnet is in (for example, 'us-west-2a').

        stability
        :stability: experimental
        """
        return self._values.get('availability_zone')

    @builtins.property
    def route_table_id(self) -> str:
        """The identifier of the route table for this subnet.

        stability
        :stability: experimental
        """
        return self._values.get('route_table_id')

    @builtins.property
    def subnet_id(self) -> str:
        """The identifier of the subnet.

        stability
        :stability: experimental
        """
        return self._values.get('subnet_id')

    @builtins.property
    def cidr(self) -> typing.Optional[str]:
        """CIDR range of the subnet.

        default
        :default: - CIDR information not available

        stability
        :stability: experimental
        """
        return self._values.get('cidr')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'VpcSubnet(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/cx-api.VpcSubnetGroup", jsii_struct_bases=[], name_mapping={'name': 'name', 'subnets': 'subnets', 'type': 'type'})
class VpcSubnetGroup():
    def __init__(self, *, name: str, subnets: typing.List["VpcSubnet"], type: "VpcSubnetGroupType") -> None:
        """A group of subnets returned by the VPC provider.

        The included subnets do NOT have to be symmetric!

        :param name: The name of the subnet group, determined by looking at the tags of of the subnets that belong to it.
        :param subnets: The subnets that are part of this group. There is no condition that the subnets have to be symmetric in the group.
        :param type: The type of the subnet group.

        stability
        :stability: experimental
        """
        self._values = {
            'name': name,
            'subnets': subnets,
            'type': type,
        }

    @builtins.property
    def name(self) -> str:
        """The name of the subnet group, determined by looking at the tags of of the subnets that belong to it.

        stability
        :stability: experimental
        """
        return self._values.get('name')

    @builtins.property
    def subnets(self) -> typing.List["VpcSubnet"]:
        """The subnets that are part of this group.

        There is no condition that the subnets have to be symmetric
        in the group.

        stability
        :stability: experimental
        """
        return self._values.get('subnets')

    @builtins.property
    def type(self) -> "VpcSubnetGroupType":
        """The type of the subnet group.

        stability
        :stability: experimental
        """
        return self._values.get('type')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'VpcSubnetGroup(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/cx-api.VpcSubnetGroupType")
class VpcSubnetGroupType(enum.Enum):
    """The type of subnet group.

    Same as SubnetType in the @aws-cdk/aws-ec2 package,
    but we can't use that because of cyclical dependencies.

    stability
    :stability: experimental
    """
    PUBLIC = "PUBLIC"
    """Public subnet group type.

    stability
    :stability: experimental
    """
    PRIVATE = "PRIVATE"
    """Private subnet group type.

    stability
    :stability: experimental
    """
    ISOLATED = "ISOLATED"
    """Isolated subnet group type.

    stability
    :stability: experimental
    """

__all__ = [
    "AssemblyBuildOptions",
    "AwsCloudFormationStackProperties",
    "CloudArtifact",
    "CloudAssembly",
    "CloudAssemblyBuilder",
    "CloudFormationStackArtifact",
    "Environment",
    "EnvironmentUtils",
    "MetadataEntry",
    "MetadataEntryResult",
    "MissingContext",
    "RuntimeInfo",
    "SynthesisMessage",
    "SynthesisMessageLevel",
    "TreeCloudArtifact",
    "VpcContextResponse",
    "VpcSubnet",
    "VpcSubnetGroup",
    "VpcSubnetGroupType",
]

publication.publish()
