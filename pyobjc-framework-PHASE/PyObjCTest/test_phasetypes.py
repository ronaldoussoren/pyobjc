from PyObjCTools.TestSupport import TestCase, fourcc

import PHASE


class TesPHASETypes(TestCase):
    def test_constants(self):
        self.assertIsEnumType(PHASE.PHASEUpdateMode)
        self.assertEqual(PHASE.PHASEUpdateModeAutomatic, 0)
        self.assertEqual(PHASE.PHASEUpdateModeManual, 1)

        self.assertIsEnumType(PHASE.PHASERenderingState)
        self.assertEqual(PHASE.PHASERenderingStateStopped, 0)
        self.assertEqual(PHASE.PHASERenderingStateStarted, 1)
        self.assertEqual(PHASE.PHASERenderingStatePaused, 2)

        self.assertIsEnumType(PHASE.PHASESpatializationMode)
        self.assertEqual(PHASE.PHASESpatializationModeAutomatic, 0)
        self.assertEqual(PHASE.PHASESpatializationModeAlwaysUseBinaural, 1)
        self.assertEqual(PHASE.PHASESpatializationModeAlwaysUseChannelBased, 2)

        self.assertIsEnumType(PHASE.PHASEReverbPreset)
        self.assertEqual(PHASE.PHASEReverbPresetNone, fourcc(b"rNon"))
        self.assertEqual(PHASE.PHASEReverbPresetSmallRoom, fourcc(b"rSRm"))
        self.assertEqual(PHASE.PHASEReverbPresetMediumRoom, fourcc(b"rMRm"))
        self.assertEqual(PHASE.PHASEReverbPresetLargeRoom, fourcc(b"rLR1"))
        self.assertEqual(PHASE.PHASEReverbPresetLargeRoom2, fourcc(b"rLR2"))
        self.assertEqual(PHASE.PHASEReverbPresetMediumChamber, fourcc(b"rMCh"))
        self.assertEqual(PHASE.PHASEReverbPresetLargeChamber, fourcc(b"rLCh"))
        self.assertEqual(PHASE.PHASEReverbPresetMediumHall, fourcc(b"rMH1"))
        self.assertEqual(PHASE.PHASEReverbPresetMediumHall2, fourcc(b"rMH2"))
        self.assertEqual(PHASE.PHASEReverbPresetMediumHall3, fourcc(b"rMH3"))
        self.assertEqual(PHASE.PHASEReverbPresetLargeHall, fourcc(b"rLH1"))
        self.assertEqual(PHASE.PHASEReverbPresetLargeHall2, fourcc(b"rLH2"))
        self.assertEqual(PHASE.PHASEReverbPresetCathedral, fourcc(b"rCth"))

        self.assertIsInstance(PHASE.PHASEErrorDomain, str)

        self.assertIsEnumType(PHASE.PHASEError)
        self.assertEqual(PHASE.PHASEErrorInitializeFailed, fourcc(b"PHEa"))
        self.assertEqual(PHASE.PHASEErrorInvalidObject, fourcc(b"PHEb"))

        self.assertIsInstance(PHASE.PHASESoundEventErrorDomain, str)

        self.assertIsEnumType(PHASE.PHASESoundEventError)
        self.assertEqual(PHASE.PHASESoundEventErrorNotFound, fourcc(b"PHta"))
        self.assertEqual(PHASE.PHASESoundEventErrorBadData, fourcc(b"PHtb"))
        self.assertEqual(PHASE.PHASESoundEventErrorInvalidInstance, fourcc(b"PHtc"))
        self.assertEqual(PHASE.PHASESoundEventErrorAPIMisuse, fourcc(b"PHtd"))
        self.assertEqual(
            PHASE.PHASESoundEventErrorSystemNotInitialized, fourcc(b"PHte")
        )
        self.assertEqual(PHASE.PHASESoundEventErrorOutOfMemory, fourcc(b"PHtf"))

        self.assertIsInstance(PHASE.PHASEAssetErrorDomain, str)

        self.assertIsEnumType(PHASE.PHASEAssetError)
        self.assertEqual(PHASE.PHASEAssetErrorFailedToLoad, fourcc(b"PHaa"))
        self.assertEqual(PHASE.PHASEAssetErrorInvalidEngineInstance, fourcc(b"PHab"))
        self.assertEqual(PHASE.PHASEAssetErrorBadParameters, fourcc(b"PHac"))
        self.assertEqual(PHASE.PHASEAssetErrorAlreadyExists, fourcc(b"PHad"))
        self.assertEqual(PHASE.PHASEAssetErrorGeneralError, fourcc(b"PHae"))
        self.assertEqual(PHASE.PHASEAssetErrorMemoryAllocation, fourcc(b"PHaf"))

        self.assertIsEnumType(PHASE.PHASESoundEventPrepareHandlerReason)
        self.assertEqual(PHASE.PHASESoundEventPrepareHandlerReasonFailure, 0)
        self.assertEqual(PHASE.PHASESoundEventPrepareHandlerReasonPrepared, 1)
        self.assertEqual(PHASE.PHASESoundEventPrepareHandlerReasonTerminated, 2)

        self.assertIsEnumType(PHASE.PHASESoundEventStartHandlerReason)
        self.assertEqual(PHASE.PHASESoundEventStartHandlerReasonFailure, 0)
        self.assertEqual(PHASE.PHASESoundEventStartHandlerReasonFinishedPlaying, 1)
        self.assertEqual(PHASE.PHASESoundEventStartHandlerReasonTerminated, 2)

        self.assertIsEnumType(PHASE.PHASESoundEventSeekHandlerReason)
        self.assertEqual(PHASE.PHASESoundEventSeekHandlerReasonFailure, 0)
        self.assertEqual(
            PHASE.PHASESoundEventSeekHandlerReasonFailureSeekAlreadyInProgress, 1
        )
        self.assertEqual(PHASE.PHASESoundEventSeekHandlerReasonSeekSuccessful, 2)

        self.assertIsEnumType(PHASE.PHASESoundEventPrepareState)
        self.assertEqual(PHASE.PHASESoundEventPrepareStatePrepareNotStarted, 0)
        self.assertEqual(PHASE.PHASESoundEventPrepareStatePrepareInProgress, 1)
        self.assertEqual(PHASE.PHASESoundEventPrepareStatePrepared, 2)

        self.assertIsEnumType(PHASE.PHASEAssetType)
        self.assertEqual(PHASE.PHASEAssetTypeResident, 0)
        self.assertEqual(PHASE.PHASEAssetTypeStreamed, 1)

        self.assertIsEnumType(PHASE.PHASECurveType)
        self.assertEqual(PHASE.PHASECurveTypeLinear, fourcc(b"crLn"))
        self.assertEqual(PHASE.PHASECurveTypeSquared, fourcc(b"crSq"))
        self.assertEqual(PHASE.PHASECurveTypeInverseSquared, fourcc(b"crIQ"))
        self.assertEqual(PHASE.PHASECurveTypeCubed, fourcc(b"crCu"))
        self.assertEqual(PHASE.PHASECurveTypeInverseCubed, fourcc(b"crIC"))
        self.assertEqual(PHASE.PHASECurveTypeSine, fourcc(b"crSn"))
        self.assertEqual(PHASE.PHASECurveTypeInverseSine, fourcc(b"crIS"))
        self.assertEqual(PHASE.PHASECurveTypeSigmoid, fourcc(b"crSg"))
        self.assertEqual(PHASE.PHASECurveTypeInverseSigmoid, fourcc(b"crIG"))
        self.assertEqual(PHASE.PHASECurveTypeHoldStartValue, fourcc(b"crHS"))
        self.assertEqual(PHASE.PHASECurveTypeJumpToEndValue, fourcc(b"crJE"))

        self.assertIsEnumType(PHASE.PHASECullOption)
        self.assertEqual(PHASE.PHASECullOptionTerminate, 0)
        self.assertEqual(PHASE.PHASECullOptionSleepWakeAtZero, 1)
        self.assertEqual(PHASE.PHASECullOptionSleepWakeAtRandomOffset, 2)
        self.assertEqual(PHASE.PHASECullOptionSleepWakeAtRealtimeOffset, 3)
        self.assertEqual(PHASE.PHASECullOptionDoNotCull, 4)

        self.assertIsEnumType(PHASE.PHASEPlaybackMode)
        self.assertEqual(PHASE.PHASEPlaybackModeOneShot, 0)
        self.assertEqual(PHASE.PHASEPlaybackModeLooping, 1)

        self.assertIsEnumType(PHASE.PHASENormalizationMode)
        self.assertEqual(PHASE.PHASENormalizationModeNone, 0)
        self.assertEqual(PHASE.PHASENormalizationModeDynamic, 1)

        self.assertIsEnumType(PHASE.PHASECalibrationMode)
        self.assertEqual(PHASE.PHASECalibrationModeNone, 0)
        self.assertEqual(PHASE.PHASECalibrationModeRelativeSpl, 1)
        self.assertEqual(PHASE.PHASECalibrationModeAbsoluteSpl, 2)
