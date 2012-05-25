from PyObjCTools.TestSupport import *
from CoreFoundation import *
from Foundation import NSCFAttributedString

try:
    long
except NameError:
    long = int



class TestAttributedString (TestCase):
    def testTypes(self):
        try:
            NSCFAttributedString = objc.lookUpClass('__NSCFAttributedString')
        except objc.error:
            NSCFAttributedString = objc.lookUpClass('NSCFAttributedString')

        self.assertIs(CFAttributedStringRef, NSCFAttributedString )
        self.assertIs(CFMutableAttributedStringRef, NSCFAttributedString )

    def testTypeID(self):
        v = CFAttributedStringGetTypeID()
        self.assertIsInstance(v, (int, long))

    def testCreate(self):
        val = CFAttributedStringCreate(None, b"hello".decode('ascii'), {b'foo'.decode('ascii'): 42})
        self.assertIsInstance(val, CFAttributedStringRef)
        val = CFAttributedStringCreateWithSubstring(None, val, (1,2))
        self.assertIsInstance(val, CFAttributedStringRef)
        val2 = CFAttributedStringCreateCopy(None, val)
        self.assertIs(val2, val)

    def testGetting(self):
        val = CFAttributedStringCreate(None, b"hello".decode('ascii'), {b'foo'.decode('ascii'): 42, b'bar'.decode('ascii'):b'baz'})
        self.assertIsInstance(val, CFAttributedStringRef)
        dta = CFAttributedStringGetString(val)
        self.assertEqual(dta , b"hello".decode('ascii') )
        l = CFAttributedStringGetLength(val)
        self.assertEqual(l , 5 )
        v, rng = CFAttributedStringGetAttributes(val, 1, None)
        self.assertEqual(v , {b'foo'.decode('ascii'): 42, b'bar'.decode('ascii'): b'baz' } )
        self.assertEqual(rng , (0, 5) )
        v, rng = CFAttributedStringGetAttributes(val, 1, objc.NULL)
        self.assertEqual(v , {b'foo'.decode('ascii'): 42, b'bar'.decode('ascii'): b'baz' } )
        self.assertEqual(rng , objc.NULL )
        v, rng = CFAttributedStringGetAttribute(val, 1, b"foo".decode('ascii'), None)
        self.assertEqual(v , 42 )
        self.assertEqual(rng , (0, 5) )
        v, rng = CFAttributedStringGetAttribute(val, 1, b"foo".decode('ascii'), objc.NULL)
        self.assertEqual(v , 42 )
        self.assertEqual(rng , objc.NULL )
        v, rng = CFAttributedStringGetAttributesAndLongestEffectiveRange(val, 1, (0,5), None)
        self.assertEqual(v , {b"foo".decode('ascii'): 42, b"bar".decode('ascii'): b'baz' } )
        self.assertEqual(rng , (0, 5) )
        v, rng = CFAttributedStringGetAttributesAndLongestEffectiveRange(val, 1, (0,5), objc.NULL)
        self.assertEqual(v , {b"foo".decode('ascii'): 42, b"bar".decode('ascii'): b'baz' } )
        self.assertEqual(rng , objc.NULL )
        v, rng = CFAttributedStringGetAttributeAndLongestEffectiveRange(val, 1, b"bar".decode('ascii'), (0,5), None)
        self.assertEqual(v , b'baz' )
        self.assertEqual(rng , (0, 5) )
        v, rng = CFAttributedStringGetAttributeAndLongestEffectiveRange(val, 1, b"bar".decode('ascii'), (0,5), objc.NULL)
        self.assertEqual(v , b'baz' )
        self.assertEqual(rng , objc.NULL )

    def testMutableCopy(self):
        val = CFAttributedStringCreateMutable(None, 0)
        self.assertIsInstance(val, CFAttributedStringRef)
        orig = CFAttributedStringCreate(None, b"hello".decode("ascii"), {b'foo'.decode("ascii"): 42, b'bar'.decode("ascii"):'baz'})
        self.assertIsInstance(orig, CFAttributedStringRef)
        val = CFAttributedStringCreateMutableCopy(None, 0, orig)
        self.assertIsInstance(orig, CFAttributedStringRef)
        self.assertIsNot(val, orig)
        CFAttributedStringReplaceString(val, (0,3), "Hal")
        dta = CFAttributedStringGetString(val)
        self.assertEqual(dta , b"Hallo".decode("ascii") )
        v = CFAttributedStringGetMutableString(val)
        self.assertIs(v, None )
        CFAttributedStringSetAttributes(val, (0, 2), {b'ronald'.decode("ascii"):99}, False)
        v, rng = CFAttributedStringGetAttributes(val, 1, None)
        self.assertEqual(v , {b'ronald'.decode("ascii"):99, b'foo'.decode("ascii"): 42, b'bar'.decode("ascii"): 'baz' } )
        self.assertEqual(rng , (0, 2) )
        v, rng = CFAttributedStringGetAttributes(val, 3, None)
        self.assertEqual(v , {b'foo'.decode("ascii"): 42, b'bar'.decode("ascii"): 'baz' } )
        self.assertEqual(rng , (2, 3) )
        self.assertIsInstance(rng, CFRange)
        CFAttributedStringSetAttributes(val, (0, 2), {b'ronald'.decode("ascii"):99}, True)
        v, rng = CFAttributedStringGetAttributes(val, 1, None)
        self.assertEqual(v , {b'ronald'.decode("ascii"):99} )
        self.assertEqual(rng , (0, 2) )
        CFAttributedStringSetAttribute(val, (1, 3), b'color'.decode("ascii"), b'blue'.decode("ascii"))
        v, rng = CFAttributedStringGetAttributes(val, 1, None)
        self.assertEqual(v , {b'ronald'.decode("ascii"):99, b'color'.decode("ascii"):b'blue'.decode("ascii")} )
        self.assertEqual(rng , (1, 1) )
        CFAttributedStringRemoveAttribute(val, (1,3), b'color'.decode("ascii"))
        v, rng = CFAttributedStringGetAttributes(val, 3, None)
        self.assertEqual(v , {b'foo'.decode("ascii"): 42, b'bar'.decode("ascii"): 'baz' } )
        self.assertEqual(rng , (2, 2) )
        rep = CFAttributedStringCreate(None, "dummy", {b'attrib'.decode("ascii"): 99} )
        CFAttributedStringReplaceAttributedString(val, (1,3), rep)
        self.assertEqual(CFAttributedStringGetString(val) , b'Hdummyo'.decode("ascii"))

    def testEditing(self):
        val = CFAttributedStringCreateMutable(None, 0)
        self.assertIsInstance(val, CFAttributedStringRef)
        CFAttributedStringBeginEditing(val)
        CFAttributedStringEndEditing(val)

if __name__ == "__main__":
    main()
