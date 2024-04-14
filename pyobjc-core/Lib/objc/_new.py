"""
Implementation of `__new__` for arbitrary Cocoa classes
"""

__all__ = ()

NEW_MAP = {}
UNSET = object()

# XXX: Need to find a way to dynamically set the docstring


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

            if name.startswith("init") and len(name) == 4 or name[4].isupper():
                return getattr(cls.alloc(), name)(**kwds)

            else:
                return getattr(cls, name)(**kwds)

        if key:
            raise TypeError(
                f"{cls.__name__}() does not support keyword arguments {', '.join(repr(k) for k in key)}"
            )
        else:
            raise TypeError(f"{cls.__name__}() requires keyword arguments")

    __new__.__name__ = cls.__name__ + ".__new__"
    __new__.__qualname__ = cls.__name__ + ".__new__"
    __new__.__module__ = cls.__module__
    return __new__
