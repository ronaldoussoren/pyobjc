"""
Python mapping for the LaunchServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import warnings

    import CoreServices
    import objc

    warnings.warn(
        "pyobjc-framework-LaunchServices is deprecated, use 'import CoreServices' instead",
        DeprecationWarning,
        stacklevel=2,
    )

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="LaunchServices",
        frameworkIdentifier="com.apple.CoreServices",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreServices.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(CoreServices,),
        metadict={},
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func


globals().pop("_setup")()


from CoreServices import _LSCopyAllApplicationURLs  # isort:skip   # noqa: F401,E402
