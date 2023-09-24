"""
Python mapping for the MetalPerformanceShadersGraph framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import MetalPerformanceShaders
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MetalPerformanceShadersGraph",
        frameworkIdentifier="com.apple.MetalPerformanceShadersGraph",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MetalPerformanceShadersGraph.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(MetalPerformanceShaders,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["MetalPerformanceShadersGraph._metadata"]


globals().pop("_setup")()
