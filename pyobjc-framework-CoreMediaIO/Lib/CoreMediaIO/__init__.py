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
