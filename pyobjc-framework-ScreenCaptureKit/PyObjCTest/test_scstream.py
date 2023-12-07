import objc
from PyObjCTools.TestSupport import TestCase, min_os_level
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
        self.assertEqual(ScreenCaptureKit.SCStreamOutputTypeAudio, 1)

        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoStatus, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoDisplayTime, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoScaleFactor, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoContentScale, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoContentRect, str)
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoDirtyRects, str)

        self.assertIsEnumType(ScreenCaptureKit.SCStreamType)
        self.assertEqual(ScreenCaptureKit.SCStreamTypeWindow, 0)
        self.assertEqual(ScreenCaptureKit.SCStreamTypeDisplay, 1)

        self.assertIsEnumType(ScreenCaptureKit.SCCaptureResolutionType)
        self.assertEqual(ScreenCaptureKit.SCCaptureResolutionAutomatic, 0)
        self.assertEqual(ScreenCaptureKit.SCCaptureResolutionBest, 1)
        self.assertEqual(ScreenCaptureKit.SCCaptureResolutionNominal, 2)

        self.assertIsEnumType(ScreenCaptureKit.SCPresenterOverlayAlertSetting)
        self.assertEqual(ScreenCaptureKit.SCPresenterOverlayAlertSettingSystem, 0)
        self.assertEqual(ScreenCaptureKit.SCPresenterOverlayAlertSettingNever, 1)
        self.assertEqual(ScreenCaptureKit.SCPresenterOverlayAlertSettingAlways, 2)

    @min_os_level("13.1")
    def test_constants13_1(self):
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoScreenRect, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(ScreenCaptureKit.SCStreamFrameInfoBoundingRect, str)

    @min_os_level("14.2")
    def test_constants14_2(self):
        self.assertIsInstance(
            ScreenCaptureKit.SCStreamFrameInfoPresenterOverlayContentRect, str
        )

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

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(ScreenCaptureKit.SCStreamConfiguration.capturesAudio)
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.setCapturesAudio_, 0
        )

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.excludesCurrentProcessAudio
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.setExcludesCurrentProcessAudio_, 0
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.preservesAspectRatio
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.setPreservesAspectRatio_, 0
        )

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.ignoreShadowsDisplay
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.setIgnoreShadowsDisplay_, 0
        )

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.ignoreShadowsSingleWindow
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.setIgnoreShadowsSingleWindow_, 0
        )

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.capturesShadowsOnly
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.setCapturesShadowsOnly_, 0
        )

        self.assertResultIsBOOL(ScreenCaptureKit.SCStreamConfiguration.shouldBeOpaque)
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.setShouldBeOpaque_, 0
        )

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.ignoreGlobalClipDisplay
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.setIgnoreGlobalClipDisplay_, 0
        )

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.ignoreGlobalClipSingleWindow
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.setIgnoreGlobalClipSingleWindow_, 0
        )

    @min_os_level("14.2")
    def test_methods14_2(self):
        self.assertResultIsBOOL(ScreenCaptureKit.SCContentFilter.includeMenuBar)
        self.assertArgIsBOOL(ScreenCaptureKit.SCContentFilter.setIncludeMenuBar_, 0)

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.includeChildWindows
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCStreamConfiguration.setIncludeChildWindows_, 0
        )

    def test_protocols(self):
        self.assertProtocolExists("SCStreamDelegate")
        self.assertProtocolExists("SCStreamOutput")

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
