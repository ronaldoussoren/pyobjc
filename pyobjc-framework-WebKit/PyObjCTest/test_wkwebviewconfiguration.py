import sys

from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebViewConfiguration(TestCase):
    def test_enums(self):
        self.assertIsEnumType(WebKit.WKUserInterfaceDirectionPolicy)
        self.assertEqual(WebKit.WKUserInterfaceDirectionPolicyContent, 0)
        self.assertEqual(WebKit.WKUserInterfaceDirectionPolicySystem, 1)

        self.assertIsEnumType(WebKit.WKAudiovisualMediaTypes)
        self.assertEqual(WebKit.WKAudiovisualMediaTypeNone, 0)
        self.assertEqual(WebKit.WKAudiovisualMediaTypeAudio, 1 << 0)
        self.assertEqual(WebKit.WKAudiovisualMediaTypeVideo, 1 << 1)
        self.assertEqual(WebKit.WKAudiovisualMediaTypeAll, sys.maxsize * 2 + 1)

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBOOL(
            WebKit.WKWebViewConfiguration.suppressesIncrementalRendering
        )
        self.assertArgIsBOOL(
            WebKit.WKWebViewConfiguration.setSuppressesIncrementalRendering_, 0
        )

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(
            WebKit.WKWebViewConfiguration.allowsAirPlayForMediaPlayback
        )
        self.assertArgIsBOOL(
            WebKit.WKWebViewConfiguration.setAllowsAirPlayForMediaPlayback_, 0
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(
            WebKit.WKWebViewConfiguration.limitsNavigationsToAppBoundDomains
        )

    @min_os_level("12.0")
    def test_methods11_3(self):
        # Not actually present on 11.6...
        self.assertResultIsBOOL(WebKit.WKWebViewConfiguration.upgradeKnownHostsToHTTPS)
        self.assertArgIsBOOL(
            WebKit.WKWebViewConfiguration.setUpgradeKnownHostsToHTTPS_, 0
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(WebKit.WKWebViewConfiguration.allowsInlinePredictions)
        self.assertArgIsBOOL(
            WebKit.WKWebViewConfiguration.setAllowsInlinePredictions_, 0
        )

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(
            WebKit.WKWebViewConfiguration.supportsAdaptiveImageGlyph
        )
        self.assertArgIsBOOL(
            WebKit.WKWebViewConfiguration.setSupportsAdaptiveImageGlyph_, 0
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(
            WebKit.WKWebViewConfiguration.showsSystemScreenTimeBlockingView
        )
        self.assertArgIsBOOL(
            WebKit.WKWebViewConfiguration.setShowsSystemScreenTimeBlockingView_, 0
        )
