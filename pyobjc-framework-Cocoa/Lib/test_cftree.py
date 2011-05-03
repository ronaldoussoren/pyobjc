from CoreFoundation import *
import unittest

class TestCFTree (unittest.TestCase):
    def testCreation(self):
        context = (1,2,3)

        tree = CFTreeCreate(None, context)
        self.assert_(isinstance(tree, CFTreeRef))

        for child in ("aap", "noot", "mies"):
            node = CFTreeCreate(None, child)
            CFTreeAppendChild(tree, node)

        self.assertEquals(CFTreeGetChildCount(tree), 3)

    def testGetContext(self):
        context = (1,2,3)

        tree = CFTreeCreate(None, context)
        self.assert_(isinstance(tree, CFTreeRef))

        self.assert_(CFTreeGetContext(tree, None) is context)


    def testSetContext(self):
        context = (1,2,3)

        tree = CFTreeCreate(None, context)
        self.assert_(isinstance(tree, CFTreeRef))

        CFTreeSetContext(tree, "fubar")
        self.assertEquals(CFTreeGetContext(tree, None), "fubar")

    def testApplyFunction(self):
        context = (1,2,3)

        tree = CFTreeCreate(None, context)
        self.assert_(isinstance(tree, CFTreeRef))

        for child in ("aap", "noot", "mies"):
            node = CFTreeCreate(None, child)
            CFTreeAppendChild(tree, node)

        childvalues = []
        contexts = []

        def function(value, context):
            childvalues.append(value)
            contexts.append(context)

        CFTreeApplyFunctionToChildren(tree, function, (42,))

        self.assertEquals(childvalues, ('aap', 'noot', 'mies'))
        self.assertEquals(contexts, ((42,), (42,), (42,)))

    def testSortChildren(self):
        context = (1,2,3)

        tree = CFTreeCreate(None, context)
        self.assert_(isinstance(tree, CFTreeRef))

        for child in ("mies", "noot", "aap"):
            node = CFTreeCreate(None, child)
            CFTreeAppendChild(tree, node)

        childvalues = []
        contexts = []

        def compare(l, r, context):
            return cmp(CFTreeGetContext(l), CFTreeGetContext(r))
        CFTreeSortChildren(tree, compare, (32,))

        def function(value, context):
            childvalues.append(value)
            contexts.append(context)
        CFTreeApplyFunctionToChildren(tree, function, (42,))

        self.assertEquals(childvalues, ('aap', 'noot', 'mies'))
        self.assertEquals(contexts, ((42,), (42,), (42,)))

if __name__ == "__main__":
    unittest.main()
