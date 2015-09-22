
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebResourceLoadDelegateHelper (NSObject):
    def webView_resource_didReceiveContentLength_fromDataSource_(self, a, b, c, d): pass

class TestWebResourceLoadDelegate (TestCase):
    @min_sdk_level('10.11')
    def testProtocols(self):
        objc.protocolNamed('WebResourceLoadDelegate')

    def testMethods(self):
        self.assertArgHasType(
            TestWebResourceLoadDelegateHelper.webView_resource_didReceiveContentLength_fromDataSource_,
            2, objc._C_NSInteger)


if __name__ == "__main__":
    main()
