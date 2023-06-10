"""
Python mapping for the CoreServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.

Note that PyObjC only wrappers the non-deprecated parts of the CoreServices
framework.
"""


def _setup():
    import FSEvents
    from CoreServices import (
        CarbonCore,
        DictionaryServices,
        LaunchServices,
        Metadata,
        SearchKit,
    )
    import objc

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CoreServices",
        frameworkIdentifier="com.apple.CoreServices",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreServices.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            FSEvents,
            DictionaryServices,
            LaunchServices,
            SearchKit,
            Metadata,
            CarbonCore,
        ),
        metadict={},
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func


globals().pop("_setup")()


from .LaunchServices import _LSCopyAllApplicationURLs  # isort:skip # noqa: F401,E402
