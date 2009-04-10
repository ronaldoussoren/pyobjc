from CoreFoundation import *
from PyObjCTools.TestSupport import *

class TestCFTree (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFTreeRef)

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


    def testTypeID(self):
        v = CFTreeGetTypeID()
        self.failUnless(isinstance(v, (int, long)))

    def testQuerying(self):
        root = CFTreeCreate(None, "root")

        for child in range(2):
            CFTreeAppendChild(root, CFTreeCreate(None, child))

        p = CFTreeGetParent(root)
        self.failUnless(p is None)

        c = CFTreeGetFirstChild(root)
        self.failUnless(isinstance(c, CFTreeRef))
        c2 = CFTreeGetChildAtIndex(root, 0)
        self.failUnless(c is c2)

        p = CFTreeGetParent(c)
        self.failUnless(p is root)

        s = CFTreeGetNextSibling(c)
        self.failUnless(isinstance(s, CFTreeRef))
        p = CFTreeGetParent(s)
        self.failUnless(p is root)
        s2 = CFTreeGetChildAtIndex(root, 1)
        self.failUnless(s is s2)

        s = CFTreeGetNextSibling(s)
        self.failUnless(s is None)

        cnt = CFTreeGetChildCount(root)
        self.assertEquals(cnt, 2)

        cnt = CFTreeGetChildCount(c)
        self.assertEquals(cnt, 0)

        children = CFTreeGetChildren(root, None)
        self.failUnless(isinstance(children, (list, tuple)))
        self.assertEquals(len(children), 2)

        r = CFTreeFindRoot(s2)
        self.failUnless(r is root)

    def testModification(self):
        root = CFTreeCreate(None, "root")

        for child in range(2):
            CFTreeAppendChild(root, CFTreeCreate(None, child))

        def applyFunc(node, context):
            context.append(CFTreeGetContext(node))

        l = []
        CFTreeApplyFunctionToChildren(root, applyFunc, l)
        self.assertEquals(len(l), 2)

        preChild = CFTreeCreate(None, "before")
        postChild = CFTreeCreate(None, "after")
        CFTreePrependChild(root, preChild)
        CFTreeAppendChild(root, postChild)

        self.assertEquals(CFTreeGetChildCount(root), 4)
        n = CFTreeGetChildAtIndex(root, 0)
        self.failUnless(n is preChild)
        n = CFTreeGetChildAtIndex(root, 3)
        self.failUnless(n is postChild)

        s = CFTreeCreate(None, "sibling")
        CFTreeInsertSibling(preChild, s)
        n = CFTreeGetChildAtIndex(root, 1)
        self.failUnless(n is s)
        self.assertEquals(CFTreeGetChildCount(root), 5)

        CFTreeRemove(s)
        self.assertEquals(CFTreeGetChildCount(root), 4)

        def compare(left, right, context):
            left = CFTreeGetContext(left)
            right = CFTreeGetContext(right)
            return -cmp(left, right)

        before = []
        after = []
        CFTreeApplyFunctionToChildren(root, applyFunc, before)
        CFTreeSortChildren(root, compare, None)
        CFTreeApplyFunctionToChildren(root, applyFunc, after)

        before.sort()
        before.reverse()
        self.assertEquals(before, after)

        CFTreeRemoveAllChildren(root)
        self.assertEquals(CFTreeGetChildCount(root), 0)








if __name__ == "__main__":
    main()
