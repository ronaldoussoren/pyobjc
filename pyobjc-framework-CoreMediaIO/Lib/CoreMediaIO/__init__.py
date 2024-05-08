"""
Python mapping for the CoreMediaIO framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _CoreMediaIO

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CoreMediaIO",
        frameworkIdentifier="com.apple.CoreMediaIO",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreMediaIO.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _CoreMediaIO,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("CMIOExtensionStreamProperties", b"init"),
        ("CMIOExtensionStreamProperties", b"new"),
        ("CMIOExtensionStream", b"init"),
        ("CMIOExtensionStream", b"new"),
        ("CMIOExtensionPropertyAttributes", b"init"),
        ("CMIOExtensionPropertyAttributes", b"new"),
        ("CMIOExtensionPropertyState", b"init"),
        ("CMIOExtensionPropertyState", b"new"),
        ("CMIOExtensionStreamCustomClockConfiguration", b"init"),
        ("CMIOExtensionStreamCustomClockConfiguration", b"new"),
        ("CMIOExtensionStreamFormat", b"init"),
        ("CMIOExtensionStreamFormat", b"new"),
        ("CMIOExtensionScheduledOutput", b"init"),
        ("CMIOExtensionScheduledOutput", b"new"),
        ("CMIOExtensionClient", b"init"),
        ("CMIOExtensionClient", b"new"),
        ("CMIOExtensionDeviceProperties", b"init"),
        ("CMIOExtensionDeviceProperties", b"new"),
        ("CMIOExtensionDevice", b"init"),
        ("CMIOExtensionDevice", b"new"),
        ("CMIOExtensionProviderProperties", b"init"),
        ("CMIOExtensionProviderProperties", b"new"),
        ("CMIOExtensionProvider", b"init"),
        ("CMIOExtensionProvider", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["CoreMediaIO._metadata"]


globals().pop("_setup")()


def CMIOGetNextSequenceNumber(value):
    if value == 0xFFFFFFFFFFFFFFFF:
        return 0
    return value + 1


from . import (  # isort:skip # noqa: E402
    kCMIOSampleBufferDiscontinuityFlag_DurationWasExtended,
)


def CMIODiscontinuityFlagsHaveHardDiscontinuities(value):
    return (value & kCMIOSampleBufferDiscontinuityFlag_DurationWasExtended) != 0
