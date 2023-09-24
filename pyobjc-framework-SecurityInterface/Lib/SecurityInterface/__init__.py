"""
Python mapping for the SecurityInterface framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import Security
    import objc
    from . import _metadata, _SecurityInterface

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SecurityInterface",
        frameworkIdentifier="com.apple.securityinterface",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/SecurityInterface.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _SecurityInterface,
            Security,
            AppKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["SecurityInterface._metadata"]


globals().pop("_setup")()
