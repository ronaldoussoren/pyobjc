from CoreFoundation import *
import unittest

class TestCFTree (unittest.TestCase):
    def testCreation(self):
        context = object()
        tree = CFTreeCreate(None, context)

        self.assert_(isinstance(tree, CFTreeRef))

        self.assert_(CFTreeGetContext(tree) is context)
        CFTreeSetContext(tree, 42)
        self.assertEquals(CFTreeGetContext(tree), 42)



    def testCreateTree(self):
        root = CFTreeCreate(None, "root")

        for child in range(10):
            CFTreeAppendChild(root, CFTreeCreate(None, child))

        self.assertEquals(CFTreeGetContext(CFTreeGetFirstChild(root)), 0)

        def compare(l, r, context):
            return -cmp(CFTreeGetContext(l), CFTreeGetContext(r))

        CFTreeSortChildren(root, compare, None)
        self.assertEquals(CFTreeGetContext(CFTreeGetFirstChild(root)), 9)



if __name__ == "__main__":
    unittest.main()
