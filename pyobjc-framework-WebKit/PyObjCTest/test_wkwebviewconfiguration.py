from PyObjCTools.TestSupport import *
from WebKit import *
import sys

class TestWKWebViewConfiguration (TestCase):
    @onlyOn64Bit
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(WKWebViewConfiguration.suppressesIncrementalRendering)
        self.assertArgIsBOOL(WKWebViewConfiguration.setSuppressesIncrementalRendering_, 0)

    @onlyOn64Bit
    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(WKWebViewConfiguration.allowsAirPlayForMediaPlayback)
        self.assertArgIsBOOL(WKWebViewConfiguration.setAllowsAirPlayForMediaPlayback_, 0)

    def testConstants(self):
        self.assertEqual(WKUserInterfaceDirectionPolicyContent, 0)
        self.assertEqual(WKUserInterfaceDirectionPolicySystem, 1)

        self.assertEqual(WKAudiovisualMediaTypeNone, 0)
        self.assertEqual(WKAudiovisualMediaTypeAudio, 1 << 0)
        self.assertEqual(WKAudiovisualMediaTypeVideo, 1 << 1)
        self.assertEqual(WKAudiovisualMediaTypeAll, sys.maxsize * 2 + 1)



if __name__ == "__main__":
    main()
