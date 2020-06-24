import operator
import sys

import objc
import objc._convenience as convenience
from PyObjCTest.sequence import OC_TestSequence, OC_TestMutableSequence
from PyObjCTools.TestSupport import TestCase

objc.addConvenienceForBasicSequence("OC_TestSequence", False)
objc.addConvenienceForBasicSequence("OC_TestMutableSequence", True)


class OC_WithHash(objc.lookUpClass("NSObject")):
    def initWithHash_(self, value):
        self = objc.super(OC_WithHash, self).init()
        if self is None:
            return None

        self._hash = value
        return self

    def hash(self):  # noqa: A003
        return self._hash

    def someKey(self):
        objc.lookUpClass("NSException").alloc().initWithName_reason_userInfo_(
            "NSRangeException", "Test exception", {}
        ).raise__()
        return 1

    def someOtherKey(self):
        raise KeyError()


class OC_Compared(objc.lookUpClass("NSObject")):
    def initWithValue_(self, value):
        self = super(OC_Compared, self).init()
        if self is None:
            return None

        self._value = value
        return self

    @objc.typedSelector(objc._C_NSBOOL + b"@:@")
    def isEqualTo_(self, other):
        return self.compare_(other) == 0

    @objc.typedSelector(objc._C_NSBOOL + b"@:@")
    def isNotEqualTo_(self, other):
        return self.compare_(other) != 0

    @objc.typedSelector(objc._C_NSInteger + b"@:@")
    def compare_(self, other):
        if isinstance(other, OC_Compared):
            other = other._value

        if self._value < other:
            return -1

        elif self._value > other:
            return 1

        else:
            return 0


class TestBasicConvenience(TestCase):
    def test_hashprotocol(self):
        v = objc.lookUpClass("NSObject").alloc().init()
        v.hash()

        hash(v) + 0

    def test_hash_not_negative_one(self):
        v = OC_WithHash.alloc().initWithHash_(-1)
        self.assertEqual(v.hash(), -1)
        self.assertEqual(hash(v), -2)

    def test_hash_not_enormous(self):
        v = OC_WithHash.alloc().initWithHash_(2 ** 64 - 1)
        self.assertEqual(v.hash(), 2 ** 64 - 1)
        self.assertTrue(-sys.maxsize - 1 <= hash(v) <= sys.maxsize)

    def test_comparisons(self):
        o1 = objc.lookUpClass("NSObject").alloc().init()
        o2 = objc.lookUpClass("NSObject").alloc().init()

        self.assertTrue(o1 == o1)
        self.assertFalse(o1 == o2)
        self.assertTrue(o1 != o2)
        self.assertFalse(o1 != o1)

        o1 = OC_Compared.alloc().initWithValue_(21)
        o2 = OC_Compared.alloc().initWithValue_(42)
        o3 = OC_Compared.alloc().initWithValue_(42)

        self.assertTrue(o1 < o2)
        self.assertTrue(o1 <= o2)
        self.assertTrue(o2 == o3)
        self.assertTrue(o1 != o2)
        self.assertTrue(o2 <= o3)
        self.assertTrue(o2 >= o3)
        self.assertTrue(o2 > o1)

        self.assertFalse(o2 < o1)
        self.assertFalse(o2 <= o1)
        self.assertFalse(o1 == o3)
        self.assertFalse(o2 != o3)
        self.assertFalse(o2 <= o1)
        self.assertFalse(o1 >= o3)
        self.assertFalse(o1 > o2)


class TestNSDecimalNumber(TestCase):
    def setUp(self):
        self.NSDecimalNumber = objc.lookUpClass("NSDecimalNumber")

    def testCreation(self):
        v = self.NSDecimalNumber()
        self.assertIsInstance(v, self.NSDecimalNumber)
        self.assertEqual(str(v), "0")

        v = self.NSDecimalNumber(1)
        self.assertIsInstance(v, self.NSDecimalNumber)
        self.assertEqual(str(v), "1")

        v = self.NSDecimalNumber(1.5)
        self.assertIsInstance(v, self.NSDecimalNumber)
        self.assertEqual(str(v), "1.5")

        v = self.NSDecimalNumber(objc.NSDecimal("2.5"))
        self.assertIsInstance(v, self.NSDecimalNumber)
        self.assertEqual(str(v), "2.5")

        w = self.NSDecimalNumber(v)
        self.assertIsInstance(w, self.NSDecimalNumber)
        self.assertEqual(str(w), "2.5")

        self.assertRaises(TypeError, self.NSDecimalNumber, {})

    def testCalculation(self):
        a_o = self.NSDecimalNumber("1.5")
        b_o = self.NSDecimalNumber("2.5")

        a_c = objc.NSDecimal("1.5")
        b_c = objc.NSDecimal("2.5")

        # Subtraction

        v_o = a_o - b_o
        v_c = a_c - b_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = 1 - b_o
        v_c = 1 - b_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = a_o - 1
        v_c = a_c - 1
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        # Addition

        v_o = a_o + b_o
        v_c = a_c + b_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = 1 + b_o
        v_c = 1 + b_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = a_o + 1
        v_c = a_c + 1
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        # Multiplication

        v_o = a_o * b_o
        v_c = a_c * b_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = 2 * b_o
        v_c = 2 * b_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = a_o * 2
        v_c = a_c * 2
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        # Division

        v_o = a_o / b_o
        v_c = a_c / b_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = 2 / b_o
        v_c = 2 / b_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = a_o / 2
        v_c = a_c / 2
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        # Floor Division

        v_o = a_o // b_o
        v_c = a_c // b_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = 2 // b_o
        v_c = 2 // b_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = a_o // 2
        v_c = a_c // 2
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        # Modulo

        # Not supported at the moment.

        self.assertRaises(TypeError, operator.mod, a_o, b_o)
        self.assertRaises(TypeError, operator.mod, a_c, b_c)
        self.assertRaises(TypeError, operator.mod, a_o, 2)
        self.assertRaises(TypeError, operator.mod, a_c, 2)
        self.assertRaises(TypeError, operator.mod, 2, b_o)
        self.assertRaises(TypeError, operator.mod, 2, b_c)

        # v_o = a_o % b_o
        # v_c = a_c % b_c
        # self.assertEqual(str(v_o), str(v_c))
        # self.assertIsInstance(v_o, self.NSDecimalNumber)

        # v_o = 2 % b_o
        # v_c = 2 % b_c
        # self.assertEqual(str(v_o), str(v_c))
        # self.assertIsInstance(v_o, self.NSDecimalNumber)

        # v_o = a_o % 2
        # v_c = a_c % 2
        self.assertEqual(str(v_o), str(v_c))
        # self.assertIsInstance(v_o, self.NSDecimalNumber)

        # Negate
        v_o = -a_o
        v_c = -a_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        # Unary plus
        v_o = +a_o
        v_c = +a_c
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        # Abs
        v_o = abs(a_o)
        v_c = abs(a_c)
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = abs(-a_o)
        v_c = abs(-a_c)
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        # Rounding
        a_o = self.NSDecimalNumber("15.125")
        a_c = objc.NSDecimal("15.125")

        v_o = round(a_o)
        v_c = round(a_c)
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = round(a_o, 1)
        v_c = round(a_c, 1)
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

        v_o = round(a_o, -1)
        v_c = round(a_c, -1)
        self.assertEqual(str(v_o), str(v_c))
        self.assertIsInstance(v_o, self.NSDecimalNumber)

    def test_compare(self):
        a_o = self.NSDecimalNumber("1.5")
        b_o = self.NSDecimalNumber("2.5")
        c_o = self.NSDecimalNumber("2.5")

        self.assertTrue(a_o < b_o)
        self.assertFalse(b_o < a_o)
        self.assertTrue(a_o <= b_o)
        self.assertFalse(b_o <= a_o)

        self.assertFalse(a_o > b_o)
        self.assertTrue(b_o > a_o)
        self.assertFalse(a_o >= b_o)
        self.assertTrue(b_o >= a_o)

        self.assertTrue(b_o == c_o)
        self.assertTrue(b_o == objc.NSDecimal("2.5"))
        self.assertFalse(b_o == a_o)

        self.assertTrue(b_o != a_o)
        self.assertFalse(b_o != c_o)


class TestNSData(TestCase):
    def test_creation(self):
        NSData = objc.lookUpClass("NSData")
        NSMutableData = objc.lookUpClass("NSMutableData")

        data = NSData(b"hello")
        data2 = NSMutableData(b"moon")

        self.assertEqual(bytes(data), b"hello")
        self.assertEqual(bytes(data2), b"moon")

        self.assertIsInstance(data, NSData)
        self.assertIsInstance(data2, NSMutableData)

    def test_to_string(self):
        NSData = objc.lookUpClass("NSData")

        data = NSData(b"hello")
        data2 = NSData()

        self.assertEqual(str(data), str(b"hello"))
        self.assertEqual(str(data2), str(b""))

    def reading(self):
        NSData = objc.lookUpClass("NSData")
        bdata = b"hello"
        data = NSData(bdata)

        self.assertEqual(data[0], bdata[0])
        self.assertEqual(data[0:2], bdata[0:2])
        self.assertEqual(data[0:6:2], bdata[0:6:2])

    def writing(self):
        NSData = objc.lookUpClass("NSMutableData")
        bdata = b"hello"
        bdata = NSData(bdata)
        barray = bytearray(bdata)

        bdata[0] = b"x"[0]
        barray[0] = b"x"[0]
        self.assertEqual(bytes(bdata), bytes(barray))

        bdata[0:2] = b".."
        barray[0:2] = b".."
        self.assertEqual(bytes(bdata), bytes(barray))

        bdata[0:4:2] = b"++"
        barray[0:4:2] = b"++"
        self.assertEqual(bytes(bdata), bytes(barray))

        for idx in range(len(barray)):
            self.assertEqual(barray[idx], bdata[idx])

        try:
            barray[0:4:2] = b"----"
            self.fail("Exception not raised")
        except ValueError:
            pass

        try:
            bdata[0:4:2] = b"----"
            self.fail("Exception not raised")
        except ValueError:
            pass

        # XXX: more testing needed?


class TestNULLConvenience(TestCase):
    def test_nsnull(self):
        NSNull = objc.lookUpClass("NSNull")
        null = NSNull.null()
        self.assertFalse(null)


class TestNSString(TestCase):
    def test_nsstring_creation(self):
        NSString = objc.lookUpClass("NSString")

        value = NSString("hello world")
        self.assertIsInstance(value, objc.pyobjc_unicode)
        self.assertEqual(value, "hello world")
        self.assertIsInstance(value.nsstring(), NSString)

        value = NSString()
        self.assertIsInstance(value, objc.pyobjc_unicode)
        self.assertEqual(value, "")
        self.assertIsInstance(value.nsstring(), NSString)

    def test_nsstring_creation2(self):
        NSMutableString = objc.lookUpClass("NSMutableString")

        value = NSMutableString("hello world")
        self.assertIsInstance(value, objc.pyobjc_unicode)
        self.assertEqual(value, "hello world")
        self.assertIsInstance(value.nsstring(), NSMutableString)

        value = NSMutableString()
        self.assertIsInstance(value, objc.pyobjc_unicode)
        self.assertEqual(value, "")
        self.assertIsInstance(value.nsstring(), NSMutableString)

    def test_apis(self):
        NSMutableString = objc.lookUpClass("NSMutableString")

        value = NSMutableString("hello world")
        self.assertIsNotInstance(value, NSMutableString)
        value = value.nsstring()
        self.assertIsInstance(value, NSMutableString)

        self.assertEqual(len(value), 11)
        self.assertFalse(value.startswith("Hello"))
        self.assertTrue(value.startswith("hello"))
        self.assertFalse(value.endswith("moon"))
        self.assertTrue(value.endswith("orld"))


class TestConvenienceHelpers(TestCase):
    def test_add_for_class(self):
        self.assertNotIn("MyObject", convenience.CLASS_METHODS)

        methods = [("info", lambda self: self.description())]

        try:
            objc.addConvenienceForClass("MyObject", methods)
            self.assertEqual(convenience.CLASS_METHODS["MyObject"], tuple(methods))

        finally:
            if "MyObject" in convenience.CLASS_METHODS:
                del convenience.CLASS_METHODS["MyObject"]


class TestBasicConveniences(TestCase):
    def testBundleForClass(self):
        orig = convenience.currentBundle
        try:
            the_bundle = object()

            def currentBundle():
                return the_bundle

            convenience.currentBundle = currentBundle

            class OC_Test_Basic_Convenience_1(objc.lookUpClass("NSObject")):
                pass

            self.assertIs(OC_Test_Basic_Convenience_1.bundleForClass(), the_bundle)
        finally:
            convenience.currentBundle = orig

    def test_kvc_helper(self):
        o = objc.lookUpClass("NSURL").URLWithString_("http://www.python.org/")
        self.assertEqual(o.host(), "www.python.org")

        self.assertEqual(o._.host, "www.python.org")
        self.assertEqual(o._["host"], "www.python.org")
        self.assertRaises(TypeError, lambda: o._[42])
        self.assertEqual(repr(o._), "<KVC accessor for %r>" % (o,))
        self.assertRaises(AttributeError, getattr, o._, "nosuchattr")
        self.assertRaises(AttributeError, getattr, o._, "")
        self.assertRaises(TypeError, o._.__getitem__, 42)

        o = objc.lookUpClass("NSMutableDictionary").dictionary()
        o._.key1 = 1
        o._["key2"] = 2

        self.assertEqual(o, {"key1": 1, "key2": 2})

        # At least on OSX 10.11 the KVC accessor for NSDictionary returns
        # nil for non-existing keys.
        # self.assertRaises(AttributeError, getattr, o._, 'nosuchattr')
        self.assertRaises(TypeError, o._.__setitem__, 42, 1)

        o = OC_WithHash.alloc().initWithHash_(1)
        self.assertRaises(IndexError, getattr, o._, "someKey")
        self.assertRaises(KeyError, getattr, o._, "someOtherKey")


class TestSequences(TestCase):
    def test_reading(self):
        o = OC_TestSequence.alloc().initWithArray_(["a", "b", "c", "d"])

        self.assertEqual(len(o), 4)
        self.assertEqual(o[0], "a")
        self.assertEqual(o[3], "d")
        self.assertEqual(o[-1], "d")
        self.assertEqual(o[-3], "b")

        self.assertRaises(IndexError, operator.getitem, o, 6)
        self.assertRaises(IndexError, operator.getitem, o, -6)
        self.assertRaises(ValueError, operator.getitem, o, slice(1, 3))

        self.assertEqual(list(iter(o)), ["a", "b", "c", "d"])
        self.assertRaises(AttributeError, operator.setitem, o, 1, "A")

        o = OC_TestSequence.alloc().initWithArray_([])
        self.assertEqual(list(iter(o)), [])

    def test_writing(self):
        o = OC_TestMutableSequence.alloc().initWithArray_(["a", "b", "c", "d"])

        o[0] = "A"
        self.assertEqual(o[0], "A")

        o[2] = "C"
        self.assertEqual(o[2], "C")

        o[-3] = "X"
        self.assertEqual(o[1], "X")

        self.assertEqual(list(o), ["A", "X", "C", "d"])

        self.assertRaises(IndexError, operator.setitem, o, 6, "x")
        self.assertRaises(IndexError, operator.setitem, o, -7, "x")
        self.assertRaises(ValueError, operator.setitem, o, slice(1, 3), (1, 2))
