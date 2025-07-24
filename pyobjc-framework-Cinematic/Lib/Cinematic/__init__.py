"""
Python mapping for the Cinematic framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Foundation
    import AVFoundation
    import CoreMedia
    import Metal

    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Cinematic",
        frameworkIdentifier="com.apple.Cinematic",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Cinematic.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation, AVFoundation, CoreMedia, Metal),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("CNDetection", b"init"),
        ("CNDetection", b"new"),
        ("CNScript", b"init"),
        ("CNScript", b"new"),
        ("CNScriptChanges", b"init"),
        ("CNScriptChanges", b"new"),
        ("CNScriptFrame", b"init"),
        ("CNScriptFrame", b"new"),
        ("CNDetectionTrack", b"init"),
        ("CNDetectionTrack", b"new"),
        ("CNDecision", b"init"),
        ("CNDecision", b"new"),
        ("CNObjectTracker", b"init"),
        ("CNObjectTracker", b"new"),
        ("CNAssetInfo", b"init"),
        ("CNAssetInfo", b"new"),
        ("CNRenderingSessionAttributes", b"init"),
        ("CNRenderingSessionAttributes", b"new"),
        ("CNRenderingSessionFrameAttributes", b"init"),
        ("CNRenderingSessionFrameAttributes", b"new"),
        ("CNRenderingSession", b"init"),
        ("CNRenderingSession", b"new"),
        ("CNAssetSpatialAudioInfo", b"init"),
        ("CNAssetSpatialAudioInfo", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["Cinematic._metadata"]


globals().pop("_setup")()
