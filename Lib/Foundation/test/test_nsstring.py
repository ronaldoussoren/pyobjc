import unittest
import objc
import types

from Foundation import *

class TestNSString(unittest.TestCase):
    def testCompare(self):
        self.assert_(
            NSString.localizedCaseInsensitiveCompare_(u'foo',u'bar') == 1,
            u"NSString doesn't compare correctly")
        self.assert_(
            NSString.localizedCaseInsensitiveCompare_(u'foo',u'Foo') == 0,
            u"NSString doesn't compare correctly")

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

if __name__ == '__main__':
    unittest.main()
