"""
Python mapping for the MapKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import CoreLocation
    import Quartz
    import objc
    from . import _metadata, _MapKit
    from ._inlines import _inline_list_

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MapKit",
        frameworkIdentifier="com.apple.MapKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MapKit.framework"
        ),
        globals_dict=globals(),
        inline_list=_inline_list_,
        parents=(
            _MapKit,
            AppKit,
            CoreLocation,
            Quartz,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("MKMapConfiguration", b"init"),
        ("MKMapConfiguration", b"new"),
        ("MKLocalPointsOfInterestRequest", b"init"),
        ("MKLocalPointsOfInterestRequest", b"new"),
        ("MKLookAroundSnapshotter", b"init"),
        ("MKLookAroundSnapshotter", b"new"),
        ("MKLookAroundSceneRequest", b"init"),
        ("MKLookAroundSceneRequest", b"new"),
        ("MKLookAroundScene", b"init"),
        ("MKLookAroundScene", b"new"),
        ("MKClusterAnnotation", b"init"),
        ("MKClusterAnnotation", b"new"),
        ("MKAddress", b"init"),
        ("MKAddress", b"new"),
        ("MKAddressRepresentations", b"init"),
        ("MKAddressRepresentations", b"new"),
        ("MKGeocodingRequest", b"init"),
        ("MKGeocodingRequest", b"new"),
        ("MKReverseGeocodingRequest", b"init"),
        ("MKReverseGeocodingRequest", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["MapKit._metadata"]


globals().pop("_setup")()
