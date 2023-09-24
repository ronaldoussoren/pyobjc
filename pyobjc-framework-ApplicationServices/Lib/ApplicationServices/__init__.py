"""
Python mapping for the ApplicationServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import CoreText
    import HIServices
    import Quartz
    import objc

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="ApplicationServices",
        frameworkIdentifier="com.apple.ApplicationServices",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/ApplicationServices.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Quartz, HIServices, CoreText),
        metadict={},
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func


globals().pop("_setup")()
