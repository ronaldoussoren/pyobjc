"""
Tests for the Key-Value Coding support in OC_PythonObject

NOTE: Testcases here should be synchronized with the Key-Value Coding tests
in PyObjCTools.test.test_keyvalue and Foundation.test.test_keyvalue.
"""
import objc
import objc.test
from objc.test.fnd import *


# Native code is needed to access the python class from Objective-C, otherwise
# the Key-Value support cannot be tested.
from objc.test.testbndl import PyObjC_TestClass3 as STUB
from objc.test.testbndl import PyObjCTest_KeyValueObserver
from objc.test.testbndl import *
from objc.test.keyvaluehelper import *

class KeyValueClass2 (object):
    def __init__(self):
        self.key3 = 3
        self._key4 = u"4"
        self._pythonConvention = u'BAD'
        self._pythonConventionValue = u'GOOD'
        self.__private = u'private'

    def addMultiple(self):
        self.multiple = KeyValueClass2()
        self.multiple.level2 = KeyValueClass2()
        self.multiple.level2.level3 = KeyValueClass2()
        self.multiple.level2.level3.keyA = u"hello"
        self.multiple.level2.level3.keyB = u"world"

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


class KeyValueClass3 (object):
    __slots__ = ('foo', )

    def __init__(self):
        self.foo = u"foobar"

    # Definition for property 'bar'. Use odd names for the methods
    # because the KeyValue support recognizes the usual names.
    def read_bar(self):
        return self.foo + self.foo

    def write_bar (self, value):
        self.foo = value + value

    bar = property(read_bar, write_bar)

    roprop = property(lambda self: u"read-only")

class PyKeyValueCoding (objc.test.TestCase):
    def testNoPrivateVars(self):
        # Private instance variables ('anObject.__value') are not accessible using
        # key-value coding.
        o = KeyValueClass2()
        self.assertRaises(KeyError,
                STUB.keyValue_forObject_key_, DO_VALUEFORKEY, o, u"private")

    def testValueForKey(self):
        o = KeyValueClass2()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, u"key1"), 1)
        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, u"key2"), 2)
        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, u"key3"), 3)
        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, u"key4"), u"4")
        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, u"multiple"), o.multiple)
        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, u"pythonConvention"), u'GOOD')

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, DO_VALUEFORKEY, o, u"nokey")

    def testValueForKey2(self):
        o = KeyValueClass3()

        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, u"foo"), u"foobar")
        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, u"bar"), u"foobarfoobar")
        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, u"roprop"), u"read-only")

    def testStoredValueForKey(self):
        o = KeyValueClass2()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, u"key1"), 1)
        self.assertEquals(STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, u"key2"), 2)
        self.assertEquals(STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, u"key3"), 3)
        self.assertEquals(STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, u"key4"), u"4")
        self.assertEquals(STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, u"multiple"), o.multiple)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, DO_STOREDVALUEFORKEY, o, u"nokey")

    def testStoredValueForKey2(self):
        o = KeyValueClass3()

        self.assertEquals(STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, u"foo"), u"foobar")
        self.assertEquals(STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, u"bar"), u"foobarfoobar")
        self.assertEquals(STUB.keyValue_forObject_key_(DO_STOREDVALUEFORKEY, o, u"roprop"), u"read-only")

    def testValueForKeyPath(self):
        o = KeyValueClass2()
        o.addMultiple()

        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, o, u"multiple"), o.multiple)
        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, o, u"multiple.level2"), o.multiple.level2)
        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, o, u"multiple.level2.level3.keyA"), o.multiple.level2.level3.keyA)
        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, o, u"multiple.level2.level3.keyB"), o.multiple.level2.level3.keyB)

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, DO_VALUEFORKEYPATH, o, u"multiple.level2.nokey")

    def testValuesForKeys(self):
        o = KeyValueClass2()

        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUESFORKEYS, o, [u"key1", u"key2", u"key3", u"key4"]), { u"key1":1, u"key2": 2, u"key3": 3, u"key4": u"4"} )

        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, DO_VALUESFORKEYS, o, [ u"key1", u"key2", u"nokey", u"key3" ])

    def testTakeValueForKey(self):
        o = KeyValueClass2()

        self.assertEquals(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEY, o, u'key3', u'drie')
        self.assertEquals(o.key3, u"drie")

        self.assertEquals(o._key4, u"4")
        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEY, o, u'key4', u'vier')
        self.assertEquals(o._key4, u"viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEY, o, u'key5', u'V')
        self.assertEquals(o.key5, u"VVVVV")

        self.assert_(not hasattr(o, u'key9'))
        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEY, o, u'key9', u'IX')
        self.assert_(hasattr(o, u'key9'))
        self.assertEquals(o.key9, u'IX')

    def testTakeValueForKey2(self):
        o = KeyValueClass3()

        self.assertEquals(o.foo, u"foobar")
        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEY, o, u'foo', u'FOO')
        self.assertEquals(o.foo, u"FOO")

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, DO_TAKEVALUE_FORKEY, o, u'key9', u'IX')

    def testTakeStoredValueForKey(self):
        o = KeyValueClass2()

        self.assertEquals(o.key3, 3)
        STUB.setKeyValue_forObject_key_value_(DO_TAKESTOREDVALUE_FORKEY, o, u'key3', u'drie')
        self.assertEquals(o.key3, u"drie")

        self.assertEquals(o._key4, u"4")
        STUB.setKeyValue_forObject_key_value_(DO_TAKESTOREDVALUE_FORKEY, o, u'key4', u'vier')
        self.assertEquals(o._key4, u"viervierviervier")

        o.key5 = 1
        STUB.setKeyValue_forObject_key_value_(DO_TAKESTOREDVALUE_FORKEY, o, u'key5', u'V')
        self.assertEquals(o.key5, u"VVVVV")

        self.assert_(not hasattr(o, u'key9'))
        STUB.setKeyValue_forObject_key_value_(DO_TAKESTOREDVALUE_FORKEY, o, u'key9', u'IX')
        self.assert_(hasattr(o, u'key9'))
        self.assertEquals(o.key9, u'IX')

    def testStoredTakeValueForKey2(self):
        o = KeyValueClass3()

        self.assertEquals(o.foo, u"foobar")
        STUB.setKeyValue_forObject_key_value_(DO_TAKESTOREDVALUE_FORKEY, o, u'foo', u'FOO')
        self.assertEquals(o.foo, u"FOO")

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, DO_TAKESTOREDVALUE_FORKEY, o, u'key9', u'IX')
        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, DO_TAKESTOREDVALUE_FORKEY, o, u'roprop', u'IX')

    def testTakeValuesFromDictionary(self):
        o = KeyValueClass2()

        self.assertEquals(o.key3, 3)
        self.assertEquals(o._key4, u"4")
        o.key5 = 1
        self.assert_(not hasattr(o, u'key9'))

        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUESFROMDICT, o, None,
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
        o = KeyValueClass3()

        self.assertEquals(o.foo, u"foobar")
        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUESFROMDICT, o, None, { u'foo': u'FOO' })
        self.assertEquals(o.foo, u"FOO")

        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, DO_TAKEVALUESFROMDICT, o, None, { u'key9':  u'IX' })
        self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, DO_TAKEVALUESFROMDICT, o, None, { u'roprop':  u'IX' })

    def testTakeValueForKeyPath(self):
        o = KeyValueClass2()
        o.addMultiple()

        self.assertEquals(o.multiple.level2.level3.keyA, u"hello")
        self.assertEquals(o.multiple.level2.level3.keyB, u"world")

        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEYPATH, o, u"multiple.level2.level3.keyA", u"KeyAValue")
        self.assertEquals(o.multiple.level2.level3.keyA, u"KeyAValue")

        STUB.setKeyValue_forObject_key_value_(DO_TAKEVALUE_FORKEYPATH, o, u"multiple.level2.level3.keyB", 9.999)
        self.assertEquals(o.multiple.level2.level3.keyB, 9.999)


class TestAccMethod (objc.test.TestCase):
    def testStrCap(self):
        class Foo:
            def callme(self):
                return u"FOO"

        # check the result for valueForKey: u"callme" on a Foo instance
        self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, Foo(), u"callme"), u"FOO")

    def testStr(self):
        # Strings are automaticly converted to NSStrings, and those don't have
        # a capitalize key.
        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, DO_VALUEFORKEY,
            u"hello", u"capitalize")
        self.assertRaises(KeyError, STUB.keyValue_forObject_key_, DO_VALUEFORKEY,
            u"hello", u"capitalize")


class AbstractKVCodingTest:
    def testBaseValueForKey(self):
        self.assertEquals(DirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, self.base, u"directString"))
        self.assertEquals(IndirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, self.base, u"indirectString"))
        self.assertEquals(DirectNumber,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, self.base, u"directNumber"))
        self.assertEquals(IndirectNumber,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, self.base, u"indirectNumber"))

    def testPathValueForKey(self):
        self.assertEquals(DirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"directHead.directString"))
        self.assertEquals(DirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"indirectHead.directString"))
        self.assertEquals(IndirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"directHead.indirectString"))
        self.assertEquals(IndirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"indirectHead.indirectString"))
        self.assertEquals(DirectNumber,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"directHead.directNumber"))
        self.assertEquals(DirectNumber,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"indirectHead.directNumber"))
        self.assertEquals(IndirectNumber,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"directHead.indirectNumber"))
        self.assertEquals(IndirectNumber,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"indirectHead.indirectNumber"))

class TestObjCKVCoding(AbstractKVCodingTest, objc.test.TestCase):
    def setUp(self):
        self.base = PyObjCTest_KVBaseClass.new()
        self.path = PyObjCTest_KVPathClass.new()

class TestPythonKVCoding(AbstractKVCodingTest, objc.test.TestCase):
    def setUp(self):
        self.base = KVPyBase()
        self.path = KVPyPath()

class TestPythonSubObjCContainerCoding(AbstractKVCodingTest, objc.test.TestCase):
    def setUp(self):
        self.base = KVPySubObjCBase.new()
        self.path = KVPySubObjCPath.new()

class TestPythonSubOverObjC(AbstractKVCodingTest, objc.test.TestCase):
    def setUp(self):
        self.base = KVPySubOverObjCBase.new()
        self.path = KVPySubOverObjCPath.new()

    def testOverValueKey(self):
        self.assertEquals(DirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, self.base, u"overDirectString"))
        self.assertEquals(IndirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEY, self.base, u"overIndirectString"))

    def testOverValueKeyPath(self):
        self.assertEquals(DirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"overDirectHead.directString"))
        self.assertEquals(DirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"overIndirectHead.directString"))
        self.assertEquals(IndirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"overDirectHead.indirectString"))
        self.assertEquals(IndirectString,
            STUB.keyValue_forObject_key_(DO_VALUEFORKEYPATH, self.path, u"overIndirectHead.indirectString"))



import sys, os
if sys.platform == "darwin" and os.uname()[2] >= '7.0.0':

    # MacOS X 10.3 and later use 'setValue:forKey: u' instead of
    # 'takeValue:forKey: u', test these as wel.

    class PyKeyValueCoding_10_3 (objc.test.TestCase):
        def testPythonConvention(self):
            o = KeyValueClass2()

            self.assertEquals(o._pythonConvention, u'BAD')
            self.assertEquals(o.pythonConvention(), u'GOOD')
            self.assertEquals(o._pythonConventionValue, u'GOOD')
            self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, u"pythonConvention"), u'GOOD')
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEY, o, u'pythonConvention', u'CHANGED')
            self.assertEquals(STUB.keyValue_forObject_key_(DO_VALUEFORKEY, o, u"pythonConvention"), u'CHANGED')
            self.assertEquals(o._pythonConvention, u'BAD')
            self.assertEquals(o.pythonConvention(), u'CHANGED')
            self.assertEquals(o._pythonConventionValue, u'CHANGED')


        def testSetValueForKey(self):
            o = KeyValueClass2()

            self.assertEquals(o.key3, 3)
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEY, o, u'key3', u'drie')
            self.assertEquals(o.key3, u"drie")

            self.assertEquals(o._key4, u"4")
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEY, o, u'key4', u'vier')
            self.assertEquals(o._key4, u"viervierviervier")

            o.key5 = 1
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEY, o, u'key5', u'V')
            self.assertEquals(o.key5, u"VVVVV")

            self.assert_(not hasattr(o, u'key9'))
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEY, o, u'key9', u'IX')
            self.assert_(hasattr(o, u'key9'))
            self.assertEquals(o.key9, u'IX')

        def testTakeValueForKey2(self):
            o = KeyValueClass3()

            self.assertEquals(o.foo, u"foobar")
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEY, o, u'foo', u'FOO')
            self.assertEquals(o.foo, u"FOO")

            self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, DO_SETVALUE_FORKEY, o, u'key9', u'IX')

        def testSetValuesForKeysFromDictionary(self):
            o = KeyValueClass2()

            self.assertEquals(o.key3, 3)
            self.assertEquals(o._key4, u"4")
            o.key5 = 1
            self.assert_(not hasattr(o, u'key9'))

            STUB.setKeyValue_forObject_key_value_(DO_SETVALUESFORKEYSFROMDICT, o, None,
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

        def testSetValuesForKeysFromDictionary2(self):
            o = KeyValueClass3()

            self.assertEquals(o.foo, u"foobar")
            STUB.setKeyValue_forObject_key_value_(DO_SETVALUESFORKEYSFROMDICT, o, None, { u'foo': u'FOO' })
            self.assertEquals(o.foo, u"FOO")

            self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, DO_SETVALUESFORKEYSFROMDICT, o, None, { u'key9': u'IX' })
            self.assertRaises(KeyError, STUB.setKeyValue_forObject_key_value_, DO_SETVALUESFORKEYSFROMDICT, o, None, { u'roprop': u'IX' })

        def testSetValueForKeyPath(self):
            o = KeyValueClass2()
            o.addMultiple()

            self.assertEquals(o.multiple.level2.level3.keyA, u"hello")
            self.assertEquals(o.multiple.level2.level3.keyB, u"world")

            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEYPATH, o, u"multiple.level2.level3.keyA", u"KeyAValue")
            self.assertEquals(o.multiple.level2.level3.keyA, u"KeyAValue")

            STUB.setKeyValue_forObject_key_value_(DO_SETVALUE_FORKEYPATH, o, u"multiple.level2.level3.keyB", 9.999)
            self.assertEquals(o.multiple.level2.level3.keyB, 9.999)


class PyObjC_TestKeyValueSource (NSObject):
    def getFoobar(self):
        return u"Hello world"

if PyObjCTest_KeyValueObserver is not None:
    class TestKeyValueObservingFromNative (objc.test.TestCase):
        # This test makes uses of Key-Value Coding/Observing from Objective-C.
        # Versions of PyObjC upto 2003-12-29 crashed on this test due to the way
        # key-value observing is implemented in Cocoa.

        def testOne(self):
            o = PyObjCTest_KeyValueObserver.alloc().initWithInstanceOfClass_withKey_(PyObjC_TestKeyValueSource, u"foobar")
            self.assertEquals(o.getValue(), u"Hello world")
            del o

    global DEALLOCS
    DEALLOCS = 0

    class PyObjCTestObserved1 (NSObject):
        __slots__ = ( '_kvo_bar', '_kvo_foo')

        FOOBASE = u"base"

        def init(self):
            self = super(PyObjCTestObserved1, self).init()
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
        bar = objc.ivar('bar')

        def init(self):
            self = super(PyObjCTestObserved2, self).init()
            self.foo = None
            return self

        def __del__(self):
            global DEALLOCS
            DEALLOCS += 1

    class TestKeyValueObservingFromPython (objc.test.TestCase):
        # Check for using KVO in python.

        def testAutomaticObserving(self):
            observer = PyObjCTestObserver.alloc().init()
            o = PyObjCTestObserved2.alloc().init()
            pool = NSAutoreleasePool.alloc().init()

            self.assertEquals(o.foo, None)
            self.assertEquals(o.bar, None)

            o.foo = u'foo'
            self.assertEquals(o.foo, u'foo')

            o.bar = u'bar'
            self.assertEquals(o.bar, u'bar')

            o.addObserver_forKeyPath_options_context_(observer, u'bar',
                (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld),
                0)
            o.addObserver_forKeyPath_options_context_(observer, u'foo',
                (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld),
                0)
            try:
                o.bar = u"world"
                self.assertEquals(o.bar, u"world")

                o.foo = u"xxx"
                self.assertEquals(o.foo, u"xxx")
            finally:
                o.removeObserver_forKeyPath_(observer, u"bar")
                o.removeObserver_forKeyPath_(observer, u"foo")

            self.assertEquals(len(observer.observed), 2)

            self.assertEquals(observer.observed[0],
                (u'bar', o,  { u'kind': 1, u'new': u'world', u'old': u'bar' }, 0))
            self.assertEquals(observer.observed[1],
                (u'foo', o, { u'kind': 1, u'new': u'xxx', u'old': u'foo' }, 0))

            del observer
            del pool

            before = DEALLOCS
            del o
            self.assertEquals(DEALLOCS, before+1, u"Leaking an observed object")

        def testObserving(self):
            observer = PyObjCTestObserver.alloc().init()

            o = PyObjCTestObserved1.alloc().init()

            self.assertEquals(o.bar(), None)
            o.setBar_(u"hello")
            self.assertEquals(o.bar(), u"hello")

            # See below
            PyObjCTestObserved1.FOOBASE = u"base3"
            try:
                o.setFoo_(u"yyy")
                self.assertEquals(o.foo(), u"base3yyy")
            finally:
                PyObjCTestObserved1.FOOBASE = u"base"


            # XXX: To be debugged, when flags == 0 everything is fine,
            # otherwise we leak a reference
            o.addObserver_forKeyPath_options_context_(observer, u'bar',
                (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld),
                0)
            o.addObserver_forKeyPath_options_context_(observer, u'foo',
                (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld),
                0)

            try:
                o.setBar_(u"world")
                self.assertEquals(o.bar(), u"world")

                o.setFoo_(u"xxx")
                self.assertEquals(o.foo(), u"basexxx")

                # Change a "class" attribute, and make sure the object sees
                # that change (e.g. the fact that Cocoa changes the ISA pointer
                # should be mostly invisible)
                PyObjCTestObserved1.FOOBASE = u"base2"

                o.setFoo_(u"yyy")
                self.assertEquals(o.foo(), u"base2yyy")

            finally:
                o.removeObserver_forKeyPath_(observer, u"bar")
                o.removeObserver_forKeyPath_(observer, u"foo")
                PyObjCTestObserved1.FOOBASE = u"base"

            self.assertEquals(len(observer.observed), 3)

            self.assertEquals(observer.observed[0],
                (u'bar', o,  { u'kind': 1, u'new': u'world', u'old': u'hello' }, 0))
            self.assertEquals(observer.observed[1],
                (u'foo', o, { u'kind': 1, u'new': u'basexxx', u'old': u'base3yyy' }, 0))
            self.assertEquals(observer.observed[2],
                (u'foo', o, { u'kind': 1, u'new': u'base2yyy', u'old': u'basexxx' }, 0))
            self.assertEquals(o.bar(), u"world")

            del observer

            before = DEALLOCS
            del o
            self.assertEquals(DEALLOCS, before+1, u"Leaking an observed object")

        def testObserving2(self):
            observer = PyObjCTestObserver.alloc().init()

            o = PyObjCTestObserved1.alloc().init()


            o.addObserver_forKeyPath_options_context_(observer, u'bar',
                (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld),
                0)

            a = NSArray.arrayWithArray_([o])
            del o
            o = a[0]

            try:
                PyObjCTestObserved1.FOOBASE = u"base2"

                o.setFoo_(u"yyy")
                self.assertEquals(o.foo(), u"base2yyy")

            finally:
                o.removeObserver_forKeyPath_(observer, u"bar")
                PyObjCTestObserved1.FOOBASE = u"base"

            self.assertEquals(len(observer.observed), 0)

        def testReceiveObserved(self):
            # Create an object in Objective-C, add an observer and then
            # pass the object to Python. Unless we take special care the
            # Python wrapper will have the wrong type (that of the
            # internal helper class).

            observer = PyObjCTestObserver.alloc().init()
            o = STUB.createObservedOfClass_observer_keyPath_(
                    NSObject, observer, u"observationInfo")

            try:
                self.assert_(isinstance(o, NSObject))
            finally:
                o.removeObserver_forKeyPath_(observer, u"observationInfo")



if __name__ == "__main__":
    objc.test.main()
