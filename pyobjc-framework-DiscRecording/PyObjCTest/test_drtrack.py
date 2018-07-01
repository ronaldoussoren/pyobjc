from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRTrackHelper (DiscRecording.NSObject):
    def estimateLengthOfTrack_(self, a): return 1
    def prepareTrack_forBurn_toMedia_(self, a, b, c): return 1
    def producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_(self, a, b, c, d, e, f): return 1
    def produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_(self, a, b, c, d, e, f): return 1
    def prepareTrackForVerification_(self, a): return 1
    def verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_(self, a, b, c, d, e, f): return 1
    def verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_(self, a, b, c, d, e, f): return 1
    def cleanupTrackAfterVerification_(self, a): return 1



class TestDRTrack (TestCase):
    def testProtocols(self):
        objc.protocolNamed('DRTrackDataProduction')

    def testMethods(self):
        self.assertResultHasType(TestDRTrackHelper.estimateLengthOfTrack_, objc._C_ULNG_LNG)
        self.assertResultIsBOOL(TestDRTrackHelper.prepareTrack_forBurn_toMedia_)

        self.assertResultHasType(TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, objc._C_UINT)
        self.assertArgHasType(TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 1, b'o^v')
        self.assertArgSizeInArg(TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 1, 2)
        self.assertArgHasType(TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 2, objc._C_UINT)
        self.assertArgHasType(TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 3, objc._C_ULNG_LNG)
        self.assertArgHasType(TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 4, objc._C_UINT)
        self.assertArgHasType(TestDRTrackHelper.producePreGapForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 5, b'N^I')

        self.assertResultHasType(TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, objc._C_UINT)
        self.assertArgHasType(TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 1, b'o^v')
        self.assertArgSizeInArg(TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 1, 2)
        self.assertArgHasType(TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 2, objc._C_UINT)
        self.assertArgHasType(TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 3, objc._C_ULNG_LNG)
        self.assertArgHasType(TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 4, objc._C_UINT)
        self.assertArgHasType(TestDRTrackHelper.produceDataForTrack_intoBuffer_length_atAddress_blockSize_ioFlags_, 5, b'N^I')

        self.assertResultIsBOOL(TestDRTrackHelper.prepareTrackForVerification_)

        self.assertResultIsBOOL(TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_)
        self.assertArgHasType(TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 1, b'n^v')
        self.assertArgSizeInArg(TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 1, 2)
        self.assertArgHasType(TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 2, objc._C_UINT)
        self.assertArgHasType(TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 3, objc._C_ULNG_LNG)
        self.assertArgHasType(TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 4, objc._C_UINT)
        self.assertArgHasType(TestDRTrackHelper.verifyPreGapForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 5, b'N^I')

        self.assertResultIsBOOL(TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_)
        self.assertArgHasType(TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 1, b'n^v')
        self.assertArgSizeInArg(TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 1, 2)
        self.assertArgHasType(TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 2, objc._C_UINT)
        self.assertArgHasType(TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 3, objc._C_ULNG_LNG)
        self.assertArgHasType(TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 4, objc._C_UINT)
        self.assertArgHasType(TestDRTrackHelper.verifyDataForTrack_inBuffer_length_atAddress_blockSize_ioFlags_, 5, b'N^I')

        self.assertResultIsBOOL(TestDRTrackHelper.cleanupTrackAfterVerification_)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.DRTrackLengthKey, unicode)
        self.assertIsInstance(DiscRecording.DRBlockSizeKey, unicode)
        self.assertIsInstance(DiscRecording.DRBlockTypeKey, unicode)
        self.assertIsInstance(DiscRecording.DRDataFormKey, unicode)
        self.assertIsInstance(DiscRecording.DRSessionFormatKey, unicode)
        self.assertIsInstance(DiscRecording.DRTrackModeKey, unicode)
        self.assertIsInstance(DiscRecording.DRVerificationTypeKey, unicode)
        self.assertIsInstance(DiscRecording.DRMaxBurnSpeedKey, unicode)
        self.assertIsInstance(DiscRecording.DRPreGapLengthKey, unicode)
        self.assertIsInstance(DiscRecording.DRPreGapIsRequiredKey, unicode)
        self.assertIsInstance(DiscRecording.DRDVDTimestampKey, unicode)
        self.assertIsInstance(DiscRecording.DRDVDCopyrightInfoKey, unicode)
        self.assertIsInstance(DiscRecording.DRTrackISRCKey, unicode)
        self.assertIsInstance(DiscRecording.DRIndexPointsKey, unicode)
        self.assertIsInstance(DiscRecording.DRAudioPreEmphasisKey, unicode)
        self.assertIsInstance(DiscRecording.DRAudioFourChannelKey, unicode)
        self.assertIsInstance(DiscRecording.DRSerialCopyManagementStateKey, unicode)
        self.assertIsInstance(DiscRecording.DRVerificationTypeProduceAgain, unicode)
        self.assertIsInstance(DiscRecording.DRVerificationTypeReceiveData, unicode)
        self.assertIsInstance(DiscRecording.DRVerificationTypeChecksum, unicode)
        self.assertIsInstance(DiscRecording.DRVerificationTypeNone, unicode)
        self.assertIsInstance(DiscRecording.DRSCMSCopyrightFree, unicode)
        self.assertIsInstance(DiscRecording.DRSCMSCopyrightProtectedOriginal, unicode)
        self.assertIsInstance(DiscRecording.DRSCMSCopyrightProtectedCopy, unicode)
        self.assertIsInstance(DiscRecording.DRNextWritableAddressKey, unicode)
        self.assertIsInstance(DiscRecording.DRTrackStartAddressKey, unicode)
        self.assertIsInstance(DiscRecording.DRFreeBlocksKey, unicode)
        self.assertIsInstance(DiscRecording.DRTrackNumberKey, unicode)
        self.assertIsInstance(DiscRecording.DRSessionNumberKey, unicode)
        self.assertIsInstance(DiscRecording.DRTrackTypeKey, unicode)
        self.assertIsInstance(DiscRecording.DRTrackIsEmptyKey, unicode)
        self.assertIsInstance(DiscRecording.DRTrackPacketTypeKey, unicode)
        self.assertIsInstance(DiscRecording.DRTrackPacketSizeKey, unicode)
        self.assertIsInstance(DiscRecording.DRTrackTypeInvisible, unicode)
        self.assertIsInstance(DiscRecording.DRTrackTypeIncomplete, unicode)
        self.assertIsInstance(DiscRecording.DRTrackTypeReserved, unicode)
        self.assertIsInstance(DiscRecording.DRTrackTypeClosed, unicode)
        self.assertIsInstance(DiscRecording.DRTrackPacketTypeFixed, unicode)
        self.assertIsInstance(DiscRecording.DRTrackPacketTypeVariable, unicode)
        self.assertIsInstance(DiscRecording.DRISOLevel, unicode)
        self.assertIsInstance(DiscRecording.DRVolumeSet, unicode)
        self.assertIsInstance(DiscRecording.DRPublisher, unicode)
        self.assertIsInstance(DiscRecording.DRDataPreparer, unicode)
        self.assertIsInstance(DiscRecording.DRApplicationIdentifier, unicode)
        self.assertIsInstance(DiscRecording.DRSystemIdentifier, unicode)
        self.assertIsInstance(DiscRecording.DRCopyrightFile, unicode)
        self.assertIsInstance(DiscRecording.DRAbstractFile, unicode)
        self.assertIsInstance(DiscRecording.DRBibliographicFile, unicode)
        self.assertIsInstance(DiscRecording.DRBlockSize, unicode)
        self.assertIsInstance(DiscRecording.DRDefaultDate, unicode)
        self.assertIsInstance(DiscRecording.DRVolumeCreationDate, unicode)
        self.assertIsInstance(DiscRecording.DRVolumeModificationDate, unicode)
        self.assertIsInstance(DiscRecording.DRVolumeCheckedDate, unicode)
        self.assertIsInstance(DiscRecording.DRVolumeExpirationDate, unicode)
        self.assertIsInstance(DiscRecording.DRVolumeEffectiveDate, unicode)
        self.assertIsInstance(DiscRecording.DRISOMacExtensions, unicode)
        self.assertIsInstance(DiscRecording.DRISORockRidgeExtensions, unicode)
        self.assertIsInstance(DiscRecording.DRSuppressMacSpecificFiles, unicode)

        self.assertEqual(DiscRecording.DRFlagSubchannelDataRequested, 1 << 1)

        self.assertIsInstance(DiscRecording.DRSubchannelDataFormKey, unicode)
        self.assertIsInstance(DiscRecording.DRSubchannelDataFormNone, unicode)
        self.assertIsInstance(DiscRecording.DRSubchannelDataFormPack, unicode)
        self.assertIsInstance(DiscRecording.DRSubchannelDataFormRaw, unicode)



if __name__ == "__main__":
    main()
