from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSCache (TestCase):
    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(NSCache.evictsObjectsWithDiscardedContent)
        self.assertArgIsBOOL(NSCache.setEvictsObjectsWithDiscardedContent_,0)

if __name__ == "__main__":
    main()
