from PyObjCTools.TestSupport import TestCase

import ScreenCaptureKit


class TestRPReportingAgent(TestCase):
    def test_constants(self):
        self.assertEqual(ScreenCaptureKit.RP_REPORTING_CLIENT_NAME, "ReplayKit")
        self.assertEqual(
            ScreenCaptureKit.RP_REPORTING_SERVICE_NAME_SYSTEM_RECORDING,
            "SystemRecording",
        )
        self.assertEqual(
            ScreenCaptureKit.RP_REPORTING_SERVICE_NAME_SYSTEM_BROADCAST,
            "SystemBroadcast",
        )
        self.assertEqual(
            ScreenCaptureKit.RP_REPORTING_SERVICE_NAME_IN_APP_RECORDING,
            "InAppRecording",
        )
        self.assertEqual(
            ScreenCaptureKit.RP_REPORTING_SERVICE_NAME_IN_APP_BROADCAST,
            "InAppBroadcast",
        )
        self.assertEqual(
            ScreenCaptureKit.RP_REPORTING_SERVICE_NAME_IN_APP_CAPTURE, "InAppCapture"
        )
        self.assertEqual(
            ScreenCaptureKit.RP_REPORTING_SERVICE_NAME_IN_APP_CLIP, "InAppClip"
        )
        self.assertEqual(
            ScreenCaptureKit.RP_REPORTING_SERVICE_NAME_SCREEN_CAPTURE_KIT, "SCKCapture"
        )

        self.assertEqual(ScreenCaptureKit.RP_REPORTING_SUMMARY_EVENT, 1)
        self.assertEqual(ScreenCaptureKit.RP_REPORTING_END_REASON_SUMMARY_EVENT, 2)
        self.assertEqual(ScreenCaptureKit.RP_REPORTING_SCREENSHOT_EVENT, 3)
