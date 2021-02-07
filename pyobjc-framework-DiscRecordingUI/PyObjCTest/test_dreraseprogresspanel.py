import DiscRecordingUI
from PyObjCTools.TestSupport import TestCase


class TestDREraseProgressPanelHelper(DiscRecordingUI.NSObject):
    def eraseProgressPanel_eraseDidFinish_(self, a, b):
        return 1


class TestDREraseProgressPanel(TestCase):
    def testConstants(self):
        self.assertIsInstance(
            DiscRecordingUI.DREraseProgressPanelWillBeginNotification, str
        )
        self.assertIsInstance(
            DiscRecordingUI.DREraseProgressPanelDidFinishNotification, str
        )

    def testMethods(self):
        self.assertResultIsBOOL(
            TestDREraseProgressPanelHelper.eraseProgressPanel_eraseDidFinish_
        )
