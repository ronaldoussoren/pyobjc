"""
Python mapping for the FSKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Foundation
    from . import _metadata, _FSKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="FSKit",
        frameworkIdentifier="com.apple.FSKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/FSKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _FSKit,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("FSClient", b"init"),
        ("FSClient", b"new"),
        ("FSContainerStatus", b"init"),
        ("FSContainerStatus", b"new"),
        ("FSFileName", b"init"),
        ("FSFileName", b"new"),
        ("FSMutableFileDataBuffer", b"init"),
        ("FSMutableFileDataBuffer", b"new"),
        ("FSResource", b"init"),
        ("FSResource", b"new"),
        ("FSMetadataRange", b"init"),
        ("FSMetadataRange", b"new"),
        ("FSProbeResult", b"init"),
        ("FSProbeResult", b"new"),
        ("FSTaskOptions", b"init"),
        ("FSTaskOptions", b"new"),
        ("FSDirectoryEntryPacker", b"init"),
        ("FSDirectoryEntryPacker", b"new"),
        ("FSVolume", b"init"),
        ("FSVolume", b"new"),
        ("FSStatFSResult", b"init"),
        ("FSStatFSResult", b"new"),
        ("FSExtentPacker", b"init"),
        ("FSExtentPacker", b"new"),
        ("FSGenericURLResource", b"init"),
        ("FSGenericURLResource", b"new"),
        ("FSPathURLResource", b"init"),
        ("FSPathURLResource", b"new"),
        ("FSContext", b"init"),
        ("FSContext", b"new"),
        ("FSActivateResult", b"init"),
        ("FSActivateResult", b"new"),
        ("FSLookupItemResult", b"init"),
        ("FSLookupItemResult", b"new"),
        ("FSCreateItemResult", b"init"),
        ("FSCreateItemResult", b"new"),
        ("FSCreateLinkResult", b"init"),
        ("FSCreateLinkResult", b"new"),
        ("FSRenameItemResult", b"init"),
        ("FSRenameItemResult", b"new"),
        ("FSRemoveItemResult", b"init"),
        ("FSRemoveItemResult", b"new"),
        ("FSGetAttributesResult", b"init"),
        ("FSGetAttributesResult", b"new"),
        ("FSSetAttributesResult", b"init"),
        ("FSSetAttributesResult", b"new"),
        ("FSEnumerateDirectoryResult", b"init"),
        ("FSEnumerateDirectoryResult", b"new"),
        ("FSReadSymlinkResult", b"init"),
        ("FSReadSymlinkResult", b"new"),
        ("FSGetXattrResult", b"init"),
        ("FSGetXattrResult", b"new"),
        ("FSSetXattrResult", b"init"),
        ("FSSetXattrResult", b"new"),
        ("FSListXattrsResult", b"init"),
        ("FSListXattrsResult", b"new"),
        ("FSReadFileResult", b"init"),
        ("FSReadFileResult", b"new"),
        ("FSWriteFileResult", b"init"),
        ("FSWriteFileResult", b"new"),
        ("FSCheckAccessResult", b"init"),
        ("FSCheckAccessResult", b"new"),
        ("FSVolumeRenameResult", b"init"),
        ("FSVolumeRenameResult", b"new"),
        ("FSPreallocateResult", b"init"),
        ("FSPreallocateResult", b"new"),
        ("FSDeactivateItemResult", b"init"),
        ("FSDeactivateItemResult", b"new"),
        ("FSSeekRegionResult", b"init"),
        ("FSSeekRegionResult", b"new"),
        ("FSBlockmapResult", b"init"),
        ("FSBlockmapResult", b"new"),
        ("FSCompleteIOResult", b"init"),
        ("FSCompleteIOResult", b"new"),
        ("FSOpenItemResult", b"init"),
        ("FSOpenItemResult", b"new"),
        ("FSUpgradeItemResult", b"init"),
        ("FSUpgradeItemResult", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["FSKit._metadata"]


globals().pop("_setup")()
