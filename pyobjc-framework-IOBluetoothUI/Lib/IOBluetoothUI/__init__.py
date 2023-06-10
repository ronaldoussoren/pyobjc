"""
Python mapping for the IOBluetoothUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import IOBluetooth
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="IOBluetoothUI",
        frameworkIdentifier="com.apple.BluetoothUI",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/IOBluetoothUI.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(IOBluetooth,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["IOBluetoothUI._metadata"]


globals().pop("_setup")()
