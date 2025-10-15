import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestAVCaptureTimecodeGeneratorHelper(AVFoundation.NSObject):
    def timecodeGenerator_didReceiveUpdate_fromSource_(self, a, b, c):
        pass

    def timecodeGenerator_transitionedToSynchronizationStatus_forSource_(self, a, b, c):
        pass


class TestAVCaptureTimecodeGenerator(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AVFoundation.AVCaptureTimecodeSourceType)
        self.assertEqual(AVFoundation.AVCaptureTimecodeSourceTypeFrameCount, 0)
        self.assertEqual(AVFoundation.AVCaptureTimecodeSourceTypeRealTimeClock, 1)
        self.assertEqual(AVFoundation.AVCaptureTimecodeSourceTypeExternal, 2)

        self.assertIsEnumType(
            AVFoundation.AVCaptureTimecodeGeneratorSynchronizationStatus
        )
        self.assertEqual(
            AVFoundation.AVCaptureTimecodeGeneratorSynchronizationStatusUnknown, 0
        )
        self.assertEqual(
            AVFoundation.AVCaptureTimecodeGeneratorSynchronizationStatusSourceSelected,
            1,
        )
        self.assertEqual(
            AVFoundation.AVCaptureTimecodeGeneratorSynchronizationStatusSynchronizing, 2
        )
        self.assertEqual(
            AVFoundation.AVCaptureTimecodeGeneratorSynchronizationStatusSynchronized, 3
        )
        self.assertEqual(
            AVFoundation.AVCaptureTimecodeGeneratorSynchronizationStatusTimedOut, 4
        )
        self.assertEqual(
            AVFoundation.AVCaptureTimecodeGeneratorSynchronizationStatusSourceUnavailable,
            5,
        )
        self.assertEqual(
            AVFoundation.AVCaptureTimecodeGeneratorSynchronizationStatusSourceUnsupported,
            6,
        )
        self.assertEqual(
            AVFoundation.AVCaptureTimecodeGeneratorSynchronizationStatusNotRequired, 7
        )

    def test_structs(self):
        v = AVFoundation.AVCaptureTimecode()
        self.assertIsInstance(v.hours, int)
        self.assertIsInstance(v.minutes, int)
        self.assertIsInstance(v.seconds, int)
        self.assertIsInstance(v.frames, int)
        self.assertIsInstance(v.userBits, int)
        self.assertIsInstance(v.frameDuration, AVFoundation.CMTime)
        self.assertIsInstance(v.sourceType, int)

    @min_os_level("26.0")
    def test_functions(self):
        self.assertResultIsCFRetained(
            AVFoundation.AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp
        )
        self.assertResultIsCFRetained(
            AVFoundation.AVCaptureTimecodeCreateMetadataSampleBufferForDuration
        )
        AVFoundation.AVCaptureTimecodeAdvancedByFrames

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("AVCaptureTimecodeGeneratorDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestAVCaptureTimecodeGeneratorHelper.timecodeGenerator_didReceiveUpdate_fromSource_,
            1,
            AVFoundation.AVCaptureTimecode.__typestr__,
        )
        self.assertArgHasType(
            TestAVCaptureTimecodeGeneratorHelper.timecodeGenerator_transitionedToSynchronizationStatus_forSource_,
            1,
            objc._C_NSInteger,
        )
