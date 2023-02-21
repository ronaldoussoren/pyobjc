"""
Minimal tests for sequence proxies

NOTE: this file is very, very incomplete and just tests copying at the moment.
"""

import objc
from PyObjCTest.pythonset import OC_TestSet
from PyObjCTest.dictint import OC_DictInt
from PyObjCTools.TestSupport import TestCase
import collections
from unittest import SkipTest

OC_PythonDictionary = objc.lookUpClass("OC_PythonDictionary")
OC_BuiltinPythonDictionary = objc.lookUpClass("OC_BuiltinPythonDictionary")
NSNull = objc.lookUpClass("NSNull")


class Fake:
    @property
    def __pyobjc_object__(self):
        raise TypeError("Cannot proxy")


class RaisingKey(str):
    __slots__ = ()

    def __hash__(self):
        return super().__hash__()

    def __eq__(self, other):
        if other == "a":
            raise TypeError("a is not valid")
        return super().__eq__(other)


class TestDictionary(TestCase):
    mapClass = dict

    def testCopy(self):
        s = self.mapClass()
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)
        self.assertIsNot(s, o)

        s = self.mapClass({1: 2, "a": "c"})
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)
        self.assertIsNot(s, o)

    def testProxyClass(self):
        # Ensure that the right class is used to proxy sets
        if self.mapClass is dict:
            self.assertIs(
                OC_TestSet.classOf_(self.mapClass()), OC_BuiltinPythonDictionary
            )
        else:
            self.assertIs(OC_TestSet.classOf_(self.mapClass()), OC_PythonDictionary)

    def testMutableCopy(self):
        s = self.mapClass({1: 2, "a": "c"})
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEqual(dict(s), o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, dict)

        s = self.mapClass()
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEqual(dict(s), o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, dict)

    def test_key_enumerator(self):
        s = self.mapClass({1: 2, "a": "c", None: "None"})

        self.assertEqual(OC_DictInt.allKeys_(s), [1, "a", NSNull.null()])

    def test_object_enumerator(self):
        s = self.mapClass({1: 2, "a": "c", "None": None})

        self.assertEqual(OC_DictInt.allValues_(s), [2, "c", NSNull.null()])

    def test_key_enumerator_raises(self):
        s = self.mapClass({Fake(): "a"})

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            OC_DictInt.allKeys_(s)

    def test_gettingRaises(self):
        s = self.mapClass({"a": Fake()})

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            OC_DictInt.dict_getItem_(s, "a")

    def test_none_vs_null(self):
        s = self.mapClass({None: "None", NSNull.null(): "null"})

        self.assertEqual(OC_DictInt.dict_getItem_(s, NSNull.null()), "None")

    def test_key_compare_raises(self):
        if self.mapClass is not dict:
            raise SkipTest("only valid for 'dict'")

        s = self.mapClass({RaisingKey("a"): 1})

        with self.assertRaisesRegex(TypeError, "a is not valid"):
            OC_DictInt.dict_getItem_(s, "a")

    def test_value_is_None(self):
        s = self.mapClass({"key": None})

        self.assertIs(OC_DictInt.dict_getItem_(s, "key"), NSNull.null())

    def test_set_item(self):
        s = self.mapClass()

        OC_DictInt.dict_set_value_(s, "key", "value")

        self.assertEqual(s["key"], "value")

    def test_set_null(self):
        s = self.mapClass()

        OC_DictInt.dict_set_value_(s, NSNull.null(), "null")
        self.assertEqual(s[None], "null")

    def test_set_None(self):
        s = self.mapClass()

        # This calls [dict setObject:@"null" forKey:nil]
        # and should be an error, but the behaviour below
        # should be kept for backward compatibility.
        OC_DictInt.dict_set_value_(s, None, "null")
        self.assertEqual(s[None], "null")

    def test_setting_raises(self):
        s = self.mapClass({RaisingKey("a"): 1})

        with self.assertRaisesRegex(TypeError, "a is not valid"):
            OC_DictInt.dict_set_value_(s, "a", "letter")

        self.assertEqual(tuple(s.values()), (1,))

    def test_removing_key(self):
        s = self.mapClass({"a": 1, "b": 2, None: "None", NSNull.null(): "null"})

        OC_DictInt.dict_remove_(s, "a")
        self.assertNotIn("a", s)

        OC_DictInt.dict_remove_(s, NSNull.null())
        self.assertNotIn(None, s)

        with self.assertRaisesRegex(
            ValueError, "NSInvalidArgumentException - key does not exist"
        ):
            # This should raise 'NSInvalidArgumentException',
            # not KeyError
            OC_DictInt.dict_remove_(s, "a")

    def test_removing_key_raises(self):
        s = self.mapClass({RaisingKey("a"): 1})
        with self.assertRaisesRegex(TypeError, "a is not valid"):
            OC_DictInt.dict_remove_(s, "a")


class TestUserDict(TestDictionary):
    mapClass = collections.UserDict


class TestMisc(TestCase):
    def test_key_enumerator_no_keys(self):
        class MyDict(collections.UserDict):
            def keys(self):
                raise RuntimeError("hidden keys")

        s = MyDict()
        with self.assertRaisesRegex(RuntimeError, "hidden keys"):
            OC_DictInt.allKeys_(s)

    def test_key_enumerator_no_key_iter(self):
        class MyDict(collections.UserDict):
            def keys(self):
                return 42

        s = MyDict()
        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            OC_DictInt.allKeys_(s)
