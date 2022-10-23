"""
Helper module that is used by objc_class.setattr and objc_class.__new__
to transform class attributes.

The primary usecase is to transform callables to Objective-C selectors.
"""
# XXX: Needs more tests
# XXX: Needs to be verified against current C implementation.
# XXX: Should the exception be ValueError or objc.error?
#      the latter is more consistent with the rest of the bridge
import objc
import types
import inspect
import dis

__all__ = ("objc_method", "python_method")


def transformCallable(name, value, class_object):
    """
    Transform 'value' before it will be added to a class

    For callables this will convert the value to an
    'objc.selector' object where appropriate, other values
    are returned as-is.
    """
    if not callable(value) and not isinstance(value, classmethod):
        return value
    elif isinstance(value, (objc.selector, staticmethod, type)):
        return value
    elif inspect.iscoroutine(value) or inspect.iscoroutinefunction(value):
        return value
    elif inspect.isgenerator(value) or inspect.isgeneratorfunction(value):
        return value
    elif isinstance(value, objc.python_method):
        # XXX: objc.python_method will be python_method in the next step
        return value.callable
    elif isinstance(value, python_method):
        return value.__wrapped__

    isclass = False
    selname = default_selector(name)
    signature = None

    # XXX: Deal with formal and informal protocols

    # DWIM: Copy classmethod-ness and signature from
    # a pre-existing method on the class.
    current = getattr(class_object, name, None)
    if isinstance(current, objc.selector):
        isclass = current.isClassMethod
        signature = current.signature
        selname = current.selector

    if isinstance(value, classmethod):
        # Unwrap "classmethod" instances.
        value = value.__wrapped__
        isclass = True

        if isinstance(value, python_method):
            # Deal with:
            #   @classmethod
            #   @python_method
            #   def ...
            #
            return classmethod(value.__wrapped__)
        if isinstance(value, objc.python_method):
            return classmethod(value.callable)

        assert not isinstance(value, classmethod)

    if isinstance(value, objc_method):
        # Unwrap "objc_method" instances
        if value.isclass is not None:
            isclass = value.isclass

        if value.selector is not None:
            selname = value.selector

        if value.signature is not None:
            signature = value.signature

        if selname is None:
            raise ValueError(
                f"{name!r} is an objc_method instance, but cannot determine Objective-C selector"
            )

        if isinstance(value.__wrapped__, classmethod):
            # Deal with:
            #    @objc_method
            #    @classsmethod
            #    def ...
            #
            if value.isclass is not None:
                raise ValueError(
                    f"{name!r} is objc_method with isclass specified wraps classmethod"
                )
            isclass = True
            value = value.__wrapped__.__wrapped__
        else:
            value = value.__wrapped__

    if selname is None:
        # The 'name' does not fit into the selector naming
        # convention, and nothing provided a better name.
        #
        # Assume this is meant to be a regular python method.
        if isclass:
            return classmethod(value)
        return value

    argcount = selname.count(b":")

    if signature is None:
        # Calculate a default signature based on the selector shape
        if isinstance(value, (types.FunctionType, types.MethodType)):
            returns_object = returns_value(value)
        else:
            returns_object = True

        signature = (
            (objc._C_ID if returns_object else objc._C_VOID)
            + objc._C_ID
            + objc._C_SEL
            + (objc._C_ID * argcount)
        )

    try:
        pysig = inspect.signature(value)
    except (ValueError, TypeError):
        pass
    else:
        pos = 0
        pos_default = 0
        kwonly = 0
        kwonly_default = 0
        has_var_pos = False

        for p in pysig.parameters.values():
            if p.kind == inspect.Parameter.KEYWORD_ONLY:
                kwonly += 1
                if p.default is not inspect.Parameter.empty:
                    kwonly_default += 1

            elif p.kind == inspect.Parameter.VAR_KEYWORD:
                pass

            elif p.kind == inspect.Parameter.VAR_POSITIONAL:
                has_var_pos = True

            else:
                pos += 1
                if p.default is not inspect.Parameter.empty:
                    pos_default += 1

        if kwonly - kwonly_default:
            # Calls from Obejctive-C to Python will never have keyword arguments,
            # therefore this callable is not compatible with use as a selector.
            raise ValueError(
                f"{value!r} has {kwonly - kwonly_default} keyword-only arguments without a default"
            )

        if not has_var_pos and (
            (pos < argcount + 1) or (pos - pos_default > argcount + 1)
        ):
            # 'value' does not have a '*arg' argument, and does not accept calls
            # with exactly 'argcount' arguments, therefore this callable is not
            # compatible with us as a selector.
            #
            # 'argcount' does not count the implicit self argument
            if pos_default:
                raise ValueError(
                    f"{selname.decode()!r} expects {argcount} arguments, "
                    f"{value!r} has between {pos-pos_default-1} and {pos-1} positional arguments"
                )
            else:
                raise ValueError(
                    f"{selname.decode()!r} expects {argcount} arguments, "
                    f"{value!r} has {pos-1} positional arguments"
                )

    return objc.selector(value, selname, signature, isclass)


def returns_value(func):
    """
    Return True if 'func' explicitly returns a value

    """
    # This will return False for functions where all explicit
    # returns are of the form "return" or "return None". The
    # latter is a false negative, but cannot be avoided with
    # bytecode inspection.

    prev = None
    for inst in dis.get_instructions(func):
        if inst.opname == "RETURN_VALUE":
            assert prev is not None
            if prev.opname == "LOAD_CONST" and prev.arg != 0:
                return True

        prev = inst

    return False


def default_selector(name):
    """
    Returns a byte string with the selector for 'name',
    or None if there is no default selector
    """
    if "_" in name and not name.endswith("_"):
        return None
    if "__" in name:
        return None

    return name.replace("_", ":").encode()


class objc_method:
    """
    Decorator that marks a method that should definitely
    be represented as an Objective-C selector

    This decorator can be used in two ways:

    - Without parens:

        @objc_method
        def someMethod(self): ...

    - With parens:

        @objc_method()
        def someMethod(self): ...

    In the second form a number of keyword-only arguments can
    be used:

    - selname [bytes]: Objective-C selector name for the method
    - signature [bytes]: Objective-C type encoding for the method
    - isclass [bool]: Determines if the value is a class method

    When these attributes are not provided they will be calculated
    from the context (name, callable, class to which this
    method is added)
    """

    __slots__ = ("__wrapped__", "selector", "signature", "isclass")

    def __init__(self, value=None, *, selector=None, signature=None, isclass=None):
        self.__wrapped__ = value
        if self.__wrapped__ is not None:
            if not callable(self.__wrapped__) and not isinstance(
                self.__wrapped__, classmethod
            ):
                raise TypeError("'value' is not a callable")

        self.selector = selector
        self.signature = signature
        self.isclass = isclass

    def __call__(self, *args, **kwds):
        if self.__wrapped__ is None:
            if len(kwds) != 0:
                raise TypeError("Unexpected keyword arguments")
            if len(args) != 1:
                raise TypeError("Expecting exactly 1 argument")
            self.__wrapped__ = args[0]
            if not callable(self.__wrapped__) and not isinstance(
                self.__wrapped__, classmethod
            ):
                raise TypeError("'value' is not a callable")
            return self

        return self.__wrapped__(*args, **kwds)


class python_method:
    """
    Decorator that marks a method that should definitely
    not be represented as an Objective-C selector

    This decorator can be used in two ways:

    - Without parens:

        @python_method
        def someMethod(self): ...

    - With parens:

        @python_method()
        def someMethod(self): ...

    The second form has no keyword arguments and is
    provided for compatibility with objc_method.
    """

    __slots__ = ("__wrapped__",)

    def __init__(self, value=None):
        self.__wrapped__ = value
        if self.__wrapped__ is not None:
            if not callable(self.__wrapped__) and not isinstance(
                self.__wrapped__, classmethod
            ):
                raise TypeError("'value' is not a callable")

    def __call__(self, *args, **kwds):
        if self.__wrapped__ is None:
            if len(kwds) != 0:
                raise TypeError("Unexpected keyword arguments")
            if len(args) != 1:
                raise TypeError("Expecting exactly 1 argument")
            self.__wrapped__ = args[0]
            if not callable(self.__wrapped__) and not isinstance(
                self.__wrapped__, classmethod
            ):
                raise TypeError("'value' is not a callable")
            return self

        return self.__wrapped__(*args, **kwds)


objc.options._transformCallable = transformCallable
