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
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["FSKit._metadata"]


globals().pop("_setup")()
