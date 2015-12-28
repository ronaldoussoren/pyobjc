from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSCache (TestCase):
    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(NSCache.evictsObjectsWithDiscardedContent)
        self.assertArgIsBOOL(NSCache.setEvictsObjectsWithDiscardedContent_,0)

    @min_sdk_level('10.10')
    def testProtocols(self):
        objc.protocolNamed('NSCacheDelegate')

if __name__ == "__main__":
    main()
