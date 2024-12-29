import sys

import objc
from PyObjCTest.testbndl import PyObjC_TestClass4
from PyObjCTools.TestSupport import TestCase

from .fnd import NSArray, NSAttributedString, NSObject


class TestConstants(TestCase):
    def testBooleans(self):
        self.assertTrue(objc.YES, "YES was not true.")
        self.assertTrue(not objc.NO, "NO was true.")

    def testNil(self):
        self.assertIsNone(objc.nil, "nil is not nil/None.")

    def testFloatLimits(self):
        self.assertIsInstance(objc._FLT_MIN, float)
        self.assertIsInstance(objc._FLT_MAX, float)


class TestClassLookup(TestCase):
    def testLookupClassNoSuchClassErrorRaised(self):
        with self.assertRaisesRegex(objc.nosuchclass_error, "^$"):
            objc.lookUpClass("")
        with self.assertRaisesRegex(
            objc.nosuchclass_error, "^ThisClassReallyShouldNotExist$"
        ):
            objc.lookUpClass("ThisClassReallyShouldNotExist")
        with self.assertRaisesRegex(TypeError, "argument 1 must be str, not int"):
            objc.lookUpClass(1)

    def testClassList(self):
        NSObject = objc.lookUpClass("NSObject")
        NSException = objc.lookUpClass("NSException")
        NSMutableArray = objc.lookUpClass("NSMutableArray")

        self.assertIn(NSObject, objc.getClassList())
        self.assertIn(NSException, objc.getClassList())
        self.assertIn(NSMutableArray, objc.getClassList())

        with self.assertRaises(TypeError):
            objc.getClassList(1, 2)


class TestMethodInvocation(TestCase):
    def setUp(self):
        self.NSObjectInstance = NSObject.alloc().init()

    def testClassInvocation(self):
        self.assertTrue(NSObject.pyobjc_classMethods.description())

    def testInstanceInvocation(self):
        self.assertTrue(self.NSObjectInstance.description())
        self.assertEqual(self.NSObjectInstance.self(), self.NSObjectInstance)
        self.assertEqual(
            self.NSObjectInstance.pyobjc_instanceMethods.self(),
            self.NSObjectInstance.self(),
        )
        self.assertEqual(
            type(self.NSObjectInstance).pyobjc_instanceMethods.self(
                self.NSObjectInstance
            ),
            self.NSObjectInstance.self(),
        )


class TestClassDict(TestCase):
    def testDict(self):
        # XXX: actually access the method to force a __dict__ update
        NSAttributedString.attributesAtIndex_longestEffectiveRange_inRange_

        self.assertIn(
            "attributesAtIndex_longestEffectiveRange_inRange_",
            NSAttributedString.__dict__,
        )


class TestPickle(TestCase):
    # We don't support pickling at the moment, make sure we enforce that.

    def testPicklePure(self):
        import pickle

        o = NSObject.alloc().init()
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            with self.subTest(proto=proto):
                with self.assertRaises((TypeError, ValueError)):
                    pickle.dumps(o, proto)


class TestDescription(TestCase):
    def testSimple(self):
        TESTS = ["a"], "hello", 2
        a = NSArray.arrayWithArray_(["a"])
        EXPECTS = "(a)", "hello", "2"
        EXPECTS = repr(a), "hello", "2"
        for obj, expect in zip(TESTS, EXPECTS):
            self.assertEqual(expect, PyObjC_TestClass4.fetchObjectDescription_(obj))


class TestPrivate(TestCase):
    def test_resolve_name(self):
        resolve = objc._resolve_name

        with self.assertRaisesRegex(ValueError, r"^sys$"):
            resolve("sys")

        self.assertIs(resolve("sys.path"), sys.path)

        v = resolve("distutils.command.sdist.show_formats")

        from distutils.command.sdist import show_formats

        self.assertIs(v, show_formats)

        with self.assertRaisesRegex(
            AttributeError,
            "module 'distutils.command.sdist' has no attribute 'dont_show_formats'",
        ):
            resolve("distutils.command.sdist.dont_show_formats")
        with self.assertRaisesRegex(
            AttributeError, "module 'sys' has no attribute 'does_not_exist'"
        ):
            resolve("sys.does_not_exist")


class TestLoadBundle(TestCase):
    def test_invalid(self):
        with self.assertRaisesRegex(TypeError, "required argument"):
            objc.loadBundle(invalid=True)

        with self.assertRaisesRegex(
            ValueError, "Need to specify either bundle_path or bundle_identifier"
        ):
            objc.loadBundle("foo", {})

        with self.assertRaisesRegex(
            ValueError, "Need to specify either bundle_path or bundle_identifier"
        ):
            objc.loadBundle("foo", {}, bundle_identifier="foo", bundle_path="")

        with self.assertRaisesRegex(TypeError, "bundle_path is not a string"):
            objc.loadBundle("foo", {}, bundle_path=42)

        with self.assertRaisesRegex(TypeError, "bundle_identifier is not a string"):
            objc.loadBundle("foo", {}, bundle_identifier=42)
