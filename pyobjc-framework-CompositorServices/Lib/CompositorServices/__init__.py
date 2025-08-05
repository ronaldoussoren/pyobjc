"""
Python mapping for the CompositorServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Metal
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CompositorServices",
        frameworkIdentifier="com.apple.CompositorServices",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CompositorServices.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Metal,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls in (
        "CP_OBJECT_cp_layer_renderer_properties",
        "CP_OBJECT_cp_layer_renderer",
    ):
        try:
            objc.lookUpClass(cls).__objc_final__ = True
        except objc.error:
            pass

    for cls, sel in (
        ("CP_OBJECT_cp_layer_renderer_properties", b"init"),
        ("CP_OBJECT_cp_layer_renderer_properties", b"new"),
        ("CP_OBJECT_cp_layer_renderer", b"init"),
        ("CP_OBJECT_cp_layer_renderer", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["CompositorServices._metadata"]


globals().pop("_setup")()
