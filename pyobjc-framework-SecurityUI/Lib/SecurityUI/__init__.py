"""
Python mapping for the SecurityUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Security
    import AppKit
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SecurityUI",
        frameworkIdentifier="com.apple.SecurityUI",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/SecurityUI.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            Security,
            AppKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("SFCertificatePresentation", b"init"),
        ("SFCertificatePresentation", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["SecurityUI._metadata"]


globals().pop("_setup")()
