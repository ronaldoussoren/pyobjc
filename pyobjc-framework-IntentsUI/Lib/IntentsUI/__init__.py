"""
Python mapping for the IntentsUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Intents
    import objc
    from . import _metadata, _IntentsUI

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="IntentsUI",
        frameworkIdentifier="com.apple.IntentsUI",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/IntentsUI.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _IntentsUI,
            Intents,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("INUIAddVoiceShortcutViewController", b"init"),
        ("INUIAddVoiceShortcutViewController", b"initWithNibName:bundle:"),
        ("INUIEditVoiceShortcutViewController", b"init"),
        ("INUIEditVoiceShortcutViewController", b"initWithNibName:bundle:"),
        ("INUIAddVoiceShortcutButton", b"init"),
        ("INUIAddVoiceShortcutButton", b"initWithFrame:"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["IntentsUI._metadata"]


globals().pop("_setup")()
