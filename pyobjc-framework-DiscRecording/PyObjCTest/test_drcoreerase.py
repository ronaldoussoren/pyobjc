import DiscRecording
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestDRCoreErase(TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DREraseRef)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.kDREraseStatusChangedNotification, str)
        self.assertIsInstance(DiscRecording.kDREraseTypeKey, str)
        self.assertIsInstance(DiscRecording.kDREraseTypeQuick, str)
        self.assertIsInstance(DiscRecording.kDREraseTypeComplete, str)

    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DREraseGetTypeID(), int)

        self.assertResultIsCFRetained(DiscRecording.DREraseCreate)

        DiscRecording.DREraseStart

        self.assertResultIsCFRetained(DiscRecording.DREraseCopyStatus)

        DiscRecording.DREraseGetDevice
        DiscRecording.DREraseSetProperties
        DiscRecording.DREraseGetProperties
