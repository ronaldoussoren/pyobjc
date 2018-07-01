from PyObjCTools.TestSupport import *

import DiscRecording

DRTrackCallbackProc = b'i^{__DRTrack=}I^v'

class TestDRCoreTrack (TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRTrackRef)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.kDRTrackLengthKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBlockSizeKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBlockTypeKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDataFormKey, unicode)
        self.assertIsInstance(DiscRecording.kDRSessionFormatKey, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackModeKey, unicode)
        self.assertIsInstance(DiscRecording.kDRVerificationTypeKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDVDCopyrightInfoKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDVDTimestampKey, unicode)
        self.assertIsInstance(DiscRecording.kDRBufferZone1DataKey, unicode)
        self.assertIsInstance(DiscRecording.kDRMaxBurnSpeedKey, unicode)
        self.assertIsInstance(DiscRecording.kDRPreGapLengthKey, unicode)
        self.assertIsInstance(DiscRecording.kDRPreGapIsRequiredKey, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackISRCKey, unicode)
        self.assertIsInstance(DiscRecording.kDRIndexPointsKey, unicode)
        self.assertIsInstance(DiscRecording.kDRAudioPreEmphasisKey, unicode)
        self.assertIsInstance(DiscRecording.kDRAudioFourChannelKey, unicode)
        self.assertIsInstance(DiscRecording.kDRSerialCopyManagementStateKey, unicode)
        self.assertIsInstance(DiscRecording.kDRVerificationTypeNone, unicode)
        self.assertIsInstance(DiscRecording.kDRVerificationTypeProduceAgain, unicode)
        self.assertIsInstance(DiscRecording.kDRVerificationTypeReceiveData, unicode)
        self.assertIsInstance(DiscRecording.kDRVerificationTypeChecksum, unicode)
        self.assertIsInstance(DiscRecording.kDRSCMSCopyrightFree, unicode)
        self.assertIsInstance(DiscRecording.kDRSCMSCopyrightProtectedOriginal, unicode)
        self.assertIsInstance(DiscRecording.kDRSCMSCopyrightProtectedCopy, unicode)
        self.assertIsInstance(DiscRecording.kDRNextWritableAddressKey, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackStartAddressKey, unicode)
        self.assertIsInstance(DiscRecording.kDRFreeBlocksKey, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackNumberKey, unicode)
        self.assertIsInstance(DiscRecording.kDRSessionNumberKey, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackTypeKey, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackIsEmptyKey, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackPacketTypeKey, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackPacketSizeKey, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackTypeInvisible, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackTypeIncomplete, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackTypeReserved, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackTypeClosed, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackPacketTypeFixed, unicode)
        self.assertIsInstance(DiscRecording.kDRTrackPacketTypeVariable, unicode)
        self.assertIsInstance(DiscRecording.kDRBurnKey, unicode)
        self.assertIsInstance(DiscRecording.kDRSubchannelDataFormKey, unicode)
        self.assertIsInstance(DiscRecording.kDRSubchannelDataFormNone, unicode)
        self.assertIsInstance(DiscRecording.kDRSubchannelDataFormPack, unicode)
        self.assertIsInstance(DiscRecording.kDRSubchannelDataFormRaw, unicode)

        self.assertEqual(DiscRecording.kDRBlockSizeAudio, 2352)
        self.assertEqual(DiscRecording.kDRBlockSizeMode1Data, 2048)
        self.assertEqual(DiscRecording.kDRBlockSizeMode2Data, 2332)
        self.assertEqual(DiscRecording.kDRBlockSizeMode2Form1Data, 2048)
        self.assertEqual(DiscRecording.kDRBlockSizeMode2Form2Data, 2324)
        self.assertEqual(DiscRecording.kDRBlockSizeDVDData, 2048)

        self.assertEqual(DiscRecording.kDRBlockTypeAudio, 0)
        self.assertEqual(DiscRecording.kDRBlockTypeMode1Data, 8)
        self.assertEqual(DiscRecording.kDRBlockTypeMode2Data, 13)
        self.assertEqual(DiscRecording.kDRBlockTypeMode2Form1Data, 10)
        self.assertEqual(DiscRecording.kDRBlockTypeMode2Form2Data, 12)
        self.assertEqual(DiscRecording.kDRBlockTypeDVDData, 8)

        self.assertEqual(DiscRecording.kDRDataFormAudio, 0)
        self.assertEqual(DiscRecording.kDRDataFormMode1Data, 16)
        self.assertEqual(DiscRecording.kDRDataFormMode2Data, 32)
        self.assertEqual(DiscRecording.kDRDataFormMode2Form1Data, 32)
        self.assertEqual(DiscRecording.kDRDataFormMode2Form2Data, 32)
        self.assertEqual(DiscRecording.kDRDataFormDVDData, 16)

        self.assertEqual(DiscRecording.kDRTrackModeAudio, 0)
        self.assertEqual(DiscRecording.kDRTrackMode1Data, 4)
        self.assertEqual(DiscRecording.kDRTrackMode2Data, 4)
        self.assertEqual(DiscRecording.kDRTrackMode2Form1Data, 4)
        self.assertEqual(DiscRecording.kDRTrackMode2Form2Data, 4)
        self.assertEqual(DiscRecording.kDRTrackModeDVDData, 5)

        self.assertEqual(DiscRecording.kDRSessionFormatAudio, 0)
        self.assertEqual(DiscRecording.kDRSessionFormatMode1Data, 0)
        self.assertEqual(DiscRecording.kDRSessionFormatCDI, 0x10)
        self.assertEqual(DiscRecording.kDRSessionFormatCDXA, 0x20)
        self.assertEqual(DiscRecording.kDRSessionFormatDVDData, 0)

        self.assertEqual(DiscRecording.kDRFlagSubchannelDataRequested, 1 << 1)
        self.assertEqual(DiscRecording.kDRFlagNoMoreData, 1 << 0)

        self.assertEqual(DiscRecording.kDRTrackMessagePreBurn, fourcc(b'pre '))
        self.assertEqual(DiscRecording.kDRTrackMessageProduceData, fourcc(b'prod'))
        self.assertEqual(DiscRecording.kDRTrackMessageVerificationStarting, fourcc(b'vstr'))
        self.assertEqual(DiscRecording.kDRTrackMessageVerifyData, fourcc(b'vrfy'))
        self.assertEqual(DiscRecording.kDRTrackMessageVerificationDone, fourcc(b'vdon'))
        self.assertEqual(DiscRecording.kDRTrackMessagePostBurn, fourcc(b'post'))
        self.assertEqual(DiscRecording.kDRTrackMessageEstimateLength, fourcc(b'esti'))
        self.assertEqual(DiscRecording.kDRTrackMessageProducePreGap, fourcc(b'prpr'))
        self.assertEqual(DiscRecording.kDRTrackMessageVerifyPreGap, fourcc(b'vrpr'))

    def testStructs(self):
        # XXX: Needs manual work
        v = DiscRecording.DRTrackProductionInfo()
        self.assertEqual(v.buffer, None)
        self.assertEqual(v.reqCount, 0)
        self.assertEqual(v.actCount, 0)
        self.assertEqual(v.flags, 0)
        self.assertEqual(v.blockSize, 0)
        self.assertEqual(v.requestedAddress, 0)

    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DRTrackGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiscRecording.DRTrackCreate)
        self.assertArgIsFunction(DiscRecording.DRTrackCreate, 1, DRTrackCallbackProc, True)

        DiscRecording.DRTrackSetProperties
        DiscRecording.DRTrackGetProperties
        DiscRecording.DRTrackSpeedTest
        DiscRecording.DRTrackEstimateLength






if __name__ == "__main__":
    main()
