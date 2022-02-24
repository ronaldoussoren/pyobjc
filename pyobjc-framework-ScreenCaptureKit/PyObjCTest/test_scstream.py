import objc
from PyObjCTools.TestSupport import TestCase
import ScreenCaptureKit


class TestSCStreamHelper(ScreenCaptureKit.NSObject):
    def stream_didOutputSampleBuffer_ofType_(self, a, b, c):
        pass


class TestSCStream(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(ScreenCaptureKit.SCStreamFrameInfo, str)

    def test_enum_types(self):
        self.assertIsEnumType(ScreenCaptureKit.SCFrameStatus)
        self.assertIsEnumType(ScreenCaptureKit.SCStreamOutputType)

    def test_constants(self):
        self.assertEqual(ScreenCaptureKit.SCFrameStatusComplete, 0)
        self.assertEqual(ScreenCaptureKit.SCFrameStatusIdle, 1)
        self.assertEqual(ScreenCaptureKit.SCFrameStatusBlank, 2)
        self.assertEqual(ScreenCaptureKit.SCFrameStatusSuspended, 3)
        self.assertEqual(ScreenCaptureKit.SCFrameStatusStarted, 4)
        self.assertEqual(ScreenCaptureKit.SCFrameStatusStopped, 5)

        self.assertEqual(ScreenCaptureKit.SCStreamOutputTypeScreen, 0)

        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoStatus, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoDisplayTime, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoScaleFactor, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoContentScale, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoContentRect, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoDirtyRects, str)

    def test_methods(self):
        self.assertResultIsBOOL(ScreenCaptureKit.SCStreamConfiguration.scalesToFit)
        self.assertArgIsBOOL(ScreenCaptureKit.SCStreamConfiguration.setScalesToFit_, 0)

        self.assertResultIsBOOL(ScreenCaptureKit.SCStreamConfiguration.showsCursor)
        self.assertArgIsBOOL(ScreenCaptureKit.SCStreamConfiguration.setShowsCursor_, 0)

        self.assertArgIsBlock(
            ScreenCaptureKit.SCStream.updateContentFilter_completionHandler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCStream.updateConfiguration_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCStream.startCaptureWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCStream.stopCaptureWithCompletionHandler_, 0, b"v@"
        )

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCStream.addStreamOutput_type_sampleHandlerQueue_error_
        )
        self.assertArgIsOut(
            ScreenCaptureKit.SCStream.addStreamOutput_type_sampleHandlerQueue_error_, 3
        )

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCStream.removeStreamOutput_type_error_
        )
        self.assertArgIsOut(ScreenCaptureKit.SCStream.removeStreamOutput_type_error_, 2)

    def test_protocols(self):
        objc.protocolNamed("SCStreamDelegate")
        objc.protocolNamed("SCStreamOutput")

    def test_proto_methods(self):
        self.assertArgHasType(
            TestSCStreamHelper.stream_didOutputSampleBuffer_ofType_,
            1,
            b"^{opaqueCMSampleBuffer=}",
        )
        self.assertArgHasType(
            TestSCStreamHelper.stream_didOutputSampleBuffer_ofType_,
            2,
            objc._C_NSInteger,
        )
