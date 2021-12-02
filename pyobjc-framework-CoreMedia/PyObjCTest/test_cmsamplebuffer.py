import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level

CMSampleBufferMakeDataReadyCallback = b"i^{opaqueCMSampleBuffer=}^v"
CMSampleBufferInvalidateHandler = b"v^{opaqueCMSampleBuffer=}"
CMSampleBufferInvalidateCallback = b"v^{opaqueCMSampleBuffer=}Q"


class TestCMSampleBuffer(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMSampleBufferError_AllocationFailed, -12730)
        self.assertEqual(
            CoreMedia.kCMSampleBufferError_RequiredParameterMissing, -12731
        )
        self.assertEqual(CoreMedia.kCMSampleBufferError_AlreadyHasDataBuffer, -12732)
        self.assertEqual(CoreMedia.kCMSampleBufferError_BufferNotReady, -12733)
        self.assertEqual(CoreMedia.kCMSampleBufferError_SampleIndexOutOfRange, -12734)
        self.assertEqual(CoreMedia.kCMSampleBufferError_BufferHasNoSampleSizes, -12735)
        self.assertEqual(
            CoreMedia.kCMSampleBufferError_BufferHasNoSampleTimingInfo, -12736
        )
        self.assertEqual(CoreMedia.kCMSampleBufferError_ArrayTooSmall, -12737)
        self.assertEqual(CoreMedia.kCMSampleBufferError_InvalidEntryCount, -12738)
        self.assertEqual(CoreMedia.kCMSampleBufferError_CannotSubdivide, -12739)
        self.assertEqual(CoreMedia.kCMSampleBufferError_SampleTimingInfoInvalid, -12740)
        self.assertEqual(
            CoreMedia.kCMSampleBufferError_InvalidMediaTypeForOperation, -12741
        )
        self.assertEqual(CoreMedia.kCMSampleBufferError_InvalidSampleData, -12742)
        self.assertEqual(CoreMedia.kCMSampleBufferError_InvalidMediaFormat, -12743)
        self.assertEqual(CoreMedia.kCMSampleBufferError_Invalidated, -12744)
        self.assertEqual(CoreMedia.kCMSampleBufferError_DataFailed, -16750)
        self.assertEqual(CoreMedia.kCMSampleBufferError_DataCanceled, -16751)

        self.assertEqual(
            CoreMedia.kCMSampleBufferFlag_AudioBufferList_Assure16ByteAlignment, 1 << 0
        )

        self.assertIsInstance(
            CoreMedia.kCMTimingInfoInvalid, CoreMedia.CMSampleTimingInfo
        )

        self.assertIsInstance(
            CoreMedia.kCMSampleBufferNotification_DataBecameReady, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferConduitNotification_InhibitOutputUntil, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferConduitNotificationParameter_ResumeTag, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferConduitNotification_ResetOutput, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged,
            str,
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange,
            str,
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS,
            str,
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferConsumerNotification_BufferConsumed, str
        )

        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_NotSync, str)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_PartialSync, str)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_HasRedundantCoding, str)
        self.assertIsInstance(
            CoreMedia.kCMSampleAttachmentKey_IsDependedOnByOthers, str
        )
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_DependsOnOthers, str)
        self.assertIsInstance(
            CoreMedia.kCMSampleAttachmentKey_EarlierDisplayTimesAllowed, str
        )
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_DisplayImmediately, str)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_DoNotDisplay, str)
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_ResetDecoderBeforeDecoding, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_DrainAfterDecoding, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_PostNotificationWhenConsumed, str
        )
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_ResumeOutput, str)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_TransitionID, str)
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_TrimDurationAtStart, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_TrimDurationAtEnd, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_SpeedMultiplier, str
        )
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_Reverse, str)
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_FillDiscontinuitiesWithSilence, str
        )
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_EmptyMedia, str)
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_PermanentEmptyMedia, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_DisplayEmptyMediaImmediately, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_EndsPreviousSampleDuration, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_SampleReferenceURL, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_SampleReferenceByteOffset, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferAttachmentKey_GradualDecoderRefresh, str
        )

    @min_os_level("10.8")
    def test_constants10_8(self):
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS,
            str,
        )

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(CoreMedia.kCMSampleBufferNotification_DataFailed, str)
        self.assertIsInstance(
            CoreMedia.kCMSampleBufferNotificationParameter_OSStatus, str
        )
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_ForceKeyFrame, str)

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(
            CoreMedia.kCMSampleAttachmentKey_HEVCTemporalLevelInfo, str
        )
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_TemporalLevel, str)
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_ProfileSpace, str)
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_TierFlag, str)
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_ProfileIndex, str)
        self.assertIsInstance(
            CoreMedia.kCMHEVCTemporalLevelInfoKey_ProfileCompatibilityFlags, str
        )
        self.assertIsInstance(
            CoreMedia.kCMHEVCTemporalLevelInfoKey_ConstraintIndicatorFlags, str
        )
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_LevelIndex, str)
        self.assertIsInstance(
            CoreMedia.kCMSampleAttachmentKey_HEVCTemporalSubLayerAccess, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleAttachmentKey_HEVCStepwiseTemporalSubLayerAccess, str
        )
        self.assertIsInstance(
            CoreMedia.kCMSampleAttachmentKey_HEVCSyncSampleNALUnitType, str
        )

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            CoreMedia.kCMSampleAttachmentKey_AudioIndependentSampleDecoderRefreshCount,
            str,
        )

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            CoreMedia.kCMSampleAttachmentKey_CryptorSubsampleAuxiliaryData,
            str,
        )

    def test_types(self):
        self.assertIsCFType(CoreMedia.CMSampleBufferRef)

    def test_structs(self):
        v = CoreMedia.CMSampleTimingInfo()
        self.assertEqual(v.duration, CoreMedia.CMTime())
        self.assertEqual(v.presentationTimeStamp, CoreMedia.CMTime())
        self.assertEqual(v.decodeTimeStamp, CoreMedia.CMTime())
        self.assertPickleRoundTrips(v)

    def test_functions(self):
        self.assertArgIsBOOL(CoreMedia.CMSampleBufferCreate, 2)
        self.assertArgIsFunction(
            CoreMedia.CMSampleBufferCreate, 3, CMSampleBufferMakeDataReadyCallback, True
        )
        self.assertArgIsIn(CoreMedia.CMSampleBufferCreate, 8)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferCreate, 8, 7)
        self.assertArgIsIn(CoreMedia.CMSampleBufferCreate, 10)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferCreate, 10, 9)
        self.assertArgIsOut(CoreMedia.CMSampleBufferCreate, 11)
        self.assertArgIsCFRetained(CoreMedia.CMSampleBufferCreate, 11)

        self.assertArgIsBOOL(
            CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions, 2
        )
        self.assertArgIsFunction(
            CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions,
            3,
            CMSampleBufferMakeDataReadyCallback,
            True,
        )
        self.assertArgIsIn(CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions, 8)
        self.assertArgSizeInArg(
            CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions, 8, 6
        )
        self.assertArgIsOut(
            CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions, 9
        )
        self.assertArgIsCFRetained(
            CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions, 9
        )

        self.assertArgIsBOOL(CoreMedia.CMSampleBufferCreateForImageBuffer, 2)
        self.assertArgIsFunction(
            CoreMedia.CMSampleBufferCreateForImageBuffer,
            3,
            CMSampleBufferMakeDataReadyCallback,
            True,
        )
        self.assertArgIsIn(CoreMedia.CMSampleBufferCreateForImageBuffer, 6)
        self.assertArgIsOut(CoreMedia.CMSampleBufferCreateForImageBuffer, 7)
        self.assertArgIsCFRetained(CoreMedia.CMSampleBufferCreateForImageBuffer, 7)

        self.assertArgIsOut(CoreMedia.CMSampleBufferCreateCopy, 2)
        self.assertArgIsCFRetained(CoreMedia.CMSampleBufferCreateCopy, 2)

        self.assertArgIsIn(CoreMedia.CMSampleBufferCreateCopyWithNewTiming, 3)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferCreateCopyWithNewTiming, 3, 2)
        self.assertArgIsOut(CoreMedia.CMSampleBufferCreateCopyWithNewTiming, 4)
        self.assertArgIsCFRetained(CoreMedia.CMSampleBufferCreateCopyWithNewTiming, 4)

        self.assertArgIsOut(CoreMedia.CMSampleBufferCopySampleBufferForRange, 3)
        self.assertArgIsCFRetained(CoreMedia.CMSampleBufferCopySampleBufferForRange, 3)

        CoreMedia.CMSampleBufferGetTypeID
        CoreMedia.CMSampleBufferSetDataBuffer
        CoreMedia.CMSampleBufferGetDataBuffer
        CoreMedia.CMSampleBufferGetImageBuffer
        CoreMedia.CMSampleBufferSetDataBufferFromAudioBufferList

        self.assertArgIsOut(
            CoreMedia.CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer, 1
        )
        self.assertArgIsOut(
            CoreMedia.CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer, 7
        )
        self.assertArgIsCFRetained(
            CoreMedia.CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer, 7
        )

        self.assertArgIsOut(CoreMedia.CMSampleBufferGetAudioStreamPacketDescriptions, 2)
        self.assertArgSizeInArg(
            CoreMedia.CMSampleBufferGetAudioStreamPacketDescriptions, 2, 1
        )
        self.assertArgIsOut(CoreMedia.CMSampleBufferGetAudioStreamPacketDescriptions, 3)

        self.assertFalse(
            hasattr(CoreMedia, "CMSampleBufferGetAudioStreamPacketDescriptionsPtr")
        )

        CoreMedia.CMSampleBufferCopyPCMDataIntoAudioBufferList
        CoreMedia.CMSampleBufferSetDataReady

        self.assertResultIsBOOL(CoreMedia.CMSampleBufferDataIsReady)

        CoreMedia.CMSampleBufferMakeDataReady
        CoreMedia.CMSampleBufferTrackDataReadiness
        CoreMedia.CMSampleBufferInvalidate

        self.assertArgIsFunction(
            CoreMedia.CMSampleBufferSetInvalidateCallback,
            1,
            CMSampleBufferInvalidateCallback,
            True,
        )

        self.assertResultIsBOOL(CoreMedia.CMSampleBufferIsValid)

        CoreMedia.CMSampleBufferGetNumSamples
        CoreMedia.CMSampleBufferGetDuration
        CoreMedia.CMSampleBufferGetPresentationTimeStamp
        CoreMedia.CMSampleBufferGetDecodeTimeStamp
        CoreMedia.CMSampleBufferGetOutputDuration
        CoreMedia.CMSampleBufferGetOutputPresentationTimeStamp
        CoreMedia.CMSampleBufferSetOutputPresentationTimeStamp
        CoreMedia.CMSampleBufferGetOutputDecodeTimeStamp

        self.assertArgIsOut(CoreMedia.CMSampleBufferGetSampleTimingInfoArray, 2)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferGetSampleTimingInfoArray, 2, 1)
        self.assertArgIsOut(CoreMedia.CMSampleBufferGetSampleTimingInfoArray, 3)

        self.assertArgIsOut(CoreMedia.CMSampleBufferGetOutputSampleTimingInfoArray, 2)
        self.assertArgSizeInArg(
            CoreMedia.CMSampleBufferGetOutputSampleTimingInfoArray, 2, 1
        )
        self.assertArgIsOut(CoreMedia.CMSampleBufferGetOutputSampleTimingInfoArray, 3)

        self.assertArgIsOut(CoreMedia.CMSampleBufferGetSampleTimingInfo, 2)

        self.assertArgIsOut(CoreMedia.CMSampleBufferGetSampleSizeArray, 2)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferGetSampleSizeArray, 2, 1)
        self.assertArgIsOut(CoreMedia.CMSampleBufferGetSampleSizeArray, 3)

        CoreMedia.CMSampleBufferGetSampleSize
        CoreMedia.CMSampleBufferGetTotalSampleSize
        CoreMedia.CMSampleBufferGetFormatDescription

        self.assertArgIsBOOL(CoreMedia.CMSampleBufferGetSampleAttachmentsArray, 1)

        self.assertArgIsFunction(
            CoreMedia.CMSampleBufferCallForEachSample,
            1,
            b"i^{opaqueCMSampleBuffer=}q^v",
            False,
        )

    @min_os_level("10.10")
    def test_functions10_10(self):
        self.assertArgIsIn(CoreMedia.CMSampleBufferCreateReady, 5)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferCreateReady, 5, 4)
        self.assertArgIsIn(CoreMedia.CMSampleBufferCreateReady, 7)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferCreateReady, 7, 6)
        self.assertArgIsOut(CoreMedia.CMSampleBufferCreateReady, 8)
        self.assertArgIsCFRetained(CoreMedia.CMSampleBufferCreateReady, 8)

        self.assertArgIsIn(
            CoreMedia.CMAudioSampleBufferCreateReadyWithPacketDescriptions, 5
        )
        self.assertArgSizeInArg(
            CoreMedia.CMAudioSampleBufferCreateReadyWithPacketDescriptions, 5, 3
        )
        self.assertArgIsOut(
            CoreMedia.CMAudioSampleBufferCreateReadyWithPacketDescriptions, 6
        )
        self.assertArgIsCFRetained(
            CoreMedia.CMAudioSampleBufferCreateReadyWithPacketDescriptions, 6
        )

        self.assertArgIsIn(CoreMedia.CMSampleBufferCreateReadyWithImageBuffer, 3)
        self.assertArgIsOut(CoreMedia.CMSampleBufferCreateReadyWithImageBuffer, 4)
        self.assertArgIsCFRetained(
            CoreMedia.CMSampleBufferCreateReadyWithImageBuffer, 4
        )

        CoreMedia.CMSampleBufferSetDataFailed

        self.assertResultIsBOOL(CoreMedia.CMSampleBufferHasDataFailed)
        self.assertArgIsOut(CoreMedia.CMSampleBufferHasDataFailed, 1)

        self.assertArgIsBlock(
            CoreMedia.CMSampleBufferSetInvalidateHandler,
            1,
            CMSampleBufferInvalidateHandler,
        )

        self.assertArgIsBlock(
            CoreMedia.CMSampleBufferCallBlockForEachSample,
            1,
            b"v^{opaqueCMSampleBuffer=}q",
        )

    @min_os_level("10.14.4")
    def test_functions_10_14_4(self):
        self.assertArgIsBOOL(CoreMedia.CMSampleBufferCreateWithMakeDataReadyHandler, 2)
        self.assertArgIsIn(CoreMedia.CMSampleBufferCreateWithMakeDataReadyHandler, 6)
        self.assertArgSizeInArg(
            CoreMedia.CMSampleBufferCreateWithMakeDataReadyHandler, 6, 5
        )
        self.assertArgIsOut(CoreMedia.CMSampleBufferCreateWithMakeDataReadyHandler, 7)
        self.assertArgIsCFRetained(
            CoreMedia.CMSampleBufferCreateWithMakeDataReadyHandler, 7
        )
        self.assertArgIsBlock(
            CoreMedia.CMSampleBufferCreateWithMakeDataReadyHandler,
            8,
            b"i^{OpaqueCMSampleBuffer=}",
        )

        self.assertArgIsBOOL(
            CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler,
            2,
        )
        self.assertArgIsIn(
            CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler,
            6,
        )
        self.assertArgSizeInArg(
            CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler,
            6,
            5,
        )
        self.assertArgIsOut(
            CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler,
            7,
        )
        self.assertArgIsCFRetained(
            CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler,
            7,
        )
        self.assertArgIsBlock(
            CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler,
            8,
            b"i^{OpaqueCMSampleBuffer=}",
        )

        self.assertArgIsBOOL(
            CoreMedia.CMSampleBufferCreateForImageBufferWithMakeDataReadyHandler, 2
        )
        self.assertArgIsOut(
            CoreMedia.CMSampleBufferCreateForImageBufferWithMakeDataReadyHandler, 5
        )
        self.assertArgIsCFRetained(
            CoreMedia.CMSampleBufferCreateForImageBufferWithMakeDataReadyHandler, 5
        )
        self.assertArgIsBlock(
            CoreMedia.CMSampleBufferCreateForImageBufferWithMakeDataReadyHandler,
            6,
            b"i^{OpaqueCMSampleBuffer=}",
        )
