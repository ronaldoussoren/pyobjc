"""
Some tests for arrays in method arguments (the 'int foo[4]' type of array).

This tests both calling such methods, as well as implementing methods with such arguments.
"""
from PyObjCTools.TestSupport import *
import objc
import array
from PyObjCTest.arrays import *
from PyObjCTest.fnd import NSObject


class TestArrayCalling (TestCase):
    def testArrayOfInts(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4Ints_([0, 1, 2, 3])
        self.assertEquals(v, [0, 1, 2, 3])

        a = array.array('i', [9, 10, 11, 12])
        v = o.arrayOf4Ints_(a)
        self.assertEquals(v, [9, 10, 11, 12])

    def testArrayOfIntsIn(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4IntsIn_([0, 1, 2, 3])
        self.assertEquals(v, [0, 1, 2, 3])

        a = array.array('i', [9, 10, 11, 12])
        v = o.arrayOf4IntsIn_(a)
        self.assertEquals(v, [9, 10, 11, 12])

    def testArrayOfIntsInOut(self):
        o = OC_ArrayTest.alloc().init()

        v, r = o.arrayOf4IntsInOut_([0, 1, 2, 3])
        self.assertEquals(v, (0, 1, 2, 3))
        self.assertEquals(r, (0+42, 1+42, 2+42, 3+42))

        a = array.array('i', [9, 10, 11, 12])
        v, r = o.arrayOf4IntsInOut_(a)
        self.assertEquals(v, [9, 10, 11, 12])
        self.assert_(r is a)
        self.assertEquals(a[0], 9 + 42)
        self.assertEquals(a[1], 10 + 42)
        self.assertEquals(a[2], 11 + 42)
        self.assertEquals(a[3], 12 + 42)

    def testArrayOfIntsOut(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4IntsOut_(None)
        self.assertEquals(v, (99, 100, 102, 110))

        a = array.array('i', [9, 10, 11, 12])
        v = o.arrayOf4IntsOut_(a)
        self.assert_(a is v)
        self.assertEquals(a[0], 99)
        self.assertEquals(a[1], 100)
        self.assertEquals(a[2], 102)
        self.assertEquals(a[3], 110)

    def testArrayOfStructs(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4Structs_([(0, 1), (10, 20), (-10, -20), (7, 8)])
        self.assertEquals(v, [(0, 1), (10, 20), (-10, -20), (7, 8)])

        a = array.array('i', [9, 10, 11, 12, -1, -2, -3, -4])
        v = o.arrayOf4Structs_(a)
        self.assertEquals(v, [(9, 10), (11, 12), (-1, -2), (-3, -4)])

    def testArrayOfStructsIn(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4StructsIn_([(0, 1), (2, 3), (-1, -2), (-3, -4)])
        self.assertEquals(v, [(0, 1), (2, 3), (-1, -2), (-3, -4)])

        a = array.array('i', [9, 10, 11, 12, -1, -2, -3, -4])
        v = o.arrayOf4StructsIn_(a)
        self.assertEquals(v, [(9, 10), (11, 12), (-1, -2), (-3, -4)])

    def testArrayOfStructsInOut(self):
        o = OC_ArrayTest.alloc().init()

        v, r = o.arrayOf4StructsInOut_([(0, 1), (2, 3), (4, 5), (6,7)])
        self.assertEquals(v, ((0,1), (2,3), (4,5), (6,7)))
        self.assertEquals(r, ((0+42, 1-42), (2+42,3-42), (4+42, 5-42), (6+42, 7-42)))

        a = array.array('i', [9, 10, 11, 12, 14, 15, 16, 17])
        v, r = o.arrayOf4StructsInOut_(a)
        self.assertEquals(v, [(9, 10), (11, 12), (14, 15), (16, 17)])
        self.assert_(r is a)
        self.assertEquals(a[0], 9 + 42)
        self.assertEquals(a[1], 10 - 42)
        self.assertEquals(a[2], 11 + 42)
        self.assertEquals(a[3], 12 - 42)
        self.assertEquals(a[4], 14 + 42)
        self.assertEquals(a[5], 15 - 42)
        self.assertEquals(a[6], 16 + 42)
        self.assertEquals(a[7], 17 - 42)

    def testArrayOfStructsOut(self):
        o = OC_ArrayTest.alloc().init()

        v = o.arrayOf4StructsOut_(None)
        self.assertEquals(list(v), [ (1+i*i, -4 - i*i*i) for i in range(4) ])

        a = array.array('i', [0]*8)
        v = o.arrayOf4StructsOut_(a)
        self.assert_(a is v)
        l = []
        for i in range(4):
            l.append(1 + i * i)
            l.append(-4 - i * i * i)
        self.assertEquals(a[0], l[0])
        self.assertEquals(a[1], l[1])
        self.assertEquals(a[2], l[2])
        self.assertEquals(a[3], l[3])
        self.assertEquals(a[4], l[4])
        self.assertEquals(a[5], l[5])
        self.assertEquals(a[6], l[6])
        self.assertEquals(a[7], l[7])

StructArrayDelegate = objc.informal_protocol(
    "ArrayDelegate",
    [
        objc.selector(None, "arrayOf4Ints:", signature="@@:[4i]", isRequired=False),
        objc.selector(None, "arrayOf4IntsOut:", signature="v@:o[4i]", isRequired=False),
        objc.selector(None, "arrayOf4Structs:", signature="@@:[4{FooStruct=ii}]", isRequired=False),
        objc.selector(None, "arrayOf4StructsOut:", signature="v@:o[4{FooStruct=ii}]", isRequired=False),
    ]
)

class OC_TestArrayInt_In (NSObject):
    def arrayOf4Ints_(self, array):
        return array

class OC_TestArrayInt_Out (NSObject):
    def arrayOf4IntsOut_(self, array):
        if array is None:
            return [ 99, 100, 98, 101 ]

class OC_TestArrayStruct_Out (NSObject):
    def arrayOf4StructsOut_(self, array):
        if array is None:
            return [ (44, 45), (46, 47), (48, 49), (50, 51) ]

class OC_TestArrayStruct_In (NSObject):
    def arrayOf4Structs_(self, array):
        return array

class TestArrayCallbacks (TestCase):
    def testCallArrayInt(self):

        obj = OC_TestArrayInt_In.alloc().init()

        v = OC_ArrayTest.callArrayOf4Ints_(obj)
        self.assertEquals(v, (1, 2, 3, 4))

    def testCallArrayIntsOut(self):

        obj = OC_TestArrayInt_Out.alloc().init()

        v = OC_ArrayTest.callArrayOf4IntsOut_(obj)
        self.assertEquals(v, [99, 100, 98, 101])

    def testCallArrayStruct(self):

        obj = OC_TestArrayStruct_In.alloc().init()

        v = OC_ArrayTest.callArrayOf4Structs_(obj)
        self.assertEquals(v, ((1,2), (3,4), (5,6), (7,8)))

    def testCallArrayStructsOut(self):

        obj = OC_TestArrayStruct_Out.alloc().init()

        v = OC_ArrayTest.callArrayOf4StructsOut_(obj)
        self.assertEquals(v, [ (44, 45), (46, 47), (48, 49), (50, 51) ])


if __name__ == "__main__":
    main()
