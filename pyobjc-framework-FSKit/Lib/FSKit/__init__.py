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
        ("FSClient", "init"),
        ("FSClient", "new"),
        ("FSContainerStatus", "init"),
        ("FSContainerStatus", "new"),
        ("FSFileName", "init"),
        ("FSFileName", "new"),
        ("FSMutableFileDataBuffer", "init"),
        ("FSMutableFileDataBuffer", "new"),
        ("FSResource", "init"),
        ("FSResource", "new"),
        ("FSMetadataRange", "init"),
        ("FSMetadataRange", "new"),
        ("FSProbeResult", "init"),
        ("FSProbeResult", "new"),
        ("FSTaskOptions", "init"),
        ("FSTaskOptions", "new"),
        ("FSDirectoryEntryPacker", "init"),
        ("FSDirectoryEntryPacker", "new"),
        ("FSVolume", "init"),
        ("FSVolume", "new"),
        ("FSStatFSResult", "init"),
        ("FSStatFSResult", "new"),
        ("FSExtentPacker", "init"),
        ("FSExtentPacker", "new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["FSKit._metadata"]


globals().pop("_setup")()
