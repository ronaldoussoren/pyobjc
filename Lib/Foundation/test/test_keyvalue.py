"""
Tests for the Key-Value Coding for hybrid python objects.

NOTE: Testcases here should be synchronized with the Key-Value Coding tests
in PyObjCTools.test.test_keyvalue and objc.test.test_keyvalue.

TODO:
    - Tests that access properties in the parent Objective-C class!
    - More key-error tests, the tests don't cover all relevant code yet.
"""
import objc
import unittest
import sys
from objc.test.testbndl import PyObjC_TestClass3 as STUB
from Foundation import *

class KeyValueClass1 (objc.runtime.NSObject):
    def init(self):
        self = super(KeyValueClass1, self).init()
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

    def get_key2(self):
        return 2

    def setKey4(self, value):
        self._key4 = value * 4

    def set_key5(self, value):
        self.key5 = value * 5

class KeyValueClass4 (objc.runtime.NSObject):
    __slots__ = ('foo', )

    def init(self):
        self = super(KeyValueClass4, self).init()
        self.foo = "foobar"
        return self

    # Definition for property 'bar'. Use odd names for the methods
    # because the KeyValue support recognizes the usual names.
    def read_bar(self):
        return self.foo + self.foo

    def write_bar (self, value):
        self.foo = value + value

    bar = property(read_bar, write_bar)

    roprop = property(lambda self: "read-only")

class KVOClass(objc.runtime.NSObject):
    def automaticallyNotifiesObserversForKey_(self, aKey):
        return objc.NO

    def test(self): return "test"


class KeyValueObserver (objc.runtime.NSObject):
    def init(self):
        self.observed = []
        return self

    def observeValueForKeyPath_ofObject_change_context_(
            self, keyPath, object, change, context):
        self.observed.append( (keyPath, object, change) )


class PyKeyValueCoding (unittest.TestCase):
    def testNoPrivateVars(self):
        # Private instance variables ('anObject.__value') are not accessible using
        # key-value coding.
        o = KeyValueClass1.alloc().init()
        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o, "private")

    def testValueForKey(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(0, o, "key1"), 1)

        self.assertEquals(STUB.keyValue_forObject_key_(0, o, "key2"), 2)
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, "key3"), 3)
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, "key4"), "4")
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, "multiple"), o.multiple)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o, "nokey")

    def testValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEquals(STUB.keyValue_forObject_key_(0, o, "foo"), "foobar")
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, "bar"), "foobarfoobar")
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, "roprop"), "read-only")


    def testStoredValueForKey(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(2, o, "key1"), 1)
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, "key2"), 2)
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, "key3"), 3)
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, "key4"), "4")
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, "multiple"), o.multiple)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 2, o, "nokey")

    def testStoredValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEquals(STUB.keyValue_forObject_key_(2, o, "foo"), "foobar")
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, "bar"), "foobarfoobar")
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, "roprop"), "read-only")

    def testValueForKeyPath(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(1, o, "multiple"), o.multiple)
        self.assertEquals(STUB.keyValue_forObject_key_(1, o, "multiple.level2"), o.multiple.level2)
        self.assertEquals(STUB.keyValue_forObject_key_(1, o, "multiple.level2.level3.keyA"),
            o.multiple.level2.level3.keyA)
        self.assertEquals(STUB.keyValue_forObject_key_(1, o, "multiple.level2.level3.keyB"),
            o.multiple.level2.level3.keyB)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 1, o, "multiple.level2.nokey")

    def testValuesForKeys(self):
        o = KeyValueClass1.alloc().init()

        self.assertEquals(STUB.keyValue_forObject_key_(3, o, ["key1", "key2", "key3", "key4"]), { "key1":1, "key2":2, "key3": 3, "key4": "4"} )

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 3, o, ["key1", "key3", "nosuchkey"])

    def testTakeValueForKey(self):
        o = KeyValueClass1.alloc().init()

        self.assertEquals(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(0, o, 'key3', 'drie')
        self.assertEquals(o.key3, "drie")

        self.assertEquals(o._key4, "4")
        STUB.setKeyValue_forObject_key_value_(0, o, 'key4', 'vier')
        self.assert_(not hasattr(o, "key4"))
        self.assertEquals(o._key4, "viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(0, o, 'key5', 'V')
        self.assertEquals(o.key5, "VVVVV")

        self.assert_(not hasattr(o, 'key9'))
        STUB.setKeyValue_forObject_key_value_(0, o, 'key9', 'IX')
        self.assert_(hasattr(o, 'key9'))
        self.assertEquals(o.key9, 'IX')

    def testTakeValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEquals(o.foo, "foobar")
        STUB.setKeyValue_forObject_key_value_(0, o, 'foo', 'FOO')
        self.assertEquals(o.foo, "FOO")

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 0, o, 'key9', 'IX')


    def testTakeStoredValueForKey(self):
        o = KeyValueClass1.alloc().init()

        self.assertEquals(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(2, o, 'key3', 'drie')
        self.assertEquals(o.key3, "drie")

        self.assertEquals(o._key4, "4")
        STUB.setKeyValue_forObject_key_value_(2, o, 'key4', 'vier')
        self.assertEquals(o._key4, "viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(2, o, 'key5', 'V')
        self.assertEquals(o.key5, "VVVVV")

        self.assert_(not hasattr(o, 'key9'))
        STUB.setKeyValue_forObject_key_value_(2, o, 'key9', 'IX')
        self.assert_(hasattr(o, 'key9'))
        self.assertEquals(o.key9, 'IX')

    def testStoredTakeValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEquals(o.foo, "foobar")
        STUB.setKeyValue_forObject_key_value_(2, o, 'foo', 'FOO')
        self.assertEquals(o.foo, "FOO")

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 2, o, 'key9', 'IX')
        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 2, o, 'roprop', 'IX')

    def testTakeValuesFromDictionary(self):
        o = KeyValueClass1.alloc().init()

        self.assertEquals(o.key3, 3)
        self.assertEquals(o._key4, "4")
        o.key5 = 1
        self.assert_(not hasattr(o, 'key9'))

        STUB.setKeyValue_forObject_key_value_(3, o, None,
            {
                'key3': 'drie',
                'key4': 'vier',
                'key5': 'V',
                'key9': 'IX',
            })

        self.assertEquals(o.key3, "drie")
        self.assertEquals(o._key4, "viervierviervier")
        self.assertEquals(o.key5, "VVVVV")
        self.assert_(hasattr(o, 'key9'))
        self.assertEquals(o.key9, 'IX')

    def testTakeValuesFromDictionary2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEquals(o.foo, "foobar")
        STUB.setKeyValue_forObject_key_value_(3, o, None, { 'foo': 'FOO' })
        self.assertEquals(o.foo, "FOO")

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 3, o, None, { 'key9':  'IX' })
        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 3, o, None, { 'roprop':  'IX' })

    def testTakeValueForKeyPath(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEquals(o.multiple.level2.level3.keyA, "hello")
        self.assertEquals(o.multiple.level2.level3.keyB, "world")

        STUB.setKeyValue_forObject_key_value_(1, o, "multiple.level2.level3.keyA", "KeyAValue")
        self.assertEquals(o.multiple.level2.level3.keyA, "KeyAValue")

        STUB.setKeyValue_forObject_key_value_(1, o, "multiple.level2.level3.keyB", 9.999)
        self.assertEquals(o.multiple.level2.level3.keyB, 9.999)

    if hasattr(objc.runtime.NSObject, "willChangeValueForKey_"):
        # NSKeyValueObserving is only available on Panther and beyond
        def testKVO1(self):
            o = KVOClass.alloc().init()
            o.addObserver_forKeyPath_options_context_(self, "test", 0, 0)
            o.removeObserver_forKeyPath_(self, "test")

        def testKVO2(self):
            """
            Check if observations work for python-based keys on ObjC classes
            """
            observer = KeyValueObserver.alloc().init()
            self.assertEquals(observer.observed, [])

            o = KeyValueClass1.alloc().init()

            o.addObserver_forKeyPath_options_context_(observer, "key3", 0, 0)
            try:
                STUB.setKeyValue_forObject_key_value_(2, o, 'key3', 'drie')
                self.assertEquals(o.key3, "drie")

                self.assertEquals(len(observer.observed), 1)

                keyPath, object, change = observer.observed[0]
                self.assertEquals(keyPath, "key3")
                self.assert_(object is o)
                self.assertEquals(change, {NSKeyValueChangeKindKey: 1 })

            finally:
                o.removeObserver_forKeyPath_(observer, 'key3')

        def testKVO3(self):
            """
            Check if observations work for python-based keys on ObjC classes
            """
            observer = KeyValueObserver.alloc().init()
            self.assertEquals(observer.observed, [])

            o = KeyValueClass1.alloc().init()
            STUB.setKeyValue_forObject_key_value_(2, o, 'key3', 'three')

            o.addObserver_forKeyPath_options_context_(observer, "key3",
                    NSKeyValueObservingOptionNew|NSKeyValueObservingOptionOld,
                    0)
            try:
                STUB.setKeyValue_forObject_key_value_(2, o, 'key3', 'drie')
                self.assertEquals(o.key3, "drie")

                self.assertEquals(len(observer.observed), 1)

                keyPath, object, change = observer.observed[0]
                self.assertEquals(keyPath, "key3")
                self.assert_(object is o)
                self.assertEquals(change,
                    {
                        NSKeyValueChangeKindKey:1,
                        NSKeyValueChangeNewKey:'drie',
                        NSKeyValueChangeOldKey:'three'
                    })

            finally:
                o.removeObserver_forKeyPath_(observer, 'key3')

class TestBaseExceptions (unittest.TestCase):
    """
    Check that NSObject implementation of Key-Value coding raises the
    exception that we expect it to raise.
    """
    def testValueForKey(self):
        o = objc.runtime.NSObject.alloc().init()

        self.assertRaises(KeyError, o.valueForKey_, "unknownKey")

    def testStoredValueForKey(self):
        o = objc.runtime.NSObject.alloc().init()

        self.assertRaises(KeyError, o.storedValueForKey_, "unknownKey")

    def testTakeStoredValue(self):
        o = objc.runtime.NSObject.alloc().init()

        self.assertRaises(KeyError,
            o.takeStoredValue_forKey_, "value", "unknownKey")



if __name__ == "__main__":
    unittest.main()
