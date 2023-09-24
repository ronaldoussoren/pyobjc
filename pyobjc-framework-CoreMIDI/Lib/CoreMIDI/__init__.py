"""
Python mapping for the CoreMIDI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _CoreMIDI
    from ._inlines import _inline_list_

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CoreMIDI",
        frameworkIdentifier="com.apple.audio.midi.CoreMIDI",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreMIDI.framework"
        ),
        globals_dict=globals(),
        inline_list=_inline_list_,
        parents=(
            _CoreMIDI,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["CoreMIDI._metadata"]


globals().pop("_setup")()
