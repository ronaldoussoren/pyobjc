import DiscRecordingUI
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestDRBurnSession(TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecordingUI.DRBurnSessionRef)

    def testConstants(self):
        self.assertEqual(DiscRecordingUI.kDRBurnSessionOK, 1)
        self.assertEqual(DiscRecordingUI.kDRBurnSessionCancel, 0)

        self.assertEqual(
            DiscRecordingUI.kBurnSessionSetupDialogOptionsCurrentVersion, 1
        )

        self.assertEqual(
            DiscRecordingUI.kBurnSessionSetupDialogDefaultOptions, 0x00000000
        )
        self.assertEqual(
            DiscRecordingUI.kBurnSessionSetupDialogForceClosedDiscs, 0x00000001
        )
        self.assertEqual(
            DiscRecordingUI.kBurnSessionSetupDialogDontHandleReservations, 0x00000002
        )
        self.assertEqual(
            DiscRecordingUI.kBurnSessionSetupDialogAllowTestBurns, 0x80000004
        )

        self.assertEqual(DiscRecordingUI.kDRBurnSessionSetupCallbacksCurrentVersion, 1)

        self.assertEqual(DiscRecordingUI.kDRBurnProgressSetupCallbacksCurrentVersion, 1)

        self.assertEqual(
            DiscRecordingUI.kBurnSessionProgressDialogOptionsCurrentVersion, 1
        )

        self.assertEqual(
            DiscRecordingUI.kBurnSessionProgressDialogDefaultOptions, 0x00000000
        )
        self.assertEqual(
            DiscRecordingUI.kBurnSessionProgressDialogDisplayVerboseProgress, 0x00000001
        )

    def testStructs(self):
        v = DiscRecordingUI.DRBurnSessionSetupDialogOptions()
        self.assertEqual(v.version, 0)
        self.assertEqual(v.dialogOptionFlags, 0)
        self.assertEqual(v.defaultButtonTitle, None)

        v = DiscRecordingUI.DRBurnSessionProgressDialogOptions()
        self.assertEqual(v.version, 0)
        self.assertEqual(v.dialogOptionFlags, 0)
        self.assertEqual(v.description, None)

    def testFunctions(self):
        self.assertIsInstance(DiscRecordingUI.DRBurnSessionGetTypeID(), int)

        self.assertResultIsCFRetained(DiscRecordingUI.DRBurnSessionCreate)

        DiscRecordingUI.DRBurnSessionSetBurn
        DiscRecordingUI.DRBurnSessionGetBurn

        # XXX: Manual bindings
        self.assertArgIsIn(DiscRecordingUI.DRBurnSessionSetupDialog, 1)
        self.assertArgIsIn(DiscRecordingUI.DRBurnSessionSetupDialog, 2)

        # XXX: Manual bindings
        self.assertArgIsIn(DiscRecordingUI.DRBurnSessionBeginProgressDialog, 2)
        self.assertArgIsIn(DiscRecordingUI.DRBurnSessionBeginProgressDialog, 3)
