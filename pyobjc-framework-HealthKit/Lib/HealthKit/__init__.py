"""
Python mapping for the HealthKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _HealthKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="HealthKit",
        frameworkIdentifier="com.apple.HealthKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/HealthKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _HealthKit,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("HKQuantity", b"init"),
        ("HKAttachment", b"init"),
        ("HKAttachment", b"new"),
        ("HKVerifiableClinicalRecord", b"init"),
        ("HKVerifiableClinicalRecord", b"new"),
        ("HKFHIRVersion", b"init"),
        ("HKSeriesBuilder", b"init"),
        ("HKObject", b"init"),
        ("HKUnit", b"init"),
        ("HKQueryAnchor", b"init"),
        ("HKAudiogramSensitivityPoint", b"init"),
        ("HKSourceRevision", b"init"),
        ("HKQuery", b"init"),
        ("HKVisionPrescription", b"init"),
        ("HKVisionPrescription", b"new"),
        ("HKClinicalRecord", b"init"),
        ("HKClinicalRecord", b"new"),
        ("HKCategorySample", b"init"),
        ("HKLiveWorkoutDataSource", b"init"),
        ("HKVerifiableClinicalRecordSubject", b"init"),
        ("HKVerifiableClinicalRecordSubject", b"new"),
        ("HKLiveWorkoutBuilder", b"initWithHealthStore:configuration:device:"),
        ("HKWorkoutBuilder", b"init"),
        ("HKGlassesPrescription", b"init"),
        ("HKGlassesPrescription", b"new"),
        (
            "HKGlassesPrescription",
            b"prescriptionWithType:dateIssued:expirationDate:device:metadata:",
        ),
        ("HKWorkoutActivity", b"init"),
        ("HKWorkoutActivity", b"new"),
        ("HKDevice", b"init"),
        ("HKWorkoutSession", b"init"),
        ("HKQueryDescriptor", b"init"),
        ("HKQueryDescriptor", b"new"),
        ("HKContactsPrescription", b"init"),
        ("HKContactsPrescription", b"new"),
        (
            "HKContactsPrescription",
            b"prescriptionWithType:dateIssued:expirationDate:device:metadata:",
        ),
        ("HKContactsLensSpecification", b"init"),
        ("HKContactsLensSpecification", b"new"),
        ("HKQuantitySeriesSampleBuilder", b"init"),
        ("HKVerifiableClinicalRecordQuery", b"init"),
        ("HKVerifiableClinicalRecordQuery", b"new"),
        ("HKLensSpecification", b"init"),
        ("HKLensSpecification", b"new"),
        ("HKFHIRResource", b"init"),
        ("HKDeletedObject", b"init"),
        ("HKStatistics", b"init"),
        ("HKVisionPrism", b"init"),
        ("HKVisionPrism", b"new"),
        ("HKSource", b"init"),
        ("HKObjectType", b"init"),
        ("HKWorkoutEvent", b"init"),
        ("HKStatisticsCollection", b"init"),
        ("HKGlassesLensSpecification", b"init"),
        ("HKGlassesLensSpecification", b"new"),
        ("HKAudiogramSensitivityPointClampingRange", b"init"),
        ("HKAudiogramSensitivityPointClampingRange", b"new"),
        ("HKAudiogramSensitivityTes", b"init"),
        ("HKAudiogramSensitivityTes", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["HealthKit._metadata"]


globals().pop("_setup")()
