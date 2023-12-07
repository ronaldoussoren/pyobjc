"""
Python mapping for the Security framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _Security

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Security",
        frameworkIdentifier="com.apple.security",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Security.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _Security,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Security._metadata"]

    # The type encoding for older versions of macOS (at least
    # up to 10.11)

    if objc.macos_available(10, 10):
        from . import SecAccessControlGetTypeID  # isort:skip

        objc.registerCFSignature(
            "SecAccessControl",
            b"^{OpaqueSecAccessControl=}",
            SecAccessControlGetTypeID(),
        )

    from . import SecTrustedApplicationGetTypeID  # isort:skip

    objc.registerCFSignature(
        "SecTrustedApplicationRef",
        b"^{OpaqueSecTrustedApplicationRef=}",
        SecTrustedApplicationGetTypeID(),
    )

    from . import SecCertificateGetTypeID  # isort:skip

    objc.registerCFSignature(
        "SecCertificateRef",
        b"^{OpaqueSecCertificateRef=}",
        SecCertificateGetTypeID(),
    )

    from . import SecAccessGetTypeID  # isort:skip

    objc.registerCFSignature(
        "SecAccessRef", b"^{OpaqueSecAccessRef=}", SecAccessGetTypeID()
    )

    from . import SecIdentityGetTypeID  # isort:skip

    objc.registerCFSignature(
        "SecIdentityRef", b"^{OpaqueSecIdentityRef=}", SecIdentityGetTypeID()
    )

    from . import SecIdentitySearchGetTypeID  # isort:skip

    objc.registerCFSignature(
        "SecIdentitySearchRef",
        b"^{OpaqueSecIdentitySearchRef=}",
        SecIdentitySearchGetTypeID(),
    )

    from . import SecTrustedApplicationGetTypeID  # isort:skip

    objc.registerCFSignature(
        "SecTrustedApplicationRef",
        b"^{OpaqueSecAccessControlRef=}",
        SecTrustedApplicationGetTypeID(),
    )


globals().pop("_setup")()
