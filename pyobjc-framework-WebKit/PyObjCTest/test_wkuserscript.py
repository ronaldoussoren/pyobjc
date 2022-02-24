from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKUserScript(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(WebKit.WKUserScriptInjectionTime)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(WebKit.WKUserScriptInjectionTimeAtDocumentStart, 0)
        self.assertEqual(WebKit.WKUserScriptInjectionTimeAtDocumentEnd, 1)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(WebKit.WKUserScript.isForMainFrameOnly)
        self.assertArgIsBOOL(
            WebKit.WKUserScript.initWithSource_injectionTime_forMainFrameOnly_, 2
        )

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertArgIsBOOL(
            WebKit.WKUserScript.initWithSource_injectionTime_forMainFrameOnly_inContentWorld_,
            2,
        )
