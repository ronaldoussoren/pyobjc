"""
Python mapping for the CoreServices/CarbonCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.

Note that PyObjC only wrappers the non-deprecated parts of the CoreServices
framework.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata
    from .._inlines import _inline_list_

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CoreServices.CarbonCore",
        frameworkIdentifier="com.apple.CarbonCore",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreServices.framework"
        ),
        globals_dict=globals(),
        inline_list=_inline_list_,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["CoreServices.CarbonCore._metadata"]


globals().pop("_setup")()
