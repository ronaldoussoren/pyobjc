"""
Python mapping for the Photos framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import objc
    from . import _metadata, _PhotosUI

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="PhotosUI",
        frameworkIdentifier="com.apple.PhotosUI",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/PhotosUI.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _PhotosUI,
            AppKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("PHProjectInfo", b"init"),
        ("PHProjectInfo", b"new"),
        ("PHProjectSection", b"init"),
        ("PHProjectSection", b"new"),
        ("PHProjectSectionContent", b"init"),
        ("PHProjectSectionContent", b"new"),
        ("PHProjectElement", b"init"),
        ("PHProjectElement", b"new"),
        ("PHProjectRegionOfInterest", b"init"),
        ("PHProjectRegionOfInterest", b"new"),
        ("PHPickerFilter", b"init"),
        ("PHPickerFilter", b"new"),
        ("PHPickerResult", b"init"),
        ("PHPickerResult", b"new"),
        ("PHPickerViewController", b"init"),
        ("PHPickerViewController", b"initWithNibName:bundle:"),
        ("PHPickerViewController", b"initWithCoder:"),
        ("PHPickerViewController", b"new"),
        ("PHProjectTypeDescription", b"init"),
        ("PHProjectTypeDescription", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["PhotosUI._metadata"]

    for cls_name in (
        "PHPickerFilter",
        "PHPickerConfiguration",
        "PHPickerResult",
        "PHPickerViewController",
    ):
        try:
            cls = objc.lookUpClass(cls_name)
            cls.__objc_final__ = True
        except objc.error:
            pass


globals().pop("_setup")()
