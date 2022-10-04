import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCMAudioDeviceClock(TestCase):
    @min_os_level("10.8")
    def test_functions(self):
        self.assertArgIsOut(CoreMedia.CMAudioDeviceClockCreate, 2)
        self.assertArgIsCFRetained(CoreMedia.CMAudioDeviceClockCreate, 2)
        self.assertArgIsIDLike(CoreMedia.CMAudioDeviceClockCreate, 0)
        self.assertArgIsIDLike(CoreMedia.CMAudioDeviceClockCreate, 1)
        self.assertArgIsIDLike(CoreMedia.CMAudioDeviceClockCreate, 2)

        self.assertArgIsOut(CoreMedia.CMAudioDeviceClockCreateFromAudioDeviceID, 2)
        self.assertArgIsCFRetained(
            CoreMedia.CMAudioDeviceClockCreateFromAudioDeviceID, 2
        )
        self.assertArgIsIDLike(CoreMedia.CMAudioDeviceClockCreateFromAudioDeviceID, 0)
        self.assertArgIsIDLike(CoreMedia.CMAudioDeviceClockCreateFromAudioDeviceID, 2)

        self.assertArgIsIDLike(CoreMedia.CMAudioDeviceClockSetAudioDeviceUID, 0)
        self.assertArgIsIDLike(CoreMedia.CMAudioDeviceClockSetAudioDeviceUID, 1)

        self.assertArgIsIDLike(CoreMedia.CMAudioDeviceClockSetAudioDeviceID, 0)

        self.assertArgIsOut(CoreMedia.CMAudioDeviceClockGetAudioDevice, 1)
        self.assertArgIsOut(CoreMedia.CMAudioDeviceClockGetAudioDevice, 2)
        self.assertArgIsOut(CoreMedia.CMAudioDeviceClockGetAudioDevice, 3)
        self.assertArgHasType(CoreMedia.CMAudioDeviceClockGetAudioDevice, 3, b"o^Z")
        self.assertArgIsIDLike(CoreMedia.CMAudioDeviceClockGetAudioDevice, 0)
        self.assertArgIsIDLike(CoreMedia.CMAudioDeviceClockGetAudioDevice, 1)
