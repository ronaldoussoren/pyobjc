from PyObjCTools.TestSupport import *
import objc
from PyObjCTest.testbndl import PyObjC_TestClass4
import fnd as Foundation
from PyObjCTest.fnd import NSObject, NSArray, NSAttributedString


class TestConstants(TestCase):
    def testBooleans(self):
        self.assertTrue(objc.YES, "YES was not true.")
        self.assertTrue(not objc.NO, "NO was true.")

    def testNil(self):
        self.assertIsNone(objc.nil, "nil is not nil/None.")


class TestObjCRuntime (TestCase):
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
        self.assertIsNotNone(objc.lookUpClass("NSObject"))
        self.assertIs(objc.lookUpClass( "NSObject" ), objc.runtime.NSObject)


class TestClassLookup(TestCase):
    def testLookupClassNoSuchClassErrorRaised(self):
        self.assertRaises(objc.nosuchclass_error, objc.lookUpClass, "")
        self.assertRaises(objc.nosuchclass_error, objc.lookUpClass, "ThisClassReallyShouldNotExist")
        self.assertRaises(TypeError, objc.lookUpClass, 1)



    def testClassList(self):
        ###! This test should probably be moved down to the Foundation test suite...

        NSObject = objc.lookUpClass('NSObject')
        NSException = objc.lookUpClass('NSException')
        NSMutableArray = objc.lookUpClass('NSMutableArray')

        self.assertIn(NSObject, objc.getClassList())
        self.assertIn(NSException, objc.getClassList())
        self.assertIn(NSMutableArray, objc.getClassList())

class TestMethodInvocation(TestCase):
    def setUp(self):
        self.NSObjectInstance = NSObject.alloc().init()


    def testClassInvocation(self):
        self.assertTrue(NSObject.pyobjc_classMethods.description())

    def testInstanceInvocation(self):
        self.assertTrue(self.NSObjectInstance.description())
        self.assertEqual(self.NSObjectInstance.self(), self.NSObjectInstance)
        self.assertEqual(self.NSObjectInstance.pyobjc_instanceMethods.self(), self.NSObjectInstance.self())
        self.assertEqual(type(self.NSObjectInstance).pyobjc_instanceMethods.self(self.NSObjectInstance), self.NSObjectInstance.self())

class TestClassDict(TestCase):
    def testDict(self):
        self.assertIn("attributesAtIndex_longestEffectiveRange_inRange_", NSAttributedString.__dict__)

class TestPickle(TestCase):
    # We don't support pickling at the moment, make sure we enforce that.

    def testPicklePure(self):
        import pickle

        o = NSObject.alloc().init()
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 0)
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 1)
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 2)

    def testCPicklePure(self):
        import cPickle as pickle

        o = NSObject.alloc().init()
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 0)
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 1)
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 2)


class TestDescription (TestCase):
    def testSimple(self):
        TESTS   = [u'a'], u'hello', 2
        a = NSArray.arrayWithArray_([u'a'])
        EXPECTS = u'(a)', u'hello', u'2'
        EXPECTS = repr(a), u'hello', u'2'
        for obj,expect in zip(TESTS, EXPECTS):
            self.assertEquals(expect, PyObjC_TestClass4.fetchObjectDescription_(obj))

if __name__ == '__main__':
    main()
