from CoreFoundation import *
from PyObjCTools.TestSupport import *

import sys
if sys.version_info[0] == 3:
    def cmp(a, b):
        try:
            if a < b:
                return -1
            elif b < a:
                return 1
            return 0

        except TypeError:
            return cmp(type(a).__name__, type(b).__name__)

class TestCFTree (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFTreeRef)

    def testCreation(self):
        context = object()
        tree = CFTreeCreate(None, context)

        self.assert_(isinstance(tree, CFTreeRef))

        self.assert_(CFTreeGetContext(tree, None) is context)
        CFTreeSetContext(tree, 42)
        self.assertEqual(CFTreeGetContext(tree, None), 42)



    def testCreateTree(self):
        root = CFTreeCreate(None, "root")

        for child in range(10):
            CFTreeAppendChild(root, CFTreeCreate(None, child))

        self.assertEqual(CFTreeGetContext(CFTreeGetFirstChild(root), None), 0)

        def compare(l, r, context):
            return -cmp(CFTreeGetContext(l, None), CFTreeGetContext(r, None))

        CFTreeSortChildren(root, compare, None)
        self.assertEqual(CFTreeGetContext(CFTreeGetFirstChild(root), None), 9)


    def testTypeID(self):
        v = CFTreeGetTypeID()
        self.assertIsInstance(v, (int, long))
    def testQuerying(self):
        root = CFTreeCreate(None, "root")

        for child in range(2):
            CFTreeAppendChild(root, CFTreeCreate(None, child))

        p = CFTreeGetParent(root)
        self.assertIs(p, None)
        c = CFTreeGetFirstChild(root)
        self.assertIsInstance(c, CFTreeRef)
        c2 = CFTreeGetChildAtIndex(root, 0)
        self.assertIs(c, c2)
        p = CFTreeGetParent(c)
        self.assertIs(p, root)
        s = CFTreeGetNextSibling(c)
        self.assertIsInstance(s, CFTreeRef)
        p = CFTreeGetParent(s)
        self.assertIs(p, root)
        s2 = CFTreeGetChildAtIndex(root, 1)
        self.assertIs(s, s2)
        s = CFTreeGetNextSibling(s)
        self.assertIs(s, None)
        cnt = CFTreeGetChildCount(root)
        self.assertEqual(cnt, 2)

        cnt = CFTreeGetChildCount(c)
        self.assertEqual(cnt, 0)

        children = CFTreeGetChildren(root, None)
        self.assertIsInstance(children, (list, tuple))
        self.assertEqual(len(children), 2)

        r = CFTreeFindRoot(s2)
        self.assertIs(r, root)
    def testModification(self):
        root = CFTreeCreate(None, "root")

        for child in range(2):
            CFTreeAppendChild(root, CFTreeCreate(None, child))

        def applyFunc(node, context):
            context.append(CFTreeGetContext(node, None))

        l = []
        CFTreeApplyFunctionToChildren(root, applyFunc, l)
        self.assertEqual(len(l), 2)

        preChild = CFTreeCreate(None, "before")
        postChild = CFTreeCreate(None, "after")
        CFTreePrependChild(root, preChild)
        CFTreeAppendChild(root, postChild)

        self.assertEqual(CFTreeGetChildCount(root), 4)
        n = CFTreeGetChildAtIndex(root, 0)
        self.assertIs(n, preChild)
        n = CFTreeGetChildAtIndex(root, 3)
        self.assertIs(n, postChild)
        s = CFTreeCreate(None, "sibling")
        CFTreeInsertSibling(preChild, s)
        n = CFTreeGetChildAtIndex(root, 1)
        self.assertIs(n, s)
        self.assertEqual(CFTreeGetChildCount(root), 5)

        CFTreeRemove(s)
        self.assertEqual(CFTreeGetChildCount(root), 4)

        def compare(left, right, context):
            left = CFTreeGetContext(left, None)
            right = CFTreeGetContext(right, None)
            return -cmp(left, right)

        before = []
        after = []
        CFTreeApplyFunctionToChildren(root, applyFunc, before)
        CFTreeSortChildren(root, compare, None)
        CFTreeApplyFunctionToChildren(root, applyFunc, after)

        before.sort()
        before.reverse()
        self.assertEqual(before, after)

        CFTreeRemoveAllChildren(root)
        self.assertEqual(CFTreeGetChildCount(root), 0)








if __name__ == "__main__":
    main()
