import objc
import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSetInteraction(TestCase):
    def testRepeatedAllocInit(self):
        for _ in range(1, 1000):
            _ = Foundation.NSSet.alloc().init()

    def testContains(self):
        x = Foundation.NSSet.setWithArray_(["foo", "bar", "baz"])

        self.assertIn("foo", x)
        self.assertNotIn("notfoo", x)

    def testIteration(self):
        x = Foundation.NSSet.setWithArray_(["foo", "bar", "baz"])

        for i in x:
            self.assertIn(i, x)
            self.assertTrue(x.containsObject_(i))

    def test_varargsConstruction(self):
        w = Foundation.NSSet.setWithObjects_(0, 1, 2, 3, None)
        x = Foundation.NSSet.alloc().initWithObjects_(0, 1, 2, 3, None)
        y = Foundation.NSSet.setWithObjects_count_(range(10), 4)
        z = Foundation.NSSet.alloc().initWithObjects_count_(range(10), 4)
        # a = Foundation.NSSet.alloc().initWithObjects_count_(range(4), None)

        self.assertEqual(len(w), 4)
        self.assertEqual(len(x), 4)
        self.assertEqual(len(y), 4)
        self.assertEqual(len(z), 4)
        # self.assertEqual(len(a), 4)

        self.assertIn(0, w)
        self.assertIn(1, x)
        self.assertIn(2, y)
        self.assertIn(3, z)
        # self.assertIn(3, a)

    def test_varargsConstruction2(self):
        w = Foundation.NSMutableSet.setWithObjects_(0, 1, 2, 3, None)
        x = Foundation.NSMutableSet.alloc().initWithObjects_(0, 1, 2, 3, None)
        y = Foundation.NSMutableSet.setWithObjects_count_(range(10), 4)
        z = Foundation.NSMutableSet.alloc().initWithObjects_count_(range(10), 4)

        self.assertEqual(len(w), 4)
        self.assertEqual(len(x), 4)
        self.assertEqual(len(y), 4)
        self.assertEqual(len(z), 4)

        self.assertIn(0, w)
        self.assertIn(1, x)
        self.assertIn(2, y)
        self.assertIn(3, z)


class TestVariadic(TestCase):
    def testSetWithObjects(self):
        o = Foundation.NSSet.setWithObjects_()
        self.assertEqual(len(o), 0)
        self.assertIsInstance(o, Foundation.NSSet)

        o = Foundation.NSSet.setWithObjects_(1, 2, 3)
        self.assertEqual(len(o), 3)
        self.assertIsInstance(o, Foundation.NSSet)
        self.assertIn(1, o)
        self.assertIn(2, o)
        self.assertIn(3, o)

        o = Foundation.NSMutableSet.setWithObjects_()
        self.assertEqual(len(o), 0)
        self.assertIsInstance(o, Foundation.NSMutableSet)

        o = Foundation.NSMutableSet.setWithObjects_(1, 2, 3)
        self.assertEqual(len(o), 3)
        self.assertIsInstance(o, Foundation.NSMutableSet)
        self.assertIn(1, o)
        self.assertIn(2, o)
        self.assertIn(3, o)

    def testInitWithObjects(self):
        o = Foundation.NSSet.alloc().initWithObjects_()
        self.assertEqual(len(o), 0)
        self.assertIsInstance(o, Foundation.NSSet)

        o = Foundation.NSSet.alloc().initWithObjects_(1, 2, 3)
        self.assertEqual(len(o), 3)
        self.assertIsInstance(o, Foundation.NSSet)
        self.assertIn(1, o)
        self.assertIn(2, o)
        self.assertIn(3, o)

        o = Foundation.NSMutableSet.alloc().initWithObjects_()
        self.assertEqual(len(o), 0)
        self.assertIsInstance(o, Foundation.NSMutableSet)

        o = Foundation.NSMutableSet.alloc().initWithObjects_(1, 2, 3)
        self.assertEqual(len(o), 3)
        self.assertIsInstance(o, Foundation.NSMutableSet)
        self.assertIn(1, o)
        self.assertIn(2, o)
        self.assertIn(3, o)

    def testSetWithObjectsCount(self):
        o = Foundation.NSSet.setWithObjects_count_([1, 2, 3], 3)
        self.assertEqual(len(o), 3)
        self.assertIsInstance(o, Foundation.NSSet)
        self.assertIn(1, o)
        self.assertIn(2, o)
        self.assertIn(3, o)
        self.assertNotIn(4, o)

        o = Foundation.NSSet.setWithObjects_count_([1, 2, 3], 0)
        self.assertEqual(len(o), 0)
        self.assertIsInstance(o, Foundation.NSSet)

        o = Foundation.NSMutableSet.setWithObjects_count_([1, 2, 3], 3)
        self.assertEqual(len(o), 3)
        self.assertIsInstance(o, Foundation.NSMutableSet)
        self.assertIn(1, o)
        self.assertIn(2, o)
        self.assertIn(3, o)

        o = Foundation.NSMutableSet.setWithObjects_count_([1, 2, 3], 0)
        self.assertEqual(len(o), 0)
        self.assertIsInstance(o, Foundation.NSMutableSet)

    def testInitWithObjectsCount(self):
        o = Foundation.NSSet.alloc().initWithObjects_count_([1, 2, 3], 3)
        self.assertEqual(len(o), 3)
        self.assertIsInstance(o, Foundation.NSSet)
        self.assertIn(1, o)
        self.assertIn(2, o)
        self.assertIn(3, o)
        self.assertNotIn(4, o)

        o = Foundation.NSSet.alloc().initWithObjects_count_([1, 2, 3], 0)
        self.assertEqual(len(o), 0)
        self.assertIsInstance(o, Foundation.NSSet)

        o = Foundation.NSMutableSet.alloc().initWithObjects_count_([1, 2, 3], 3)
        self.assertEqual(len(o), 3)
        self.assertIsInstance(o, Foundation.NSMutableSet)
        self.assertIn(1, o)
        self.assertIn(2, o)
        self.assertIn(3, o)

        o = Foundation.NSMutableSet.alloc().initWithObjects_count_([1, 2, 3], 0)
        self.assertEqual(len(o), 0)
        self.assertIsInstance(o, Foundation.NSMutableSet)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSSet.containsObject_)
        self.assertResultIsBOOL(Foundation.NSSet.intersectsSet_)
        self.assertResultIsBOOL(Foundation.NSSet.isEqualToSet_)
        self.assertResultIsBOOL(Foundation.NSSet.isSubsetOfSet_)

        self.assertArgIsIn(Foundation.NSSet.setWithObjects_count_, 0)
        self.assertArgSizeInArg(Foundation.NSSet.setWithObjects_count_, 0, 1)
        self.assertArgIsIn(Foundation.NSSet.initWithObjects_count_, 0)
        self.assertArgSizeInArg(Foundation.NSSet.initWithObjects_count_, 0, 1)

        self.assertArgIsBOOL(Foundation.NSSet.initWithSet_copyItems_, 1)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBlock(
            Foundation.NSSet.enumerateObjectsUsingBlock_, 0, b"v@o^" + objc._C_NSBOOL
        )
        self.assertArgIsBlock(
            Foundation.NSSet.enumerateObjectsWithOptions_usingBlock_,
            1,
            b"v@o^" + objc._C_NSBOOL,
        )

        self.assertArgIsBlock(
            Foundation.NSSet.objectsPassingTest_,
            0,
            objc._C_NSBOOL + b"@o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSSet.objectsWithOptions_passingTest_,
            1,
            objc._C_NSBOOL + b"@o^" + objc._C_NSBOOL,
        )
