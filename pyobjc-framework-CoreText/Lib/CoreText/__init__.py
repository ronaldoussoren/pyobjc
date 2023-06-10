"""
Python mapping for the CoreText framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import CoreFoundation
    import Quartz
    import objc
    from . import _metadata, _manual

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CoreText",
        frameworkIdentifier="com.apple.CoreText",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreText.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_manual, CoreFoundation, Quartz),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["CoreText._metadata"]


globals().pop("_setup")()
