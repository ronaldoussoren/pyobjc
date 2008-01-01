"""
XXX: Add tests that check that the type actually works as expected:

* Use struct value as method argument
* Return struct value from a method

Add tests for nested structs as well (that is assert that NSRect.location is 
an NSPoint, but using our own types)
"""
import objc.test
import objc
from objc.test.structs import *


class TestStructs (objc.test.TestCase):
    def testCreateExplicit(self):
        tp = objc.createStructType("FooStruct", "{_FooStruct=ffff}", ["a","b","c","d"])
        self.assert_(isinstance(tp, type))
        self.assert_(tp.__typestr__, "{_FooStruct=ffff}")

        o = tp()
        self.assert_(hasattr(o, 'a'))
        self.assert_(hasattr(o, 'b'))
        self.assert_(hasattr(o, 'c'))
        self.assert_(hasattr(o, 'd'))

    def testCreateImplicit(self):
        tp = objc.createStructType("BarStruct", '{_BarStruct="e"f"f"f"g"f"h"f}', None)
        self.assert_(isinstance(tp, type))
        self.assert_(tp.__typestr__, "{_BarStruct=ffff}")

        o = tp()
        self.assert_(hasattr(o, 'e'))
        self.assert_(hasattr(o, 'f'))
        self.assert_(hasattr(o, 'g'))
        self.assert_(hasattr(o, 'h'))

        self.assertRaises(ValueError, objc.createStructType, "Foo2", '{_Foo=f"a"}', None) 
        self.assertRaises(ValueError, objc.createStructType, "Foo3", '{_Foo="a"f', None) 
        self.assertRaises(ValueError, objc.createStructType, "Foo4", '^{_Foo="a"f}', None) 

    def testPointerFields(self):
        # Note: the created type won't be all that useful unless the pointer
        # happens to be something that PyObjC knows how to deal with, this is
        # more a check to see if createStructType knows how to cope with 
        # non-trivial types.
        tp = objc.createStructType("XBarStruct", '{_XBarStruct="e"^f"f"^f"g"^@"h"f}', None)
        self.assert_(isinstance(tp, type))
        self.assert_(tp.__typestr__, "{_BarStruct=^f^f^of}")

        o = tp()
        self.assert_(hasattr(o, 'e'))
        self.assert_(hasattr(o, 'f'))
        self.assert_(hasattr(o, 'g'))
        self.assert_(hasattr(o, 'h'))

    def testEmbeddedFields(self):
        tp = objc.createStructType("FooStruct", '{FooStruct="first"i"second"i}', None)

        v = OC_StructTest.createWithFirst_andSecond_(1, 2)
        self.assert_(isinstance(v, tp))

        x = OC_StructTest.sumFields_(v)
        self.assertEquals(x, v.first + v.second)
        self.assertEquals(v.first, 1)
        self.assertEquals(v.second, 2)

if __name__ == "__main__":
    objc.test.main()
