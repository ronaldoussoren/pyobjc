"""
Tests for the Key-Value Coding support in OC_PythonObject

NOTE: Testcases here should be synchronized with the Key-Value Coding tests
in PyObjCTools.test.test_keyvalue and Foundation.test.test_keyvalue.
"""

import os
import sys

import objc
from PyObjCTest.fnd import (
    NSObject,
    NSArray,
    NSKeyValueObservingOptionOld,
    NSKeyValueObservingOptionNew,
    NSAutoreleasePool,
)
from PyObjCTest.keyvaluehelper import (
    PyObjCTestObserver,
    DO_SETVALUE_FORKEYPATH,
    DO_SETVALUESFORKEYSFROMDICT,
    DO_SETVALUE_FORKEY,
    DO_VALUEFORKEY,
    DO_VALUEFORKEYPATH,
    DO_STOREDVALUEFORKEY,
    DO_TAKESTOREDVALUE_FORKEY,
    DO_TAKEVALUESFROMDICT,
    DO_TAKEVALUE_FORKEY,
    DO_TAKEVALUE_FORKEYPATH,
    DO_VALUESFORKEYS,
    IndirectString,
    IndirectNumber,
    DirectString,
    DirectNumber,
    KVPySubOverObjCPath,
    KVPySubOverObjCBase,
    KVPySubObjCPath,
    KVPySubObjCBase,
    KVPyPath,
    KVPyBase,
    PyObjCTest_KVPathClass,
    PyObjCTest_KVBaseClass,
)
from .objectint import OC_ObjectInt

# Native code is needed to access the python class from Objective-C, otherwise
# the Key-Value support cannot be tested.
from PyObjCTest.testbndl import PyObjC_TestClass3 as STUB
from PyObjCTest.testbndl import PyObjCTest_KeyValueObserver
from PyObjCTools.TestSupport import TestCase, min_os_level


class KeyValueClass2:
    def __init__(self):
        self.key3 = 3
        self._key4 = "4"
        self._pythonConvention = "BAD"
        self._pythonConventionValue = "GOOD"
        self.__private = "private"

    def addMultiple(self):
        self.multiple = KeyValueClass2()
        self.multiple.level2 = KeyValueClass2()
        self.multiple.level2.level3 = KeyValueClass2()
        self.multiple.level2.level3.keyA = "hello"
        self.multiple.level2.level3.keyB = "world"

    def pythonConvention(self):
        return self._pythonConventionValue

    def setPythonConvention_(self, value):
        self._pythonConventionValue = value

    def getKey1(self):
        return 1

    def get_key2(self):
        return 2

    def setKey4(self, value):
        self._key4 = value * 4

    def set_key5(self, value):
        self.key5 = value * 5


class KeyValueClass3:
    __slots__ = ("foo",)

    def __init__(self):
        self.foo = "foobar"

    # Definition for property 'bar'. Use odd names for the methods
    # because the KeyValue support recognizes the usual names.
    def read_bar(self):
        return self.foo + self.foo

    def write_bar(self, value):
        self.foo = value + value

    bar = property(read_bar, write_bar)

    roprop = property(lambda self: "read-only")


class PyKeyValueCoding(TestCase):
    def testNoPrivateVars(self):
        # Private instance variables ('anObject.__value') are not accessible using
        # key-value coding.
        o = KeyValueClass2()
        with self.assertRaisesRegex(KeyError, "private"):
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "private")

    def testValueForKey(self):
        o = KeyValueClass2()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "key1"), 1)
        self.assertEqual(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "key2"), 2)
        self.assertEqual(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "key3"), 3)
        self.assertEqual(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "key4"), "4")
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "multiple"), o.multiple
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "pythonConvention"), "GOOD"
        )

        with self.assertRaisesRegex(KeyError, "nokey"):
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "nokey")

    def testValueForKey2(self):
        o = KeyValueClass3()

        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "foo"), "foobar"
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "bar"), "foobarfoobar"
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "roprop"), "read-only"
        )

    def testStoredValueForKey(self):
        o = KeyValueClass2()
        o.addMultiple()

        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, "key1"), 1
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, "key2"), 2
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, "key3"), 3
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, "key4"), "4"
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, "multiple"),
            o.multiple,
        )

        with self.assertRaisesRegex(KeyError, "nokey"):
            STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, "nokey")

    def testStoredValueForKey2(self):
        o = KeyValueClass3()

        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, "foo"), "foobar"
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, "bar"), "foobarfoobar"
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, "roprop"), "read-only"
        )

    def testValueForKeyPath(self):
        o = KeyValueClass2()
        o.addMultiple()

        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, o, "multiple"), o.multiple
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, o, "multiple.level2"),
            o.multiple.level2,
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, o, "multiple.level2.level3.keyA"
            ),
            o.multiple.level2.level3.keyA,
        )
        self.assertEqual(
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, o, "multiple.level2.level3.keyB"
            ),
            o.multiple.level2.level3.keyB,
        )

        with self.assertRaisesRegex(KeyError, "nokey"):
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH,
                o,
                "multiple.level2.nokey",
            )

    def testValuesForKeys(self):
        o = KeyValueClass2()

        self.assertEqual(
            STUB.keyValue_forObject_key_(
                DO_VALUESFORKEYS, o, ["key1", "key2", "key3", "key4"]
            ),
            {"key1": 1, "key2": 2, "key3": 3, "key4": "4"},
        )

        with self.assertRaisesRegex(KeyError, "nokey"):
            STUB.keyValue_forObject_key_(
                DO_VALUESFORKEYS,
                o,
                ["key1", "key2", "nokey", "key3"],
            )

    def testTakeValueForKey(self):
        o = KeyValueClass2()

        self.assertEqual(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEY, o, "key3", "drie")
        self.assertEqual(o.key3, "drie")

        self.assertEqual(o._key4, "4")
        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEY, o, "key4", "vier")
        self.assertEqual(o._key4, "viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEY, o, "key5", "V")
        self.assertEqual(o.key5, "VVVVV")

        self.assertNotHasAttr(o, "key9")
        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEY, o, "key9", "IX")
        self.assertHasAttr(o, "key9")
        self.assertEqual(o.key9, "IX")

    def testTakeValueForKey2(self):
        o = KeyValueClass3()

        self.assertEqual(o.foo, "foobar")
        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEY, o, "foo", "FOO")
        self.assertEqual(o.foo, "FOO")

        with self.assertRaisesRegex(KeyError, "key9"):
            STUB.setKeyValue_forObject_key_value_(
                DO_TAKEVALUE_FORKEY,
                o,
                "key9",
                "IX",
            )

    def testTakeStoredValueForKey(self):
        o = KeyValueClass2()

        self.assertEqual(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(
            DO_TAKESTOREDVALUE_FORKEY, o, "key3", "drie"
        )
        self.assertEqual(o.key3, "drie")

        self.assertEqual(o._key4, "4")
        STUB.setKeyValue_forObject_key_value_(
            DO_TAKESTOREDVALUE_FORKEY, o, "key4", "vier"
        )
        self.assertEqual(o._key4, "viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(DO_TAKESTOREDVALUE_FORKEY, o, "key5", "V")
        self.assertEqual(o.key5, "VVVVV")

        self.assertNotHasAttr(o, "key9")
        STUB.setKeyValue_forObject_key_value_(
            DO_TAKESTOREDVALUE_FORKEY, o, "key9", "IX"
        )
        self.assertHasAttr(o, "key9")
        self.assertEqual(o.key9, "IX")

    def testStoredTakeValueForKey2(self):
        o = KeyValueClass3()

        self.assertEqual(o.foo, "foobar")
        STUB.setKeyValue_forObject_key_value_(
            DO_TAKESTOREDVALUE_FORKEY, o, "foo", "FOO"
        )
        self.assertEqual(o.foo, "FOO")

        with self.assertRaisesRegex(KeyError, "Key key9 does not exist'"):
            STUB.setKeyValue_forObject_key_value_(
                DO_TAKESTOREDVALUE_FORKEY,
                o,
                "key9",
                "IX",
            )
        with self.assertRaisesRegex(KeyError, "Key roprop does not exist'"):
            STUB.setKeyValue_forObject_key_value_(
                DO_TAKESTOREDVALUE_FORKEY,
                o,
                "roprop",
                "IX",
            )

    def testTakeValuesFromDictionary(self):
        o = KeyValueClass2()

        self.assertEqual(o.key3, 3)
        self.assertEqual(o._key4, "4")
        o.key5 = 1
        self.assertNotHasAttr(o, "key9")

        STUB.setKeyValue_forObject_key_value_(
            DO_TAKEVALUESFROMDICT,
            o,
            None,
            {"key3": "drie", "key4": "vier", "key5": "V", "key9": "IX"},
        )

        self.assertEqual(o.key3, "drie")
        self.assertEqual(o._key4, "viervierviervier")
        self.assertEqual(o.key5, "VVVVV")
        self.assertHasAttr(o, "key9")
        self.assertEqual(o.key9, "IX")

    def testTakeValuesFromDictionary2(self):
        o = KeyValueClass3()

        self.assertEqual(o.foo, "foobar")
        STUB.setKeyValue_forObject_key_value_(
            DO_TAKEVALUESFROMDICT, o, None, {"foo": "FOO"}
        )
        self.assertEqual(o.foo, "FOO")

        with self.assertRaisesRegex(KeyError, "Key key9 does not exist"):
            STUB.setKeyValue_forObject_key_value_(
                DO_TAKEVALUESFROMDICT,
                o,
                None,
                {"key9": "IX"},
            )
        with self.assertRaisesRegex(KeyError, "Key roprop does not exist"):
            STUB.setKeyValue_forObject_key_value_(
                DO_TAKEVALUESFROMDICT,
                o,
                None,
                {"roprop": "IX"},
            )

    def testTakeValueForKeyPath(self):
        o = KeyValueClass2()
        o.addMultiple()

        self.assertEqual(o.multiple.level2.level3.keyA, "hello")
        self.assertEqual(o.multiple.level2.level3.keyB, "world")

        STUB.setKeyValue_forObject_key_value_(
            DO_TAKEVALUE_FORKEYPATH, o, "multiple.level2.level3.keyA", "KeyAValue"
        )
        self.assertEqual(o.multiple.level2.level3.keyA, "KeyAValue")

        STUB.setKeyValue_forObject_key_value_(
            DO_TAKEVALUE_FORKEYPATH, o, "multiple.level2.level3.keyB", 9.999
        )
        self.assertEqual(o.multiple.level2.level3.keyB, 9.999)


class TestAccMethod(TestCase):
    def testStrCap(self):
        class Foo:
            def callme(self):
                return "FOO"

        # check the result for valueForKey: "callme" on a Foo instance
        self.assertEqual(
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, Foo(), "callme"), "FOO"
        )

    def testStr(self):
        # Strings are automaticly converted to NSStrings, and those don't have
        # a capitalize key.
        with self.assertRaisesRegex(
            KeyError,
            r"NSUnknownKeyException - \[.*\]: this class is not key value coding-compliant for the key capitalize.",
        ):
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEY,
                "hello",
                "capitalize",
            )
        with self.assertRaisesRegex(
            KeyError,
            r"NSUnknownKeyException - \[.*\]: this class is not key value coding-compliant for the key capitalize.",
        ):
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEY,
                "hello",
                "capitalize",
            )


class AbstractKVCodingTest:
    def testBaseValueForKey(self):
        self.assertEqual(
            DirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, self.base, "directString"),
        )
        self.assertEqual(
            IndirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, self.base, "indirectString"),
        )
        self.assertEqual(
            DirectNumber,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, self.base, "directNumber"),
        )
        self.assertEqual(
            IndirectNumber,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, self.base, "indirectNumber"),
        )

    def testPathValueForKey(self):
        self.assertEqual(
            DirectString,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "directHead.directString"
            ),
        )
        self.assertEqual(
            DirectString,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "indirectHead.directString"
            ),
        )
        self.assertEqual(
            IndirectString,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "directHead.indirectString"
            ),
        )
        self.assertEqual(
            IndirectString,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "indirectHead.indirectString"
            ),
        )
        self.assertEqual(
            DirectNumber,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "directHead.directNumber"
            ),
        )
        self.assertEqual(
            DirectNumber,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "indirectHead.directNumber"
            ),
        )
        self.assertEqual(
            IndirectNumber,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "directHead.indirectNumber"
            ),
        )
        self.assertEqual(
            IndirectNumber,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "indirectHead.indirectNumber"
            ),
        )


class TestObjCKVCoding(AbstractKVCodingTest, TestCase):
    def setUp(self):
        self.base = PyObjCTest_KVBaseClass.new()
        self.path = PyObjCTest_KVPathClass.new()


class TestPythonKVCoding(AbstractKVCodingTest, TestCase):
    def setUp(self):
        self.base = KVPyBase()
        self.path = KVPyPath()


class TestPythonSubObjCContainerCoding(AbstractKVCodingTest, TestCase):
    def setUp(self):
        self.base = KVPySubObjCBase.new()
        self.path = KVPySubObjCPath.new()


class TestPythonSubOverObjC(AbstractKVCodingTest, TestCase):
    def setUp(self):
        self.base = KVPySubOverObjCBase.new()
        self.path = KVPySubOverObjCPath.new()

    def testOverValueKey(self):
        self.assertEqual(
            DirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, self.base, "overDirectString"),
        )
        self.assertEqual(
            IndirectString,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEY, self.base, "overIndirectString"
            ),
        )

    def testOverValueKeyPath(self):
        self.assertEqual(
            DirectString,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "overDirectHead.directString"
            ),
        )
        self.assertEqual(
            DirectString,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "overIndirectHead.directString"
            ),
        )
        self.assertEqual(
            IndirectString,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "overDirectHead.indirectString"
            ),
        )
        self.assertEqual(
            IndirectString,
            STUB.keyValue_forObject_key_(
                DO_VALUEFORKEYPATH, self.path, "overIndirectHead.indirectString"
            ),
        )


if sys.platform == "darwin" and os.uname()[2] >= "7.0.0":
    # macOS 10.3 and later use 'setValue:forKey: u' instead of
    # 'takeValue:forKey: u', test these as wel.

    class PyKeyValueCoding_10_3(TestCase):
        def testPythonConvention(self):
            o = KeyValueClass2()

            self.assertEqual(o._pythonConvention, "BAD")
            self.assertEqual(o.pythonConvention(), "GOOD")
            self.assertEqual(o._pythonConventionValue, "GOOD")
            self.assertEqual(
                STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "pythonConvention"),
                "GOOD",
            )
            STUB.setKeyValue_forObject_key_value_(
                DO_SETVALUE_FORKEY, o, "pythonConvention", "CHANGED"
            )
            self.assertEqual(
                STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, "pythonConvention"),
                "CHANGED",
            )
            self.assertEqual(o._pythonConvention, "BAD")
            self.assertEqual(o.pythonConvention(), "CHANGED")
            self.assertEqual(o._pythonConventionValue, "CHANGED")

        def testSetValueForKey(self):
            o = KeyValueClass2()

            self.assertEqual(o.key3, 3)
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEY, o, "key3", "drie")
            self.assertEqual(o.key3, "drie")

            self.assertEqual(o._key4, "4")
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEY, o, "key4", "vier")
            self.assertEqual(o._key4, "viervierviervier")

            o.key5 = 1
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEY, o, "key5", "V")
            self.assertEqual(o.key5, "VVVVV")

            self.assertNotHasAttr(o, "key9")
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEY, o, "key9", "IX")
            self.assertHasAttr(o, "key9")
            self.assertEqual(o.key9, "IX")

        def testTakeValueForKey2(self):
            o = KeyValueClass3()

            self.assertEqual(o.foo, "foobar")
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEY, o, "foo", "FOO")
            self.assertEqual(o.foo, "FOO")

            with self.assertRaisesRegex(KeyError, "foo"):
                STUB.setKeyValue_forObject_key_value_(
                    DO_SETVALUE_FORKEY,
                    o,
                    "key9",
                    "IX",
                )

        def testSetValuesForKeysFromDictionary(self):
            o = KeyValueClass2()

            self.assertEqual(o.key3, 3)
            self.assertEqual(o._key4, "4")
            o.key5 = 1
            self.assertNotHasAttr(o, "key9")

            STUB.setKeyValue_forObject_key_value_(
                DO_SETVALUESFORKEYSFROMDICT,
                o,
                None,
                {"key3": "drie", "key4": "vier", "key5": "V", "key9": "IX"},
            )

            self.assertEqual(o.key3, "drie")
            self.assertEqual(o._key4, "viervierviervier")
            self.assertEqual(o.key5, "VVVVV")
            self.assertHasAttr(o, "key9")
            self.assertEqual(o.key9, "IX")

        def testSetValuesForKeysFromDictionary2(self):
            o = KeyValueClass3()

            self.assertEqual(o.foo, "foobar")
            STUB.setKeyValue_forObject_key_value_(
                DO_SETVALUESFORKEYSFROMDICT, o, None, {"foo": "FOO"}
            )
            self.assertEqual(o.foo, "FOO")

            with self.assertRaisesRegex(KeyError, "foo"):
                STUB.setKeyValue_forObject_key_value_(
                    DO_SETVALUESFORKEYSFROMDICT,
                    o,
                    None,
                    {"key9": "IX"},
                )
            with self.assertRaisesRegex(KeyError, "foo"):
                STUB.setKeyValue_forObject_key_value_(
                    DO_SETVALUESFORKEYSFROMDICT,
                    o,
                    None,
                    {"roprop": "IX"},
                )

        def testSetValueForKeyPath(self):
            o = KeyValueClass2()
            o.addMultiple()

            self.assertEqual(o.multiple.level2.level3.keyA, "hello")
            self.assertEqual(o.multiple.level2.level3.keyB, "world")

            STUB.setKeyValue_forObject_key_value_(
                DO_SETVALUE_FORKEYPATH, o, "multiple.level2.level3.keyA", "KeyAValue"
            )
            self.assertEqual(o.multiple.level2.level3.keyA, "KeyAValue")

            STUB.setKeyValue_forObject_key_value_(
                DO_SETVALUE_FORKEYPATH, o, "multiple.level2.level3.keyB", 9.999
            )
            self.assertEqual(o.multiple.level2.level3.keyB, 9.999)


class PyObjC_TestKeyValueSource(NSObject):
    def getFoobar(self):
        return "Hello world"


if PyObjCTest_KeyValueObserver is not None:

    class TestKeyValueObservingFromNative(TestCase):
        # This test makes uses of Key-Value Coding/Observing from Objective-C.
        # Versions of PyObjC upto 2003-12-29 crashed on this test due to the way
        # key-value observing is implemented in Cocoa.

        def testOne(self):
            o = PyObjCTest_KeyValueObserver.alloc().initWithInstanceOfClass_withKey_(
                PyObjC_TestKeyValueSource, "foobar"
            )
            self.assertEqual(o.getValue(), "Hello world")
            del o

    global DEALLOCS
    DEALLOCS = 0

    class PyObjCTestObserved1(NSObject):
        __slots__ = ("_kvo_bar", "_kvo_foo")

        FOOBASE = "base"

        def init(self):
            self = objc.super(PyObjCTestObserved1, self).init()
            if self is not None:
                self._kvo_bar = None
                self._kvo_foo = None
            return self

        def initiateDestructionSequence(self):
            # Exercise a bug between KVO and the old
            # initialization scheme.
            pass

        def setBar_(self, value):
            self.initiateDestructionSequence()
            self._kvo_bar = value

        setBar_ = objc.accessor(setBar_)

        def bar(self):
            self.initiateDestructionSequence()
            return self._kvo_bar

        bar = objc.accessor(bar)

        def setFoo_(self, value):
            self.initiateDestructionSequence()
            self._kvo_foo = self.FOOBASE + value

        setFoo_ = objc.accessor(setFoo_)

        def foo(self):
            self.initiateDestructionSequence()
            return self._kvo_foo

        foo = objc.accessor(foo)

        def __del__(self):
            global DEALLOCS
            DEALLOCS += 1

    class PyObjCTestObserved2(NSObject):
        bar = objc.ivar("bar")

        def init(self):
            self = objc.super(PyObjCTestObserved2, self).init()
            self.foo = None
            return self

        def __del__(self):
            global DEALLOCS
            DEALLOCS += 1

    class TestKeyValueObservingFromPython(TestCase):
        # Check for using KVO in python.

        def testAutomaticObserving(self):
            with objc.autorelease_pool():
                observer = PyObjCTestObserver.alloc().init()
                o = PyObjCTestObserved2.alloc().init()
                with objc.autorelease_pool():
                    self.assertEqual(o.foo, None)
                    self.assertEqual(o.bar, None)

                    o.foo = "foo"
                    self.assertEqual(o.foo, "foo")

                    o.bar = "bar"
                    self.assertEqual(o.bar, "bar")

                    o.addObserver_forKeyPath_options_context_(
                        observer,
                        "bar",
                        (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld),
                        0,
                    )
                    o.addObserver_forKeyPath_options_context_(
                        observer,
                        "foo",
                        (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld),
                        0,
                    )
                    try:
                        o.bar = "world"
                        self.assertEqual(o.bar, "world")

                        o.foo = "xxx"
                        self.assertEqual(o.foo, "xxx")
                    finally:
                        o.removeObserver_forKeyPath_(observer, "bar")
                        o.removeObserver_forKeyPath_(observer, "foo")
                    self.assertEqual(len(observer.observed), 2)

                    self.assertEqual(
                        observer.observed[0],
                        ("bar", o, {"kind": 1, "new": "world", "old": "bar"}, 0),
                    )
                    self.assertEqual(
                        observer.observed[1],
                        ("foo", o, {"kind": 1, "new": "xxx", "old": "foo"}, 0),
                    )

                    del observer

                before = DEALLOCS
                del o

            self.assertEqual(DEALLOCS, before + 1, "Leaking an observed object")

        def testObserving(self):
            outer_pool = NSAutoreleasePool.alloc().init()  # noqa: F841
            observer = PyObjCTestObserver.alloc().init()

            o = PyObjCTestObserved1.alloc().init()

            self.assertEqual(o.bar(), None)
            o.setBar_("hello")
            self.assertEqual(o.bar(), "hello")

            # See below
            PyObjCTestObserved1.FOOBASE = "base3"
            try:
                o.setFoo_("yyy")
                self.assertEqual(o.foo(), "base3yyy")
            finally:
                PyObjCTestObserved1.FOOBASE = "base"

            # XXX: To be debugged, when flags == 0 everything is fine,
            # otherwise we leak a reference
            o.addObserver_forKeyPath_options_context_(
                observer,
                "bar",
                (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld),
                0,
            )
            o.addObserver_forKeyPath_options_context_(
                observer,
                "foo",
                (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld),
                0,
            )

            try:
                o.setBar_("world")
                self.assertEqual(o.bar(), "world")

                o.setFoo_("xxx")
                self.assertEqual(o.foo(), "basexxx")

                # Change a "class" attribute, and make sure the object sees
                # that change (e.g. the fact that Cocoa changes the ISA pointer
                # should be mostly invisible)
                PyObjCTestObserved1.FOOBASE = "base2"

                o.setFoo_("yyy")
                self.assertEqual(o.foo(), "base2yyy")

            finally:
                o.removeObserver_forKeyPath_(observer, "bar")
                o.removeObserver_forKeyPath_(observer, "foo")
                PyObjCTestObserved1.FOOBASE = "base"

            self.assertEqual(len(observer.observed), 3)

            self.assertEqual(
                observer.observed[0],
                ("bar", o, {"kind": 1, "new": "world", "old": "hello"}, 0),
            )
            self.assertEqual(
                observer.observed[1],
                ("foo", o, {"kind": 1, "new": "basexxx", "old": "base3yyy"}, 0),
            )
            self.assertEqual(
                observer.observed[2],
                ("foo", o, {"kind": 1, "new": "base2yyy", "old": "basexxx"}, 0),
            )
            self.assertEqual(o.bar(), "world")

            del observer

            before = DEALLOCS
            del o
            del outer_pool
            self.assertEqual(DEALLOCS, before + 1, "Leaking an observed object")

        def testObserving2(self):
            observer = PyObjCTestObserver.alloc().init()

            o = PyObjCTestObserved1.alloc().init()

            o.addObserver_forKeyPath_options_context_(
                observer,
                "bar",
                (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld),
                0,
            )

            a = NSArray.arrayWithArray_([o])
            del o
            o = a[0]

            try:
                PyObjCTestObserved1.FOOBASE = "base2"

                o.setFoo_("yyy")
                self.assertEqual(o.foo(), "base2yyy")

            finally:
                o.removeObserver_forKeyPath_(observer, "bar")
                PyObjCTestObserved1.FOOBASE = "base"

            self.assertEqual(len(observer.observed), 0)

        @min_os_level("10.5")
        def testReceiveObserved(self):
            # Create an object in Objective-C, add an observer and then
            # pass the object to Python. Unless we take special care the
            # Python wrapper will have the wrong type (that of the
            # internal helper class).
            #
            # NOTE: This test is known to fail on OSX 10.5 due to the way
            # KVO is implemented there.

            observer = PyObjCTestObserver.alloc().init()
            o = STUB.makeObservedOfClass_observer_keyPath_(
                NSObject, observer, "observationInfo"
            )

            try:
                self.assertIsInstance(o, NSObject)
            finally:
                o.removeObserver_forKeyPath_(observer, "observationInfo")


class Helper:
    pass


class TestWithoutHelper(TestCase):
    def test_get_keypath(self):
        orig = objc.options._getKeyPath
        try:
            objc.options._getKeyPath = None

            value = Helper()
            value.key = 42

            a = NSArray.arrayWithArray_([value])
            with self.assertRaisesRegex(
                ValueError, "helper function for getKeyPath not set"
            ):
                a.valueForKeyPath_("@unionOfObjects.key")

        finally:
            objc.options._getKeyPath = orig

    def test_get_key(self):
        orig = objc.options._getKey
        try:
            objc.options._getKey = None

            value = Helper()
            value.key = 42

            a = NSArray.arrayWithArray_([value])
            with self.assertRaisesRegex(
                ValueError, "helper function for getKey not set"
            ):
                a.makeObjectsPerformSelector_withObject_(b"valueForKey:", "key")

        finally:
            objc.options._getKey = orig

    def test_set_key(self):
        orig = objc.options._setKey
        try:
            objc.options._setKey = None

            value = Helper()
            value.key = 42

            with self.assertRaisesRegex(
                ValueError, "helper function for setKey not set"
            ):
                OC_ObjectInt.setValue_forKey_of_("value", "key", value)

            self.assertEqual(value.key, 42)

        finally:
            objc.options._setKey = orig

    def test_set_keypath(self):
        orig = objc.options._setKeyPath
        try:
            objc.options._setKeyPath = None

            value = Helper()
            value.key = 42

            with self.assertRaisesRegex(
                ValueError, "helper function for setKeyPath not set"
            ):
                OC_ObjectInt.setValue_forKeyPath_of_("value", "key.path", value)

            objc.options._setKeyPath = 42
            with self.assertRaisesRegex(TypeError, "not callable"):
                OC_ObjectInt.setValue_forKeyPath_of_("value", "key.path", value)

            self.assertEqual(value.key, 42)

        finally:
            objc.options._setKeyPath = orig
