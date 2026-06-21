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
        ("PHPickerSearchText", b"init"),
        ("PHPickerSearchText", b"new"),
        ("PHSharedAlbumCreationConfiguration", b"init"),
        ("PHSharedAlbumCreationConfiguration", b"new"),
        ("PHSharedAlbumCreationResult", b"init"),
        ("PHSharedAlbumCreationResult", b"new"),
        ("PHSharedAlbumCreationViewController", b"init"),
        ("PHSharedAlbumCreationViewController", b"initWithNibName:bundle:"),
        ("PHSharedAlbumCreationViewController", b"initWithCoder:"),
        ("PHSharedAlbumCreationViewController", b"new"),
        ("PHSharedAlbumCustomizationViewController", b"init"),
        ("PHSharedAlbumCustomizationViewController", b"initWithNibName:bundle:"),
        ("PHSharedAlbumCustomizationViewController", b"initWithCoder:"),
        ("PHSharedAlbumCustomizationViewController", b"new"),
        ("PHSharedAlbumPostingViewController", b"init"),
        ("PHSharedAlbumPostingViewController", b"initWithNibName:bundle:"),
        ("PHSharedAlbumPostingViewController", b"initWithCoder:"),
        ("PHSharedAlbumPostingViewController", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["PhotosUI._metadata"]


globals().pop("_setup")()
