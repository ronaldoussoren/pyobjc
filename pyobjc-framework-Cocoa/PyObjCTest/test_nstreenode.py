import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTreeNode(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSTreeNode.isLeaf)
        self.assertArgIsBOOL(AppKit.NSTreeNode.sortWithSortDescriptors_recursively_, 1)
