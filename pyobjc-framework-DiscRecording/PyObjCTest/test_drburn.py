import DiscRecording
from PyObjCTools.TestSupport import TestCase


class TestDRBurn(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DiscRecording.DRBurn.appendable)
        self.assertArgIsBOOL(DiscRecording.DRBurn.setAppendable_, 0)

        self.assertResultIsBOOL(DiscRecording.DRBurn.verifyDisc)
        self.assertArgIsBOOL(DiscRecording.DRBurn.setVerifyDisc_, 0)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.DRBurnRequestedSpeedKey, str)
        self.assertIsInstance(DiscRecording.DRBurnAppendableKey, str)
        self.assertIsInstance(DiscRecording.DRBurnOverwriteDiscKey, str)
        self.assertIsInstance(DiscRecording.DRBurnVerifyDiscKey, str)
        self.assertIsInstance(DiscRecording.DRBurnCompletionActionKey, str)
        self.assertIsInstance(DiscRecording.DRBurnUnderrunProtectionKey, str)
        self.assertIsInstance(DiscRecording.DRBurnTestingKey, str)
        self.assertIsInstance(DiscRecording.DRSynchronousBehaviorKey, str)
        self.assertIsInstance(DiscRecording.DRBurnFailureActionKey, str)
        self.assertIsInstance(DiscRecording.DRMediaCatalogNumberKey, str)
        self.assertIsInstance(DiscRecording.DRBurnDoubleLayerL0DataZoneBlocksKey, str)
        self.assertIsInstance(DiscRecording.DRBurnStrategyKey, str)
        self.assertIsInstance(DiscRecording.DRBurnStrategyIsRequiredKey, str)
        self.assertIsInstance(DiscRecording.DRCDTextKey, str)
        self.assertIsInstance(DiscRecording.DRBurnCompletionActionEject, str)
        self.assertIsInstance(DiscRecording.DRBurnCompletionActionMount, str)
        self.assertIsInstance(DiscRecording.DRBurnFailureActionEject, str)
        self.assertIsInstance(DiscRecording.DRBurnFailureActionNone, str)
        self.assertIsInstance(DiscRecording.DRBurnStrategyCDTAO, str)
        self.assertIsInstance(DiscRecording.DRBurnStrategyCDSAO, str)
        self.assertIsInstance(DiscRecording.DRBurnStrategyDVDDAO, str)
        self.assertIsInstance(DiscRecording.DRBurnStrategyBDDAO, str)
        self.assertIsInstance(DiscRecording.DRBurnStatusChangedNotification, str)
