"""
Python mapping for the Vision framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import Quartz
    import CoreML
    import objc
    from . import _metadata, _Vision

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Vision",
        frameworkIdentifier="com.apple.VN",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Vision.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _Vision,
            Quartz,
            CoreML,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("VNVideoProcessorFrameRateCadence", b"init"),
        ("VNVideoProcessorTimeIntervalCadence", b"init"),
        ("VNVideoProcessor", b"init"),
        (
            "VNGeneratePersonSegmentationRequest",
            b"initWithFrameAnalysisSpacing:completionHandler:",
        ),
        ("VNDetectedPoint", b"init"),
        ("VNDetectedPoint", b"new"),
        ("VNDetectedPoint", b"initWithX:y:"),
        ("VNDetectedPoint", b"initWithLocation:"),
        ("VNFaceLandmarkRegion", b"init"),
        ("VNFaceLandmarkRegion", b"new"),
        ("VNFaceLandmarks", b"init"),
        ("VNCoreMLModel", b"init"),
        ("VNCoreMLRequest", b"init"),
        ("VNCoreMLRequest", b"initWithCompletionHandler:"),
        ("VNTrackingRequest", b"init"),
        ("VNTrackingRequest", b"initWithCompletionHandler:"),
        ("VNHumanBodyRecognizedPoint3D", b"init"),
        ("VNHumanBodyRecognizedPoint3D", b"new"),
        ("VNImageRequestHandler", b"init"),
        ("VNPoint3D", b"init"),
        ("VNContour", b"init"),
        ("VNContour", b"new"),
        ("VNRecognizedPointsObservation", b"init"),
        ("VNRecognizedPointsObservation", b"new"),
        ("VNRecognizedPoints3DObservation", b"init"),
        ("VNRecognizedPoints3DObservation", b"new"),
        ("VNTrackObjectRequest", b"init"),
        ("VNTrackObjectRequest", b"initWithCompletionHandler:"),
        ("VNTargetedImageRequest", b"init"),
        ("VNTargetedImageRequest", b"initWithCompletionHandler:"),
        (
            "VNDetectTrajectoriesRequest",
            b"initWithFrameAnalysisSpacing:completionHandler:",
        ),
        ("VNTrackRectangleRequest", b"init"),
        ("VNTrackRectangleRequest", b"initWithCompletionHandler:"),
        ("VNStatefulRequest", b"init"),
        ("VNStatefulRequest", b"initWithCompletionHandler:"),
        ("VNStatefulRequest", b"new"),
        ("VNRecognizedPoint3D", b"init"),
        ("VNRecognizedPoint3D", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["Vision._metadata"]


globals().pop("_setup")()
