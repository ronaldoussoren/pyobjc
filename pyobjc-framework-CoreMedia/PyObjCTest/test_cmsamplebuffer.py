from PyObjCTools.TestSupport import *

import CoreMedia

CMSampleBufferMakeDataReadyCallback = b'i^{opaqueCMSampleBuffer=}^v'
CMSampleBufferInvalidateHandler = b'v^{opaqueCMSampleBuffer=}'
CMSampleBufferInvalidateCallback = b'v^{opaqueCMSampleBuffer=}Q'

class TestCMSampleBuffer (TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMSampleBufferError_AllocationFailed, -12730)
        self.assertEqual(CoreMedia.kCMSampleBufferError_RequiredParameterMissing, -12731)
        self.assertEqual(CoreMedia.kCMSampleBufferError_AlreadyHasDataBuffer, -12732)
        self.assertEqual(CoreMedia.kCMSampleBufferError_BufferNotReady, -12733)
        self.assertEqual(CoreMedia.kCMSampleBufferError_SampleIndexOutOfRange, -12734)
        self.assertEqual(CoreMedia.kCMSampleBufferError_BufferHasNoSampleSizes, -12735)
        self.assertEqual(CoreMedia.kCMSampleBufferError_BufferHasNoSampleTimingInfo, -12736)
        self.assertEqual(CoreMedia.kCMSampleBufferError_ArrayTooSmall, -12737)
        self.assertEqual(CoreMedia.kCMSampleBufferError_InvalidEntryCount, -12738)
        self.assertEqual(CoreMedia.kCMSampleBufferError_CannotSubdivide, -12739)
        self.assertEqual(CoreMedia.kCMSampleBufferError_SampleTimingInfoInvalid, -12740)
        self.assertEqual(CoreMedia.kCMSampleBufferError_InvalidMediaTypeForOperation, -12741)
        self.assertEqual(CoreMedia.kCMSampleBufferError_InvalidSampleData, -12742)
        self.assertEqual(CoreMedia.kCMSampleBufferError_InvalidMediaFormat, -12743)
        self.assertEqual(CoreMedia.kCMSampleBufferError_Invalidated, -12744)
        self.assertEqual(CoreMedia.kCMSampleBufferError_DataFailed, -16750)
        self.assertEqual(CoreMedia.kCMSampleBufferError_DataCanceled, -16751)

        self.assertEqual(CoreMedia.kCMSampleBufferFlag_AudioBufferList_Assure16ByteAlignment, 1<<0)

        self.assertIsInstance(CoreMedia.kCMTimingInfoInvalid, CoreMedia.CMSampleTimingInfo)

        self.assertIsInstance(CoreMedia.kCMSampleBufferNotification_DataBecameReady, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferConduitNotification_InhibitOutputUntil, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferConduitNotificationParameter_ResumeTag, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferConduitNotification_ResetOutput, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferConsumerNotification_BufferConsumed, unicode)

        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_NotSync, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_PartialSync, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_HasRedundantCoding, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_IsDependedOnByOthers, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_DependsOnOthers, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_EarlierDisplayTimesAllowed, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_DisplayImmediately, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_DoNotDisplay, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_ResetDecoderBeforeDecoding, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_DrainAfterDecoding, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_PostNotificationWhenConsumed, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_ResumeOutput, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_TransitionID, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_TrimDurationAtStart, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_TrimDurationAtEnd, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_SpeedMultiplier, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_Reverse, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_FillDiscontinuitiesWithSilence, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_EmptyMedia, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_PermanentEmptyMedia, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_DisplayEmptyMediaImmediately, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_EndsPreviousSampleDuration, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_SampleReferenceURL, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_SampleReferenceByteOffset, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_GradualDecoderRefresh, unicode)

    @min_os_level('10.8')
    def test_constants10_8(self):
        self.assertIsInstance(CoreMedia.kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS, unicode)

    @min_os_level('10.10')
    def test_constants10_10(self):
        self.assertIsInstance(CoreMedia.kCMSampleBufferNotification_DataFailed, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferNotificationParameter_OSStatus, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleBufferAttachmentKey_ForceKeyFrame, unicode)

    @min_os_level('10.13')
    def test_constants10_13(self):
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_HEVCTemporalLevelInfo, unicode)
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_TemporalLevel, unicode)
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_ProfileSpace, unicode)
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_TierFlag, unicode)
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_ProfileIndex, unicode)
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_ProfileCompatibilityFlags, unicode)
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_ConstraintIndicatorFlags, unicode)
        self.assertIsInstance(CoreMedia.kCMHEVCTemporalLevelInfoKey_LevelIndex, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_HEVCTemporalSubLayerAccess, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_HEVCStepwiseTemporalSubLayerAccess, unicode)
        self.assertIsInstance(CoreMedia.kCMSampleAttachmentKey_HEVCSyncSampleNALUnitType, unicode)

    def test_types(self):
        self.assertIsCFType(CoreMedia.CMSampleBufferRef)

    def test_structs(self):
        v = CoreMedia.CMSampleTimingInfo()
        self.assertEqual(v.duration, CoreMedia.CMTime())
        self.assertEqual(v.presentationTimeStamp, CoreMedia.CMTime())
        self.assertEqual(v.decodeTimeStamp, CoreMedia.CMTime())

    def test_functions(self):
        self.assertArgIsBOOL(CoreMedia.CMSampleBufferCreate, 2)
        self.assertArgIsFunction(CoreMedia.CMSampleBufferCreate, 3, CMSampleBufferMakeDataReadyCallback, True)
        self.assertArgIsIn(CoreMedia.CMSampleBufferCreate, 8)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferCreate, 8, 7)
        self.assertArgIsIn(CoreMedia.CMSampleBufferCreate, 10)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferCreate, 10, 9)
        self.assertArgIsOut(CoreMedia.CMSampleBufferCreate, 11)
        self.assertArgIsCFRetained(CoreMedia.CMSampleBufferCreate, 11)


        self.assertArgIsBOOL(CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions, 2)
        self.assertArgIsFunction(CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions, 3, CMSampleBufferMakeDataReadyCallback, True)
        self.assertArgIsIn(CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions, 8)
        self.assertArgSizeInArg(CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions, 8, 6)
        self.assertArgIsOut(CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions, 9)
        self.assertArgIsCFRetained(CoreMedia.CMAudioSampleBufferCreateWithPacketDescriptions, 9)


        self.assertArgIsBOOL(CoreMedia.CMSampleBufferCreateForImageBuffer, 2)
        self.assertArgIsFunction(CoreMedia.CMSampleBufferCreateForImageBuffer, 3, CMSampleBufferMakeDataReadyCallback, True)
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

        self.assertArgIsOut(CoreMedia.CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer, 1)
        self.assertArgIsOut(CoreMedia.CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer, 7)
        self.assertArgIsCFRetained(CoreMedia.CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer, 7)

        self.assertArgIsOut(CoreMedia.CMSampleBufferGetAudioStreamPacketDescriptions, 2)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferGetAudioStreamPacketDescriptions, 2, 1)
        self.assertArgIsOut(CoreMedia.CMSampleBufferGetAudioStreamPacketDescriptions, 3)

        self.assertFalse(hasattr(CoreMedia, 'CMSampleBufferGetAudioStreamPacketDescriptionsPtr'))

        CoreMedia.CMSampleBufferCopyPCMDataIntoAudioBufferList
        CoreMedia.CMSampleBufferSetDataReady

        self.assertResultIsBOOL(CoreMedia.CMSampleBufferDataIsReady)

        CoreMedia.CMSampleBufferMakeDataReady
        CoreMedia.CMSampleBufferTrackDataReadiness
        CoreMedia.CMSampleBufferInvalidate

        self.assertArgIsFunction(CoreMedia.CMSampleBufferSetInvalidateCallback, 1, CMSampleBufferInvalidateCallback, True)

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
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferGetOutputSampleTimingInfoArray, 2, 1)
        self.assertArgIsOut(CoreMedia.CMSampleBufferGetOutputSampleTimingInfoArray, 3)

        self.assertArgIsOut(CoreMedia.CMSampleBufferGetSampleTimingInfo, 2)

        self.assertArgIsOut(CoreMedia.CMSampleBufferGetSampleSizeArray, 2)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferGetSampleSizeArray, 2, 1)
        self.assertArgIsOut(CoreMedia.CMSampleBufferGetSampleSizeArray, 3)

        CoreMedia.CMSampleBufferGetSampleSize
        CoreMedia.CMSampleBufferGetTotalSampleSize
        CoreMedia.CMSampleBufferGetFormatDescription

        self.assertArgIsBOOL(CoreMedia.CMSampleBufferGetSampleAttachmentsArray, 1)

        self.assertArgIsFunction(CoreMedia.CMSampleBufferCallForEachSample, 1, b'i^{opaqueCMSampleBuffer=}q^v', False)


    @min_os_level('10.10')
    def test_functions10_10(self):
        self.assertArgIsIn(CoreMedia.CMSampleBufferCreateReady, 5)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferCreateReady, 5, 4)
        self.assertArgIsIn(CoreMedia.CMSampleBufferCreateReady, 7)
        self.assertArgSizeInArg(CoreMedia.CMSampleBufferCreateReady, 7, 6)
        self.assertArgIsOut(CoreMedia.CMSampleBufferCreateReady, 8)
        self.assertArgIsCFRetained(CoreMedia.CMSampleBufferCreateReady, 8)

        self.assertArgIsIn(CoreMedia.CMAudioSampleBufferCreateReadyWithPacketDescriptions, 5)
        self.assertArgSizeInArg(CoreMedia.CMAudioSampleBufferCreateReadyWithPacketDescriptions, 5, 3)
        self.assertArgIsOut(CoreMedia.CMAudioSampleBufferCreateReadyWithPacketDescriptions, 6)
        self.assertArgIsCFRetained(CoreMedia.CMAudioSampleBufferCreateReadyWithPacketDescriptions, 6)

        self.assertArgIsIn(CoreMedia.CMSampleBufferCreateReadyWithImageBuffer, 3)
        self.assertArgIsOut(CoreMedia.CMSampleBufferCreateReadyWithImageBuffer, 4)
        self.assertArgIsCFRetained(CoreMedia.CMSampleBufferCreateReadyWithImageBuffer, 4)

        CoreMedia.CMSampleBufferSetDataFailed

        self.assertResultIsBOOL(CoreMedia.CMSampleBufferHasDataFailed)
        self.assertArgIsOut(CoreMedia.CMSampleBufferHasDataFailed, 1)

        self.assertArgIsBlock(CoreMedia.CMSampleBufferSetInvalidateHandler, 1, CMSampleBufferInvalidateHandler)

        self.assertArgIsBlock(CoreMedia.CMSampleBufferCallBlockForEachSample, 1, b'v^{opaqueCMSampleBuffer=}q')

if __name__ == "__main__":
    main()
