from PyObjCTools.TestSupport import *

import DiscRecordingUI

class TestDRBurnProgressPanelHelper (DiscRecordingUI.NSObject):
    def burnProgressPanel_burnDidFinish_(self, a, b): return 1

class TestDRBurnProgressPanel (TestCase):
    def testConstants(self):
        self.assertIsInstance(DiscRecordingUI.DRBurnProgressPanelWillBeginNotification, unicode)
        self.assertIsInstance(DiscRecordingUI.DRBurnProgressPanelDidFinishNotification, unicode)

    def testMethods(self):
        self.assertArgIsBOOL(DiscRecordingUI.DRBurnProgressPanel.setVerboseProgressStatus_, 0)
        self.assertResultIsBOOL(DiscRecordingUI.DRBurnProgressPanel.verboseProgressStatus)

        self.assertResultIsBOOL(TestDRBurnProgressPanelHelper.burnProgressPanel_burnDidFinish_)


if __name__ == "__main__":
    main()
