"""
Python mapping for the SensitiveContentAnalysis framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Foundation
    import Quartz
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SensitiveContentAnalysis",
        frameworkIdentifier="com.apple.SensitiveContentAnalysis",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/SensitiveContentAnalysis.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation, Quartz),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("SCVideoStreamAnalyzer", b"new"),
        ("SCVideoStreamAnalyzer", b"init"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["SensitiveContentAnalysis._metadata"]


globals().pop("_setup")()
