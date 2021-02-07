from PyObjCTools.TestSupport import TestCase, min_os_level
import AVKit
import objc


class TestAVCaptureView(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(AVKit.AVCaptureView, objc.objc_class)

    @min_os_level("10.10")
    def testProtocols(self):
        self.assertIsInstance(
            objc.protocolNamed("AVCaptureViewDelegate"), objc.formal_protocol
        )

    @min_os_level("10.10")
    def testMethods(self):
        self.assertArgIsBOOL(
            AVKit.AVCaptureView.setSession_showVideoPreview_showAudioPreview_, 1
        )
        self.assertArgIsBOOL(
            AVKit.AVCaptureView.setSession_showVideoPreview_showAudioPreview_, 2
        )

    @min_os_level("10.10")
    def test_constants(self):
        self.assertEqual(AVKit.AVCaptureViewControlsStyleInline, 0)
        self.assertEqual(AVKit.AVCaptureViewControlsStyleFloating, 1)
        self.assertEqual(AVKit.AVCaptureViewControlsStyleInlineDeviceSelection, 2)
        self.assertEqual(
            AVKit.AVCaptureViewControlsStyleDefault,
            AVKit.AVCaptureViewControlsStyleInline,
        )
