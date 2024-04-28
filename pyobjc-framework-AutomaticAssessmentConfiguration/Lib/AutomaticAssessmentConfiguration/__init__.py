"""
Python mapping for the AutomaticAssessmentConfiguration framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _AutomaticAssessmentConfiguration

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="AutomaticAssessmentConfiguration",
        frameworkIdentifier="com.apple.AutomaticAssessmentConfiguration",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _AutomaticAssessmentConfiguration,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("AEAssessmentApplication", b"init"),
        ("AEAssessmentApplication", b"new"),
        ("AEAssessmentSession", b"init"),
        ("AEAssessmentSession", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["AutomaticAssessmentConfiguration._metadata"]


globals().pop("_setup")()
