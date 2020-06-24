import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCMAudioDeviceClock(TestCase):
    @min_os_level("10.8")
    def test_functions(self):
        self.assertArgIsOut(CoreMedia.CMAudioDeviceClockCreate, 2)
        self.assertArgIsCFRetained(CoreMedia.CMAudioDeviceClockCreate, 2)

        self.assertArgIsOut(CoreMedia.CMAudioDeviceClockCreateFromAudioDeviceID, 2)
        self.assertArgIsCFRetained(
            CoreMedia.CMAudioDeviceClockCreateFromAudioDeviceID, 2
        )

        CoreMedia.CMAudioDeviceClockSetAudioDeviceUID
        CoreMedia.CMAudioDeviceClockSetAudioDeviceID

        self.assertArgIsOut(CoreMedia.CMAudioDeviceClockGetAudioDevice, 1)
        self.assertArgIsOut(CoreMedia.CMAudioDeviceClockGetAudioDevice, 2)
        self.assertArgIsOut(CoreMedia.CMAudioDeviceClockGetAudioDevice, 3)
        self.assertArgHasType(CoreMedia.CMAudioDeviceClockGetAudioDevice, 3, b"o^Z")
