
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebFrameLoadDelegateHelper (NSObject):
    def webView_willPerformClientRedirectToURL_delay_fireDate_forFrame_(self, a, b, c, d, e): pass


class TestWebFrameLoadDelegate (TestCase):
    @min_sdk_level('10.11')
    def testProtocols(self):
        objc.protocolNamed('WebFrameLoadDelegate')

    def testMethods(self):
        self.assertArgHasType(
                TestWebFrameLoadDelegateHelper.webView_willPerformClientRedirectToURL_delay_fireDate_forFrame_,
                2, objc._C_DBL)

if __name__ == "__main__":
    main()
