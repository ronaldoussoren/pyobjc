import unittest
import objc
import types

from Foundation import *

class TestNSString(unittest.TestCase):
    def testCompare(self):
        self.assert_( 
            NSString.localizedCaseInsensitiveCompare_('foo','bar') == 1,
            "NSString doesn't compare correctly")
        self.assert_( 
            NSString.localizedCaseInsensitiveCompare_('foo','Foo') == 0,
            "NSString doesn't compare correctly")

class TestEncoding(unittest.TestCase):
    def testEncoding(self):
        try:
            u = u'\xc3\xbc\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8d\xc3\xa8'
            s = NSString.stringWithString_(u.encode('iso-8859-1'))
            self.assertEqual(u,s)
            # unlikely to be equal since stringWithString_
            # has no way of guessing the correct encoding
        except UnicodeError:
            pass
            # should get here, UnicodeError raised
            # when passing non-ascii str to objc

class TestNSStringBridging(unittest.TestCase):
    def setUp(self):
        self.ns7String = NSString.stringWithString_("foo")
        self.py7String = "foo"

        self.nsUnitString = NSString.stringWithString_(u"unifoo")
        self.pyUniString = u"unifoo"

    def testBasicComparison(self):
        self.assertEquals("foo", NSString.stringWithString_("foo"))
        self.assertEquals(u"unifoo", NSString.stringWithString_(u"unifoo"))

        u = u'\xc3\xbc\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8d\xc3\xa8'
        self.assertEquals(u, NSString.stringWithString_(u));

    def testTypesAndClasses(self):
        self.assert_(isinstance(self.py7String, "".__class__))
        self.assert_(isinstance(self.pyUniString, u"".__class__))
        self.assert_(isinstance(self.ns7String, unicode))
        self.assert_(isinstance(self.pyUniString, unicode))

class TestMutable(unittest.TestCase):
    def testSync(self):
        """
        Test that python and ObjC string representation are not
        automaticly synchronized.
        """
        pyStr = NSMutableString.stringWithString_("hello")
        ocStr= pyStr.nsstring()
        self.assertEquals(pyStr, "hello")
        self.assert_(isinstance(ocStr, NSMutableString))
        ocStr.appendString_(" world")
        self.assertEquals(pyStr, "hello")

        pyStr.syncFromNSString()

        self.assertEquals(pyStr, "hello world")

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

if __name__ == '__main__':
    unittest.main()
