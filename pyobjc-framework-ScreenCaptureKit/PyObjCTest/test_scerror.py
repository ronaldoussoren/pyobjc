from PyObjCTools.TestSupport import TestCase
import ScreenCaptureKit


class TestSCError(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ScreenCaptureKit.SCStreamErrorCode)

    def test_constants(self):
        self.assertEqual(ScreenCaptureKit.SCStreamErrorUserDeclined, -3801)
        self.assertEqual(ScreenCaptureKit.SCStreamErrorFailedToStart, -3802)
        self.assertEqual(ScreenCaptureKit.SCStreamErrorMissingEntitlements, -3803)
        self.assertEqual(
            ScreenCaptureKit.SCStreamErrorFailedApplicationConnectionInvalid, -3804
        )
        self.assertEqual(
            ScreenCaptureKit.SCStreamErrorFailedApplicationConnectionInterrupted, -3805
        )
        self.assertEqual(
            ScreenCaptureKit.SCStreamErrorFailedNoMatchingApplicationContext, -3806
        )
        self.assertEqual(ScreenCaptureKit.SCStreamErrorAttemptToStartStreamState, -3807)
        self.assertEqual(ScreenCaptureKit.SCStreamErrorAttemptToStopStreamState, -3808)
        self.assertEqual(
            ScreenCaptureKit.SCStreamErrorAttemptToUpdateFilterState, -3809
        )
        self.assertEqual(ScreenCaptureKit.SCStreamErrorAttemptToConfigState, -3810)
        self.assertEqual(ScreenCaptureKit.SCStreamErrorInternalError, -3811)
        self.assertEqual(ScreenCaptureKit.SCStreamErrorInvalidParameter, -3812)
        self.assertEqual(ScreenCaptureKit.SCStreamErrorNoWindowList, -3813)
        self.assertEqual(ScreenCaptureKit.SCStreamErrorNoDisplayList, -3814)
        self.assertEqual(ScreenCaptureKit.SCStreamErrorNoCaptureSource, -3815)
        self.assertEqual(ScreenCaptureKit.SCStreamErrorRemovingStream, -3816)
