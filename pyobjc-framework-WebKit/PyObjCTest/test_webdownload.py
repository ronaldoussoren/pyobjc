from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebDownload (TestCase):
    @min_sdk_level('10.11')
    def testProtocols(self):
        objc.protocolNamed('WebDownloadDelegate')

if __name__ == "__main__":
    main()
