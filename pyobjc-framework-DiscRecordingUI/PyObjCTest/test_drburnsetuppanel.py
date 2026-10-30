import DiscRecordingUI
from PyObjCTools.TestSupport import TestCase


class TestDRBurnSetupPanel(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(DiscRecordingUI.DRBurnSetupPanel.setCanSelectTestBurn_, 0)
        self.assertArgIsBOOL(
            DiscRecordingUI.DRBurnSetupPanel.setCanSelectAppendableMedia_, 0
        )

    def test_constants(self):
        self.assertIsInstance(
            DiscRecordingUI.DRBurnSetupPanelDefaultButtonDefaultTitle, str
        )
