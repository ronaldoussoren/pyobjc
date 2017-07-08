from PyObjCTools.TestSupport import *
from WebKit import *


class TestWKUrlSchemeTask (TestCase):
    @min_sdk_level('10.13')
    def testProtocols(self):
        objc.protocolNamed('WKURLSchemeTask')


if __name__ == "__main__":
    main()
