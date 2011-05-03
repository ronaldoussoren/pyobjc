from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSTreeNode (TestCase):

    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(NSTreeNode.isLeaf)
        self.assertArgIsBOOL(NSTreeNode.sortWithSortDescriptors_recursively_, 1)

if __name__ == "__main__":
    main()
