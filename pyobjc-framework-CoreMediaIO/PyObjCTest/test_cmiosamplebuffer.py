from PyObjCTools.TestSupport import *

import CoreMediaIO

MIODeviceStreamQueueAlteredProc = b'vI^v^v'

CMIOStreamScheduledOutputNotificationProc = b'vQQ^v'


class TestCMIOSampleBuffer (TestCase):
    def testDefines(self):
        self.assertEqual(CoreMediaIO.CMIOGetNextSequenceNumber(0), 1)
        self.assertEqual(CoreMediaIO.CMIOGetNextSequenceNumber(42), 43)
        self.assertEqual(CoreMediaIO.CMIOGetNextSequenceNumber(CoreMediaIO.kCMIOInvalidSequenceNumber), 0)

        self.assertIs(CoreMediaIO.CMIODiscontinuityFlagsHaveHardDiscontinuities(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_MalformedData | CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DurationWasExtended), True)
        self.assertIs(CoreMediaIO.CMIODiscontinuityFlagsHaveHardDiscontinuities(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_MalformedData), False)

    def testConstants(self):
        self.assertEqual(CoreMediaIO.kCMIOInvalidSequenceNumber, 0xffffffffffffffff)

        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDiscontinuities, 0)

        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_UnknownDiscontinuity, 1 << 0)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_TimecodeDiscontinuity, 1 << 1)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_PacketError, 1 << 2)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_StreamDiscontinuity, 1 << 3)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_MalformedData, 1 << 4)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DataWasFlushed, 1 << 5)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DataWasDropped, 1 << 6)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_BufferOverrun, 1 << 7)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DiscontinuityInDTS, 1 << 8)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_RelatedToDiscontinuity, 1 << 9)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_ClientSyncDiscontinuity, 1 << 10)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_TrickPlay, 1 << 11)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_NoDataMarker, 1 << 12)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DataFormatChanged, 1 << 13)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_TimingReferenceJumped, 1 << 14)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DurationWasExtended, 1 << 15)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_SleepWakeCycle, 1 << 16)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_CodecSettingsChanged, 1 << 17)

        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_Unknown, 0)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_NoMedia, 1)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_DeviceDidNotSync, 2)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_DeviceInWrongMode, 3)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_ProcessingError, 4)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_SleepWakeCycle, 5)


    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_DiscontinuityFlags, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_SequenceNumber, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_HDV1_PackData, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_HDV2_VAUX, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_CAAudioTimeStamp, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_SMPTETime, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_NativeSMPTEFrameCount, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_NumberOfVideoFramesInBuffer, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_NumberOfVideoFramesInGOP, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_MuxedSourcePresentationTimeStamp, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_HostTime, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_RepeatedBufferContents, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_SourceAudioFormatDescription, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_PulldownCadenceInfo, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_ClosedCaptionSampleBuffer, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_NoDataMarker, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOBlockBufferAttachmentKey_CVPixelBufferReference, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_ClientSequenceID, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_MouseAndKeyboardModifiers, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorPositionX, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorPositionY, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_MouseButtonState, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_KeyboardModifiers, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorIsVisible, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorFrameRect, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorReference, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorSeed, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorScale, unicode)

    @min_os_level('10.14')
    def testConstants10_14(self):
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorIsDrawnInFramebuffer, unicode)
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_KeyboardModifiersEvent, unicode)

    def testFunctions(self):
        self.assertArgIsIn(CoreMediaIO.CMIOSampleBufferCreate, 5)
        self.assertArgSizeInArg(CoreMediaIO.CMIOSampleBufferCreate, 5, 4)
        self.assertArgIsIn(CoreMediaIO.CMIOSampleBufferCreate, 7)
        self.assertArgSizeInArg(CoreMediaIO.CMIOSampleBufferCreate, 7, 6)
        self.assertArgIsOut(CoreMediaIO.CMIOSampleBufferCreate, 10)
        self.assertArgIsCFRetained(CoreMediaIO.CMIOSampleBufferCreate, 10)

        self.assertArgIsIn(CoreMediaIO.CMIOSampleBufferCreateForImageBuffer, 3)
        self.assertArgIsOut(CoreMediaIO.CMIOSampleBufferCreateForImageBuffer, 6)
        self.assertArgIsCFRetained(CoreMediaIO.CMIOSampleBufferCreateForImageBuffer, 6)

        self.assertArgIsOut(CoreMediaIO.CMIOSampleBufferCreateNoDataMarker, 5)
        self.assertArgIsCFRetained(CoreMediaIO.CMIOSampleBufferCreateNoDataMarker, 5)

        CoreMediaIO.CMIOSampleBufferSetSequenceNumber
        CoreMediaIO.CMIOSampleBufferGetSequenceNumber
        CoreMediaIO.CMIOSampleBufferSetDiscontinuityFlags
        CoreMediaIO.CMIOSampleBufferGetDiscontinuityFlags
        CoreMediaIO.CMIOSampleBufferCopyNonRequiredAttachments
        CoreMediaIO.CMIOSampleBufferCopySampleAttachments


if __name__ == "__main__":
        main()
