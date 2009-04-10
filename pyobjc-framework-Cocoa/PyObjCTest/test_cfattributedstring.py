from PyObjCTools.TestSupport import *
from CoreFoundation import *
from Foundation import NSCFAttributedString


class TestAttributedString (TestCase):
    def testTypes(self):
        self.failUnless( CFAttributedStringRef is NSCFAttributedString )
        self.failUnless( CFMutableAttributedStringRef is NSCFAttributedString )

    def testTypeID(self):
        v = CFAttributedStringGetTypeID()
        self.failUnless(  isinstance(v, (int, long)) )

    def testCreate(self):
        val = CFAttributedStringCreate(None, u"hello", {u'foo': 42})
        self.failUnless(  isinstance(val, CFAttributedStringRef) )

        val = CFAttributedStringCreateWithSubstring(None, val, (1,2))
        self.failUnless(  isinstance(val, CFAttributedStringRef) )

        val2 = CFAttributedStringCreateCopy(None, val)
        self.failUnless(val2 is val)

    def testGetting(self):
        val = CFAttributedStringCreate(None, u"hello", {u'foo': 42, u'bar':'baz'})
        self.failUnless(  isinstance(val, CFAttributedStringRef) )

        dta = CFAttributedStringGetString(val)
        self.failUnless( dta == u"hello" )

        l = CFAttributedStringGetLength(val)
        self.failUnless( l == 5 )

        v, rng = CFAttributedStringGetAttributes(val, 1, None)
        self.failUnless( v == {u'foo': 42, u'bar': 'baz' } )
        self.failUnless( rng == (0, 5) )

        v, rng = CFAttributedStringGetAttributes(val, 1, objc.NULL)
        self.failUnless( v == {u'foo': 42, u'bar': 'baz' } )
        self.failUnless( rng == objc.NULL )

        v, rng = CFAttributedStringGetAttribute(val, 1, u"foo", None)
        self.failUnless( v == 42 )
        self.failUnless( rng == (0, 5) )

        v, rng = CFAttributedStringGetAttribute(val, 1, u"foo", objc.NULL)
        self.failUnless( v == 42 )
        self.failUnless( rng == objc.NULL )

        v, rng = CFAttributedStringGetAttributesAndLongestEffectiveRange(val, 1, (0,5), None)
        self.failUnless( v == {u'foo': 42, u'bar': 'baz' } )
        self.failUnless( rng == (0, 5) )

        v, rng = CFAttributedStringGetAttributesAndLongestEffectiveRange(val, 1, (0,5), objc.NULL)
        self.failUnless( v == {u'foo': 42, u'bar': 'baz' } )
        self.failUnless( rng == objc.NULL )

        v, rng = CFAttributedStringGetAttributeAndLongestEffectiveRange(val, 1, u'bar', (0,5), None)
        self.failUnless( v == 'baz' )
        self.failUnless( rng == (0, 5) )

        v, rng = CFAttributedStringGetAttributeAndLongestEffectiveRange(val, 1, u'bar', (0,5), objc.NULL)
        self.failUnless( v == 'baz' )
        self.failUnless( rng == objc.NULL )

    
    def testMutableCopy(self):
        val = CFAttributedStringCreateMutable(None, 0)
        self.failUnless(  isinstance(val, CFAttributedStringRef) )

        orig = CFAttributedStringCreate(None, u"hello", {u'foo': 42, u'bar':'baz'})
        self.failUnless(  isinstance(orig, CFAttributedStringRef) )

        val = CFAttributedStringCreateMutableCopy(None, 0, orig)
        self.failUnless(  isinstance(orig, CFAttributedStringRef) )
        self.failIf( val is orig)

        CFAttributedStringReplaceString(val, (0,3), "Hal")
        dta = CFAttributedStringGetString(val)
        self.failUnless( dta == u"Hallo" )

        v = CFAttributedStringGetMutableString(val)
        self.failUnless( v is None )


        CFAttributedStringSetAttributes(val, (0, 2), {u'ronald':99}, False)
        v, rng = CFAttributedStringGetAttributes(val, 1, None)
        self.failUnless( v == {u'ronald':99, u'foo': 42, u'bar': 'baz' } )
        self.failUnless( rng == (0, 2) )

        v, rng = CFAttributedStringGetAttributes(val, 3, None)
        self.failUnless( v == {u'foo': 42, u'bar': 'baz' } )
        self.failUnless( rng == (2, 3) )
        self.failUnless( isinstance(rng, CFRange) )

        CFAttributedStringSetAttributes(val, (0, 2), {u'ronald':99}, True)
        v, rng = CFAttributedStringGetAttributes(val, 1, None)
        self.failUnless( v == {u'ronald':99} )
        self.failUnless( rng == (0, 2) )

        CFAttributedStringSetAttribute(val, (1, 3), u'color', u'blue')
        v, rng = CFAttributedStringGetAttributes(val, 1, None)
        self.failUnless( v == {u'ronald':99, u'color':u'blue'} )
        self.failUnless( rng == (1, 1) )


        CFAttributedStringRemoveAttribute(val, (1,3), u'color')
        v, rng = CFAttributedStringGetAttributes(val, 3, None)
        self.failUnless( v == {u'foo': 42, u'bar': 'baz' } )
        self.failUnless( rng == (2, 2) )

        rep = CFAttributedStringCreate(None, "dummy", {u'attrib': 99} )
        CFAttributedStringReplaceAttributedString(val, (1,3), rep)
        self.failUnless( CFAttributedStringGetString(val) == u'Hdummyo')

    def testEditing(self):
        val = CFAttributedStringCreateMutable(None, 0)
        self.failUnless(  isinstance(val, CFAttributedStringRef) )

        CFAttributedStringBeginEditing(val)
        CFAttributedStringEndEditing(val)

if __name__ == "__main__":
    main()
