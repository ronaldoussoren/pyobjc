import unittest

import objc
from objc.test.testbndl import PyObjC_TestClass4

NSObject = objc.lookUpClass('NSObject')
NSArray = objc.lookUpClass('NSArray')
NSAttributedString = objc.lookUpClass('NSAttributedString')

class TestConstants(unittest.TestCase):
    def testBooleans(self):
        self.assert_(objc.YES, "YES was not true.")
        self.assert_(not objc.NO, "NO was true.")

    def testNil(self):
        from types import NoneType
        self.assert_(not objc.nil, "nil is not nil/None.")


class TestObjCRuntime (unittest.TestCase):
    # Tests for objc.runtime
    def setUp(self):
        import warnings
        warnings.filterwarnings('ignore', category=DeprecationWarning)

    def tearDown(self):
        import warnings
        del warnings.filters[0]

    def testRuntimeNoSuchClassErrorRaised(self):
        try:
            objc.runtime.ThisClassReallyShouldNotExist
        except AttributeError:
            pass
        except AttributeError:
            pass
        else:
            fail("objc.runtime.ThisClassReallyShouldNotExist should have thrown a nosuchclass_error.  It didn't.")

    def testRuntimeConsistency(self):
        self.assert_(objc.lookUpClass("NSObject"), "Failed to find NSObject class.")
        self.assert_(objc.lookUpClass( "NSObject" ) is objc.runtime.NSObject,
                          "objc.runtime.NSObject and objc.lookUpClass('NSObject') were different.")


class TestClassLookup(unittest.TestCase):
    def testLookupClassNoSuchClassErrorRaised(self):
        self.assertRaises(objc.nosuchclass_error, objc.lookUpClass, "")
        self.assertRaises(objc.nosuchclass_error, objc.lookUpClass, "ThisClassReallyShouldNotExist")
        self.assertRaises(TypeError, objc.lookUpClass, 1)



    def testClassList(self):
        ###! This test should probably be moved down to the Foundation test suite...

        NSObject = objc.lookUpClass('NSObject')
        NSException = objc.lookUpClass('NSException')
        NSMutableArray = objc.lookUpClass('NSMutableArray')

        self.assert_(NSObject in objc.getClassList(), "getClassList() does not appear to contain NSObject class")
        self.assert_(NSException in objc.getClassList(), "getClassList() does not appear to contain NSException class")
        self.assert_(NSMutableArray in objc.getClassList(), "getClassList() does not appear to contain NSMutableArray class")

class TestMethodInvocation(unittest.TestCase):
    def setUp(self):
        self.NSObjectInstance = NSObject.alloc().init()


    def testWithZones(self):
        obj = NSObject.allocWithZone_(None).init()
        zone = obj.zone()
        self.assert_(zone is not None)
        self.assert_(zone.pointer != 0)

        obj2 = NSObject.allocWithZone_(zone).init()
        zone2 = obj2.zone()
        self.assertEquals(zone.pointer, zone2.pointer)


        self.assertRaises(ValueError, NSObject.allocWithZone_, 10)


    def testClassInvocation(self):
        self.assert_(NSObject.pyobjc_classMethods.description(), "Failed to invoke the +description method.")

    def testInstanceInvocation(self):
        self.assert_(self.NSObjectInstance.description(), "Failed to invoke the -description method.")
        self.assertEqual(self.NSObjectInstance.self(), self.NSObjectInstance, "-self did not return same self.")
        self.assertEqual(self.NSObjectInstance.pyobjc_instanceMethods.self(), self.NSObjectInstance.self())
        self.assertEqual(type(self.NSObjectInstance).pyobjc_instanceMethods.self(self.NSObjectInstance), self.NSObjectInstance.self())

    def testVarargsInvocation(self):
        NSArray.arrayWithObjects_(u"foo", u"bar", None)

class TestClassDict(unittest.TestCase):
    def testDict(self):
        self.assert_("attributesAtIndex_longestEffectiveRange_inRange_" in NSAttributedString.__dict__)

class TestPickle(unittest.TestCase):
    # We don't support pickling at the moment, make sure we enforce that.

    def testPicklePure(self):
        import pickle

        o = NSObject.alloc().init()
        self.assertRaises(TypeError, pickle.dumps, o, 0)
        self.assertRaises(TypeError, pickle.dumps, o, 1)
        self.assertRaises(TypeError, pickle.dumps, o, 2)

    def testCPicklePure(self):
        import cPickle as pickle

        o = NSObject.alloc().init()
        self.assertRaises(TypeError, pickle.dumps, o, 0)
        self.assertRaises(TypeError, pickle.dumps, o, 1)
        self.assertRaises(TypeError, pickle.dumps, o, 2)


class TestDescription (unittest.TestCase):
    def testSimple(self):
        TESTS   = [u'a'], u'hello', 2
        EXPECTS = u'(a)', u'hello', u'2'
        for obj,expect in zip(TESTS, EXPECTS):
            self.assertEquals(expect, PyObjC_TestClass4.fetchObjectDescription_(obj))

if __name__ == '__main__':
    unittest.main()
