
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebResourceLoadDelegateHelper (NSObject):
    def webView_resource_didReceiveContentLength_fromDataSource_(self, a, b, c, d): pass

class TestWebResourceLoadDelegate (TestCase):
    def testMethods(self):
        self.failUnlessArgHasType(
            TestWebResourceLoadDelegateHelper.webView_resource_didReceiveContentLength_fromDataSource_,
            2, objc._C_NSInteger)
        

if __name__ == "__main__":
    main()
