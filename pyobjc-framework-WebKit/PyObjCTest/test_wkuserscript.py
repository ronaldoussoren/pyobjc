from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit
import WebKit


class TestWKUserScript(TestCase):
    @onlyOn64Bit
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(WebKit.WKUserScriptInjectionTimeAtDocumentStart, 0)
        self.assertEqual(WebKit.WKUserScriptInjectionTimeAtDocumentEnd, 1)

    @onlyOn64Bit
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(WebKit.WKUserScript.isForMainFrameOnly)
        self.assertArgIsBOOL(
            WebKit.WKUserScript.initWithSource_injectionTime_forMainFrameOnly_, 2
        )
