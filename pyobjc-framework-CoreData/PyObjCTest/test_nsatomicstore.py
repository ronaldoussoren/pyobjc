
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSAtomicStore (TestCase):

    def testMethods(self):
        self.failUnlessArgIsOut(NSAtomicStore.load_, 0)
        self.failUnlessArgIsOut(NSAtomicStore.save_, 0)

if __name__ == "__main__":
    main()
