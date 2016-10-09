from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSFilePromiseProviderHelper (NSObject):
    def filePromiseProvider_writePromiseToURL_completionHandler_(self, p, u, h): pass

class TestNSFilePromiseProvider (TestCase):
    @min_sdk_level('10.12')
    def testProtocols(self):
        objc.protocolNamed('NSFilePromiseProviderDelegate')

    def testMethods(self):
        self.assertArgIsBlock(TestNSFilePromiseProviderHelper.filePromiseProvider_writePromiseToURL_completionHandler_, 2, b'v@')


if __name__ == "__main__":
    main()
