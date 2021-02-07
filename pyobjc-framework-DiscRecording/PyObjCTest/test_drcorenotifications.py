import DiscRecording
from PyObjCTools.TestSupport import TestCase, expectedFailure

DRNotificationCallback = (
    b"v^{__DRNotificationCenter=}^v^{__CFString=}@^{__CFDictionary=}"
)


class TestDRCoreNotifications(TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRNotificationCenterRef)

    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DRNotificationCenterGetTypeID(), int)

        self.assertResultIsCFRetained(DiscRecording.DRNotificationCenterCreate)

        self.assertResultIsCFRetained(
            DiscRecording.DRNotificationCenterCreateRunLoopSource
        )

        self.assertArgIsFunction(
            DiscRecording.DRNotificationCenterAddObserver,
            2,
            DRNotificationCallback,
            True,
        )

        DiscRecording.DRNotificationCenterRemoveObserver
