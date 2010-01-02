"""
XXX: Add tests that check that the type actually works as expected:

* Use struct value as method argument
* Return struct value from a method

Add tests for nested structs as well (that is assert that NSRect.location is 
an NSPoint, but using our own types)
"""
from PyObjCTools.TestSupport import *
import objc
from PyObjCTest.structs import *
from PyObjCTest.fnd import NSObject


class TestStructs (TestCase):
    def testCreateExplicit(self):
        tp = objc.createStructType("FooStruct", b"{_FooStruct=ffff}", ["a","b","c","d"])
        self.assertIsInstance(tp, type)
        self.assertEquals(tp.__typestr__, b"{_FooStruct=ffff}")

        o = tp()
        self.assertHasAttr(o, 'a')
        self.assertHasAttr(o, 'b')
        self.assertHasAttr(o, 'c')
        self.assertHasAttr(o, 'd')

    def testCreateImplicit(self):
        tp = objc.createStructType("BarStruct", b'{_BarStruct="e"f"f"f"g"f"h"f}', None)
        self.assertIsInstance(tp, type)
        self.assertEquals(tp.__typestr__, b"{_BarStruct=ffff}")

        o = tp()
        self.assertHasAttr(o, 'e')
        self.assertHasAttr(o, 'f')
        self.assertHasAttr(o, 'g')
        self.assertHasAttr(o, 'h')

        self.assertRaises(ValueError, objc.createStructType, "Foo2", b'{_Foo=f"a"}', None) 
        self.assertRaises(ValueError, objc.createStructType, "Foo3", b'{_Foo="a"f', None) 
        self.assertRaises(ValueError, objc.createStructType, "Foo4", b'^{_Foo="a"f}', None) 

    def testPointerFields(self):
        # Note: the created type won't be all that useful unless the pointer
        # happens to be something that PyObjC knows how to deal with, this is
        # more a check to see if createStructType knows how to cope with 
        # non-trivial types.
        tp = objc.createStructType("XBarStruct", b'{_XBarStruct="e"^f"f"^f"g"^@"h"f}', None)
        self.assertIsInstance(tp, type)
        self.assertEquals(tp.__typestr__, b"{_XBarStruct=^f^f^@f}")

        o = tp()
        self.assertHasAttr(o, 'e')
        self.assertHasAttr(o, 'f')
        self.assertHasAttr(o, 'g')
        self.assertHasAttr(o, 'h')

    def testEmbeddedFields(self):
        tp = objc.createStructType("FooStruct", b'{FooStruct="first"i"second"i}', None)

        v = OC_StructTest.createWithFirst_andSecond_(1, 2)
        self.assertIsInstance(v, tp)

        x = OC_StructTest.sumFields_(v)
        self.assertEquals(x, v.first + v.second)
        self.assertEquals(v.first, 1)
        self.assertEquals(v.second, 2)

    def testStructCallback(self):
        """
        Regression test for an issue reported on the PyObjC mailinglist.
        """
        tp = objc.createStructType("FooStruct", b'{FooStruct="first"i"second"i}', None)

        StructArrayDelegate = objc.informal_protocol(
            "StructArrayDelegate",
            [
                objc.selector(None, b"arrayOf4Structs:",
                    signature=b"@@:[4{FooStruct=ii}]"),
            ])

        class OC_PyStruct (NSObject):
            
            def arrayOf4Structs_(self, value):
                return value

        self.assertEquals(OC_PyStruct.arrayOf4Structs_.signature, b"@@:[4{FooStruct=" + objc._C_INT + objc._C_INT + b"}]")

        o = OC_PyStruct.alloc().init()
        v = OC_StructTest.callArrayOf4Structs_(o)
        self.assertEquals(len(v), 4)
        for i in range(3):
            self.assertIsInstance(v[i], tp)

        self.assertEquals(v[0], tp(1, 2))
        self.assertEquals(v[1], tp(3, 4))
        self.assertEquals(v[2], tp(5, 6))
        self.assertEquals(v[3], tp(7, 8))


if __name__ == "__main__":
    main()
