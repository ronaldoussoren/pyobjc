
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDragging (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSDragOperationNone, 0)
        self.failUnlessEqual(NSDragOperationCopy, 1)
        self.failUnlessEqual(NSDragOperationLink, 2)
        self.failUnlessEqual(NSDragOperationGeneric, 4)
        self.failUnlessEqual(NSDragOperationPrivate, 8)
        self.failUnlessEqual(NSDragOperationAll_Obsolete, 15)
        self.failUnlessEqual(NSDragOperationMove, 16)
        self.failUnlessEqual(NSDragOperationDelete, 32)
        self.failUnlessEqual(NSDragOperationEvery, -1)

        self.failUnlessEqual(NSDragOperationAll, NSDragOperationAll_Obsolete)

if __name__ == "__main__":
    main()
