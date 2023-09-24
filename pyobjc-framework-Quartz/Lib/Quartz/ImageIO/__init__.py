"""
Python mapping for the ImageIO framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    from Quartz import CoreGraphics
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Quartz.ImageIO",
        frameworkIdentifier="com.apple.ApplicationServices",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/ApplicationServices.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(CoreGraphics,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Quartz.ImageIO._metadata"]


globals().pop("_setup")()
