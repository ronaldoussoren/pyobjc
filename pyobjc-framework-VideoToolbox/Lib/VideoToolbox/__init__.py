"""
Python mapping for the VideoToolbox framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Quartz
    import CoreMedia
    import Foundation
    import objc
    from . import _metadata, _VideoToolbox

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="VideoToolbox",
        frameworkIdentifier="com.apple.VideoToolbox",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/VideoToolbox.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _VideoToolbox,
            Quartz,
            CoreMedia,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls in (
        "VTFrameProcessor",
        "VTFrameProcessorFrame",
        "VTFrameProcessorOpticalFlow",
        "VTFrameRateConversionConfiguration",
        "VTFrameRateConversionParameters",
        "VTMotionBlurConfiguration",
        "VTMotionBlurParameters",
        "VTOpticalFlowConfiguration",
        "VTOpticalFlowParameters",
    ):
        try:
            objc.lookUpClass(cls).__objc_final__ = True
        except objc.error:
            pass

    for cls, sel in (
        ("VTFrameProcessorFrame", b"init"),
        ("VTFrameProcessorFrame", b"new"),
        ("VTFrameProcessorOpticalFlow", b"init"),
        ("VTFrameProcessorOpticalFlow", b"new"),
        ("VTFrameRateConversionConfiguration", b"init"),
        ("VTFrameRateConversionConfiguration", b"new"),
        ("VTFrameRateConversionParameters", b"init"),
        ("VTFrameRateConversionParameters", b"new"),
        ("VTMotionBlurConfiguration", b"init"),
        ("VTMotionBlurConfiguration", b"new"),
        ("VTMotionBlurParameters", b"init"),
        ("VTMotionBlurParameters", b"new"),
        ("VTOpticalFlowConfiguration", b"init"),
        ("VTOpticalFlowConfiguration", b"new"),
        ("VTOpticalFlowParameters", b"init"),
        ("VTOpticalFlowParameters", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["VideoToolbox._metadata"]


globals().pop("_setup")()
