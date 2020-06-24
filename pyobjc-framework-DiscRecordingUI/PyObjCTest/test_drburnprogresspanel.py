import DiscRecordingUI
from PyObjCTools.TestSupport import TestCase


class TestDRBurnProgressPanelHelper(DiscRecordingUI.NSObject):
    def burnProgressPanel_burnDidFinish_(self, a, b):
        return 1


class TestDRBurnProgressPanel(TestCase):
    def testConstants(self):
        self.assertIsInstance(
            DiscRecordingUI.DRBurnProgressPanelWillBeginNotification, str
        )
        self.assertIsInstance(
            DiscRecordingUI.DRBurnProgressPanelDidFinishNotification, str
        )

    def testMethods(self):
        self.assertArgIsBOOL(
            DiscRecordingUI.DRBurnProgressPanel.setVerboseProgressStatus_, 0
        )
        self.assertResultIsBOOL(
            DiscRecordingUI.DRBurnProgressPanel.verboseProgressStatus
        )

        self.assertResultIsBOOL(
            TestDRBurnProgressPanelHelper.burnProgressPanel_burnDidFinish_
        )
