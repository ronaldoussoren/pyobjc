import DiscRecording
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestDRCoreBurn(TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRBurnRef)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.kDRBurnStatusChangedNotification, str)
        self.assertIsInstance(DiscRecording.kDRBurnRequestedSpeedKey, str)
        self.assertIsInstance(DiscRecording.kDRBurnAppendableKey, str)
        self.assertIsInstance(DiscRecording.kDRBurnOverwriteDiscKey, str)
        self.assertIsInstance(DiscRecording.kDRBurnVerifyDiscKey, str)
        self.assertIsInstance(DiscRecording.kDRBurnCompletionActionKey, str)
        self.assertIsInstance(DiscRecording.kDRBurnUnderrunProtectionKey, str)
        self.assertIsInstance(DiscRecording.kDRBurnTestingKey, str)
        self.assertIsInstance(DiscRecording.kDRSynchronousBehaviorKey, str)
        self.assertIsInstance(DiscRecording.kDRBurnFailureActionKey, str)
        self.assertIsInstance(DiscRecording.kDRMediaCatalogNumberKey, str)
        self.assertIsInstance(DiscRecording.kDRBurnDoubleLayerL0DataZoneBlocksKey, str)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyKey, str)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyIsRequiredKey, str)
        self.assertIsInstance(DiscRecording.kDRCDTextKey, str)
        self.assertIsInstance(DiscRecording.kDRBurnCompletionActionEject, str)
        self.assertIsInstance(DiscRecording.kDRBurnCompletionActionMount, str)
        self.assertIsInstance(DiscRecording.kDRBurnFailureActionEject, str)
        self.assertIsInstance(DiscRecording.kDRBurnFailureActionNone, str)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyCDTAO, str)
        self.assertIsInstance(DiscRecording.kDRBurnFailureActionNone, str)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyCDTAO, str)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyCDSAO, str)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyBDDAO, str)

    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DRBurnGetTypeID(), int)

        self.assertResultIsCFRetained(DiscRecording.DRBurnCreate)

        DiscRecording.DRBurnWriteLayout
        DiscRecording.DRBurnAbort

        self.assertResultIsCFRetained(DiscRecording.DRBurnCopyStatus)

        DiscRecording.DRBurnGetDevice
        DiscRecording.DRBurnSetProperties
        DiscRecording.DRBurnGetProperties
