import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCMGenlockClock(TestCase):
    @min_os_level("27.0")
    def test_constants(self):
        self.assertIsInstance(
            CoreMedia.kCMGenlockClockNotification_DisplayGenlockModeChanged, str
        )
        self.assertIsInstance(
            CoreMedia.kCMGenlockClockNotificationPayload_AnyDisplayIsSynchronizedToLockedGenlockSignal,
            str,
        )

    @min_os_level("27.0")
    def test_functions(self):
        self.assertResultIsCFRetained(CoreMedia.CMClockCreateGenlockClock)
        self.assertResultIsBOOL(
            CoreMedia.CMIsAnyDisplaySynchronizedToLockedGenlockSignal
        )
