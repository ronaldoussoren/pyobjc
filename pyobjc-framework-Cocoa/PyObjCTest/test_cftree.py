import sys

import CoreFoundation
from PyObjCTools.TestSupport import TestCase

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


class TestCFTree(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFTreeRef)

    def testCreation(self):
        context = object()
        tree = CoreFoundation.CFTreeCreate(None, context)

        self.assertIsInstance(tree, CoreFoundation.CFTreeRef)

        self.assertTrue(CoreFoundation.CFTreeGetContext(tree, None) is context)
        CoreFoundation.CFTreeSetContext(tree, 42)
        self.assertEqual(CoreFoundation.CFTreeGetContext(tree, None), 42)

    def testCreateTree(self):
        root = CoreFoundation.CFTreeCreate(None, "root")

        for child in range(10):
            CoreFoundation.CFTreeAppendChild(
                root, CoreFoundation.CFTreeCreate(None, child)
            )

        self.assertEqual(
            CoreFoundation.CFTreeGetContext(
                CoreFoundation.CFTreeGetFirstChild(root), None
            ),
            0,
        )

        def compare(l, r, context):
            return -cmp(
                CoreFoundation.CFTreeGetContext(l, None),
                CoreFoundation.CFTreeGetContext(r, None),
            )

        CoreFoundation.CFTreeSortChildren(root, compare, None)
        self.assertEqual(
            CoreFoundation.CFTreeGetContext(
                CoreFoundation.CFTreeGetFirstChild(root), None
            ),
            9,
        )

    def testTypeID(self):
        v = CoreFoundation.CFTreeGetTypeID()
        self.assertIsInstance(v, int)

    def testQuerying(self):
        root = CoreFoundation.CFTreeCreate(None, "root")

        for child in range(2):
            CoreFoundation.CFTreeAppendChild(
                root, CoreFoundation.CFTreeCreate(None, child)
            )

        p = CoreFoundation.CFTreeGetParent(root)
        self.assertIs(p, None)
        c = CoreFoundation.CFTreeGetFirstChild(root)
        self.assertIsInstance(c, CoreFoundation.CFTreeRef)
        c2 = CoreFoundation.CFTreeGetChildAtIndex(root, 0)
        self.assertIs(c, c2)
        p = CoreFoundation.CFTreeGetParent(c)
        self.assertIs(p, root)
        s = CoreFoundation.CFTreeGetNextSibling(c)
        self.assertIsInstance(s, CoreFoundation.CFTreeRef)
        p = CoreFoundation.CFTreeGetParent(s)
        self.assertIs(p, root)
        s2 = CoreFoundation.CFTreeGetChildAtIndex(root, 1)
        self.assertIs(s, s2)
        s = CoreFoundation.CFTreeGetNextSibling(s)
        self.assertIs(s, None)
        cnt = CoreFoundation.CFTreeGetChildCount(root)
        self.assertEqual(cnt, 2)

        cnt = CoreFoundation.CFTreeGetChildCount(c)
        self.assertEqual(cnt, 0)

        children = CoreFoundation.CFTreeGetChildren(root, None)
        self.assertIsInstance(children, (list, tuple))
        self.assertEqual(len(children), 2)

        r = CoreFoundation.CFTreeFindRoot(s2)
        self.assertIs(r, root)

    def testModification(self):
        root = CoreFoundation.CFTreeCreate(None, "root")

        for child in range(2):
            CoreFoundation.CFTreeAppendChild(
                root, CoreFoundation.CFTreeCreate(None, child)
            )

        def applyFunc(node, context):
            context.append(CoreFoundation.CFTreeGetContext(node, None))

        lst = []
        CoreFoundation.CFTreeApplyFunctionToChildren(root, applyFunc, lst)
        self.assertEqual(len(lst), 2)

        preChild = CoreFoundation.CFTreeCreate(None, "before")
        postChild = CoreFoundation.CFTreeCreate(None, "after")
        CoreFoundation.CFTreePrependChild(root, preChild)
        CoreFoundation.CFTreeAppendChild(root, postChild)

        self.assertEqual(CoreFoundation.CFTreeGetChildCount(root), 4)
        n = CoreFoundation.CFTreeGetChildAtIndex(root, 0)
        self.assertIs(n, preChild)
        n = CoreFoundation.CFTreeGetChildAtIndex(root, 3)
        self.assertIs(n, postChild)
        s = CoreFoundation.CFTreeCreate(None, "sibling")
        CoreFoundation.CFTreeInsertSibling(preChild, s)
        n = CoreFoundation.CFTreeGetChildAtIndex(root, 1)
        self.assertIs(n, s)
        self.assertEqual(CoreFoundation.CFTreeGetChildCount(root), 5)

        CoreFoundation.CFTreeRemove(s)
        self.assertEqual(CoreFoundation.CFTreeGetChildCount(root), 4)

        def compare(left, right, context):
            left = CoreFoundation.CFTreeGetContext(left, None)
            right = CoreFoundation.CFTreeGetContext(right, None)
            return -cmp(left, right)

        before = []
        after = []
        CoreFoundation.CFTreeApplyFunctionToChildren(root, applyFunc, before)
        CoreFoundation.CFTreeSortChildren(root, compare, None)
        CoreFoundation.CFTreeApplyFunctionToChildren(root, applyFunc, after)

        self.assertItemsEqual(before, after)

        CoreFoundation.CFTreeRemoveAllChildren(root)
        self.assertEqual(CoreFoundation.CFTreeGetChildCount(root), 0)
