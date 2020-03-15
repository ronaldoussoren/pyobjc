import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTreeNode(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTreeNode.isLeaf)
        self.assertArgIsBOOL(AppKit.NSTreeNode.sortWithSortDescriptors_recursively_, 1)
