
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebFrameLoadDelegateHelper (NSObject):
    def webView_willPerformClientRedirectToURL_delay_fireDate_forFrame_(self, a, b, c, d, e): pass


class TestWebFrameLoadDelegate (TestCase):
    def testMethods(self):
        self.failUnlessArgHasType(
                TestWebFrameLoadDelegateHelper.webView_willPerformClientRedirectToURL_delay_fireDate_forFrame_,
                2, objc._C_DBL)

if __name__ == "__main__":
    main()
