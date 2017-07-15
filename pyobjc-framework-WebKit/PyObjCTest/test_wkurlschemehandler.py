from PyObjCTools.TestSupport import *
from WebKit import *


class TestWKUrlSchemeHandler (TestCase):
    @min_sdk_level('10.13')
    def testProtocols(self):
        # Only on iOS:
        # objc.protocolNamed('WKURLSchemeHandler')
        pass


if __name__ == "__main__":
    main()
