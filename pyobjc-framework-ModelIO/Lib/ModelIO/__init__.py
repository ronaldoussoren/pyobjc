"""
Python mapping for the ModelIO framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import Quartz
    import objc
    from . import _metadata, _ModelIO

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="ModelIO",
        frameworkIdentifier="com.apple.ModelIO",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/ModelIO.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _ModelIO,
            AppKit,
            Quartz,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("MDLMaterialProperty", b"init"),
        ("MDLMaterialPropertyConnection", b"init"),
        ("MDLMaterialPropertyNode", b"init"),
        ("MDLMaterialPropertyNode", b"init"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["ModelIO._metadata"]


globals().pop("_setup")()
