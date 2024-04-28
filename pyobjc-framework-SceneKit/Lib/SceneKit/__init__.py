"""
Python mapping for the SceneKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import Quartz
    import objc
    from . import _metadata, _SceneKit
    from ._inlines import _inline_list_

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SceneKit",
        frameworkIdentifier="com.apple.SceneKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/SceneKit.framework"
        ),
        globals_dict=globals(),
        inline_list=_inline_list_,
        parents=(
            _SceneKit,
            AppKit,
            Quartz,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (("SCNAudioPlayer", b"init"),):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["SceneKit._metadata"]

    import SceneKit as mod  # isort:skip

    global SCNMatrix4Identity, SCNMatrix4MakeTranslation, SCNMatrix4MakeScale
    try:
        mod.SCNMatrix4Identity
    except AttributeError:
        # Two "inline" functions that use a symbol that is available on 10.10 or later,
        # avoid crashes by removing the inline function wrappers when that symbol
        # is not available.
        try:
            mod.SCNMatrix4MakeTranslation
            del mod.SCNMatrix4MakeTranslation
        except AttributeError:
            pass

        try:
            mod.SCNMatrix4MakeScale
            del mod.SCNMatrix4MakeScale
        except AttributeError:
            pass


globals().pop("_setup")()
