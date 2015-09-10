from PyObjCTools.TestSupport import *
from WebKit import *

class TestWKUserScript (TestCase):
    @onlyOn64Bit
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(WKUserScriptInjectionTimeAtDocumentStart, 0)
        self.assertEqual(WKUserScriptInjectionTimeAtDocumentEnd, 1)

    @onlyOn64Bit
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(WKUserScript.isForMainFrameOnly)
        self.assertArgIsBOOL(WKUserScript.initWithSource_injectionTime_forMainFrameOnly_, 2)

if __name__ == "__main__":
    main()
