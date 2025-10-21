"""
Python mapping for the AVRouting framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _AVRouting

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="AVRouting",
        frameworkIdentifier="com.apple.AVRouting",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/AVRouting.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_AVRouting, Foundation),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("AVCustomRoutingPartialIP", b"init"),
        ("AVCustomRoutingPartialIP", b"new"),
        ("AVRoutingPlaybackArbiter", b"init"),
        ("AVRoutingPlaybackArbiter", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["AVRouting._metadata"]


globals().pop("_setup")()
