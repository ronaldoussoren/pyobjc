"""
Tests for the Key-Value Coding for hybrid python objects.

NOTE: Testcases here should be synchronized with the Key-Value Coding tests
in PyObjCTools.test.test_keyvalue and objc.test.test_keyvalue.

TODO:
    - This test uses C code, that code should be added to this package!
    - Tests that access properties in the parent Objective-C class!
    - More key-error tests, the tests don't cover all relevant code yet.
"""
import objc
import unittest
import sys
from objc.test.testbndl import PyObjC_TestClass3 as STUB
from Foundation import *

class KeyValueClass1 (NSObject):
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

    def key2(self):
        return 2

    def setKey4_(self, value):
        self._key4 = value * 4

    def setKey5_(self, value):
        self.key5 = value * 5

    def keyRaisingValueError(self):
        raise ValueError, "42"

    def keyRaisingNSUnknownKeyException(self):
        return self.valueForKey_("thisKeyDoesNotExist")

    def keyReturningSameSlector(self):
        return self.keyReturningSameSelector

    def keyReturningOtherSelector(self):
        return self.getKey1

class KeyValueClass1Explicit (NSObject):
    def init(self):
        self = super(KeyValueClass1Explicit, self).init()
        self._values = {}
        self._values[u'key3'] = 3
        self._values[u'key4'] = u"4"
        self._values['_private'] = u"private"
        return self

    def addMultiple(self):
        self._values["multiple"] = KeyValueClass1Explicit.alloc().init()
        self._values["multiple"]._values["level2"] = KeyValueClass1Explicit.alloc().init()
        self._values["multiple"]._values["level2"]._values["level3"] = KeyValueClass1Explicit.alloc().init()
        self._values["multiple"]._values["level2"]._values["level3"]._values["keyA"] = u"hello"
        self._values["multiple"]._values["level2"]._values["level3"]._values["keyB"] = u"world"

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

class KeyValueClass4 (NSObject):
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

class KVOClass(NSObject):
    def automaticallyNotifiesObserversForKey_(self, aKey):
        return objc.NO

    def test(self): return u"test"


class KeyValueObserver (NSObject):
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

        self.assertRaises(ValueError, STUB.keyValue_forObject_key_, 0, o,
                u"keyRaisingValueError")
        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o,
                u"keyRaisingNSUnknownKeyException")
        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o,
                u"keyReturningSameSelector")

        obj = STUB.keyValue_forObject_key_( 0, o, u"keyReturningOtherSelector")
        self.failUnless( isinstance(obj, objc.selector) )
        self.assertEquals(obj.selector, "getKey1")
        self.failUnless( obj.self is o )


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

    if hasattr(NSObject, u"willChangeValueForKey_"):
        # NSKeyValueObserving is only available on Panther and beyond
        def testKVO1(self):
            o = KVOClass.alloc().init()
            o.addObserver_forKeyPath_options_context_(self, u"test", 0, None)
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

class PyKeyValueCodingExplicit (unittest.TestCase):

    def testValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"key1"), 1)

        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"key2"), 2)
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"key3"), 3)
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"key4"), "4")
        self.assertEquals(STUB.keyValue_forObject_key_(0, o, u"multiple"), o._values['multiple'])

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o, u"nokey")

    def testStoredValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"key1"), 1)
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"key2"), 2)
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"key3"), 3)
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"key4"), "4")
        self.assertEquals(STUB.keyValue_forObject_key_(2, o, u"multiple"), o._values['multiple'])

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 2, o, u"nokey")

    def testValueForKeyPath(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(1, o, u"multiple"), o._values['multiple'])
        self.assertEquals(STUB.keyValue_forObject_key_(1, o, u"multiple.level2"), o._values['multiple']._values['level2'])
        self.assertEquals(STUB.keyValue_forObject_key_(1, o, u"multiple.level2.level3.keyA"),
            o._values['multiple']._values['level2']._values['level3']._values['keyA'])
        self.assertEquals(STUB.keyValue_forObject_key_(1, o, u"multiple.level2.level3.keyB"),
            o._values['multiple']._values['level2']._values['level3']._values['keyB'])

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 1, o, u"multiple.level2.nokey")

    def testValuesForKeys(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEquals(STUB.keyValue_forObject_key_(3, o, [u"key1", u"key2", u"key3", u"key4"]), { u"key1":1, u"key2":2, u"key3": 3, u"key4": u"4"} )

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 3, o, [u"key1", u"key3", u"nosuchkey"])

    def testTakeValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEquals(o._values['key3'], 3)
        STUB.setKeyValue_forObject_key_value_(0, o, u'key3', u'drie')
        self.assertEquals(o._values['key3'], u"drie")

        self.assertEquals(o._values['key4'], u"4")
        STUB.setKeyValue_forObject_key_value_(0, o, u'key4', u'vier')
        self.assert_(not hasattr(o, u"key4"))
        self.assertEquals(o._values['key4'], u"viervierviervier")

        o._values['key5'] = 1
        STUB.setKeyValue_forObject_key_value_(0, o, u'key5', u'V')
        self.assertEquals(o._values['key5'], u"VVVVV")

        self.assert_(not hasattr(o, u'key9'))
        self.assert_('key9' not in o._values)
        STUB.setKeyValue_forObject_key_value_(0, o, u'key9', u'IX')
        self.assert_(not hasattr(o, u'key9'))
        self.assert_('key9' in o._values)
        self.assertEquals(o._values['key9'], u'IX')

    def testTakeStoredValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEquals(o._values['key3'], 3)
        STUB.setKeyValue_forObject_key_value_(2, o, u'key3', u'drie')
        self.assertEquals(o._values['key3'], u"drie")

        self.assertEquals(o._values['key4'], u"4")
        STUB.setKeyValue_forObject_key_value_(2, o, u'key4', u'vier')
        self.assertEquals(o._values['key4'], u"viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(2, o, u'key5', u'V')
        self.assertEquals(o._values['key5'], u"VVVVV")

        self.assert_('key9' not in o._values)
        STUB.setKeyValue_forObject_key_value_(2, o, u'key9', u'IX')
        self.assert_('key9' in o._values)
        self.assertEquals(o._values['key9'], u'IX')

    def testTakeValuesFromDictionary(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEquals(o._values['key3'], 3)
        self.assertEquals(o._values['key4'], u"4")
        o._values['key5'] = 1
        self.assert_('key9' not in o._values)

        STUB.setKeyValue_forObject_key_value_(3, o, None,
            {
                u'key3': u'drie',
                u'key4': u'vier',
                u'key5': u'V',
                u'key9': u'IX',
            })

        self.assertEquals(o._values['key3'], u"drie")
        self.assertEquals(o._values['key4'], u"viervierviervier")
        self.assertEquals(o._values['key5'], u"VVVVV")
        self.assertEquals(o._values['key9'], u'IX')

    def testTakeValueForKeyPath(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEquals(o._values['multiple']._values['level2']._values['level3']._values['keyA'], u"hello")
        self.assertEquals(o._values['multiple']._values['level2']._values['level3']._values['keyB'], u"world")

        STUB.setKeyValue_forObject_key_value_(1, o, u"multiple.level2.level3.keyA", u"KeyAValue")
        self.assertEquals(o._values['multiple']._values['level2']._values['level3']._values['keyA'], u"KeyAValue")

        STUB.setKeyValue_forObject_key_value_(1, o, u"multiple.level2.level3.keyB", 9.999)
        self.assertEquals(o._values['multiple']._values['level2']._values['level3']._values['keyB'], 9.999)


class TestBaseExceptions (unittest.TestCase):
    """
    Check that NSObject implementation of Key-Value coding raises the
    exception that we expect it to raise.
    """
    def testValueForKey(self):
        o = NSObject.alloc().init()

        self.assertRaises(KeyError, o.valueForKey_, u"unknownKey")

    def testStoredValueForKey(self):
        o = NSObject.alloc().init()

        self.assertRaises(KeyError, o.storedValueForKey_, u"unknownKey")

    def testTakeStoredValue(self):
        o = NSObject.alloc().init()

        self.assertRaises(KeyError,
            o.takeStoredValue_forKey_, u"value", u"unknownKey")



if __name__ == "__main__":
    unittest.main()
