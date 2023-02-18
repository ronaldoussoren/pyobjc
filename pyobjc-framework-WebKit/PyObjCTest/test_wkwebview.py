from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit
import objc


class TestWKWebView(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(WebKit.WKFullscreenState)
        self.assertIsEnumType(WebKit.WKMediaCaptureState)
        self.assertIsEnumType(WebKit.WKMediaPlaybackState)

    def testConstants(self):
        self.assertEqual(WebKit.WKMediaPlaybackStateNone, 0)
        self.assertEqual(WebKit.WKMediaPlaybackStatePlaying, 1)
        self.assertEqual(WebKit.WKMediaPlaybackStatePaused, 2)
        self.assertEqual(WebKit.WKMediaPlaybackStateSuspended, 3)

        self.assertEqual(WebKit.WKMediaCaptureStateNone, 0)
        self.assertEqual(WebKit.WKMediaCaptureStateActive, 1)
        self.assertEqual(WebKit.WKMediaCaptureStateMuted, 2)

        self.assertEqual(WebKit.WKFullscreenStateNotInFullscreen, 0)
        self.assertEqual(WebKit.WKFullscreenStateEnteringFullscreen, 1)
        self.assertEqual(WebKit.WKFullscreenStateInFullscreen, 2)
        self.assertEqual(WebKit.WKFullscreenStateExitingFullscreen, 3)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(WebKit.WKWebView.isLoading)
        self.assertResultIsBOOL(WebKit.WKWebView.hasOnlySecureContent)
        self.assertResultIsBOOL(WebKit.WKWebView.canGoBack)
        self.assertResultIsBOOL(WebKit.WKWebView.canGoForward)
        self.assertResultIsBOOL(WebKit.WKWebView.allowsBackForwardNavigationGestures)
        self.assertArgIsBOOL(
            WebKit.WKWebView.setAllowsBackForwardNavigationGestures_, 0
        )
        self.assertResultIsBOOL(WebKit.WKWebView.allowsMagnification)
        self.assertArgIsBOOL(WebKit.WKWebView.setAllowsMagnification_, 0)
        self.assertArgIsBlock(
            WebKit.WKWebView.evaluateJavaScript_completionHandler_, 1, b"v@@"
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(WebKit.WKWebView.allowsLinkPreview)
        self.assertArgIsBOOL(WebKit.WKWebView.setAllowsLinkPreview_, 0)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            WebKit.WKWebView.takeSnapshotWithConfiguration_completionHandler_, 1, b"v@@"
        )
        self.assertResultIsBOOL(WebKit.WKWebView.handlesURLScheme_)

    @min_os_level("10.15.4")
    def testMethods10_15_4(self):
        self.assertArgIsBlock(
            WebKit.WKWebView.createPDFWithConfiguration_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.createWebArchiveDataWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.findString_withConfiguration_completionHandler_, 2, b"v@"
        )

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertArgIsBlock(
            WebKit.WKWebView.evaluateJavaScript_inFrame_inContentWorld_completionHandler_,
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.callAsyncJavaScript_arguments_inFrame_inContentWorld_completionHandler_,
            4,
            b"v@@",
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.pauseAllMediaPlayback_,
            0,
            b"v",
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.suspendAllMediaPlayback_,
            0,
            b"v",
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.resumeAllMediaPlayback_,
            0,
            b"v",
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.requestMediaPlaybackState_,
            0,
            b"v" + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.startDownloadUsingRequest_completionHandler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.resumeDownloadFromResumeData_completionHandler_, 1, b"v@"
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertArgIsBlock(
            WebKit.WKWebView.closeAllMediaPresentationsWithCompletionHandler_,
            0,
            b"v",
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.pauseAllMediaPlaybackWithCompletionHandler_,
            0,
            b"v",
        )

        self.assertArgIsBOOL(
            WebKit.WKWebView.setAllMediaPlaybackSuspended_completionHandler_, 0
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.setAllMediaPlaybackSuspended_completionHandler_,
            1,
            b"v",
        )

        self.assertArgIsBlock(
            WebKit.WKWebView.requestMediaPlaybackStateWithCompletionHandler_,
            0,
            b"vq",
        )

        self.assertArgIsBlock(
            WebKit.WKWebView.setMicrophoneCaptureState_completionHandler_,
            1,
            b"v",
        )

    @min_os_level("13.3")
    def testMethods13_3(self):
        self.assertResultIsBOOL(WebKit.WKWebView.isInspectable)
        self.assertArgIsBOOL(WebKit.WKWebView.setInspectable_, 0)
