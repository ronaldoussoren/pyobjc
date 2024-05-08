"""
Python mapping for the Virtualization framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _Virtualization

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Virtualization",
        frameworkIdentifier="com.apple.Virtualization",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Virtualization.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _Virtualization,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("VZDirectoryShare", b"init"),
        ("VZDirectoryShare", b"new"),
        ("VZVirtioSoundDeviceStreamConfiguration", b"init"),
        ("VZVirtioSoundDeviceStreamConfiguration", b"new"),
        ("VZVirtioConsoleDevice", b"init"),
        ("VZVirtioConsoleDevice", b"new"),
        ("VZSharedDirectory", b"init"),
        ("VZSharedDirectory", b"new"),
        ("VZBootLoader", b"init"),
        ("VZBootLoader", b"new"),
        ("VZKeyboardConfiguration", b"init"),
        ("VZKeyboardConfiguration", b"new"),
        ("VZGraphicsDevice", b"init"),
        ("VZGraphicsDevice", b"new"),
        ("VZVirtioSocketDevice", b"init"),
        ("VZVirtioSocketDevice", b"new"),
        ("VZAudioDeviceConfiguration", b"init"),
        ("VZAudioDeviceConfiguration", b"new"),
        ("VZEntropyDeviceConfiguration", b"init"),
        ("VZEntropyDeviceConfiguration", b"new"),
        ("VZGraphicsDisplayConfiguration", b"init"),
        ("VZGraphicsDisplayConfiguration", b"new"),
        ("VZMacOSRestoreImage", b"init"),
        ("VZMacOSRestoreImage", b"new"),
        ("VZSerialPortAttachment", b"init"),
        ("VZSerialPortAttachment", b"new"),
        ("VZVirtioSocketConnection", b"init"),
        ("VZVirtioSocketConnection", b"new"),
        ("VZVirtioConsolePortConfigurationArray", b"init"),
        ("VZVirtioConsolePortConfigurationArray", b"new"),
        ("VZDirectorySharingDevice", b"init"),
        ("VZDirectorySharingDevice", b"new"),
        ("VZAudioInputStreamSource", b"init"),
        ("VZAudioInputStreamSource", b"new"),
        ("VZStorageDeviceAttachment", b"init"),
        ("VZStorageDeviceAttachment", b"new"),
        ("VZFileHandleSerialPortAttachment", b"init"),
        ("VZFileHandleSerialPortAttachment", b"new"),
        ("VZGraphicsDisplay", b"init"),
        ("VZGraphicsDisplay", b"new"),
        ("VZGraphicsDeviceConfiguration", b"init"),
        ("VZGraphicsDeviceConfiguration", b"new"),
        ("VZVirtioConsolePort", b"init"),
        ("VZVirtioConsolePort", b"new"),
        ("VZFileSerialPortAttachment", b"init"),
        ("VZFileSerialPortAttachment", b"new"),
        ("VZSocketDeviceConfiguration", b"init"),
        ("VZSocketDeviceConfiguration", b"new"),
        ("VZEFIVariableStore", b"init"),
        ("VZEFIVariableStore", b"new"),
        ("VZNetworkDevice", b"init"),
        ("VZNetworkDevice", b"new"),
        ("VZLinuxRosettaCachingOptions", b"init"),
        ("VZLinuxRosettaCachingOptions", b"new"),
        ("VZConsoleDeviceConfiguration", b"init"),
        ("VZConsoleDeviceConfiguration", b"new"),
        ("VZMacOSInstaller", b"init"),
        ("VZMacOSInstaller", b"new"),
        ("VZMacOSConfigurationRequirements", b"init"),
        ("VZMacOSConfigurationRequirements", b"new"),
        ("VZVirtioTraditionalMemoryBalloonDevice", b"init"),
        ("VZVirtioTraditionalMemoryBalloonDevice", b"new"),
        ("VZMacAuxiliaryStorage", b"init"),
        ("VZMacAuxiliaryStorage", b"new"),
        ("VZConsoleDevice", b"init"),
        ("VZConsoleDevice", b"new"),
        ("VZBridgedNetworkInterface", b"init"),
        ("VZBridgedNetworkInterface", b"new"),
        ("VZSerialPortConfiguration", b"init"),
        ("VZSerialPortConfiguration", b"new"),
        ("VZMemoryBalloonDevice", b"init"),
        ("VZMemoryBalloonDevice", b"new"),
        ("VZVirtualMachine", b"init"),
        ("VZVirtualMachine", b"new"),
        ("VZAudioOutputStreamSink", b"init"),
        ("VZAudioOutputStreamSink", b"new"),
        ("VZMacHardwareModel", b"init"),
        ("VZMacHardwareModel", b"new"),
        ("VZNetworkDeviceConfiguration", b"init"),
        ("VZNetworkDeviceConfiguration", b"new"),
        ("VZDirectorySharingDeviceConfiguration", b"init"),
        ("VZDirectorySharingDeviceConfiguration", b"new"),
        ("VZSocketDevice", b"init"),
        ("VZSocketDevice", b"new"),
        ("VZMemoryBalloonDeviceConfiguration", b"init"),
        ("VZMemoryBalloonDeviceConfiguration", b"new"),
        ("VZStorageDeviceConfiguration", b"init"),
        ("VZStorageDeviceConfiguration", b"new"),
        ("VZVirtioConsolePortArray", b"init"),
        ("VZVirtioConsolePortArray", b"new"),
        ("VZPlatformConfiguration", b"init"),
        ("VZPlatformConfiguration", b"new"),
        ("VZNetworkDeviceAttachment", b"init"),
        ("VZNetworkDeviceAttachment", b"new"),
        ("VZPointingDeviceConfiguration", b"init"),
        ("VZPointingDeviceConfiguration", b"new"),
        ("VZMACAddress", b"init"),
        ("VZMACAddress", b"new"),
        ("VZConsolePortConfiguration", b"init"),
        ("VZConsolePortConfiguration", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["Virtualization._metadata"]


globals().pop("_setup")()
