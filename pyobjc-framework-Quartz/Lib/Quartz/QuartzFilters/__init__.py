"""
Python mapping for the QuartzCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Quartz.QuartzFilters",
        frameworkIdentifier="com.apple.quartzframework",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Quartz.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Quartz.QuartzFilters._metadata"]


globals().pop("_setup")()
