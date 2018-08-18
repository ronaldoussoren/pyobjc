from PyObjCTools.TestSupport import *

import DiscRecording

DRNotificationCallback = b'v^{__DRNotificationCenter=}^v^{__CFString=}@^{__CFDictionary=}'

class TestDRCoreNotifications (TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRNotificationCenterRef)

    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DRNotificationCenterGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiscRecording.DRNotificationCenterCreate)

        self.assertResultIsCFRetained(DiscRecording.DRNotificationCenterCreateRunLoopSource)

        self.assertArgIsFunction(DiscRecording.DRNotificationCenterAddObserver, 2, DRNotificationCallback, True)

        DiscRecording.DRNotificationCenterRemoveObserver


if __name__ == "__main__":
    main()
