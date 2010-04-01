
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSAtomicStore (TestCase):

    @min_os_level('10.5')
    def testMethods(self):
        self.assertArgIsOut(NSAtomicStore.load_, 0)
        self.assertArgIsOut(NSAtomicStore.save_, 0)

if __name__ == "__main__":
    main()
