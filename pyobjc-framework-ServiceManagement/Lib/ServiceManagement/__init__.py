"""
Python mapping for the ServiceManagement framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import CoreFoundation
    import objc
    from . import _metadata

    if objc.macos_available(10, 10):  # pragma: no branch
        identifier = "com.apple.xpc.ServiceManagement"
    else:
        identifier = "com.apple.bsd.ServiceManagement"  # pragma: no cover

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="ServiceManagement",
        frameworkIdentifier=identifier,
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/ServiceManagement.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(CoreFoundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["ServiceManagement._metadata"]


globals().pop("_setup")()
