from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRCoreErase (TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DREraseRef)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.kDREraseStatusChangedNotification, unicode)
        self.assertIsInstance(DiscRecording.kDREraseTypeKey, unicode)
        self.assertIsInstance(DiscRecording.kDREraseTypeQuick, unicode)
        self.assertIsInstance(DiscRecording.kDREraseTypeComplete, unicode)

    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DREraseGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiscRecording.DREraseCreate)

        DiscRecording.DREraseStart

        self.assertResultIsCFRetained(DiscRecording.DREraseCopyStatus)

        DiscRecording.DREraseGetDevice
        DiscRecording.DREraseSetProperties
        DiscRecording.DREraseGetProperties


if __name__ == "__main__":
    main()
