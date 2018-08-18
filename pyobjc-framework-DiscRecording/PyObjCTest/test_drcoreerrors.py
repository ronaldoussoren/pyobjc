from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRCoreErrors (TestCase):
    def testConstants(self):
        self.assertEqual(DiscRecording.kDRFirstErr, 0x80020000)
        self.assertEqual(DiscRecording.kDRInternalErr, DiscRecording.kDRFirstErr)
        self.assertEqual(DiscRecording.kDRDeviceAccessErr, 0x80020020)
        self.assertEqual(DiscRecording.kDRDeviceBusyErr, 0x80020021)
        self.assertEqual(DiscRecording.kDRDeviceCommunicationErr, 0x80020022)
        self.assertEqual(DiscRecording.kDRDeviceInvalidErr, 0x80020023)
        self.assertEqual(DiscRecording.kDRDeviceNotReadyErr, 0x80020024)
        self.assertEqual(DiscRecording.kDRDeviceNotSupportedErr, 0x80020025)
        self.assertEqual(DiscRecording.kDRMediaBusyErr, 0x80020040)
        self.assertEqual(DiscRecording.kDRMediaNotPresentErr, 0x80020041)
        self.assertEqual(DiscRecording.kDRMediaNotWritableErr, 0x80020042)
        self.assertEqual(DiscRecording.kDRMediaNotSupportedErr, 0x80020043)
        self.assertEqual(DiscRecording.kDRMediaNotBlankErr, 0x80020044)
        self.assertEqual(DiscRecording.kDRMediaNotErasableErr, 0x80020045)
        self.assertEqual(DiscRecording.kDRMediaInvalidErr, 0x80020046)
        self.assertEqual(DiscRecording.kDRBurnUnderrunErr, 0x80020060)
        self.assertEqual(DiscRecording.kDRBurnNotAllowedErr, 0x80020061)
        self.assertEqual(DiscRecording.kDRDataProductionErr, 0x80020062)
        self.assertEqual(DiscRecording.kDRVerificationFailedErr, 0x80020063)
        self.assertEqual(DiscRecording.kDRTooManyTracksForDVDErr, 0x80020064)
        self.assertEqual(DiscRecording.kDRBadLayoutErr, 0x80020065)
        self.assertEqual(DiscRecording.kDRUserCanceledErr, 0x80020066)
        self.assertEqual(DiscRecording.kDRFunctionNotSupportedErr, 0x80020067)
        self.assertEqual(DiscRecording.kDRSpeedTestAlreadyRunningErr, 0x80020068)
        self.assertEqual(DiscRecording.kDRInvalidIndexPointsErr, 0x80020069)
        self.assertEqual(DiscRecording.kDRDoubleLayerL0DataZoneBlocksParamErr, 0x8002006A)
        self.assertEqual(DiscRecording.kDRDoubleLayerL0AlreadySpecifiedErr, 0x8002006B)
        self.assertEqual(DiscRecording.kDRAudioFileNotSupportedErr, 0x8002006C)
        self.assertEqual(DiscRecording.kDRBurnPowerCalibrationErr, 0x8002006D)
        self.assertEqual(DiscRecording.kDRBurnMediaWriteFailureErr, 0x8002006E)
        self.assertEqual(DiscRecording.kDRTrackReusedErr, 0x8002006F)
        self.assertEqual(DiscRecording.kDRFileModifiedDuringBurnErr, 0x80020100)
        self.assertEqual(DiscRecording.kDRFileLocationConflictErr, 0x80020101)
        self.assertEqual(DiscRecording.kDRTooManyNameConflictsErr, 0x80020102)
        self.assertEqual(DiscRecording.kDRFilesystemsNotSupportedErr, 0x80020103)
        self.assertEqual(DiscRecording.kDRDeviceBurnStrategyNotAvailableErr, 0x80020200)
        self.assertEqual(DiscRecording.kDRDeviceCantWriteCDTextErr, 0x80020201)
        self.assertEqual(DiscRecording.kDRDeviceCantWriteIndexPointsErr, 0x80020202)
        self.assertEqual(DiscRecording.kDRDeviceCantWriteISRCErr, 0x80020203)
        self.assertEqual(DiscRecording.kDRDeviceCantWriteSCMSErr, 0x80020204)
        self.assertEqual(DiscRecording.kDRDevicePreGapLengthNotValidErr, 0x80020205)

        self.assertIsInstance(DiscRecording.kDRErrorStatusKey, unicode)
        self.assertIsInstance(DiscRecording.kDRErrorStatusErrorKey, unicode)
        self.assertIsInstance(DiscRecording.kDRErrorStatusErrorStringKey, unicode)
        self.assertIsInstance(DiscRecording.kDRErrorStatusErrorInfoStringKey, unicode)
        self.assertIsInstance(DiscRecording.kDRErrorStatusSenseKey, unicode)
        self.assertIsInstance(DiscRecording.kDRErrorStatusSenseCodeStringKey, unicode)
        self.assertIsInstance(DiscRecording.kDRErrorStatusAdditionalSenseStringKey, unicode)




    def testFunctions(self):
        self.assertResultIsCFRetained(DiscRecording.DRCopyLocalizedStringForDiscRecordingError)
        self.assertResultIsCFRetained(DiscRecording.DRCopyLocalizedStringForSenseCode)
        self.assertResultIsCFRetained(DiscRecording.DRCopyLocalizedStringForAdditionalSense)


if __name__ == "__main__":
    main()
