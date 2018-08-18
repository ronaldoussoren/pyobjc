from PyObjCTools.TestSupport import *

import DiscRecordingUI

class TestDRBurnSetupPanel (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(DiscRecordingUI.DRBurnSetupPanel.setCanSelectTestBurn_, 0)
        self.assertArgIsBOOL(DiscRecordingUI.DRBurnSetupPanel.setCanSelectAppendableMedia_, 0)

    def testConstants(self):
        self.assertIsInstance(DiscRecordingUI.DRBurnSetupPanelDefaultButtonDefaultTitle, unicode)



if __name__ == "__main__":
    main()
