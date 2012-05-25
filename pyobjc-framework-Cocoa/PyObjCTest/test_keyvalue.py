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
from PyObjCTools.TestSupport import *
import sys
from PyObjCTest.testhelper import PyObjC_TestClass3 as STUB
from Foundation import *

class KeyValueClass1 (NSObject):
    def init(self):
        self = super(KeyValueClass1, self).init()
        self.key3 = 3
        self._key4 = b"4".decode('ascii')
        self.__private = b"private".decode('ascii')
        return self

    def addMultiple(self):
        self.multiple = KeyValueClass1.alloc().init()
        self.multiple.level2 = KeyValueClass1.alloc().init()
        self.multiple.level2.level3 = KeyValueClass1.alloc().init()
        self.multiple.level2.level3.keyA = b"hello".decode('ascii')
        self.multiple.level2.level3.keyB = b"world".decode('ascii')

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

class KeyValueClass1Explicit (NSObject):
    def init(self):
        self = super(KeyValueClass1Explicit, self).init()
        self._values = {}
        self._values[b'key3'.decode('ascii')] = 3
        self._values[b'key4'.decode('ascii')] = b"4".decode('ascii')
        self._values['_private'] = b"private".decode('ascii')
        return self

    def addMultiple(self):
        self._values["multiple"] = KeyValueClass1Explicit.alloc().init()
        self._values["multiple"]._values["level2"] = KeyValueClass1Explicit.alloc().init()
        self._values["multiple"]._values["level2"]._values["level3"] = KeyValueClass1Explicit.alloc().init()
        self._values["multiple"]._values["level2"]._values["level3"]._values["keyA"] = b"hello".decode('ascii')
        self._values["multiple"]._values["level2"]._values["level3"]._values["keyB"] = b"world".decode('ascii')

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
        self.foo = b"foobar".decode('ascii')
        return self

    # Definition for property 'bar'. Use odd names for the methods
    # because the KeyValue support recognizes the usual names.
    def read_bar(self):
        return self.foo + self.foo

    def write_bar (self, value):
        self.foo = value + value

    bar = property(read_bar, write_bar)

    roprop = property(lambda self: b"read-only".decode('ascii'))

class KVOClass(NSObject):
    def automaticallyNotifiesObserversForKey_(self, aKey):
        return objc.NO

    def test(self): return b"test".decode('ascii')


class KeyValueObserver (NSObject):
    def init(self):
        self.observed = []
        return self

    def observeValueForKeyPath_ofObject_change_context_(
            self, keyPath, object, change, context):
        self.observed.append( (keyPath, object, change) )


class PyKeyValueCoding (TestCase):
    def testNoPrivateVars(self):
        # Private instance variables ('anObject.__value') are not accessible using
        # key-value coding.
        o = KeyValueClass1.alloc().init()
        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o, b"private".decode('ascii'))

    def testValueForKey(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"key1".decode('ascii')), 1)

        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"key2".decode('ascii')), 2)
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"key3".decode('ascii')), 3)
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"key4".decode('ascii')), "4")
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"multiple".decode('ascii')), o.multiple)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o, b"nokey".decode('ascii'))

        self.assertRaises(ValueError, STUB.keyValue_forObject_key_, 0, o,
                b"keyRaisingValueError".decode('ascii'))
        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o,
                b"keyRaisingNSUnknownKeyException".decode('ascii'))
        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o,
                b"keyReturningSameSelector".decode('ascii'))

        obj = STUB.keyValue_forObject_key_( 0, o, b"keyReturningOtherSelector".decode('ascii'))
        self.assertIsInstance(obj, objc.selector)
        self.assertEqual(obj.selector, b"getKey1")
        self.assertIs(obj.self, o )
    def testValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"foo".decode('ascii')), b"foobar".decode('ascii'))
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"bar".decode('ascii')), b"foobarfoobar".decode('ascii'))
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"roprop".decode('ascii')), b"read-only".decode('ascii'))


    def testStoredValueForKey(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"key1".decode('ascii')), 1)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"key2".decode('ascii')), 2)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"key3".decode('ascii')), 3)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"key4".decode('ascii')), "4")
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"multiple".decode('ascii')), o.multiple)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 2, o, b"nokey".decode('ascii'))

    def testStoredValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"foo".decode('ascii')), b"foobar".decode('ascii'))
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"bar".decode('ascii')), b"foobarfoobar".decode('ascii'))
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"roprop".decode('ascii')), b"read-only".decode('ascii'))

    def testValueForKeyPath(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(1, o, b"multiple".decode('ascii')), o.multiple)
        self.assertEqual(STUB.keyValue_forObject_key_(1, o, b"multiple.level2".decode('ascii')), o.multiple.level2)
        self.assertEqual(STUB.keyValue_forObject_key_(1, o, b"multiple.level2.level3.keyA".decode('ascii')),
            o.multiple.level2.level3.keyA)
        self.assertEqual(STUB.keyValue_forObject_key_(1, o, b"multiple.level2.level3.keyB".decode('ascii')),
            o.multiple.level2.level3.keyB)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 1, o, b"multiple.level2.nokey".decode('ascii'))

    @max_os_level('10.5')
    def testValuesForKeys(self):
        o = KeyValueClass1.alloc().init()

        self.assertEqual(STUB.keyValue_forObject_key_(3, o, [b"key1".decode('ascii'), b"key2".decode('ascii'), b"key3".decode('ascii'), b"key4".decode('ascii')]), { b"key1".decode('ascii'):1, b"key2".decode('ascii'):2, b"key3".decode('ascii'): 3, b"key4".decode('ascii'): b"4".decode('ascii')} )

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 3, o, [b"key1".decode('ascii'), b"key3".decode('ascii'), b"nosuchkey".decode('ascii')])

    @max_os_level('10.5')
    def testTakeValueForKey(self):
        o = KeyValueClass1.alloc().init()

        self.assertEqual(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(0, o, b'key3'.decode('ascii'), b'drie'.decode('ascii'))
        self.assertEqual(o.key3, b"drie".decode('ascii'))

        self.assertEqual(o._key4, b"4".decode('ascii'))
        STUB.setKeyValue_forObject_key_value_(0, o, b'key4'.decode('ascii'), b'vier'.decode('ascii'))
        self.assert_(not hasattr(o, b"key4".decode('ascii')))
        self.assertEqual(o._key4, b"viervierviervier".decode('ascii'))

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(0, o, b'key5'.decode('ascii'), b'V'.decode('ascii'))
        self.assertEqual(o.key5, b"VVVVV".decode('ascii'))

        self.assert_(not hasattr(o, b'key9'.decode('ascii')))
        STUB.setKeyValue_forObject_key_value_(0, o, b'key9'.decode('ascii'), b'IX'.decode('ascii'))
        self.assert_(hasattr(o, b'key9'.decode('ascii')))
        self.assertEqual(o.key9, b'IX'.decode('ascii'))

    @max_os_level('10.5')
    def testTakeValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEqual(o.foo, b"foobar".decode('ascii'))
        STUB.setKeyValue_forObject_key_value_(0, o, b'foo'.decode('ascii'), b'FOO'.decode('ascii'))
        self.assertEqual(o.foo, b"FOO".decode('ascii'))

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 0, o, b'key9'.decode('ascii'), b'IX'.decode('ascii'))


    def testTakeStoredValueForKey(self):
        o = KeyValueClass1.alloc().init()

        self.assertEqual(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(2, o, b'key3'.decode('ascii'), b'drie'.decode('ascii'))
        self.assertEqual(o.key3, b"drie".decode('ascii'))

        self.assertEqual(o._key4, b"4".decode('ascii'))
        STUB.setKeyValue_forObject_key_value_(2, o, b'key4'.decode('ascii'), b'vier'.decode('ascii'))
        self.assertEqual(o._key4, b"viervierviervier".decode('ascii'))

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(2, o, b'key5'.decode('ascii'), b'V'.decode('ascii'))
        self.assertEqual(o.key5, b"VVVVV".decode('ascii'))

        self.assert_(not hasattr(o, b'key9'.decode('ascii')))
        STUB.setKeyValue_forObject_key_value_(2, o, b'key9'.decode('ascii'), b'IX'.decode('ascii'))
        self.assert_(hasattr(o, b'key9'.decode('ascii')))
        self.assertEqual(o.key9, b'IX'.decode('ascii'))

    def testStoredTakeValueForKey2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEqual(o.foo, b"foobar".decode('ascii'))
        STUB.setKeyValue_forObject_key_value_(2, o, b'foo'.decode('ascii'), b'FOO'.decode('ascii'))
        self.assertEqual(o.foo, b"FOO".decode('ascii'))

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 2, o, b'key9'.decode('ascii'), b'IX'.decode('ascii'))
        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 2, o, b'roprop'.decode('ascii'), b'IX'.decode('ascii'))

    @max_os_level('10.5')
    def testTakeValuesFromDictionary(self):
        o = KeyValueClass1.alloc().init()

        self.assertEqual(o.key3, 3)
        self.assertEqual(o._key4, b"4".decode('ascii'))
        o.key5 = 1
        self.assert_(not hasattr(o, b'key9'.decode('ascii')))

        STUB.setKeyValue_forObject_key_value_(3, o, None,
            {
                b'key3'.decode('ascii'): b'drie'.decode('ascii'),
                b'key4'.decode('ascii'): b'vier'.decode('ascii'),
                b'key5'.decode('ascii'): b'V'.decode('ascii'),
                b'key9'.decode('ascii'): b'IX'.decode('ascii'),
            })

        self.assertEqual(o.key3, b"drie".decode('ascii'))
        self.assertEqual(o._key4, b"viervierviervier".decode('ascii'))
        self.assertEqual(o.key5, b"VVVVV".decode('ascii'))
        self.assert_(hasattr(o, b'key9'.decode('ascii')))
        self.assertEqual(o.key9, b'IX'.decode('ascii'))

    @max_os_level('10.5')
    def testTakeValuesFromDictionary2(self):
        o = KeyValueClass4.alloc().init()

        self.assertEqual(o.foo, b"foobar".decode('ascii'))
        STUB.setKeyValue_forObject_key_value_(3, o, None, { b'foo'.decode('ascii'): b'FOO'.decode('ascii') })
        self.assertEqual(o.foo, b"FOO".decode('ascii'))

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 3, o, None, { b'key9'.decode('ascii'):  b'IX'.decode('ascii') })
        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, 3, o, None, { b'roprop'.decode('ascii'):  b'IX'.decode('ascii') })

    @max_os_level('10.5')
    def testTakeValueForKeyPath(self):
        o = KeyValueClass1.alloc().init()
        o.addMultiple()

        self.assertEqual(o.multiple.level2.level3.keyA, b"hello".decode('ascii'))
        self.assertEqual(o.multiple.level2.level3.keyB, b"world".decode('ascii'))

        STUB.setKeyValue_forObject_key_value_(1, o, b"multiple.level2.level3.keyA".decode('ascii'), b"KeyAValue".decode('ascii'))
        self.assertEqual(o.multiple.level2.level3.keyA, b"KeyAValue".decode('ascii'))

        STUB.setKeyValue_forObject_key_value_(1, o, b"multiple.level2.level3.keyB".decode('ascii'), 9.999)
        self.assertEqual(o.multiple.level2.level3.keyB, 9.999)

    if hasattr(NSObject, b"willChangeValueForKey_".decode('ascii')):
        # NSKeyValueObserving is only available on Panther and beyond
        def testKVO1(self):
            o = KVOClass.alloc().init()
            o.addObserver_forKeyPath_options_context_(self, b"test".decode('ascii'), 0, None)
            o.removeObserver_forKeyPath_(self, b"test".decode('ascii'))

        def testKVO2(self):
            """
            Check if observations work for python-based keys on ObjC classes
            """
            observer = KeyValueObserver.alloc().init()
            self.assertEqual(observer.observed, [])

            o = KeyValueClass1.alloc().init()

            o.addObserver_forKeyPath_options_context_(observer, b"key3".decode('ascii'), 0, 0)
            try:
                STUB.setKeyValue_forObject_key_value_(2, o, b'key3'.decode('ascii'), b'drie'.decode('ascii'))
                self.assertEqual(o.key3, b"drie".decode('ascii'))

                self.assertEqual(len(observer.observed), 1)

                keyPath, object, change = observer.observed[0]
                self.assertEqual(keyPath, b"key3".decode('ascii'))
                self.assert_(object is o)
                self.assertEqual(change, {NSKeyValueChangeKindKey: 1 })

            finally:
                o.removeObserver_forKeyPath_(observer, b'key3'.decode('ascii'))

        def testKVO3(self):
            """
            Check if observations work for python-based keys on ObjC classes
            """
            observer = KeyValueObserver.alloc().init()
            self.assertEqual(observer.observed, [])

            o = KeyValueClass1.alloc().init()
            STUB.setKeyValue_forObject_key_value_(2, o, b'key3'.decode('ascii'), b'three'.decode('ascii'))

            o.addObserver_forKeyPath_options_context_(observer, b"key3".decode('ascii'),
                    NSKeyValueObservingOptionNew|NSKeyValueObservingOptionOld,
                    0)
            try:
                STUB.setKeyValue_forObject_key_value_(2, o, b'key3'.decode('ascii'), b'drie'.decode('ascii'))
                self.assertEqual(o.key3, b"drie".decode('ascii'))

                self.assertEqual(len(observer.observed), 1)

                keyPath, object, change = observer.observed[0]
                self.assertEqual(keyPath, b"key3".decode('ascii'))
                self.assert_(object is o)
                self.assertEqual(change,
                    {
                        NSKeyValueChangeKindKey:1,
                        NSKeyValueChangeNewKey:b'drie'.decode('ascii'),
                        NSKeyValueChangeOldKey:b'three'.decode('ascii')
                    })

            finally:
                o.removeObserver_forKeyPath_(observer, b'key3'.decode('ascii'))

class PyKeyValueCodingExplicit (TestCase):

    def testValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"key1".decode('ascii')), 1)

        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"key2".decode('ascii')), 2)
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"key3".decode('ascii')), 3)
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"key4".decode('ascii')), "4")
        self.assertEqual(STUB.keyValue_forObject_key_(0, o, b"multiple".decode('ascii')), o._values['multiple'])

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 0, o, b"nokey".decode('ascii'))

    def testStoredValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"key1".decode('ascii')), 1)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"key2".decode('ascii')), 2)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"key3".decode('ascii')), 3)
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"key4".decode('ascii')), "4")
        self.assertEqual(STUB.keyValue_forObject_key_(2, o, b"multiple".decode('ascii')), o._values['multiple'])

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 2, o, b"nokey".decode('ascii'))

    def testValueForKeyPath(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEqual(STUB.keyValue_forObject_key_(1, o, b"multiple".decode('ascii')), o._values['multiple'])
        self.assertEqual(STUB.keyValue_forObject_key_(1, o, b"multiple.level2".decode('ascii')), o._values['multiple']._values['level2'])
        self.assertEqual(STUB.keyValue_forObject_key_(1, o, b"multiple.level2.level3.keyA".decode('ascii')),
            o._values['multiple']._values['level2']._values['level3']._values['keyA'])
        self.assertEqual(STUB.keyValue_forObject_key_(1, o, b"multiple.level2.level3.keyB".decode('ascii')),
            o._values['multiple']._values['level2']._values['level3']._values['keyB'])

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 1, o, b"multiple.level2.nokey".decode('ascii'))

    @max_os_level('10.5')
    def testValuesForKeys(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEqual(STUB.keyValue_forObject_key_(3, o, [b"key1".decode('ascii'), b"key2".decode('ascii'), b"key3".decode('ascii'), b"key4".decode('ascii')]), { b"key1".decode('ascii'):1, b"key2".decode('ascii'):2, b"key3".decode('ascii'): 3, b"key4".decode('ascii'): b"4".decode('ascii')} )

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, 3, o, [b"key1".decode('ascii'), b"key3".decode('ascii'), b"nosuchkey".decode('ascii')])

    def testTakeValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEqual(o._values['key3'], 3)
        STUB.setKeyValue_forObject_key_value_(0, o, b'key3'.decode('ascii'), b'drie'.decode('ascii'))
        self.assertEqual(o._values['key3'], b"drie".decode('ascii'))

        self.assertEqual(o._values['key4'], b"4".decode('ascii'))
        STUB.setKeyValue_forObject_key_value_(0, o, b'key4'.decode('ascii'), b'vier'.decode('ascii'))
        self.assert_(not hasattr(o, b"key4".decode('ascii')))
        self.assertEqual(o._values['key4'], b"viervierviervier".decode('ascii'))

        o._values['key5'] = 1
        STUB.setKeyValue_forObject_key_value_(0, o, b'key5'.decode('ascii'), b'V'.decode('ascii'))
        self.assertEqual(o._values['key5'], b"VVVVV".decode('ascii'))

        self.assert_(not hasattr(o, b'key9'.decode('ascii')))
        self.assert_('key9' not in o._values)
        STUB.setKeyValue_forObject_key_value_(0, o, b'key9'.decode('ascii'), b'IX'.decode('ascii'))
        self.assert_(not hasattr(o, b'key9'.decode('ascii')))
        self.assert_('key9' in o._values)
        self.assertEqual(o._values['key9'], b'IX'.decode('ascii'))

    def testTakeStoredValueForKey(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEqual(o._values['key3'], 3)
        STUB.setKeyValue_forObject_key_value_(2, o, b'key3'.decode('ascii'), b'drie'.decode('ascii'))
        self.assertEqual(o._values['key3'], b"drie".decode('ascii'))

        self.assertEqual(o._values['key4'], b"4".decode('ascii'))
        STUB.setKeyValue_forObject_key_value_(2, o, b'key4'.decode('ascii'), b'vier'.decode('ascii'))
        self.assertEqual(o._values['key4'], b"viervierviervier".decode('ascii'))

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(2, o, b'key5'.decode('ascii'), b'V'.decode('ascii'))
        self.assertEqual(o._values['key5'], b"VVVVV".decode('ascii'))

        self.assert_('key9' not in o._values)
        STUB.setKeyValue_forObject_key_value_(2, o, b'key9'.decode('ascii'), b'IX'.decode('ascii'))
        self.assert_('key9' in o._values)
        self.assertEqual(o._values['key9'], b'IX'.decode('ascii'))

    @max_os_level('10.5')
    def testTakeValuesFromDictionary(self):
        o = KeyValueClass1Explicit.alloc().init()

        self.assertEqual(o._values['key3'], 3)
        self.assertEqual(o._values['key4'], b"4".decode('ascii'))
        o._values['key5'] = 1
        self.assert_('key9' not in o._values)

        STUB.setKeyValue_forObject_key_value_(3, o, None,
            {
                b'key3'.decode('ascii'): b'drie'.decode('ascii'),
                b'key4'.decode('ascii'): b'vier'.decode('ascii'),
                b'key5'.decode('ascii'): b'V'.decode('ascii'),
                b'key9'.decode('ascii'): b'IX'.decode('ascii'),
            })

        self.assertEqual(o._values['key3'], b"drie".decode('ascii'))
        self.assertEqual(o._values['key4'], b"viervierviervier".decode('ascii'))
        self.assertEqual(o._values['key5'], b"VVVVV".decode('ascii'))
        self.assertEqual(o._values['key9'], b'IX'.decode('ascii'))

    @max_os_level('10.5')
    def testTakeValueForKeyPath(self):
        o = KeyValueClass1Explicit.alloc().init()
        o.addMultiple()

        self.assertEqual(o._values['multiple']._values['level2']._values['level3']._values['keyA'], b"hello".decode('ascii'))
        self.assertEqual(o._values['multiple']._values['level2']._values['level3']._values['keyB'], b"world".decode('ascii'))

        STUB.setKeyValue_forObject_key_value_(1, o, b"multiple.level2.level3.keyA".decode('ascii'), b"KeyAValue".decode('ascii'))
        self.assertEqual(o._values['multiple']._values['level2']._values['level3']._values['keyA'], b"KeyAValue".decode('ascii'))

        STUB.setKeyValue_forObject_key_value_(1, o, b"multiple.level2.level3.keyB".decode('ascii'), 9.999)
        self.assertEqual(o._values['multiple']._values['level2']._values['level3']._values['keyB'], 9.999)


class TestBaseExceptions (TestCase):
    """
    Check that NSObject implementation of Key-Value coding raises the
    exception that we expect it to raise.
    """
    def testValueForKey(self):
        o = NSObject.alloc().init()

        self.assertRaises(KeyError, o.valueForKey_, b"unknownKey".decode('ascii'))

    def testStoredValueForKey(self):
        o = NSObject.alloc().init()

        self.assertRaises(KeyError, o.storedValueForKey_, b"unknownKey".decode('ascii'))

    def testTakeStoredValue(self):
        o = NSObject.alloc().init()

        self.assertRaises(KeyError,
            o.takeStoredValue_forKey_, b"value".decode('ascii'), b"unknownKey".decode('ascii'))



if __name__ == "__main__":
    main()
