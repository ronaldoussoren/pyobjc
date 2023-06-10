"""
Python mapping for the SearchKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import CoreServices
    import objc
    import warnings

    warnings.warn(
        "pyobjc-framework-SearchKit is deprecated, use 'import CoreServices' instead",
        DeprecationWarning,
        stacklevel=2,
    )

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SearchKit",
        frameworkIdentifier=None,
        frameworkPath=None,
        globals_dict=globals(),
        inline_list=None,
        parents=(CoreServices,),
        metadict={},
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func


globals().pop("_setup")()
