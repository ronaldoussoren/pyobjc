"""
Python mapping for the Accessibility framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Quartz
    from . import _metadata, _Accessibility

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Accessibility",
        frameworkIdentifier="com.apple.Accessibility",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Accessibility.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_Accessibility, Quartz),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls in (
        "AXNumericDataAxisDescriptor",
        "AXDataPointValue",
        "AXDataPoint",
        "AXChartDescriptor",
    ):
        try:
            objc.lookUpClass(cls).__objc_final__ = True
        except objc.error:
            pass

    for cls, sel in (
        ("AXNumericDataAxisDescriptor", b"init"),
        ("AXNumericDataAxisDescriptor", b"new"),
        ("AXCategoricalDataAxisDescriptor", b"init"),
        ("AXCategoricalDataAxisDescriptor", b"new"),
        ("AXDataPointValue", b"init"),
        ("AXDataPointValue", b"new"),
        ("AXDataPoint", b"init"),
        ("AXDataPoint", b"new"),
        ("AXDataSeriesDescriptor", b"init"),
        ("AXDataSeriesDescriptor", b"new"),
        ("AXChartDescriptor", b"init"),
        ("AXChartDescriptor", b"new"),
        ("AXCustomContent", b"init"),
        ("AXCustomContent", b"new"),
        ("AXBrailleMap", b"init"),
        ("AXBrailleMap", b"new"),
        ("AXRequest", b"init"),
        ("AXRequest", b"new"),
        ("AXFeatureOverrideSession", b"init"),
        ("AXFeatureOverrideSession", b"new"),
        ("AXFeatureOverrideSessionManager", b"init"),
        ("AXFeatureOverrideSessionManager", b"new"),
        ("AXBrailleTable", b"init"),
        ("AXBrailleTable", b"new"),
        ("AXBrailleTranslationResult", b"init"),
        ("AXBrailleTranslationResult", b"new"),
        ("AXBrailleTranslator", b"init"),
        ("AXBrailleTranslator", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["Accessibility._metadata"]


globals().pop("_setup")()
