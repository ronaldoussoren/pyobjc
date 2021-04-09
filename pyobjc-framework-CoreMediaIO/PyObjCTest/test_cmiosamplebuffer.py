import CoreMediaIO
from PyObjCTools.TestSupport import TestCase, min_os_level

MIODeviceStreamQueueAlteredProc = b"vI^v^v"

CMIOStreamScheduledOutputNotificationProc = b"vQQ^v"


class TestCMIOSampleBuffer(TestCase):
    def testDefines(self):
        self.assertEqual(CoreMediaIO.CMIOGetNextSequenceNumber(0), 1)
        self.assertEqual(CoreMediaIO.CMIOGetNextSequenceNumber(42), 43)
        self.assertEqual(
            CoreMediaIO.CMIOGetNextSequenceNumber(
                CoreMediaIO.kCMIOInvalidSequenceNumber
            ),
            0,
        )

        self.assertIs(
            CoreMediaIO.CMIODiscontinuityFlagsHaveHardDiscontinuities(
                CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_MalformedData
                | CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DurationWasExtended
            ),
            True,
        )
        self.assertIs(
            CoreMediaIO.CMIODiscontinuityFlagsHaveHardDiscontinuities(
                CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_MalformedData
            ),
            False,
        )

    def testConstants(self):
        self.assertEqual(CoreMediaIO.kCMIOInvalidSequenceNumber, 0xFFFFFFFFFFFFFFFF)

        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDiscontinuities, 0)

        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_UnknownDiscontinuity, 1 << 0
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_TimecodeDiscontinuity, 1 << 1
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_PacketError, 1 << 2
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_StreamDiscontinuity, 1 << 3
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_MalformedData, 1 << 4
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DataWasFlushed, 1 << 5
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DataWasDropped, 1 << 6
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_BufferOverrun, 1 << 7
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DiscontinuityInDTS, 1 << 8
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_RelatedToDiscontinuity,
            1 << 9,
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_ClientSyncDiscontinuity,
            1 << 10,
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_TrickPlay, 1 << 11
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_NoDataMarker, 1 << 12
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DataFormatChanged, 1 << 13
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_TimingReferenceJumped,
            1 << 14,
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_DurationWasExtended, 1 << 15
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_SleepWakeCycle, 1 << 16
        )
        self.assertEqual(
            CoreMediaIO.kCMIOSampleBufferDiscontinuityFlag_CodecSettingsChanged, 1 << 17
        )

        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_Unknown, 0)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_NoMedia, 1)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_DeviceDidNotSync, 2)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_DeviceInWrongMode, 3)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_ProcessingError, 4)
        self.assertEqual(CoreMediaIO.kCMIOSampleBufferNoDataEvent_SleepWakeCycle, 5)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_DiscontinuityFlags, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_SequenceNumber, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_HDV1_PackData, str
        )
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_HDV2_VAUX, str)
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_CAAudioTimeStamp, str
        )
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_SMPTETime, str)
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_NativeSMPTEFrameCount, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_NumberOfVideoFramesInBuffer, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_NumberOfVideoFramesInGOP, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_MuxedSourcePresentationTimeStamp,
            str,
        )
        self.assertIsInstance(CoreMediaIO.kCMIOSampleBufferAttachmentKey_HostTime, str)
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_RepeatedBufferContents, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_SourceAudioFormatDescription, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_PulldownCadenceInfo, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_ClosedCaptionSampleBuffer, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_NoDataMarker, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOBlockBufferAttachmentKey_CVPixelBufferReference, str
        )

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_ClientSequenceID, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachmentKey_MouseAndKeyboardModifiers, str
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorPositionX,
            str,
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorPositionY,
            str,
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_MouseButtonState,
            str,
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_KeyboardModifiers,
            str,
        )

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorIsVisible,
            str,
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorFrameRect,
            str,
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorReference,
            str,
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorSeed,
            str,
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorScale,
            str,
        )

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorIsDrawnInFramebuffer,
            str,
        )
        self.assertIsInstance(
            CoreMediaIO.kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_KeyboardModifiersEvent,
            str,
        )

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
