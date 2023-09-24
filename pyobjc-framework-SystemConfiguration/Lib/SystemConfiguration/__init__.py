"""
Python mapping for the SystemConfiguration framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _manual

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SystemConfiguration",
        frameworkIdentifier="com.apple.SystemConfiguration",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/SystemConfiguration.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _manual,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["SystemConfiguration._metadata"]


globals().pop("_setup")()

from . import SCNetworkInterfaceRef  # isort: skip  # noqa: E402

SCBondInterfaceRef = SCNetworkInterfaceRef
SCVLANInterfaceRef = SCNetworkInterfaceRef
