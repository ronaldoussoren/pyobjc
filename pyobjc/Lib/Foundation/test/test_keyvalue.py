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
        self._key4 = u"4"
        self.__private = u"private"
        return self

    def addMultiple(self):
        self.multiple = KeyValueClass1.alloc().init()
        self.multiple.level2 = KeyValueClass1.alloc().init()
        self.multiple.level2.level3 = KeyValueClass1.alloc().init()
        self.multiple.level2.level3.keyA = u"hello"
        self.multiple.level2.level3.keyB = u"world"

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
        self.foo = u"foobar"
        return self

    # Definition for property 'bar'. Use odd names for the methods
    # because the KeyValue support recognizes the usual names.
    def read_bar(self):
        return self.foo + self.foo

    def write_bar (self, value):
        self.foo = value + value

    bar = property(read_bar, write_bar)

    roprop = property(lambda self: u"read-only")

class KVOClass(objc.runtime.NSObject):
    def automaticallyNotifiesObserversForKey_(self, aKey):
        return objc.NO

    def test(self): return u"test"


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
        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o, u"private")

    def testValueForKey(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"key1"), 1)

        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"key2"), 2)
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"key3"), 3)
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"key4"), "4")
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"multiple"), o.multiple)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o, u"nokey")

    def testValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"foo"), u"foobar")
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"bar"), u"foobarfoobar")
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"roprop"), u"read-only")


    def testStoredValueForKey(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"key1"), 1)
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"key2"), 2)
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"key3"), 3)
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"key4"), "4")
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"multiple"), o.multiple)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 2, o, u"nokey")

    def testStoredValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"foo"), u"foobar")
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"bar"), u"foobarfoobar")
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"roprop"), u"read-only")

    def testValueForKeyPath(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(1, o, u"multiple"), o.multiple)
        self.assertEquals(STUB.keyValue_forObject_key_(1, o, u"multiple.level2"), o.multiple.level2)
        self.assertEquals(STUB.keyValue_forObject_key_(1, o, u"multiple.level2.level3.keyA"),
            o.multiple.level2.level3.keyA)
        self.assertEquals(STUB.keyValue_forObject_key_(1, o, u"multiple.level2.level3.keyB"),
            o.multiple.level2.level3.keyB)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 1, o, u"multiple.level2.nokey")

    def testValuesForKeys(self):
        o = KeyValueClass1.alloc().init()

        self.assertEquals(STUB.keyValue_forObject_key_(3, o, [u"key1", u"key2", u"key3", u"key4"]), { u"key1":1, u"key2":2, u"key3": 3, u"key4": u"4"} )

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 3, o, [u"key1", u"key3", u"nosuchkey"])

    def testTakeValueForKey(self):
        o = KeyValueClass1.alloc().init()

        self.assertEquals(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(0, o, u'key3', u'drie')
        self.assertEquals(o.key3, u"drie")

        self.assertEquals(o._key4, u"4")
        STUB.setKeyValue_forObject_key_value_(0, o, u'key4', u'vier')
        self.assert_(not hasattr(o, u"key4"))
        self.assertEquals(o._key4, u"viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(0, o, u'key5', u'V')
        self.assertEquals(o.key5, u"VVVVV")

        self.assert_(not hasattr(o, u'key9'))
        STUB.setKeyValue_forObject_key_value_(0, o, u'key9', u'IX')
        self.assert_(hasattr(o, u'key9'))
        self.assertEquals(o.key9, u'IX')

    def testTakeValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEquals(o.foo, u"foobar")
        STUB.setKeyValue_forObject_key_value_(0, o, u'foo', u'FOO')
        self.assertEquals(o.foo, u"FOO")

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 0, o, u'key9', u'IX')


    def testTakeStoredValueForKey(self):
        o = KeyValueClass1.alloc().init()

        self.assertEquals(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(2, o, u'key3', u'drie')
        self.assertEquals(o.key3, u"drie")

        self.assertEquals(o._key4, u"4")
        STUB.setKeyValue_forObject_key_value_(2, o, u'key4', u'vier')
        self.assertEquals(o._key4, u"viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(2, o, u'key5', u'V')
        self.assertEquals(o.key5, u"VVVVV")

        self.assert_(not hasattr(o, u'key9'))
        STUB.setKeyValue_forObject_key_value_(2, o, u'key9', u'IX')
        self.assert_(hasattr(o, u'key9'))
        self.assertEquals(o.key9, u'IX')

    def testStoredTakeValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEquals(o.foo, u"foobar")
        STUB.setKeyValue_forObject_key_value_(2, o, u'foo', u'FOO')
        self.assertEquals(o.foo, u"FOO")

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 2, o, u'key9', u'IX')
        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 2, o, u'roprop', u'IX')

    def testTakeValuesFromDictionary(self):
        o = KeyValueClass1.alloc().init()

        self.assertEquals(o.key3, 3)
        self.assertEquals(o._key4, u"4")
        o.key5 = 1
        self.assert_(not hasattr(o, u'key9'))

        STUB.setKeyValue_forObject_key_value_(3, o, None,
            {
                u'key3': u'drie',
                u'key4': u'vier',
                u'key5': u'V',
                u'key9': u'IX',
            })

        self.assertEquals(o.key3, u"drie")
        self.assertEquals(o._key4, u"viervierviervier")
        self.assertEquals(o.key5, u"VVVVV")
        self.assert_(hasattr(o, u'key9'))
        self.assertEquals(o.key9, u'IX')

    def testTakeValuesFromDictionary2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEquals(o.foo, u"foobar")
        STUB.setKeyValue_forObject_key_value_(3, o, None, { u'foo': u'FOO' })
        self.assertEquals(o.foo, u"FOO")

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 3, o, None, { u'key9':  u'IX' })
        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 3, o, None, { u'roprop':  u'IX' })

    def testTakeValueForKeyPath(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEquals(o.multiple.level2.level3.keyA, u"hello")
        self.assertEquals(o.multiple.level2.level3.keyB, u"world")

        STUB.setKeyValue_forObject_key_value_(1, o, u"multiple.level2.level3.keyA", u"KeyAValue")
        self.assertEquals(o.multiple.level2.level3.keyA, u"KeyAValue")

        STUB.setKeyValue_forObject_key_value_(1, o, u"multiple.level2.level3.keyB", 9.999)
        self.assertEquals(o.multiple.level2.level3.keyB, 9.999)

    if hasattr(objc.runtime.NSObject, u"willChangeValueForKey_"):
        # NSKeyValueObserving is only available on Panther and beyond
        def testKVO1(self):
            o = KVOClass.alloc().init()
            o.addObserver_forKeyPath_options_context_(self, u"test", 0, 0)
            o.removeObserver_forKeyPath_(self, u"test")

        def testKVO2(self):
            """
            Check if observations work for python-based keys on ObjC classes
            """
            observer = KeyValueObserver.alloc().init()
            self.assertEquals(observer.observed, [])

            o = KeyValueClass1.alloc().init()

            o.addObserver_forKeyPath_options_context_(observer, u"key3", 0, 0)
            try:
                STUB.setKeyValue_forObject_key_value_(2, o, u'key3', u'drie')
                self.assertEquals(o.key3, u"drie")

                self.assertEquals(len(observer.observed), 1)

                keyPath, object, change = observer.observed[0]
                self.assertEquals(keyPath, u"key3")
                self.assert_(object is o)
                self.assertEquals(change, {NSKeyValueChangeKindKey: 1 })

            finally:
                o.removeObserver_forKeyPath_(observer, u'key3')

        def testKVO3(self):
            """
            Check if observations work for python-based keys on ObjC classes
            """
            observer = KeyValueObserver.alloc().init()
            self.assertEquals(observer.observed, [])

            o = KeyValueClass1.alloc().init()
            STUB.setKeyValue_forObject_key_value_(2, o, u'key3', u'three')

            o.addObserver_forKeyPath_options_context_(observer, u"key3",
                    NSKeyValueObservingOptionNew|NSKeyValueObservingOptionOld,
                    0)
            try:
                STUB.setKeyValue_forObject_key_value_(2, o, u'key3', u'drie')
                self.assertEquals(o.key3, u"drie")

                self.assertEquals(len(observer.observed), 1)

                keyPath, object, change = observer.observed[0]
                self.assertEquals(keyPath, u"key3")
                self.assert_(object is o)
                self.assertEquals(change,
                    {
                        NSKeyValueChangeKindKey:1,
                        NSKeyValueChangeNewKey:u'drie',
                        NSKeyValueChangeOldKey:u'three'
                    })

            finally:
                o.removeObserver_forKeyPath_(observer, u'key3')

class TestBaseExceptions (unittest.TestCase):
    """
    Check that NSObject implementation of Key-Value coding raises the
    exception that we expect it to raise.
    """
    def testValueForKey(self):
        o = objc.runtime.NSObject.alloc().init()

        self.assertRaises(KeyError, o.valueForKey_, u"unknownKey")

    def testStoredValueForKey(self):
        o = objc.runtime.NSObject.alloc().init()

        self.assertRaises(KeyError, o.storedValueForKey_, u"unknownKey")

    def testTakeStoredValue(self):
        o = objc.runtime.NSObject.alloc().init()

        self.assertRaises(KeyError,
            o.takeStoredValue_forKey_, u"value", u"unknownKey")



if __name__ == "__main__":
    unittest.main()
