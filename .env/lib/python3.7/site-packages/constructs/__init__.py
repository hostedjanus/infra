"""
# Constructs Programming Model

> Define composable configuration models through code

![Release](https://github.com/awslabs/constructs/workflows/Release/badge.svg)
[![npm version](https://badge.fury.io/js/constructs.svg)](https://badge.fury.io/js/constructs)
[![PyPI version](https://badge.fury.io/py/constructs.svg)](https://badge.fury.io/py/constructs)
[![NuGet version](https://badge.fury.io/nu/Constructs.svg)](https://badge.fury.io/nu/Constructs)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/software.constructs/constructs/badge.svg?style=plastic)](https://maven-badges.herokuapp.com/maven-central/software.constructs/constructs)

## Contributing

This project has adopted the [Amazon Open Source Code of
Conduct](https://aws.github.io/code-of-conduct).

We welcome community contributions and pull requests. See our [contribution
guide](./CONTRIBUTING.md) for more information on how to report issues, set up a
development environment and submit code.

## License

This project is distributed under the [Apache License, Version 2.0](./LICENSE).
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


class ConstructMetadata(metaclass=jsii.JSIIMeta, jsii_type="constructs.ConstructMetadata"):
    """Metadata keys used by constructs."""
    @jsii.python.classproperty
    @jsii.member(jsii_name="DISABLE_STACK_TRACE_IN_METADATA")
    def DISABLE_STACK_TRACE_IN_METADATA(cls) -> str:
        """If set in the construct's context, omits stack traces from metadata entries."""
        return jsii.sget(cls, "DISABLE_STACK_TRACE_IN_METADATA")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ERROR_METADATA_KEY")
    def ERROR_METADATA_KEY(cls) -> str:
        """Context type for error level messages."""
        return jsii.sget(cls, "ERROR_METADATA_KEY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="INFO_METADATA_KEY")
    def INFO_METADATA_KEY(cls) -> str:
        """Context type for info level messages."""
        return jsii.sget(cls, "INFO_METADATA_KEY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="WARNING_METADATA_KEY")
    def WARNING_METADATA_KEY(cls) -> str:
        """Context type for warning level messages."""
        return jsii.sget(cls, "WARNING_METADATA_KEY")


@jsii.data_type(jsii_type="constructs.ConstructOptions", jsii_struct_bases=[], name_mapping={'node_factory': 'nodeFactory'})
class ConstructOptions():
    def __init__(self, *, node_factory: typing.Optional["INodeFactory"]=None) -> None:
        """Options for creating constructs.

        :param node_factory: A factory for attaching ``Node``s to the construct. Default: - the default ``Node`` is associated
        """
        self._values = {
        }
        if node_factory is not None: self._values["node_factory"] = node_factory

    @builtins.property
    def node_factory(self) -> typing.Optional["INodeFactory"]:
        """A factory for attaching ``Node``s to the construct.

        default
        :default: - the default ``Node`` is associated
        """
        return self._values.get('node_factory')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ConstructOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="constructs.ConstructOrder")
class ConstructOrder(enum.Enum):
    """In what order to return constructs."""
    PREORDER = "PREORDER"
    """Depth-first, pre-order."""
    POSTORDER = "POSTORDER"
    """Depth-first, post-order (leaf nodes first)."""

@jsii.data_type(jsii_type="constructs.Dependency", jsii_struct_bases=[], name_mapping={'source': 'source', 'target': 'target'})
class Dependency():
    def __init__(self, *, source: "IConstruct", target: "IConstruct") -> None:
        """A single dependency.

        :param source: Source the dependency.
        :param target: Target of the dependency.
        """
        self._values = {
            'source': source,
            'target': target,
        }

    @builtins.property
    def source(self) -> "IConstruct":
        """Source the dependency."""
        return self._values.get('source')

    @builtins.property
    def target(self) -> "IConstruct":
        """Target of the dependency."""
        return self._values.get('target')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'Dependency(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.interface(jsii_type="constructs.IAspect")
class IAspect(jsii.compat.Protocol):
    """Represents an Aspect."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IAspectProxy

    @jsii.member(jsii_name="visit")
    def visit(self, node: "IConstruct") -> None:
        """All aspects can visit an IConstruct.

        :param node: -
        """
        ...


class _IAspectProxy():
    """Represents an Aspect."""
    __jsii_type__ = "constructs.IAspect"
    @jsii.member(jsii_name="visit")
    def visit(self, node: "IConstruct") -> None:
        """All aspects can visit an IConstruct.

        :param node: -
        """
        return jsii.invoke(self, "visit", [node])


@jsii.interface(jsii_type="constructs.IConstruct")
class IConstruct(jsii.compat.Protocol):
    """Represents a construct."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IConstructProxy

    pass

class _IConstructProxy():
    """Represents a construct."""
    __jsii_type__ = "constructs.IConstruct"
    pass

@jsii.interface(jsii_type="constructs.INodeFactory")
class INodeFactory(jsii.compat.Protocol):
    """A factory for attaching ``Node``s to the construct."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _INodeFactoryProxy

    @jsii.member(jsii_name="createNode")
    def create_node(self, host: "Construct", scope: "IConstruct", id: str) -> "Node":
        """Returns a new ``Node`` associated with ``host``.

        :param host: the associated construct.
        :param scope: the construct's scope (parent).
        :param id: the construct id.
        """
        ...


class _INodeFactoryProxy():
    """A factory for attaching ``Node``s to the construct."""
    __jsii_type__ = "constructs.INodeFactory"
    @jsii.member(jsii_name="createNode")
    def create_node(self, host: "Construct", scope: "IConstruct", id: str) -> "Node":
        """Returns a new ``Node`` associated with ``host``.

        :param host: the associated construct.
        :param scope: the construct's scope (parent).
        :param id: the construct id.
        """
        return jsii.invoke(self, "createNode", [host, scope, id])


@jsii.interface(jsii_type="constructs.ISynthesisSession")
class ISynthesisSession(jsii.compat.Protocol):
    """Represents a single session of synthesis.

    Passed into ``construct.onSynthesize()`` methods.
    """
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _ISynthesisSessionProxy

    @builtins.property
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> str:
        """The output directory for this synthesis session."""
        ...


class _ISynthesisSessionProxy():
    """Represents a single session of synthesis.

    Passed into ``construct.onSynthesize()`` methods.
    """
    __jsii_type__ = "constructs.ISynthesisSession"
    @builtins.property
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> str:
        """The output directory for this synthesis session."""
        return jsii.get(self, "outdir")


@jsii.data_type(jsii_type="constructs.MetadataEntry", jsii_struct_bases=[], name_mapping={'data': 'data', 'type': 'type', 'trace': 'trace'})
class MetadataEntry():
    def __init__(self, *, data: typing.Any, type: str, trace: typing.Optional[typing.List[str]]=None) -> None:
        """An entry in the construct metadata table.

        :param data: The data.
        :param type: The metadata entry type.
        :param trace: Stack trace. Can be omitted by setting the context key ``ConstructMetadata.DISABLE_STACK_TRACE_IN_METADATA`` to 1. Default: - no trace information
        """
        self._values = {
            'data': data,
            'type': type,
        }
        if trace is not None: self._values["trace"] = trace

    @builtins.property
    def data(self) -> typing.Any:
        """The data."""
        return self._values.get('data')

    @builtins.property
    def type(self) -> str:
        """The metadata entry type."""
        return self._values.get('type')

    @builtins.property
    def trace(self) -> typing.Optional[typing.List[str]]:
        """Stack trace.

        Can be omitted by setting the context key
        ``ConstructMetadata.DISABLE_STACK_TRACE_IN_METADATA`` to 1.

        default
        :default: - no trace information
        """
        return self._values.get('trace')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'MetadataEntry(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class Node(metaclass=jsii.JSIIMeta, jsii_type="constructs.Node"):
    """Represents the construct node in the scope tree."""
    def __init__(self, host: "Construct", scope: "IConstruct", id: str) -> None:
        """
        :param host: -
        :param scope: -
        :param id: -
        """
        jsii.create(Node, self, [host, scope, id])

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, construct: "IConstruct") -> "Node":
        """Returns the node associated with a construct.

        :param construct: the construct.
        """
        return jsii.sinvoke(cls, "of", [construct])

    @jsii.member(jsii_name="addDependency")
    def add_dependency(self, *dependencies: "IConstruct") -> None:
        """Add an ordering dependency on another Construct.

        All constructs in the dependency's scope will be deployed before any
        construct in this construct's scope.

        :param dependencies: -
        """
        return jsii.invoke(self, "addDependency", [*dependencies])

    @jsii.member(jsii_name="addError")
    def add_error(self, message: str) -> None:
        """Adds an { "error":  } metadata entry to this construct.

        The toolkit will fail synthesis when errors are reported.

        :param message: The error message.
        """
        return jsii.invoke(self, "addError", [message])

    @jsii.member(jsii_name="addInfo")
    def add_info(self, message: str) -> None:
        """Adds a { "info":  } metadata entry to this construct.

        The toolkit will display the info message when apps are synthesized.

        :param message: The info message.
        """
        return jsii.invoke(self, "addInfo", [message])

    @jsii.member(jsii_name="addMetadata")
    def add_metadata(self, type: str, data: typing.Any, from_function: typing.Any=None) -> None:
        """Adds a metadata entry to this construct.

        Entries are arbitrary values and will also include a stack trace to allow tracing back to
        the code location for when the entry was added. It can be used, for example, to include source
        mapping in CloudFormation templates to improve diagnostics.

        :param type: a string denoting the type of metadata.
        :param data: the value of the metadata (can be a Token). If null/undefined, metadata will not be added.
        :param from_function: a function under which to restrict the metadata entry's stack trace (defaults to this.addMetadata).
        """
        return jsii.invoke(self, "addMetadata", [type, data, from_function])

    @jsii.member(jsii_name="addWarning")
    def add_warning(self, message: str) -> None:
        """Adds a { "warning":  } metadata entry to this construct.

        The toolkit will display the warning when an app is synthesized, or fail
        if run in --strict mode.

        :param message: The warning message.
        """
        return jsii.invoke(self, "addWarning", [message])

    @jsii.member(jsii_name="applyAspect")
    def apply_aspect(self, aspect: "IAspect") -> None:
        """Applies the aspect to this Constructs node.

        :param aspect: -
        """
        return jsii.invoke(self, "applyAspect", [aspect])

    @jsii.member(jsii_name="findAll")
    def find_all(self, order: typing.Optional["ConstructOrder"]=None) -> typing.List["IConstruct"]:
        """Return this construct and all of its children in the given order.

        :param order: -
        """
        return jsii.invoke(self, "findAll", [order])

    @jsii.member(jsii_name="findChild")
    def find_child(self, id: str) -> "IConstruct":
        """Return a direct child by id.

        Throws an error if the child is not found.

        :param id: Identifier of direct child.

        return
        :return: Child with the given id.
        """
        return jsii.invoke(self, "findChild", [id])

    @jsii.member(jsii_name="prepare")
    def prepare(self) -> None:
        """Invokes "prepare" on all constructs (depth-first, post-order) in the tree under ``node``."""
        return jsii.invoke(self, "prepare", [])

    @jsii.member(jsii_name="setContext")
    def set_context(self, key: str, value: typing.Any) -> None:
        """This can be used to set contextual values.

        Context must be set before any children are added, since children may consult context info during construction.
        If the key already exists, it will be overridden.

        :param key: The context key.
        :param value: The context value.
        """
        return jsii.invoke(self, "setContext", [key, value])

    @jsii.member(jsii_name="synthesize")
    def synthesize(self, *, outdir: str, session_context: typing.Optional[typing.Mapping[str, typing.Any]]=None, skip_validation: typing.Optional[bool]=None) -> None:
        """Synthesizes a CloudAssembly from a construct tree.

        :param outdir: The output directory into which to synthesize the cloud assembly. Default: - creates a temporary directory
        :param session_context: Additional context passed into the synthesis session object when ``construct.synth`` is called. Default: - no additional context is passed to ``onSynthesize``
        :param skip_validation: Whether synthesis should skip the validation phase. Default: false
        """
        options = SynthesisOptions(outdir=outdir, session_context=session_context, skip_validation=skip_validation)

        return jsii.invoke(self, "synthesize", [options])

    @jsii.member(jsii_name="tryFindChild")
    def try_find_child(self, id: str) -> typing.Optional["IConstruct"]:
        """Return a direct child by id, or undefined.

        :param id: Identifier of direct child.

        return
        :return: the child if found, or undefined
        """
        return jsii.invoke(self, "tryFindChild", [id])

    @jsii.member(jsii_name="tryGetContext")
    def try_get_context(self, key: str) -> typing.Any:
        """Retrieves a value from tree context.

        Context is usually initialized at the root, but can be overridden at any point in the tree.

        :param key: The context key.

        return
        :return: The context value or ``undefined`` if there is no context value for thie key.
        """
        return jsii.invoke(self, "tryGetContext", [key])

    @jsii.member(jsii_name="tryRemoveChild")
    def try_remove_child(self, child_name: str) -> bool:
        """Remove the child with the given name, if present.

        :param child_name: -

        return
        :return: Whether a child with the given name was deleted.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "tryRemoveChild", [child_name])

    @jsii.member(jsii_name="validate")
    def validate(self) -> typing.List["ValidationError"]:
        """Invokes "validate" on all constructs in the tree (depth-first, pre-order) and returns the list of all errors.

        An empty list indicates that there are no errors.
        """
        return jsii.invoke(self, "validate", [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PATH_SEP")
    def PATH_SEP(cls) -> str:
        """Separator used to delimit construct path components."""
        return jsii.sget(cls, "PATH_SEP")

    @builtins.property
    @jsii.member(jsii_name="children")
    def children(self) -> typing.List["IConstruct"]:
        """All direct children of this construct."""
        return jsii.get(self, "children")

    @builtins.property
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.List["Dependency"]:
        """Return all dependencies registered on this node or any of its children."""
        return jsii.get(self, "dependencies")

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> str:
        """The id of this construct within the current scope.

        This is a a scope-unique id. To obtain an app-unique id for this construct, use ``uniqueId``.
        """
        return jsii.get(self, "id")

    @builtins.property
    @jsii.member(jsii_name="locked")
    def locked(self) -> bool:
        """Returns true if this construct or the scopes in which it is defined are locked."""
        return jsii.get(self, "locked")

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.List["MetadataEntry"]:
        """An immutable array of metadata objects associated with this construct.

        This can be used, for example, to implement support for deprecation notices, source mapping, etc.
        """
        return jsii.get(self, "metadata")

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> str:
        """The full, absolute path of this construct in the tree.

        Components are separated by '/'.
        """
        return jsii.get(self, "path")

    @builtins.property
    @jsii.member(jsii_name="root")
    def root(self) -> "IConstruct":
        """Returns the root of the construct tree.

        return
        :return: The root of the construct tree.
        """
        return jsii.get(self, "root")

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.List["IConstruct"]:
        """All parent scopes of this construct.

        return
        :return:

        a list of parent scopes. The last element in the list will always
        be the current construct and the first element will be the root of the
        tree.
        """
        return jsii.get(self, "scopes")

    @builtins.property
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> str:
        """A tree-global unique alphanumeric identifier for this construct.

        Includes all components of the tree.
        """
        return jsii.get(self, "uniqueId")

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> typing.Optional["IConstruct"]:
        """Returns the scope in which this construct is defined.

        The value is ``undefined`` at the root of the construct scope tree.
        """
        return jsii.get(self, "scope")

    @builtins.property
    @jsii.member(jsii_name="defaultChild")
    def default_child(self) -> typing.Optional["IConstruct"]:
        """Returns the child construct that has the id ``Default`` or ``Resource"``.

        This is usually the construct that provides the bulk of the underlying functionality.
        Useful for modifications of the underlying construct that are not available at the higher levels.
        Override the defaultChild property.

        This should only be used in the cases where the correct
        default child is not named 'Resource' or 'Default' as it
        should be.

        If you set this to undefined, the default behavior of finding
        the child named 'Resource' or 'Default' will be used.

        return
        :return: a construct or undefined if there is no default child

        throws:
        :throws:: if there is more than one child
        """
        return jsii.get(self, "defaultChild")

    @default_child.setter
    def default_child(self, value: typing.Optional["IConstruct"]):
        jsii.set(self, "defaultChild", value)


@jsii.data_type(jsii_type="constructs.SynthesisOptions", jsii_struct_bases=[], name_mapping={'outdir': 'outdir', 'session_context': 'sessionContext', 'skip_validation': 'skipValidation'})
class SynthesisOptions():
    def __init__(self, *, outdir: str, session_context: typing.Optional[typing.Mapping[str, typing.Any]]=None, skip_validation: typing.Optional[bool]=None) -> None:
        """Options for synthesis.

        :param outdir: The output directory into which to synthesize the cloud assembly. Default: - creates a temporary directory
        :param session_context: Additional context passed into the synthesis session object when ``construct.synth`` is called. Default: - no additional context is passed to ``onSynthesize``
        :param skip_validation: Whether synthesis should skip the validation phase. Default: false
        """
        self._values = {
            'outdir': outdir,
        }
        if session_context is not None: self._values["session_context"] = session_context
        if skip_validation is not None: self._values["skip_validation"] = skip_validation

    @builtins.property
    def outdir(self) -> str:
        """The output directory into which to synthesize the cloud assembly.

        default
        :default: - creates a temporary directory
        """
        return self._values.get('outdir')

    @builtins.property
    def session_context(self) -> typing.Optional[typing.Mapping[str, typing.Any]]:
        """Additional context passed into the synthesis session object when ``construct.synth`` is called.

        default
        :default: - no additional context is passed to ``onSynthesize``
        """
        return self._values.get('session_context')

    @builtins.property
    def skip_validation(self) -> typing.Optional[bool]:
        """Whether synthesis should skip the validation phase.

        default
        :default: false
        """
        return self._values.get('skip_validation')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SynthesisOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="constructs.ValidationError", jsii_struct_bases=[], name_mapping={'message': 'message', 'source': 'source'})
class ValidationError():
    def __init__(self, *, message: str, source: "Construct") -> None:
        """An error returned during the validation phase.

        :param message: The error message.
        :param source: The construct which emitted the error.
        """
        self._values = {
            'message': message,
            'source': source,
        }

    @builtins.property
    def message(self) -> str:
        """The error message."""
        return self._values.get('message')

    @builtins.property
    def source(self) -> "Construct":
        """The construct which emitted the error."""
        return self._values.get('source')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ValidationError(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(IConstruct)
class Construct(metaclass=jsii.JSIIMeta, jsii_type="constructs.Construct"):
    """Represents the building block of the construct graph.

    All constructs besides the root construct must be created within the scope of
    another construct.
    """
    def __init__(self, scope: "Construct", id: str, *, node_factory: typing.Optional["INodeFactory"]=None) -> None:
        """Creates a new construct node.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings. If the ID includes a path separator (``/``), then it will be replaced by double dash ``--``.
        :param node_factory: A factory for attaching ``Node``s to the construct. Default: - the default ``Node`` is associated
        """
        options = ConstructOptions(node_factory=node_factory)

        jsii.create(Construct, self, [scope, id, options])

    @jsii.member(jsii_name="onPrepare")
    def _on_prepare(self) -> None:
        """Perform final modifications before synthesis.

        This method can be implemented by derived constructs in order to perform
        final changes before synthesis. prepare() will be called after child
        constructs have been prepared.

        This is an advanced framework feature. Only use this if you
        understand the implications.
        """
        return jsii.invoke(self, "onPrepare", [])

    @jsii.member(jsii_name="onSynthesize")
    def _on_synthesize(self, session: "ISynthesisSession") -> None:
        """Allows this construct to emit artifacts into the cloud assembly during synthesis.

        This method is usually implemented by framework-level constructs such as ``Stack`` and ``Asset``
        as they participate in synthesizing the cloud assembly.

        :param session: The synthesis session.
        """
        return jsii.invoke(self, "onSynthesize", [session])

    @jsii.member(jsii_name="onValidate")
    def _on_validate(self) -> typing.List[str]:
        """Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        return
        :return: An array of validation error messages, or an empty array if there the construct is valid.
        """
        return jsii.invoke(self, "onValidate", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        """Returns a string representation of this construct."""
        return jsii.invoke(self, "toString", [])


__all__ = [
    "Construct",
    "ConstructMetadata",
    "ConstructOptions",
    "ConstructOrder",
    "Dependency",
    "IAspect",
    "IConstruct",
    "INodeFactory",
    "ISynthesisSession",
    "MetadataEntry",
    "Node",
    "SynthesisOptions",
    "ValidationError",
]

publication.publish()
