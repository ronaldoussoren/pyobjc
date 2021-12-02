import DiscRecording
from PyObjCTools.TestSupport import TestCase, expectedFailure, fourcc

DRTrackCallbackProc = b"i^{__DRTrack=}I^v"


class TestDRCoreTrack(TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRTrackRef)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.kDRTrackLengthKey, str)
        self.assertIsInstance(DiscRecording.kDRBlockSizeKey, str)
        self.assertIsInstance(DiscRecording.kDRBlockTypeKey, str)
        self.assertIsInstance(DiscRecording.kDRDataFormKey, str)
        self.assertIsInstance(DiscRecording.kDRSessionFormatKey, str)
        self.assertIsInstance(DiscRecording.kDRTrackModeKey, str)
        self.assertIsInstance(DiscRecording.kDRVerificationTypeKey, str)
        self.assertIsInstance(DiscRecording.kDRDVDCopyrightInfoKey, str)
        self.assertIsInstance(DiscRecording.kDRDVDTimestampKey, str)
        self.assertIsInstance(DiscRecording.kDRBufferZone1DataKey, str)
        self.assertIsInstance(DiscRecording.kDRMaxBurnSpeedKey, str)
        self.assertIsInstance(DiscRecording.kDRPreGapLengthKey, str)
        self.assertIsInstance(DiscRecording.kDRPreGapIsRequiredKey, str)
        self.assertIsInstance(DiscRecording.kDRTrackISRCKey, str)
        self.assertIsInstance(DiscRecording.kDRIndexPointsKey, str)
        self.assertIsInstance(DiscRecording.kDRAudioPreEmphasisKey, str)
        self.assertIsInstance(DiscRecording.kDRAudioFourChannelKey, str)
        self.assertIsInstance(DiscRecording.kDRSerialCopyManagementStateKey, str)
        self.assertIsInstance(DiscRecording.kDRVerificationTypeNone, str)
        self.assertIsInstance(DiscRecording.kDRVerificationTypeProduceAgain, str)
        self.assertIsInstance(DiscRecording.kDRVerificationTypeReceiveData, str)
        self.assertIsInstance(DiscRecording.kDRVerificationTypeChecksum, str)
        self.assertIsInstance(DiscRecording.kDRSCMSCopyrightFree, str)
        self.assertIsInstance(DiscRecording.kDRSCMSCopyrightProtectedOriginal, str)
        self.assertIsInstance(DiscRecording.kDRSCMSCopyrightProtectedCopy, str)
        self.assertIsInstance(DiscRecording.kDRNextWritableAddressKey, str)
        self.assertIsInstance(DiscRecording.kDRTrackStartAddressKey, str)
        self.assertIsInstance(DiscRecording.kDRFreeBlocksKey, str)
        self.assertIsInstance(DiscRecording.kDRTrackNumberKey, str)
        self.assertIsInstance(DiscRecording.kDRSessionNumberKey, str)
        self.assertIsInstance(DiscRecording.kDRTrackTypeKey, str)
        self.assertIsInstance(DiscRecording.kDRTrackIsEmptyKey, str)
        self.assertIsInstance(DiscRecording.kDRTrackPacketTypeKey, str)
        self.assertIsInstance(DiscRecording.kDRTrackPacketSizeKey, str)
        self.assertIsInstance(DiscRecording.kDRTrackTypeInvisible, str)
        self.assertIsInstance(DiscRecording.kDRTrackTypeIncomplete, str)
        self.assertIsInstance(DiscRecording.kDRTrackTypeReserved, str)
        self.assertIsInstance(DiscRecording.kDRTrackTypeClosed, str)
        self.assertIsInstance(DiscRecording.kDRTrackPacketTypeFixed, str)
        self.assertIsInstance(DiscRecording.kDRTrackPacketTypeVariable, str)
        self.assertIsInstance(DiscRecording.kDRBurnKey, str)
        self.assertIsInstance(DiscRecording.kDRSubchannelDataFormKey, str)
        self.assertIsInstance(DiscRecording.kDRSubchannelDataFormNone, str)
        self.assertIsInstance(DiscRecording.kDRSubchannelDataFormPack, str)
        self.assertIsInstance(DiscRecording.kDRSubchannelDataFormRaw, str)

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

        self.assertEqual(DiscRecording.kDRTrackMessagePreBurn, fourcc(b"pre "))
        self.assertEqual(DiscRecording.kDRTrackMessageProduceData, fourcc(b"prod"))
        self.assertEqual(
            DiscRecording.kDRTrackMessageVerificationStarting, fourcc(b"vstr")
        )
        self.assertEqual(DiscRecording.kDRTrackMessageVerifyData, fourcc(b"vrfy"))
        self.assertEqual(DiscRecording.kDRTrackMessageVerificationDone, fourcc(b"vdon"))
        self.assertEqual(DiscRecording.kDRTrackMessagePostBurn, fourcc(b"post"))
        self.assertEqual(DiscRecording.kDRTrackMessageEstimateLength, fourcc(b"esti"))
        self.assertEqual(DiscRecording.kDRTrackMessageProducePreGap, fourcc(b"prpr"))
        self.assertEqual(DiscRecording.kDRTrackMessageVerifyPreGap, fourcc(b"vrpr"))

    def testStructs(self):
        # XXX: Needs manual work
        v = DiscRecording.DRTrackProductionInfo()
        self.assertEqual(v.buffer, None)
        self.assertEqual(v.reqCount, 0)
        self.assertEqual(v.actCount, 0)
        self.assertEqual(v.flags, 0)
        self.assertEqual(v.blockSize, 0)
        self.assertEqual(v.requestedAddress, 0)
        self.assertPickleRoundTrips(v)

    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DRTrackGetTypeID(), int)

        self.assertResultIsCFRetained(DiscRecording.DRTrackCreate)
        self.assertArgIsFunction(
            DiscRecording.DRTrackCreate, 1, DRTrackCallbackProc, True
        )

        DiscRecording.DRTrackSetProperties
        DiscRecording.DRTrackGetProperties
        DiscRecording.DRTrackSpeedTest
        DiscRecording.DRTrackEstimateLength
