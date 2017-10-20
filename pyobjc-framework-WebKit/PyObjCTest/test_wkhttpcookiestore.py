from PyObjCTools.TestSupport import *
from WebKit import *


class TestWKError (TestCase):
    @min_sdk_level('10.13')
    def testProtocols(self):
        # Only on iOS:
        # objc.protocolNamed('WKHTTPCookieStoreObserver')
        pass

    @onlyOn64Bit
    @min_os_level('10.13')
    def test_methods(self):
        self.assertArgIsBlock(WKHTTPCookieStore.getAllCookies_, 0, b'v@')
        self.assertArgIsBlock(WKHTTPCookieStore.setCookie_completionHandler_, 1, b'v')
        self.assertArgIsBlock(WKHTTPCookieStore.deleteCookie_completionHandler_, 1, b'v')

if __name__ == "__main__":
    main()
