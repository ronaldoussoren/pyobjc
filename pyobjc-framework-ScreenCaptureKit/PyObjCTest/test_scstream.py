import objc
from PyObjCTools.TestSupport import TestCase
import ScreenCaptureKit


class TestSCStream(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(ScreenCaptureKit.SCStreamFrameInfo, str)

    def test_enum_types(self):
        self.assertIsEnumType(ScreenCaptureKit.SCFrameStatus)
        self.assertIsEnumType(ScreenCaptureKit.SCStreamFrameInfo)

    def test_constants(self):
        self.assertEqual(ScreenCaptureKit.SCFrameStatusFrameComplete, 0)
        self.assertEqual(ScreenCaptureKit.SCFrameStatusFrameIdle, 1)
        self.assertEqual(ScreenCaptureKit.SCFrameStatusFrameBlank, 2)
        self.assertEqual(ScreenCaptureKit.SCFrameStatusFrameSuspended, 3)
        self.assertEqual(ScreenCaptureKit.SCFrameStatusFrameStarted, 4)
        self.assertEqual(ScreenCaptureKit.SCFrameStatusFrameStopped, 5)

        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoStatusKey, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoDisplayTimeKey, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoScaleFactorKey, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoContentScaleKey, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoContentRectKey, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoDirtyRectsKey, str)

    def test_methods(self):
        self.assertResultIsBOOL(ScreenCaptureKit.SCStreamConfiguration.scalesToFit)
        self.assertArgIsBOOL(ScreenCaptureKit.SCStreamConfiguration.setScalesToFit_, 0)

        self.assertResultIsBOOL(ScreenCaptureKit.SCStreamConfiguration.showsCursor)
        self.assertArgIsBOOL(ScreenCaptureKit.SCStreamConfiguration.setShowsCursor_, 0)

        self.assertArgIsBlock(
            ScreenCaptureKit.SCStream.updateContentFilter_completionHandler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCStream.updateStreamConfiguration_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCStream.startCaptureWithFrameHandler_,
            0,
            b"v^{CMSampleBuffer}",
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCStream.stopWithCompletionHandler_, 0, b"v@"
        )

    def test_protocols(self):
        objc.protocolNamed("SCStreamDelegate")
