import DiscRecording
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestDRCoreErase(TestCase):
    @expectedFailure
    def test_cftypess(self):
        self.assertIsCFType(DiscRecording.DREraseRef)

    def test_constants(self):
        self.assertIsInstance(DiscRecording.kDREraseStatusChangedNotification, str)
        self.assertIsInstance(DiscRecording.kDREraseTypeKey, str)
        self.assertIsInstance(DiscRecording.kDREraseTypeQuick, str)
        self.assertIsInstance(DiscRecording.kDREraseTypeComplete, str)

    def test_functions(self):
        self.assertIsInstance(DiscRecording.DREraseGetTypeID(), int)

        self.assertResultIsCFRetained(DiscRecording.DREraseCreate)

        DiscRecording.DREraseStart

        self.assertResultIsCFRetained(DiscRecording.DREraseCopyStatus)

        DiscRecording.DREraseGetDevice
        DiscRecording.DREraseSetProperties
        DiscRecording.DREraseGetProperties
