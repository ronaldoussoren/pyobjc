"""
Python mapping for the SoundAnalysis framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SoundAnalysis",
        frameworkIdentifier="com.apple.SoundAnalysis",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/SoundAnalysis.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("SNTimeDurationConstraint", b"init"),
        ("SNTimeDurationConstraint", b"new"),
        ("SNClassification", b"init"),
        ("SNClassification", b"new"),
        ("SNClassificationResult", b"init"),
        ("SNClassificationResult", b"new"),
        ("SNClassifySoundRequest", b"init"),
        ("SNClassifySoundRequest", b"new"),
        ("SNAudioStreamAnalyzer", b"init"),
        ("SNAudioFileAnalyzer", b"init"),
        ("SNAudioStreamAnalyzer", b"init"),
        ("SNAudioFileAnalyzer", b"init"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["SoundAnalysis._metadata"]


globals().pop("_setup")()
