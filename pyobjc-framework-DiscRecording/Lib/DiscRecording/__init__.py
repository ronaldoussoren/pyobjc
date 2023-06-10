"""
Python mapping for the DiscRecording framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
from math import floor


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _DiscRecording

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="DiscRecording",
        frameworkIdentifier="com.apple.DiscRecording",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/DiscRecording.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _DiscRecording,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["DiscRecording._metadata"]


globals().pop("_setup")()


def DRDeviceKPSForCDXFactor(xfactor):
    from . import kDRDeviceBurnSpeedCD1x

    return float(xfactor) * kDRDeviceBurnSpeedCD1x


def DRDeviceKPSForDVDXFactor(xfactor):
    from . import kDRDeviceBurnSpeedDVD1x

    return float(xfactor) * kDRDeviceBurnSpeedDVD1x


def DRDeviceCDXFactorForKPS(kps):
    from . import kDRDeviceBurnSpeedCD1x

    return floor(kps / kDRDeviceBurnSpeedCD1x + 0.5)


def DRDeviceDVDXFactorForKPS(kps):
    from . import kDRDeviceBurnSpeedDVD1x

    return floor(kps / kDRDeviceBurnSpeedDVD1x + 0.5)
