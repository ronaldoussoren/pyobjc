import sys

from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebViewConfiguration(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(WebKit.WKAudiovisualMediaTypes)
        self.assertIsEnumType(WebKit.WKUserInterfaceDirectionPolicy)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(
            WebKit.WKWebViewConfiguration.suppressesIncrementalRendering
        )
        self.assertArgIsBOOL(
            WebKit.WKWebViewConfiguration.setSuppressesIncrementalRendering_, 0
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(
            WebKit.WKWebViewConfiguration.allowsAirPlayForMediaPlayback
        )
        self.assertArgIsBOOL(
            WebKit.WKWebViewConfiguration.setAllowsAirPlayForMediaPlayback_, 0
        )

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(
            WebKit.WKWebViewConfiguration.limitsNavigationsToAppBoundDomains
        )

    @min_os_level("12.0")
    def testMethods11_3(self):
        # Not actually present on 11.6...
        self.assertResultIsBOOL(WebKit.WKWebViewConfiguration.upgradeKnownHostsToHTTPS)
        self.assertArgIsBOOL(
            WebKit.WKWebViewConfiguration.setUpgradeKnownHostsToHTTPS_, 0
        )

    def testConstants(self):
        self.assertEqual(WebKit.WKUserInterfaceDirectionPolicyContent, 0)
        self.assertEqual(WebKit.WKUserInterfaceDirectionPolicySystem, 1)

        self.assertEqual(WebKit.WKAudiovisualMediaTypeNone, 0)
        self.assertEqual(WebKit.WKAudiovisualMediaTypeAudio, 1 << 0)
        self.assertEqual(WebKit.WKAudiovisualMediaTypeVideo, 1 << 1)

        # The entire enum is only available in 64-bit code.
        self.assertEqual(WebKit.WKAudiovisualMediaTypeAll, sys.maxsize * 2 + 1)
