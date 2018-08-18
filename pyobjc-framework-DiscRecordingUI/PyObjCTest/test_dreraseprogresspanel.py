from PyObjCTools.TestSupport import *

import DiscRecordingUI

class TestDREraseProgressPanelHelper (DiscRecordingUI.NSObject):
    def eraseProgressPanel_eraseDidFinish_(self, a, b): return 1

class TestDREraseProgressPanel (TestCase):
    def testConstants(self):
        self.assertIsInstance(DiscRecordingUI.DREraseProgressPanelWillBeginNotification, unicode)
        self.assertIsInstance(DiscRecordingUI.DREraseProgressPanelDidFinishNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(TestDREraseProgressPanelHelper.eraseProgressPanel_eraseDidFinish_)


if __name__ == "__main__":
    main()
