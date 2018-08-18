from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRCoreBurn (TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRBurnRef)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.kDRBurnStatusChangedNotification, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnRequestedSpeedKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnAppendableKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnOverwriteDiscKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnVerifyDiscKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnCompletionActionKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnUnderrunProtectionKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnTestingKey, unicode)
        self.assertIsInstance(DiscRecording.kDRSynchronousBehaviorKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnFailureActionKey, unicode)
        self.assertIsInstance(DiscRecording.kDRMediaCatalogNumberKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnDoubleLayerL0DataZoneBlocksKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyIsRequiredKey, unicode)
        self.assertIsInstance(DiscRecording.kDRCDTextKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnCompletionActionEject, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnCompletionActionMount, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnFailureActionEject, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnFailureActionNone, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyCDTAO, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnFailureActionNone, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyCDTAO, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyCDSAO, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnStrategyBDDAO, unicode)

    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DRBurnGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiscRecording.DRBurnCreate)

        DiscRecording.DRBurnWriteLayout
        DiscRecording.DRBurnAbort

        self.assertResultIsCFRetained(DiscRecording.DRBurnCopyStatus)

        DiscRecording.DRBurnGetDevice
        DiscRecording.DRBurnSetProperties
        DiscRecording.DRBurnGetProperties







if __name__ == "__main__":
    main()
