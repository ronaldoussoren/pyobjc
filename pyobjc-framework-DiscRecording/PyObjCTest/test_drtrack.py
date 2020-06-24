import DiscRecording
from PyObjCTools.TestSupport import TestCase
import objc


class TestDRTrackHelper(DiscRecording.NSObject):
    def estimateLengthOfTrack_(self, a):
        return 1

    def prepareTrack_forBurn_toMedia_(self, a, b, c):
        return 1

    def producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_(
        self, a, b, c, d, e, f
    ):
        return 1

    def produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_(
        self, a, b, c, d, e, f
    ):
        return 1

    def prepareTrackForVerification_(self, a):
        return 1

    def verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_(
        self, a, b, c, d, e, f
    ):
        return 1

    def verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_(
        self, a, b, c, d, e, f
    ):
        return 1

    def cleanupTrackAfterVerification_(self, a):
        return 1


class TestDRTrack(TestCase):
    def testProtocols(self):
        objc.protocolNamed("DRTrackDataProduction")

    def testMethods(self):
        self.assertResultHasType(
            TestDRTrackHelper.estimateLengthOfTrack_, objc._C_ULNG_LNG
        )
        self.assertResultIsBOOL(TestDRTrackHelper.prepareTrack_forBurn_toMedia_)

        self.assertResultHasType(
            TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            1,
            b"o^v",
        )
        self.assertArgSizeInArg(
            TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            1,
            2,
        )
        self.assertArgHasType(
            TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            2,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            3,
            objc._C_ULNG_LNG,
        )
        self.assertArgHasType(
            TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            4,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            5,
            b"N^I",
        )

        self.assertResultHasType(
            TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            1,
            b"o^v",
        )
        self.assertArgSizeInArg(
            TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            1,
            2,
        )
        self.assertArgHasType(
            TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            2,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            3,
            objc._C_ULNG_LNG,
        )
        self.assertArgHasType(
            TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            4,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_,
            5,
            b"N^I",
        )

        self.assertResultIsBOOL(TestDRTrackHelper.prepareTrackForVerification_)

        self.assertResultIsBOOL(
            TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_
        )
        self.assertArgHasType(
            TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            1,
            b"n^v",
        )
        self.assertArgSizeInArg(
            TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            1,
            2,
        )
        self.assertArgHasType(
            TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            2,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            3,
            objc._C_ULNG_LNG,
        )
        self.assertArgHasType(
            TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            4,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            5,
            b"N^I",
        )

        self.assertResultIsBOOL(
            TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_
        )
        self.assertArgHasType(
            TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            1,
            b"n^v",
        )
        self.assertArgSizeInArg(
            TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            1,
            2,
        )
        self.assertArgHasType(
            TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            2,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            3,
            objc._C_ULNG_LNG,
        )
        self.assertArgHasType(
            TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            4,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_,
            5,
            b"N^I",
        )

        self.assertResultIsBOOL(TestDRTrackHelper.cleanupTrackAfterVerification_)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.DRTrackLengthKey, str)
        self.assertIsInstance(DiscRecording.DRBlockSizeKey, str)
        self.assertIsInstance(DiscRecording.DRBlockTypeKey, str)
        self.assertIsInstance(DiscRecording.DRDataFormKey, str)
        self.assertIsInstance(DiscRecording.DRSessionFormatKey, str)
        self.assertIsInstance(DiscRecording.DRTrackModeKey, str)
        self.assertIsInstance(DiscRecording.DRVerificationTypeKey, str)
        self.assertIsInstance(DiscRecording.DRMaxBurnSpeedKey, str)
        self.assertIsInstance(DiscRecording.DRPreGapLengthKey, str)
        self.assertIsInstance(DiscRecording.DRPreGapIsRequiredKey, str)
        self.assertIsInstance(DiscRecording.DRDVDTimestampKey, str)
        self.assertIsInstance(DiscRecording.DRDVDCopyrightInfoKey, str)
        self.assertIsInstance(DiscRecording.DRTrackISRCKey, str)
        self.assertIsInstance(DiscRecording.DRIndexPointsKey, str)
        self.assertIsInstance(DiscRecording.DRAudioPreEmphasisKey, str)
        self.assertIsInstance(DiscRecording.DRAudioFourChannelKey, str)
        self.assertIsInstance(DiscRecording.DRSerialCopyManagementStateKey, str)
        self.assertIsInstance(DiscRecording.DRVerificationTypeProduceAgain, str)
        self.assertIsInstance(DiscRecording.DRVerificationTypeReceiveData, str)
        self.assertIsInstance(DiscRecording.DRVerificationTypeChecksum, str)
        self.assertIsInstance(DiscRecording.DRVerificationTypeNone, str)
        self.assertIsInstance(DiscRecording.DRSCMSCopyrightFree, str)
        self.assertIsInstance(DiscRecording.DRSCMSCopyrightProtectedOriginal, str)
        self.assertIsInstance(DiscRecording.DRSCMSCopyrightProtectedCopy, str)
        self.assertIsInstance(DiscRecording.DRNextWritableAddressKey, str)
        self.assertIsInstance(DiscRecording.DRTrackStartAddressKey, str)
        self.assertIsInstance(DiscRecording.DRFreeBlocksKey, str)
        self.assertIsInstance(DiscRecording.DRTrackNumberKey, str)
        self.assertIsInstance(DiscRecording.DRSessionNumberKey, str)
        self.assertIsInstance(DiscRecording.DRTrackTypeKey, str)
        self.assertIsInstance(DiscRecording.DRTrackIsEmptyKey, str)
        self.assertIsInstance(DiscRecording.DRTrackPacketTypeKey, str)
        self.assertIsInstance(DiscRecording.DRTrackPacketSizeKey, str)
        self.assertIsInstance(DiscRecording.DRTrackTypeInvisible, str)
        self.assertIsInstance(DiscRecording.DRTrackTypeIncomplete, str)
        self.assertIsInstance(DiscRecording.DRTrackTypeReserved, str)
        self.assertIsInstance(DiscRecording.DRTrackTypeClosed, str)
        self.assertIsInstance(DiscRecording.DRTrackPacketTypeFixed, str)
        self.assertIsInstance(DiscRecording.DRTrackPacketTypeVariable, str)
        self.assertIsInstance(DiscRecording.DRISOLevel, str)
        self.assertIsInstance(DiscRecording.DRVolumeSet, str)
        self.assertIsInstance(DiscRecording.DRPublisher, str)
        self.assertIsInstance(DiscRecording.DRDataPreparer, str)
        self.assertIsInstance(DiscRecording.DRApplicationIdentifier, str)
        self.assertIsInstance(DiscRecording.DRSystemIdentifier, str)
        self.assertIsInstance(DiscRecording.DRCopyrightFile, str)
        self.assertIsInstance(DiscRecording.DRAbstractFile, str)
        self.assertIsInstance(DiscRecording.DRBibliographicFile, str)
        self.assertIsInstance(DiscRecording.DRBlockSize, str)
        self.assertIsInstance(DiscRecording.DRDefaultDate, str)
        self.assertIsInstance(DiscRecording.DRVolumeCreationDate, str)
        self.assertIsInstance(DiscRecording.DRVolumeModificationDate, str)
        self.assertIsInstance(DiscRecording.DRVolumeCheckedDate, str)
        self.assertIsInstance(DiscRecording.DRVolumeExpirationDate, str)
        self.assertIsInstance(DiscRecording.DRVolumeEffectiveDate, str)
        self.assertIsInstance(DiscRecording.DRISOMacExtensions, str)
        self.assertIsInstance(DiscRecording.DRISORockRidgeExtensions, str)
        self.assertIsInstance(DiscRecording.DRSuppressMacSpecificFiles, str)

        self.assertEqual(DiscRecording.DRFlagSubchannelDataRequested, 1 << 1)

        self.assertIsInstance(DiscRecording.DRSubchannelDataFormKey, str)
        self.assertIsInstance(DiscRecording.DRSubchannelDataFormNone, str)
        self.assertIsInstance(DiscRecording.DRSubchannelDataFormPack, str)
        self.assertIsInstance(DiscRecording.DRSubchannelDataFormRaw, str)
