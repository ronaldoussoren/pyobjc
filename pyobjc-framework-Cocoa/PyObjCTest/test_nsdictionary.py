import types

import objc
import Foundation
from PyObjCTest.testhelper import PyObjC_TestClass3
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSDictionarySubclassing(TestCase):
    # These tests seem to be specific for macOS
    def testExceptionInInit(self):
        if objc.platform != "MACOSX":
            return

        class DictTestExceptionClass(Foundation.NSDictionary):
            pass

        # Don't use self.assertRaises here, we once had a bug that
        # causes this to fail, while the assertRaises version would
        # (probably) have worked.
        import warnings

        warnings.filterwarnings("ignore", category=objc.UninitializedDeallocWarning)

        try:
            try:
                _ = DictTestExceptionClass.alloc().initWithDictionary_({})
                self.fail()
            except ValueError:
                pass
        finally:
            del warnings.filters[0]

    def testAnotherExceptionInInit(self):
        if objc.platform != "MACOSX":
            return

        class DictTestExceptionClass2(Foundation.NSDictionary):
            def initWithObjects_forKeys_count_(self, o, k, c):
                return objc.super(
                    DictTestExceptionClass2, self
                ).initWithObjects_forKeys_count_(o, k, c)

        import warnings

        warnings.filterwarnings("ignore", category=objc.UninitializedDeallocWarning)

        try:
            try:
                _ = DictTestExceptionClass2.alloc().initWithDictionary_({})
                self.fail()
            except ValueError:
                pass
        finally:
            del warnings.filters[0]

    def testExceptionInInitClsMeth(self):
        if objc.platform != "MACOSX":
            return

        class DictTestExceptionClass3(Foundation.NSDictionary):
            def initWithObjects_forKeys_count_(self, o, k, c):
                return objc.super(
                    DictTestExceptionClass3, self
                ).initWithObjects_forKeys_count_(o, k, c)

        try:
            _ = DictTestExceptionClass3.dictionaryWithDictionary_({})
            self.fail()
        except ValueError:
            pass


class TestNSDictionaryInteraction(TestCase):
    def testMethods(self):
        for nm in dir(dict):
            if nm.startswith("__"):
                continue

            if isinstance(
                getattr(dict, nm), (types.BuiltinFunctionType, types.FunctionType)
            ):
                # Skip class methods, that needs more work in the core
                continue

            self.assertTrue(
                hasattr(Foundation.NSMutableDictionary, nm),
                "NSMutableDictionary has no method '%s'" % (nm,),
            )

    def testRepeatedAllocInit(self):
        for _ in range(1, 1000):
            _ = Foundation.NSDictionary.alloc().init()

    def testBasicInteraction(self):
        d = Foundation.NSMutableDictionary.dictionary()
        d["a"] = "foo"
        d["b"] = "bar"

        self.assertEqual(
            d["a"],
            "foo",
            "Failed to retrieve the same thing that was put into the dict.",
        )
        try:
            d["c"]
            self.fail("Should have raised...")
        except KeyError:
            pass

    def testPythonIteraction(self):
        d = Foundation.NSMutableDictionary.dictionary()
        d["a"] = "foo"
        d["b"] = "bar"

        k = list(d.keys())
        k.sort()
        self.assertTrue(k == ["a", "b"])

        k = list(d.values())
        k.sort()
        self.assertTrue(k == ["bar", "foo"])

        k = list(d.items())
        k.sort()
        self.assertTrue(k == [("a", "foo"), ("b", "bar")])

    def testIn(self):
        d = Foundation.NSMutableDictionary.dictionary()
        d["a"] = "foo"
        d["b"] = "bar"
        d[1] = "baz"
        d[0] = "bob"

        self.assertTrue("a" in d)
        self.assertTrue(1 in d)
        # self.assertTrue( -1 in d )
        # self.assertTrue( d[-1] is None )
        self.assertTrue("q" not in d)

        for k in d.allKeys():
            self.assertEqual(d.objectForKey_(k), d[k])

        for k in d:
            self.assertEqual(d.objectForKey_(k), d[k])

        del d["a"]
        self.assertTrue("a" not in d)

    def test_varargConstruction(self):
        u = Foundation.NSDictionary.dictionaryWithObjects_forKeys_(
            [1, 2, 3, 4], ["one", "two", "three", "four"]
        )
        v = Foundation.NSDictionary.alloc().initWithObjects_forKeys_(
            [1, 2, 3, 4], ["one", "two", "three", "four"]
        )
        w = Foundation.NSDictionary.dictionaryWithObjects_forKeys_count_(
            [1, 2, 3, 4, 5], ["one", "two", "three", "four", "five"], 4
        )
        x = Foundation.NSDictionary.alloc().initWithObjects_forKeys_count_(
            [1, 2, 3, 4, 5], ["one", "two", "three", "four", "five"], 4
        )
        y = Foundation.NSDictionary.dictionaryWithObjectsAndKeys_(
            1, "one", 2, "two", 3, "three", 4, "four", None
        )
        z = Foundation.NSDictionary.alloc().initWithObjectsAndKeys_(
            1, "one", 2, "two", 3, "three", 4, "four", None
        )

        self.assertEqual(len(u), 4)
        self.assertEqual(len(v), 4)
        self.assertEqual(len(w), 4)
        self.assertEqual(len(x), 4)
        self.assertEqual(len(y), 4)
        self.assertEqual(len(z), 4)

        self.assertEqual(u["one"], 1)
        self.assertEqual(v["two"], 2)
        self.assertEqual(w["three"], 3)
        self.assertEqual(x["one"], 1)
        self.assertEqual(y["two"], 2)
        self.assertEqual(z["four"], 4)

    def test_varargConstruction2(self):
        u = Foundation.NSMutableDictionary.dictionaryWithObjects_forKeys_(
            [1, 2, 3, 4], ["one", "two", "three", "four"]
        )
        self.assertIsNot(u, None)
        v = Foundation.NSMutableDictionary.alloc().initWithObjects_forKeys_(
            [1, 2, 3, 4], ["one", "two", "three", "four"]
        )
        self.assertIsNot(v, None)
        w = Foundation.NSMutableDictionary.dictionaryWithObjects_forKeys_count_(
            [1, 2, 3, 4, 5], ["one", "two", "three", "four", "five"], 4
        )
        self.assertIsNot(w, None)
        x = Foundation.NSMutableDictionary.alloc().initWithObjects_forKeys_count_(
            [1, 2, 3, 4, 5], ["one", "two", "three", "four", "five"], 4
        )
        self.assertIsNot(x, None)

        y = Foundation.NSMutableDictionary.dictionaryWithObjectsAndKeys_(
            1, "one", 2, "two", 3, "three", 4, "four", None
        )
        self.assertIsNot(y, None)
        z = Foundation.NSMutableDictionary.alloc().initWithObjectsAndKeys_(
            1, "one", 2, "two", 3, "three", 4, "four", None
        )
        self.assertIsNot(z, None)

        self.assertEqual(len(u), 4)
        self.assertEqual(len(v), 4)
        self.assertEqual(len(w), 4)
        self.assertEqual(len(x), 4)
        self.assertEqual(len(y), 4)
        self.assertEqual(len(z), 4)

        self.assertEqual(u["one"], 1)
        self.assertEqual(v["two"], 2)
        self.assertEqual(w["three"], 3)
        self.assertEqual(x["one"], 1)
        self.assertEqual(y["two"], 2)
        self.assertEqual(z["four"], 4)


class MyDictionaryBase(Foundation.NSDictionary):
    def count(self):
        if hasattr(self, "_count"):
            return self._count
        return -1

    def keyEnumerator(self):
        return None

    def objectForKey_(self, key):
        return None


class MyDictionary1(MyDictionaryBase):
    def initWithObjects_forKeys_count_(self, objects, keys, count):
        self._count = count
        self._objects = objects
        self._keys = keys
        return self


class MyDictionary2(MyDictionaryBase):
    def dictionaryWithObjects_forKeys_count_(self, objects, keys, count):
        if self is not MyDictionary2:
            raise AssertionError(self)
        return (objects, keys, count)


class TestSubclassing(TestCase):
    def testInitWithObjects(self):
        o = PyObjC_TestClass3.makeDictFromClass_method_(MyDictionary1, 1)

        self.assertIsInstance(o, MyDictionary1)
        self.assertEqual(o._count, 4)
        self.assertEqual(len(o._keys), 4)
        self.assertEqual(len(o._objects), 4)

    def testDictWithObjects(self):
        o = PyObjC_TestClass3.makeDictFromClass_method_(MyDictionary2, 0)

        self.assertIsInstance(o, tuple)
        self.assertEqual(o[2], 4)
        self.assertEqual(len(o[1]), 4)
        self.assertEqual(len(o[0]), 4)


class TestVariadic(TestCase):
    def testDictionaryWithObjectsAndKeys(self):
        o = Foundation.NSDictionary.dictionaryWithObjectsAndKeys_(42, "a", 43, "b")
        self.assertEqual(o, {"a": 42, "b": 43})
        self.assertIsInstance(o, Foundation.NSDictionary)

        o = Foundation.NSMutableDictionary.dictionaryWithObjectsAndKeys_(
            42, "a", 43, "b"
        )
        self.assertEqual(o, {"a": 42, "b": 43})
        self.assertIsInstance(o, Foundation.NSMutableDictionary)

    def testInitWithObjectsAndKeys(self):
        o = Foundation.NSDictionary.alloc().initWithObjectsAndKeys_(42, "a", 43, "b")
        self.assertEqual(o, {"a": 42, "b": 43})
        self.assertIsInstance(o, Foundation.NSDictionary)

        o = Foundation.NSMutableDictionary.alloc().initWithObjectsAndKeys_(
            42, "a", 43, "b"
        )
        self.assertEqual(o, {"a": 42, "b": 43})
        self.assertIsInstance(o, Foundation.NSMutableDictionary)


class TestNSDictionary(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSDictionary.isEqualToDictionary_)
        self.assertResultIsBOOL(Foundation.NSDictionary.writeToFile_atomically_)
        self.assertArgIsBOOL(Foundation.NSDictionary.writeToFile_atomically_, 1)
        self.assertResultIsBOOL(Foundation.NSDictionary.writeToURL_atomically_)
        self.assertArgIsBOOL(Foundation.NSDictionary.writeToURL_atomically_, 1)

        self.assertArgIsSEL(
            Foundation.NSDictionary.keysSortedByValueUsingSelector_, 0, b"i@:@"
        )

        self.assertArgIsIn(
            Foundation.NSDictionary.dictionaryWithObjects_forKeys_count_, 0
        )
        self.assertArgSizeInArg(
            Foundation.NSDictionary.dictionaryWithObjects_forKeys_count_, 0, 2
        )
        self.assertArgIsIn(
            Foundation.NSDictionary.dictionaryWithObjects_forKeys_count_, 1
        )
        self.assertArgSizeInArg(
            Foundation.NSDictionary.dictionaryWithObjects_forKeys_count_, 1, 2
        )

        self.assertArgIsIn(Foundation.NSDictionary.initWithObjects_forKeys_count_, 0)
        self.assertArgSizeInArg(
            Foundation.NSDictionary.initWithObjects_forKeys_count_, 0, 2
        )
        self.assertArgIsIn(Foundation.NSDictionary.initWithObjects_forKeys_count_, 1)
        self.assertArgSizeInArg(
            Foundation.NSDictionary.initWithObjects_forKeys_count_, 1, 2
        )

        self.assertArgIsBOOL(Foundation.NSDictionary.initWithDictionary_copyItems_, 1)

        self.assertIsNullTerminated(Foundation.NSDictionary.initWithObjectsAndKeys_)
        self.assertIsNullTerminated(
            Foundation.NSDictionary.dictionaryWithObjectsAndKeys_
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBlock(
            Foundation.NSDictionary.enumerateKeysAndObjectsUsingBlock_,
            0,
            b"v@@o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSDictionary.enumerateKeysAndObjectsWithOptions_usingBlock_,
            1,
            b"v@@o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSDictionary.keysSortedByValueUsingComparator_, 0, b"i@@"
        )
        self.assertArgIsBlock(
            Foundation.NSDictionary.keysSortedByValueWithOptions_usingComparator_,
            1,
            objc._C_NSInteger + b"@@",
        )

        self.assertArgIsBlock(
            Foundation.NSDictionary.keysOfEntriesPassingTest_,
            0,
            objc._C_NSBOOL + b"@@o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSDictionary.keysOfEntriesWithOptions_passingTest_,
            1,
            objc._C_NSBOOL + b"@@o^" + objc._C_NSBOOL,
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(Foundation.NSDictionary.writeToURL_error_, 1)
        self.assertResultIsBOOL(Foundation.NSDictionary.writeToURL_error_)

        self.assertArgIsOut(Foundation.NSDictionary.initWithContentsOfURL_error_, 1)
        self.assertArgIsOut(
            Foundation.NSDictionary.dictionaryWithContentsOfURL_error_, 1
        )
