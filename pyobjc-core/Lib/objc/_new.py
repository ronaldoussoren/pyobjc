"""
Implementation of `__new__` for arbitrary Cocoa classes

The __new__ method just translates invocations into the
corresponding invocation of the Cocoa pattern (
`cls.alloc().init()` or `cls.new()`), based on a mapping
maintaind in this file.

The mapping is updated in two ways:
    1. From framework bindings for native classes
    2. Based on `init` methods in Python subclasses

"""

# TODO:
# - Update support code for framework bindings
# - Update framework binding tooling (and then the
#   bindings themselves)
# - Document
# - Add tests [in progress]
# - Maybe: somehow add __doc__ to classes that reflect the
#   __new__ API.
# - Maybe: In 3.13 switch to MultiSignature instead of
#   __doc__ (assuming #117671 is merged)
#
# FIXME: __init__ invocation is a mess, consider trying
# to suppress its invocation. Currently: __init__ is
# invoked by the interpreter when __new__ is called, unless
# __new__ returns more than one value (e.g. has some output
# arguments, such as -[FooClass initWithValue:(int)value error:(NSError**)error]

__all__ = ()

# Mapping: cls -> { kwds: selector_name }
#
# That is, keys are Objective-C classes, values
# are mappings from keyword argument names to
# the name of a selector.
#
# The selector_name can be `None` to disable a
# mapping in a subclass.
#
# The complete mapping for a class is a chain map
# for the submaps of all classes on the MRO.
NEW_MAP = {}


# Sentinel value
UNSET = object()

# Added to the docstring for __new__
DOC_SUFFIX = "The order of keyword arguments is significant\n"


class _function:
    """
    Wrapper for the __new__ function to generate the
    docstring dynamically.
    """

    __slots__ = ("_function", "_cls")

    def __init__(self, function, cls):
        self._function = function
        self._cls = cls

    @property
    def __class__(self):
        return self._function.__class__

    @property
    def __doc__(self):
        result = {}
        for c in reversed(self._cls.__mro__):
            new_map = NEW_MAP.get(c, UNSET)
            if new_map is UNSET:
                continue

            for kwds, selector in new_map.items():
                if selector is None:
                    result.pop(kwds, None)

                if not kwds:
                    result[kwds] = f"{self._cls.__name__}(): "
                else:
                    result[kwds] = f"{self._cls.__name__}(*, " + ", ".join(kwds) + "): "
                if selector.startswith("init"):
                    result[kwds] += f"   returns cls.alloc().{selector}()\n\n"
                else:
                    result[kwds] += f"   returns cls.{selector}()\n\n"
        return "".join(sorted(result.values())) + DOC_SUFFIX

    def __getattr__(self, name):
        return getattr(self._function, name)

    def __setattr__(self, name, value):
        if name in ("_function", "_cls"):
            object.__setattr__(self, name, value)
        return setattr(self._function, name, value)

    def __call__(self, *args, **kwds):
        return self._function(*args, **kwds)


def _make_new(cls):
    def __new__(cls, **kwds):
        """
        Generic implementation for Objective-C `__new__`.
        """
        # XXX: should this sort the keywords?
        key = tuple(kwds.keys())

        for c in cls.__mro__:
            new_map = NEW_MAP.get(c, UNSET)
            if new_map is UNSET:
                continue

            name = new_map.get(key, UNSET)
            if name is UNSET:
                continue

            if name is None:
                if key:
                    raise TypeError(
                        f"{cls.__name__}() does not support keyword arguments {', '.join(repr(k) for k in key)}"
                    )
                else:
                    raise TypeError(f"{cls.__name__}() requires keyword arguments")

            args = [kwds[n] for n in key]
            if name.startswith("init") and len(name) == 4 or name[4].isupper():
                return getattr(cls.alloc(), name)(*args)

            else:
                return getattr(cls, name)(*args)

        if key:
            raise TypeError(
                f"{cls.__name__}() does not support keyword arguments {', '.join(repr(k) for k in key)}"
            )
        else:
            raise TypeError(f"{cls.__name__}() requires keyword arguments")

    # XXX: Settings these helps, but does not yet result in the correct
    #      output from help()
    __new__.__name__ = cls.__name__ + ".__new__"
    __new__.__qualname__ = cls.__name__ + ".__new__"
    __new__.__module__ = cls.__module__
    __new__._oc_generic_new = True
    return _function(__new__, cls)
