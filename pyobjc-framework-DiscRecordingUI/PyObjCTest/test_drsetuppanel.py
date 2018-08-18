from PyObjCTools.TestSupport import *

import DiscRecordingUI

class TestDRSetupPanelHelper (DiscRecordingUI.NSObject):
    def setupPanel_deviceCouldBeTarget_(self, a, b): return 1
    def setupPanelShouldHandleMediaReservations_(self, a): return 1
    def setupPanel_deviceContainsSuitableMedia_promptString_(self, a, b, c): return 1

class TestDRSetupPanel (TestCase):

    @expectedFailure
    def testConstants(self):
        # Documented, but not actually available...
        self.assertIsInstance(DiscRecordingUI.DRSetupPanelDeviceSelectionChangedNotification, unicode)
        self.assertIsInstance(DiscRecordingUI.DRSetupPanelSelectedDeviceKey, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(TestDRSetupPanelHelper.setupPanel_deviceCouldBeTarget_)
        self.assertResultIsBOOL(TestDRSetupPanelHelper.setupPanelShouldHandleMediaReservations_)
        self.assertResultIsBOOL(TestDRSetupPanelHelper.setupPanel_deviceContainsSuitableMedia_promptString_)



if __name__ == "__main__":
    main()
