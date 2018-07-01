from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRBurn (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DiscRecording.DRBurn.appendable)
        self.assertArgIsBOOL(DiscRecording.DRBurn.setAppendable_, 0)

        self.assertResultIsBOOL(DiscRecording.DRBurn.verifyDisc)
        self.assertArgIsBOOL(DiscRecording.DRBurn.setVerifyDisc_, 0)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.DRBurnRequestedSpeedKey, unicode)
        self.assertIsInstance(DiscRecording.DRBurnAppendableKey, unicode)
        self.assertIsInstance(DiscRecording.DRBurnOverwriteDiscKey, unicode)
        self.assertIsInstance(DiscRecording.DRBurnVerifyDiscKey, unicode)
        self.assertIsInstance(DiscRecording.DRBurnCompletionActionKey, unicode)
        self.assertIsInstance(DiscRecording.DRBurnUnderrunProtectionKey, unicode)
        self.assertIsInstance(DiscRecording.DRBurnTestingKey, unicode)
        self.assertIsInstance(DiscRecording.DRSynchronousBehaviorKey, unicode)
        self.assertIsInstance(DiscRecording.DRBurnFailureActionKey, unicode)
        self.assertIsInstance(DiscRecording.DRMediaCatalogNumberKey, unicode)
        self.assertIsInstance(DiscRecording.DRBurnDoubleLayerL0DataZoneBlocksKey, unicode)
        self.assertIsInstance(DiscRecording.DRBurnStrategyKey, unicode)
        self.assertIsInstance(DiscRecording.DRBurnStrategyIsRequiredKey, unicode)
        self.assertIsInstance(DiscRecording.DRCDTextKey, unicode)
        self.assertIsInstance(DiscRecording.DRBurnCompletionActionEject, unicode)
        self.assertIsInstance(DiscRecording.DRBurnCompletionActionMount, unicode)
        self.assertIsInstance(DiscRecording.DRBurnFailureActionEject, unicode)
        self.assertIsInstance(DiscRecording.DRBurnFailureActionNone, unicode)
        self.assertIsInstance(DiscRecording.DRBurnStrategyCDTAO, unicode)
        self.assertIsInstance(DiscRecording.DRBurnStrategyCDSAO, unicode)
        self.assertIsInstance(DiscRecording.DRBurnStrategyDVDDAO, unicode)
        self.assertIsInstance(DiscRecording.DRBurnStrategyBDDAO, unicode)
        self.assertIsInstance(DiscRecording.DRBurnStatusChangedNotification, unicode)

if __name__ == "__main__":
    main()
