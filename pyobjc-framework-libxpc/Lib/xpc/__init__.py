"""
Python mapping for the xpc library on macOS

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _xpc

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="xpc",
        frameworkIdentifier=None,
        frameworkPath=None,
        globals_dict=globals(),
        inline_list=None,
        parents=(_xpc, Foundation),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["xpc._metadata"]


globals().pop("_setup")()
