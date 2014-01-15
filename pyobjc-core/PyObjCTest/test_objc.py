from __future__ import unicode_literals
from PyObjCTools.TestSupport import *
import objc
from PyObjCTest.testbndl import PyObjC_TestClass4
from . import fnd as Foundation
from .fnd import NSObject, NSArray, NSAttributedString
import sys
import os


class TestConstants(TestCase):
    def testBooleans(self):
        self.assertTrue(objc.YES, "YES was not true.")
        self.assertTrue(not objc.NO, "NO was true.")

    def testNil(self):
        self.assertIsNone(objc.nil, "nil is not nil/None.")


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

        # XXX: actually access the method to force a __dict__ update
        NSAttributedString.attributesAtIndex_longestEffectiveRange_inRange_

        self.assertIn("attributesAtIndex_longestEffectiveRange_inRange_", NSAttributedString.__dict__)

class TestPickle(TestCase):
    # We don't support pickling at the moment, make sure we enforce that.

    def testPicklePure(self):
        import pickle

        o = NSObject.alloc().init()
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 0)
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 1)
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 2)

    @onlyPython2
    def testCPicklePure(self):
        import cPickle as pickle

        o = NSObject.alloc().init()
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 0)
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 1)
        self.assertRaises((TypeError, ValueError), pickle.dumps, o, 2)


class TestDescription (TestCase):
    def testSimple(self):
        TESTS   = ['a'], 'hello', 2
        a = NSArray.arrayWithArray_(['a'])
        EXPECTS = '(a)', 'hello', '2'
        EXPECTS = repr(a), 'hello', '2'
        for obj,expect in zip(TESTS, EXPECTS):
            self.assertEqual(expect, PyObjC_TestClass4.fetchObjectDescription_(obj))

class TestPrivate (TestCase):
    def test_resolve_name(self):
        resolve = objc._resolve_name

        self.assertRaises(ValueError, resolve, "sys")

        self.assertIs(resolve("sys.path"), sys.path)

        v = resolve("distutils.command.sdist.show_formats")

        from distutils.command.sdist import show_formats
        self.assertIs(v, show_formats)

        self.assertRaises(AttributeError, resolve, "distutils.command.sdist.dont_show_formats")
        self.assertRaises(AttributeError, resolve, "sys.does_not_exist")

if __name__ == '__main__':
    main()
