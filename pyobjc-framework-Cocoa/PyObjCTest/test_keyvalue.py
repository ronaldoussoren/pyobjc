"""
Tests for the Key-Value Coding for hybrid python objects.

NOTE: Testcases here should be synchronized with the Key-Value Coding tests
in PyObjCTools.test.test_keyvalue and objc.test.test_keyvalue.

TODO:
    - This test uses C code, that code should be added to this package!
    - Tests that access properties in the parent Objective-C class!
    - More key-error tests, the tests don't cover all relevant code yet.
"""

import Foundation
from PyObjCTest.testhelper import PyObjC_TestClass3 as STUB
from PyObjCTools.TestSupport import TestCase, max_os_level
import objc


class KeyValueClass1(Foundation.NSObject):
    def init(self):
        self = objc.super(KeyValueClass1, self).init()
        self.key3 = 3
        self._key4 = "4"
        self.__private = "private"
        return self

    def addMultiple(self):
        self.multiple = KeyValueClass1.alloc().init()
        self.multiple.level2 = KeyValueClass1.alloc().init()
        self.multiple.level2.level3 = KeyValueClass1.alloc().init()
        self.multiple.level2.level3.keyA = "hello"
        self.multiple.level2.level3.keyB = "world"

    def getKey1(self):
        return 1

    def key2(self):
        return 2

    def setKey4_(self, value):
        self._key4 = value * 4

    def setKey5_(self, value):
        self.key5 = value * 5

    def keyRaisingValueError(self):
        raise ValueError("42")

    def keyRaisingNSUnknownKeyException(self):
        return self.valueForKey_("thisKeyDoesNotExist")

    def keyReturningSameSlector(self):
        return self.keyReturningSameSelector

    def keyReturningOtherSelector(self):
        return self.getKey1


class KeyValueClass1Explicit(Foundation.NSObject):
    def init(self):
        self = objc.super(KeyValueClass1Explicit, self).init()
        self._values = {}
        self._values["key3"] = 3
        self._values["key4"] = "4"
        self._values["_private"] = "private"
        return self

    def addMultiple(self):
        self._values["multiple"] = KeyValueClass1Explicit.alloc().init()
        self._values["multiple"]._values[
            "level2"
        ] = KeyValueClass1Explicit.alloc().init()
        self._values["multiple"]._values["level2"]._values[
            "level3"
        ] = KeyValueClass1Explicit.alloc().init()
        self._values["multiple"]._values["level2"]._values["level3"]._values[
            "keyA"
        ] = "hello"
        self._values["multiple"]._values["level2"]._values["level3"]._values[
            "keyB"
        ] = "world"

    def valueForKey_(self, key):
        if key == "key1":
            return 1

        elif key == "key2":
            return 2

        return self._values[key]

    def storedValueForKey_(self, key):
        return self.valueForKey_(key)

    def setValue_forKey_(self, value, key):
        if key == "key4":
            value = value * 4
        elif key == "key5":
            value = value * 5

        self._values[key] = value

    def takeStoredValue_forKey_(self, value, key):
        self.setValue_forKey_(value, key)

    def takeValue_forKey_(self, value, key):
        self.setValue_forKey_(value, key)


class KeyValueClass4(Foundation.NSObject):
    __slots__ = ("foo",)

    def init(self):
        self = objc.super(KeyValueClass4, self).init()
        self.foo = "foobar"
        return self

    # Definition for property 'bar'. Use odd names for the methods
    # because the KeyValue support recognizes the usual names.
    @objc.python_method
    def read_bar(self):
        return self.foo + self.foo

    @objc.python_method
    def write_bar(self, value):
        self.foo = value + value

    bar = property(read_bar, write_bar)

    roprop = property(lambda self: "read-only")


class KVOClass(Foundation.NSObject):
    def automaticallyNotifiesObserversForKey_(self, aKey):
        return objc.NO

    def test(self):
        return "test"


class KeyValueObserver(Foundation.NSObject):
    def init(self):
        self.observed = []
        return self

    def observeValueForKeyPath_ofObject_change_context_(
        self, keyPath, value, change, context
    ):
        self.observed.append((keyPath, value, change))


class PyKeyValueCoding(TestCase):
    def testNoPrivateVars(self):
        # Private instance variables ('anObject.__value') are not accessible using
        # key-value coding.
        o = KeyValueClass1.alloc().init()
        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o, "private")

    def testValueForKey(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "key1"), 1)

        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "key2"), 2)
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "key3"), 3)
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "key4"), "4")
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "multiple"), o.multiple)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o, "nokey")

        self.assertRaises(
            ValueError, STUB.keyValue_forObject_key_, 0, o, "keyRaisingValueError"
        )
        self.assertRaises(
            KeyError,
            STUB.keyValue_forObject_key_,
            0,
            o,
            "keyRaisingNSUnknownKeyException",
        )
        self.assertRaises(
            KeyError, STUB.keyValue_forObject_key_, 0, o, "keyReturningSameSelector"
        )

        obj = STUB.keyValue_forObject_key_(0, o, "keyReturningOtherSelector")
        self.assertIsInstance(obj, objc.selector)
        self.assertEqual(obj.selector, b"getKey1")
        self.assertIs(obj.self, o)

    def testValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "foo"), "foobar")
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "bar"), "foobarfoobar")
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "roprop"), "read-only")

    def testStoredValueForKey(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "key1"), 1)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "key2"), 2)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "key3"), 3)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "key4"), "4")
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "multiple"), o.multiple)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 2, o, "nokey")

    def testStoredValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "foo"), "foobar")
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "bar"), "foobarfoobar")
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "roprop"), "read-only")

    def testValueForKeyPath(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(1, o, "multiple"), o.multiple)
        self.assertEqual(
            STUB.keyValue_forObject_key_(1, o, "multiple.level2"), o.multiple.level2
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(1, o, "multiple.level2.level3.keyA"),
            o.multiple.level2.level3.keyA,
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(1, o, "multiple.level2.level3.keyB"),
            o.multiple.level2.level3.keyB,
        )

        self.assertRaises(
            KeyError, STUB.keyValue_forObject_key_, 1, o, "multiple.level2.nokey"
        )

    @max_os_level("10.5")
    def testValuesForKeys(self):
        o = KeyValueClass1.alloc().init()

        self.assertEqual(
            STUB.keyValue_forObject_key_(3, o, ["key1", "key2", "key3", "key4"]),
            {"key1": 1, "key2": 2, "key3": 3, "key4": "4"},
        )

        self.assertRaises(
            KeyError, STUB.keyValue_forObject_key_, 3, o, ["key1", "key3", "nosuchkey"]
        )

    @max_os_level("10.5")
    def testTakeValueForKey(self):
        o = KeyValueClass1.alloc().init()

        self.assertEqual(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(0, o, "key3", "drie")
        self.assertEqual(o.key3, "drie")

        self.assertEqual(o._key4, "4")
        STUB.setKeyValue_forObject_key_value_(0, o, "key4", "vier")
        self.assertNotHasAttr(o, "key4")
        self.assertEqual(o._key4, "viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(0, o, "key5", "V")
        self.assertEqual(o.key5, "VVVVV")

        self.assertNotHasAttr(o, "key9")
        STUB.setKeyValue_forObject_key_value_(0, o, "key9", "IX")
        self.assertHasAttr(o, "key9")
        self.assertEqual(o.key9, "IX")

    @max_os_level("10.5")
    def testTakeValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEqual(o.foo, "foobar")
        STUB.setKeyValue_forObject_key_value_(0, o, "foo", "FOO")
        self.assertEqual(o.foo, "FOO")

        self.assertRaises(
            KeyError, STUB.setKeyValue_forObject_key_value_, 0, o, "key9", "IX"
        )

    def testTakeStoredValueForKey(self):
        o = KeyValueClass1.alloc().init()

        self.assertEqual(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(2, o, "key3", "drie")
        self.assertEqual(o.key3, "drie")

        self.assertEqual(o._key4, "4")
        STUB.setKeyValue_forObject_key_value_(2, o, "key4", "vier")
        self.assertEqual(o._key4, "viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(2, o, "key5", "V")
        self.assertEqual(o.key5, "VVVVV")

        self.assertNotHasAttr(o, "key9")
        STUB.setKeyValue_forObject_key_value_(2, o, "key9", "IX")
        self.assertHasAttr(o, "key9")
        self.assertEqual(o.key9, "IX")

    def testStoredTakeValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEqual(o.foo, "foobar")
        STUB.setKeyValue_forObject_key_value_(2, o, "foo", "FOO")
        self.assertEqual(o.foo, "FOO")

        self.assertRaises(
            KeyError, STUB.setKeyValue_forObject_key_value_, 2, o, "key9", "IX"
        )
        self.assertRaises(
            KeyError, STUB.setKeyValue_forObject_key_value_, 2, o, "roprop", "IX"
        )

    @max_os_level("10.5")
    def testTakeValuesFromDictionary(self):
        o = KeyValueClass1.alloc().init()

        self.assertEqual(o.key3, 3)
        self.assertEqual(o._key4, "4")
        o.key5 = 1
        self.assertNotHasAttr(o, "key9")

        STUB.setKeyValue_forObject_key_value_(
            3, o, None, {"key3": b"drie", "key4": b"vier", "key5": b"V", "key9": b"IX"}
        )

        self.assertEqual(o.key3, "drie")
        self.assertEqual(o._key4, "viervierviervier")
        self.assertEqual(o.key5, "VVVVV")
        self.assertHasAttr(o, "key9")
        self.assertEqual(o.key9, "IX")

    @max_os_level("10.5")
    def testTakeValuesFromDictionary2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEqual(o.foo, "foobar")
        STUB.setKeyValue_forObject_key_value_(3, o, None, {"foo": "FOO"})
        self.assertEqual(o.foo, "FOO")

        self.assertRaises(
            KeyError, STUB.setKeyValue_forObject_key_value_, 3, o, None, {"key9": "IX"}
        )
        self.assertRaises(
            KeyError,
            STUB.setKeyValue_forObject_key_value_,
            3,
            o,
            None,
            {"roprop": "IX"},
        )

    @max_os_level("10.5")
    def testTakeValueForKeyPath(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEqual(o.multiple.level2.level3.keyA, "hello")
        self.assertEqual(o.multiple.level2.level3.keyB, "world")

        STUB.setKeyValue_forObject_key_value_(
            1, o, "multiple.level2.level3.keyA", "KeyAValue"
        )
        self.assertEqual(o.multiple.level2.level3.keyA, "KeyAValue")

        STUB.setKeyValue_forObject_key_value_(
            1, o, "multiple.level2.level3.keyB", 9.999
        )
        self.assertEqual(o.multiple.level2.level3.keyB, 9.999)

    if hasattr(Foundation.NSObject, "willChangeValueForKey_"):
        # NSKeyValueObserving is only available on Panther and beyond
        def testKVO1(self):
            o = KVOClass.alloc().init()
            o.addObserver_forKeyPath_options_context_(self, "test", 0, None)
            o.removeObserver_forKeyPath_(self, "test")

        def testKVO2(self):
            # Check if observations work for python-based keys on ObjC classes
            observer = KeyValueObserver.alloc().init()
            self.assertEqual(observer.observed, [])

            o = KeyValueClass1.alloc().init()

            o.addObserver_forKeyPath_options_context_(observer, "key3", 0, 0)
            try:
                STUB.setKeyValue_forObject_key_value_(2, o, "key3", "drie")
                self.assertEqual(o.key3, "drie")

                self.assertEqual(len(observer.observed), 1)

                keyPath, value, change = observer.observed[0]
                self.assertEqual(keyPath, "key3")
                self.assertIs(value, o)
                self.assertEqual(change, {Foundation.NSKeyValueChangeKindKey: 1})

            finally:
                o.removeObserver_forKeyPath_(observer, "key3")

        def testKVO3(self):
            # Check if observations work for python-based keys on ObjC classes
            observer = KeyValueObserver.alloc().init()
            self.assertEqual(observer.observed, [])

            o = KeyValueClass1.alloc().init()
            STUB.setKeyValue_forObject_key_value_(2, o, "key3", "three")

            o.addObserver_forKeyPath_options_context_(
                observer,
                "key3",
                Foundation.NSKeyValueObservingOptionNew
                | Foundation.NSKeyValueObservingOptionOld,
                0,
            )
            try:
                STUB.setKeyValue_forObject_key_value_(2, o, "key3", "drie")
                self.assertEqual(o.key3, "drie")

                self.assertEqual(len(observer.observed), 1)

                keyPath, value, change = observer.observed[0]
                self.assertEqual(keyPath, "key3")
                self.assertIs(value, o)
                self.assertEqual(
                    change,
                    {
                        Foundation.NSKeyValueChangeKindKey: 1,
                        Foundation.NSKeyValueChangeNewKey: "drie",
                        Foundation.NSKeyValueChangeOldKey: "three",
                    },
                )

            finally:
                o.removeObserver_forKeyPath_(observer, "key3")


class PyKeyValueCodingExplicit(TestCase):
    def testValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "key1"), 1)

        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "key2"), 2)
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "key3"), 3)
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, "key4"), "4")
        self.assertEqual(
            STUB.keyValue_forObject_key_(0, o, "multiple"), o._values["multiple"]
        )

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o, "nokey")

    def testStoredValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "key1"), 1)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "key2"), 2)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "key3"), 3)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, "key4"), "4")
        self.assertEqual(
            STUB.keyValue_forObject_key_(2, o, "multiple"), o._values["multiple"]
        )

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 2, o, "nokey")

    def testValueForKeyPath(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEqual(
            STUB.keyValue_forObject_key_(1, o, "multiple"), o._values["multiple"]
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(1, o, "multiple.level2"),
            o._values["multiple"]._values["level2"],
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(1, o, "multiple.level2.level3.keyA"),
            o._values["multiple"]._values["level2"]._values["level3"]._values["keyA"],
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(1, o, "multiple.level2.level3.keyB"),
            o._values["multiple"]._values["level2"]._values["level3"]._values["keyB"],
        )

        self.assertRaises(
            KeyError, STUB.keyValue_forObject_key_, 1, o, "multiple.level2.nokey"
        )

    @max_os_level("10.5")
    def testValuesForKeys(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEqual(
            STUB.keyValue_forObject_key_(3, o, ["key1", "key2", "key3", "key4"]),
            {"key1": 1, "key2": 2, "key3": 3, "key4": "4"},
        )

        self.assertRaises(
            KeyError, STUB.keyValue_forObject_key_, 3, o, ["key1", "key3", "nosuchkey"]
        )

    def testTakeValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEqual(o._values["key3"], 3)
        STUB.setKeyValue_forObject_key_value_(0, o, "key3", "drie")
        self.assertEqual(o._values["key3"], "drie")

        self.assertEqual(o._values["key4"], "4")
        STUB.setKeyValue_forObject_key_value_(0, o, "key4", "vier")
        self.assertNotHasAttr(o, "key4")
        self.assertEqual(o._values["key4"], "viervierviervier")

        o._values["key5"] = 1
        STUB.setKeyValue_forObject_key_value_(0, o, "key5", "V")
        self.assertEqual(o._values["key5"], "VVVVV")

        self.assertNotHasAttr(o, "key9")
        self.assertNotIn("key9", o._values)
        STUB.setKeyValue_forObject_key_value_(0, o, "key9", "IX")
        self.assertNotHasAttr(o, "key9")
        self.assertIn("key9", o._values)
        self.assertEqual(o._values["key9"], "IX")

    def testTakeStoredValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEqual(o._values["key3"], 3)
        STUB.setKeyValue_forObject_key_value_(2, o, "key3", "drie")
        self.assertEqual(o._values["key3"], "drie")

        self.assertEqual(o._values["key4"], "4")
        STUB.setKeyValue_forObject_key_value_(2, o, "key4", "vier")
        self.assertEqual(o._values["key4"], "viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(2, o, "key5", "V")
        self.assertEqual(o._values["key5"], "VVVVV")

        self.assertNotIn("key9", o._values)
        STUB.setKeyValue_forObject_key_value_(2, o, "key9", "IX")
        self.assertIn("key9", o._values)
        self.assertEqual(o._values["key9"], "IX")

    @max_os_level("10.5")
    def testTakeValuesFromDictionary(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEqual(o._values["key3"], 3)
        self.assertEqual(o._values["key4"], "4")
        o._values["key5"] = 1
        self.assertNotIn("key9", o._values)

        STUB.setKeyValue_forObject_key_value_(
            3, o, None, {"key3": "drie", "key4": "vier", "key5": "V", "key9": "IX"}
        )

        self.assertEqual(o._values["key3"], "drie")
        self.assertEqual(o._values["key4"], "viervierviervier")
        self.assertEqual(o._values["key5"], "VVVVV")
        self.assertEqual(o._values["key9"], "IX")

    @max_os_level("10.5")
    def testTakeValueForKeyPath(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEqual(
            o._values["multiple"]._values["level2"]._values["level3"]._values["keyA"],
            "hello",
        )
        self.assertEqual(
            o._values["multiple"]._values["level2"]._values["level3"]._values["keyB"],
            "world",
        )

        STUB.setKeyValue_forObject_key_value_(
            1, o, "multiple.level2.level3.keyA", "KeyAValue"
        )
        self.assertEqual(
            o._values["multiple"]._values["level2"]._values["level3"]._values["keyA"],
            "KeyAValue",
        )

        STUB.setKeyValue_forObject_key_value_(
            1, o, "multiple.level2.level3.keyB", 9.999
        )
        self.assertEqual(
            o._values["multiple"]._values["level2"]._values["level3"]._values["keyB"],
            9.999,
        )


class TestBaseExceptions(TestCase):
    # Check that NSObject implementation of Key-Value coding raises the
    # exception that we expect it to raise.

    def testValueForKey(self):
        o = Foundation.NSObject.alloc().init()

        self.assertRaises(KeyError, o.valueForKey_, "unknownKey")

    def testStoredValueForKey(self):
        o = Foundation.NSObject.alloc().init()

        self.assertRaises(KeyError, o.storedValueForKey_, "unknownKey")

    def testTakeStoredValue(self):
        o = Foundation.NSObject.alloc().init()

        self.assertRaises(KeyError, o.takeStoredValue_forKey_, "value", "unknownKey")
