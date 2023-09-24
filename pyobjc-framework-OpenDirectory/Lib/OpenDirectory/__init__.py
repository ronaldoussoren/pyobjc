"""
Wrappers for the OpenDirectory framework
"""


def _setup():
    import sys

    import Foundation
    import CFOpenDirectory
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="OpenDirectory",
        frameworkIdentifier="com.apple.OpenDirectory",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/OpenDirectory.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            CFOpenDirectory,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["OpenDirectory._metadata"]


globals().pop("_setup")()
