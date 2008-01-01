import unittest
import objc
import types
import warnings

from Foundation import *

class TestNSString(unittest.TestCase):
    def testClassTree(self):
        self.assert_(issubclass(objc.pyobjc_unicode, unicode))

    def testCompare(self):
        self.assert_(
            NSString.localizedCaseInsensitiveCompare_(u'foo',u'bar') == 1,
            u"NSString doesn't compare correctly")
        self.assert_(
            NSString.localizedCaseInsensitiveCompare_(u'foo',u'Foo') == 0,
            u"NSString doesn't compare correctly")

    def testFormatting(self):
        # The test on instances is slightly more verbose to avoid warnings
        obj = NSString.alloc().initWithFormat_(u"foo %d", 42)
        self.assertEquals(obj, u"foo 42")

        obj = NSString.alloc().initWithFormat_locale_(u"foo %d", {}, 42)
        self.assertEquals(obj, u"foo 42")

        try:
            obj = NSString.alloc()
            self.assertRaises(TypeError, obj.initWithFormat_arguments_, u"foo", [])
            obj = obj.initWithString_(u"foo")
        except AssertionError, msg:
            raise

        try:
            obj = NSString.alloc()
            self.assertRaises(TypeError, obj.initWithFormat_locale_arguments_, u"foo", {}, [])
            obj = obj.initWithString_(u"foo")
        except AssertionError, msg:
            raise


    def testGetCString(self):
        # Custom wrappers
        v = NSString.stringWithString_(u"hello world")
        
        self.assertEquals(v, u"hello world")

        x = v.getCString_maxLength_(16)
        self.assertEquals(x, u"hello world")

        self.assertRaises(objc.error, v.getCString_maxLength_, 4)

        x, l = v.getCString_maxLength_range_remainingRange_(4, (1, 4))
        self.assertEquals(x, "ello")
        self.assertEquals(l.location, 5)
        self.assertEquals(l.length, 0)


class TestNSStringBridging(unittest.TestCase):
    def setUp(self):
        self.nsUniString = NSString.stringWithString_(u"unifoo")
        self.pyUniString = u"unifoo"

    def testBasicComparison(self):
        self.assertEquals(u"unifoo", NSString.stringWithString_(u"unifoo"))

        u = u'\xc3\xbc\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8d\xc3\xa8'
        self.assertEquals(u, NSString.stringWithString_(u));

    def testTypesAndClasses(self):
        self.assert_(isinstance(self.nsUniString, unicode))
        self.assert_(isinstance(self.pyUniString, unicode))

    def testStrConversion(self):
        curEnabledFlag = objc.getStrBridgeEnabled()
        objc.setStrBridgeEnabled(True)
        try:
            v = NSString.stringWithString_("hello2")
            self.assert_(isinstance(v, objc.pyobjc_unicode))
            self.assertEquals(v, u"hello2")


            self.assertRaises(UnicodeError, unicode, "\xff")
            # XXX: string bridge now uses the default NSString encoding
            # self.assertRaises(UnicodeError, NSString.stringWithString_, '\xff')

            objc.setStrBridgeEnabled(False)

            warnings.filterwarnings('error', category=objc.PyObjCStrBridgeWarning)
            try:
                #v = NSString.stringWithString_("hello")

                # we need to make sure that the str is unique
                # because an already bridged one might have crossed
                # and would be cached
                newString = type('test_str', (str,), {})('hello2')
                self.assertRaises(objc.PyObjCStrBridgeWarning,
                        NSString.stringWithString_, newString)

            finally:
                del warnings.filters[0]


        finally:
            objc.setStrBridgeEnabled(curEnabledFlag)

    def testNSStringMethodAccess(self):
        self.assert_(isinstance(self.nsUniString, objc.pyobjc_unicode))
        v = self.nsUniString.stringByAppendingString_
        self.assert_(isinstance(v, objc.selector))

class TestMutable(unittest.TestCase):
    def testSync(self):
        """
        Test that python and ObjC string representation are not
        automaticly synchronized.
        """
        pyStr = NSMutableString.stringWithString_(u"hello")
        ocStr= pyStr.nsstring()
        self.assertEquals(pyStr, u"hello")
        self.assert_(isinstance(ocStr, NSMutableString))
        ocStr.appendString_(u" world")
        self.assertEquals(pyStr, u"hello")

class TestPickle(unittest.TestCase):
    """
    Testcases for pickling of Objective-C strings. Those are pickled as
    unicode strings.
    """

    def setUp(self):
        self.strVal = NSTaskDidTerminateNotification

    def testPickle(self):
        """
        Check that ObjC-strings pickle as unicode strings
        """
        import pickle

        s = pickle.dumps(self.strVal, 0)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 1)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 2)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

    def testCPickle(self):
        """
        Check that ObjC-strings pickle as unicode strings
        """
        import cPickle as pickle

        s = pickle.dumps(self.strVal, 0)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 1)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 2)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

    def testFormat(self):
        v = self.strVal

        d = v.stringByAppendingFormat_(u"hello")
        self.assertEquals(d, v + u'hello')

        d = v.stringByAppendingFormat_(u"hello %s %d", "world", 101)
        self.assertEquals(d, v + u'hello world 101')

        v = NSString.alloc().initWithFormat_("%s %d %s", "a", 44, "cc")
        self.assertEquals(v, "a 44 cc")

        v = NSString.alloc().initWithFormat_locale_("%s %d %s", {}, "a", 44, "cc")
        self.assertEquals(v, "a 44 cc")

        v = NSString.stringWithFormat_("aap %s mies", "noot")
        self.assertEquals(v, "aap noot mies")

        v = NSString.localizedStringWithFormat_("aap %s mies", "noot")
        self.assertEquals(v, "aap noot mies")


        v = NSMutableString.stringWithString_("hello")
        v.appendFormat_(" bar %s", "baz")
        self.assertEquals(v.nsstring(), "hello bar baz")

if __name__ == '__main__':
    unittest.main()
