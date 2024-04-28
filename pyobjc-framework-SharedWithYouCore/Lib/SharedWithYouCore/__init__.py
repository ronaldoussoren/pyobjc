"""
Python mapping for the SharedWithYouCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import objc
    from . import _metadata, _SharedWithYouCore

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SharedWithYouCore",
        frameworkIdentifier="com.apple.SharedWithYouCore",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/SharedWithYouCore.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _SharedWithYouCore,
            AppKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("SWUpdateCollaborationParticipantsAction", b"init"),
        ("SWUpdateCollaborationParticipantsAction", b"new"),
        ("SWPersonIdentity", b"init"),
        ("SWPersonIdentity", b"new"),
        ("SWPerson", b"init"),
        ("SWPerson", b"new"),
        ("SWPersonIdentityProof", b"init"),
        ("SWPersonIdentityProof", b"new"),
        ("SWCollaborationMetadata", b"init"),
        ("SWCollaborationMetadata", b"new"),
        ("SWCollaborationOption", b"init"),
        ("SWCollaborationOption", b"new"),
        ("SWStartCollaborationAction", b"init"),
        ("SWStartCollaborationAction", b"new"),
        ("SWCollaborationOptionsGroup", b"init"),
        ("SWCollaborationOptionsGroup", b"new"),
        ("SWCollaborationShareOptions", b"init"),
        ("SWCollaborationShareOptions", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["SharedWithYouCore._metadata"]


globals().pop("_setup")()
