from PyObjCTools.TestSupport import *

import DiscRecordingUI

class TestDREraseSession (TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecordingUI.DREraseSessionRef)

    def testConstants(self):
        self.assertEqual(DiscRecordingUI.kDREraseSessionOK, 1)
        self.assertEqual(DiscRecordingUI.kDREraseSessionCancel, 0)

        self.assertEqual(DiscRecordingUI.kEraseSessionSetupDialogOptionsCurrentVersion, 1)

        self.assertEqual(DiscRecordingUI.kEraseSessionSetupDialogDefaultOptions, 0x00000000)
        self.assertEqual(DiscRecordingUI.kEraseSessionSetupDialogDontHandleReservations, 0x00000001)

        self.assertEqual(DiscRecordingUI.kDREraseSessionSetupCallbacksCurrentVersion, 1)

        self.assertEqual(DiscRecordingUI.kDREraseProgressSetupCallbacksCurrentVersion, 1)

        self.assertEqual(DiscRecordingUI.kEraseSessionProgressDialogOptionsCurrentVersion, 1)

        self.assertEqual(DiscRecordingUI.kEraseSessionProgressDialogDefaultOptions, 0x00000000)

    def testStructs(self):
        v = DiscRecordingUI.DREraseSessionSetupDialogOptions()
        self.assertEqual(v.version, 0)
        self.assertEqual(v.dialogOptionFlags, 0)

        v = DiscRecordingUI.DREraseSessionProgressDialogOptions()
        self.assertEqual(v.version, 0)
        self.assertEqual(v.dialogOptionFlags, 0)
        self.assertEqual(v.description, None)

    def testFunctions(self):
        self.assertIsInstance(DiscRecordingUI.DREraseSessionGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiscRecordingUI.DREraseSessionCreate)

        DiscRecordingUI.DREraseSessionSetErase
        DiscRecordingUI.DREraseSessionGetErase

        self.assertArgIsIn(DiscRecordingUI.DREraseSessionSetupDialog, 1)
        self.assertArgIsIn(DiscRecordingUI.DREraseSessionSetupDialog, 2)

        self.assertArgIsIn(DiscRecordingUI.DREraseSessionBeginProgressDialog, 1)
        self.assertArgIsIn(DiscRecordingUI.DREraseSessionBeginProgressDialog, 2)


if __name__ == "__main__":
    main()
