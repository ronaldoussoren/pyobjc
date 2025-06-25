"""
Some tests for arrays in method arguments (the 'int foo[4]' type of array).

This tests both calling such methods, as well as implementing methods with such arguments.
"""

import array

import objc
from PyObjCTest.arrays import OC_ArrayTest
from PyObjCTest.fnd import NSObject
from PyObjCTools.TestSupport import TestCase


class TestArrayCalling(TestCase):
    def testArrayOfInts(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4Ints_([0, 1, 2, 3])
        self.assertEqual(v, [0, 1, 2, 3])

        a = array.array("i", [9, 10, 11, 12])
        v = o.arrayOf4Ints_(a)
        self.assertEqual(v, [9, 10, 11, 12])

    def testArrayOfIntsIn(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4IntsIn_([0, 1, 2, 3])
        self.assertEqual(v, [0, 1, 2, 3])

        a = array.array("i", [9, 10, 11, 12])
        v = o.arrayOf4IntsIn_(a)
        self.assertEqual(v, [9, 10, 11, 12])

    def testArrayOfIntsInOut(self):
        o = OC_ArrayTest.alloc().init()

        v, r = o.arrayOf4IntsInOut_([0, 1, 2, 3])
        self.assertEqual(v, (0, 1, 2, 3))
        self.assertEqual(r, (0 + 42, 1 + 42, 2 + 42, 3 + 42))

        a = array.array("i", [9, 10, 11, 12])
        v, r = o.arrayOf4IntsInOut_(a)
        self.assertEqual(v, [9, 10, 11, 12])
        self.assertIs(r, a)
        self.assertEqual(a[0], 9 + 42)
        self.assertEqual(a[1], 10 + 42)
        self.assertEqual(a[2], 11 + 42)
        self.assertEqual(a[3], 12 + 42)

    def testArrayOfIntsOut(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4IntsOut_(None)
        self.assertEqual(v, (99, 100, 102, 110))

        a = array.array("i", [9, 10, 11, 12])
        v = o.arrayOf4IntsOut_(a)
        self.assertIs(a, v)
        self.assertEqual(a[0], 99)
        self.assertEqual(a[1], 100)
        self.assertEqual(a[2], 102)
        self.assertEqual(a[3], 110)

    def testArrayOfStructs(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4Structs_([(0, 1), (10, 20), (-10, -20), (7, 8)])
        self.assertEqual(v, [(0, 1), (10, 20), (-10, -20), (7, 8)])

        a = array.array("i", [9, 10, 11, 12, -1, -2, -3, -4])
        v = o.arrayOf4Structs_(a)
        self.assertEqual(v, [(9, 10), (11, 12), (-1, -2), (-3, -4)])

    def testArrayOfStructsIn(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4StructsIn_([(0, 1), (2, 3), (-1, -2), (-3, -4)])
        self.assertEqual(v, [(0, 1), (2, 3), (-1, -2), (-3, -4)])

        a = array.array("i", [9, 10, 11, 12, -1, -2, -3, -4])
        v = o.arrayOf4StructsIn_(a)
        self.assertEqual(v, [(9, 10), (11, 12), (-1, -2), (-3, -4)])

    def testArrayOfStructsInOut(self):
        o = OC_ArrayTest.alloc().init()

        v, r = o.arrayOf4StructsInOut_([(0, 1), (2, 3), (4, 5), (6, 7)])
        self.assertEqual(v, ((0, 1), (2, 3), (4, 5), (6, 7)))
        self.assertEqual(
            r, ((0 + 42, 1 - 42), (2 + 42, 3 - 42), (4 + 42, 5 - 42), (6 + 42, 7 - 42))
        )

        a = array.array("i", [9, 10, 11, 12, 14, 15, 16, 17])
        v, r = o.arrayOf4StructsInOut_(a)
        self.assertEqual(v, [(9, 10), (11, 12), (14, 15), (16, 17)])
        self.assertIs(r, a)
        self.assertEqual(a[0], 9 + 42)
        self.assertEqual(a[1], 10 - 42)
        self.assertEqual(a[2], 11 + 42)
        self.assertEqual(a[3], 12 - 42)
        self.assertEqual(a[4], 14 + 42)
        self.assertEqual(a[5], 15 - 42)
        self.assertEqual(a[6], 16 + 42)
        self.assertEqual(a[7], 17 - 42)

    def testArrayOfStructsOut(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4StructsOut_(None)
        self.assertEqual(list(v), [(1 + i * i, -4 - i * i * i) for i in range(4)])

        a = array.array("i", [0] * 8)
        v = o.arrayOf4StructsOut_(a)
        self.assertIs(a, v)
        lst = []
        for i in range(4):
            lst.append(1 + i * i)
            lst.append(-4 - i * i * i)
        self.assertEqual(a[0], lst[0])
        self.assertEqual(a[1], lst[1])
        self.assertEqual(a[2], lst[2])
        self.assertEqual(a[3], lst[3])
        self.assertEqual(a[4], lst[4])
        self.assertEqual(a[5], lst[5])
        self.assertEqual(a[6], lst[6])
        self.assertEqual(a[7], lst[7])


StructArrayDelegate = objc.informal_protocol(
    "ArrayDelegate",
    [
        objc.selector(None, b"arrayOf4Ints:", signature=b"@@:[4i]", isRequired=0),
        objc.selector(None, b"arrayOf4IntsOut:", signature=b"v@:o[4i]", isRequired=False),
        objc.selector(
            None,
            b"arrayOf4Structs:",
            signature=b"@@:[4{FooStruct=ii}]",
            isRequired=False,
        ),
        objc.selector(
            None,
            b"arrayOf4StructsOut:",
            signature=b"v@:o[4{FooStruct=ii}]",
            isRequired=False,
        ),
    ],
)


class OC_TestArrayInt_In(NSObject):
    def arrayOf4Ints_(self, array):
        return array


class OC_TestArrayInt_Out(NSObject):
    def arrayOf4IntsOut_(self, array):
        if array is None:
            return [99, 100, 98, 101]


class OC_TestArrayStruct_Out(NSObject):
    def arrayOf4StructsOut_(self, array):
        if array is None:
            return [(44, 45), (46, 47), (48, 49), (50, 51)]


class OC_TestArrayStruct_In(NSObject):
    def arrayOf4Structs_(self, array):
        return array


class TestArrayCallbacks(TestCase):
    def testCallArrayInt(self):
        obj = OC_TestArrayInt_In.alloc().init()

        v = OC_ArrayTest.callArrayOf4Ints_(obj)
        self.assertEqual(v, (1, 2, 3, 4))

    def testCallArrayIntsOut(self):
        obj = OC_TestArrayInt_Out.alloc().init()

        v = OC_ArrayTest.callArrayOf4IntsOut_(obj)
        self.assertEqual(v, [99, 100, 98, 101])

    def testCallArrayStruct(self):
        obj = OC_TestArrayStruct_In.alloc().init()

        v = OC_ArrayTest.callArrayOf4Structs_(obj)
        self.assertEqual(v, ((1, 2), (3, 4), (5, 6), (7, 8)))

    def testCallArrayStructsOut(self):
        obj = OC_TestArrayStruct_Out.alloc().init()

        v = OC_ArrayTest.callArrayOf4StructsOut_(obj)
        self.assertEqual(v, [(44, 45), (46, 47), (48, 49), (50, 51)])
