"""
Python mapping for the ImageKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import objc
    from . import _metadata, _imagekit

    if objc.macos_available(14, 0):
        identifier = "com.apple.quartzframework"
    elif objc.macos_available(13, 0):
        identifier = "com.apple.Quartz"
    else:
        identifier = "com.apple.quartzframework"

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Quartz.ImageKit",
        frameworkIdentifier=identifier,
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Quartz.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _imagekit,
            AppKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Quartz.ImageKit._metadata"]

    objc.addConvenienceForBasicMapping("IKImageBrowserGridGroup", False)
    objc.addConvenienceForBasicMapping("IKImageCell", False)
    objc.addConvenienceForBasicMapping("IKImageState", False)
    objc.addConvenienceForBasicSequence("IKLinkedList", True)


globals().pop("_setup")()
