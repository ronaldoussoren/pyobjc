from PyObjCTest.coding import PyObjC_TestCodingClass, OC_RaisingCoder, OC_NilBytes
from PyObjCTools.TestSupport import TestCase
from .test_metadata import NoObjCClass
import objc
from objc import super  # noqa: A004
import warnings

NSObject = objc.lookUpClass("NSObject")
NSMutableData = objc.lookUpClass("NSMutableData")
NSArchiver = objc.lookUpClass("NSArchiver")
NSUnarchiver = objc.lookUpClass("NSUnarchiver")
NSKeyedArchiver = objc.lookUpClass("NSKeyedArchiver")
NSKeyedUnarchiver = objc.lookUpClass("NSKeyedUnarchiver")
NSCoder = objc.lookUpClass("NSCoder")


class TestNSCoderUsage(TestCase):
    def testUsage(self):
        class CoderClass1(NSObject):
            def encodeWithCoder_(self, coder):
                # NSObject does not implement NSCoding, no need to
                # call superclass implementation:
                #    super(CoderClass1, self).encodeWithCoder_(coder)
                imp = coder.methodForSelector_(b"encodeValueOfObjCType:at:")
                coder.encodeValueOfObjCType_at_(objc._C_INT, 2)
                coder.encodeValueOfObjCType_at_(objc._C_INT, 3)
                imp(coder, objc._C_DBL, 2.0)
                coder.encodeValueOfObjCType_at_(objc._C_FLT, 2.5)
                coder.encodeValueOfObjCType_at_(objc._C_LNG_LNG, 2**62)
                coder.encodeArrayOfObjCType_count_at_(
                    objc._C_DBL, 4, (1.0, 2.0, 3.0, 4.0)
                )
                imp = coder.methodForSelector_(b"encodeArrayOfObjCType:count:at:")
                imp(coder, objc._C_DBL, 2, (42.0, -42.0))

                coder.encodeBytes_length_(b"hello world!", 5)
                imp = coder.methodForSelector_(b"encodeBytes:length:")
                imp(coder, b"moonbase alpha", 10)

                coder.encodeBytes_length_(None, 0)
                coder.encodeValueOfObjCType_at_(objc._C_INT, 44)

                try:
                    coder.encodeValueOfObjCType_at_(objc._C_INT, "foo")
                except ValueError as exc:
                    if "depythonify" not in str(exc):
                        raise
                else:
                    raise AssertionError("Invalid argument type didn't raise")

                try:
                    coder.encodeValueOfObjCType_at_(objc._C_INT, 2, 3)
                except TypeError as exc:
                    if "expected 2 arguments, got 3" not in str(exc):
                        raise
                else:
                    raise AssertionError("Too many arguments didn't raise")

                try:
                    coder.encodeValueOfObjCType_at_(objc._C_INT)
                except TypeError as exc:
                    if "expected 2 arguments, got 1" not in str(exc):
                        raise
                else:
                    raise AssertionError("Too few arguments didn't raise")

                try:
                    coder.encodeValueOfObjCType_at_("i", 2)
                except TypeError as exc:
                    if "a bytes-like object is required, not 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad encoding type")

                try:
                    coder.encodeValueOfObjCType_at_(b"X", 2)
                except objc.error as exc:
                    if "type encoding is not valid" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad encoding type")

                try:
                    coder.encodeArrayOfObjCType_count_at_(objc._C_DBL, 4)
                except TypeError as exc:
                    if "expected 3 arguments, got 2" not in str(exc):
                        raise
                else:
                    raise AssertionError("Too few arguments")

                try:
                    coder.encodeArrayOfObjCType_count_at_(
                        objc._C_DBL, "4", (1.0, 2.0, 3.0, 4.0)
                    )
                except ValueError as exc:
                    if "depythonifying 'unsigned long long', got 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("Too many arguments")

                try:
                    coder.encodeArrayOfObjCType_count_at_(
                        objc._C_DBL, 4, (1.0, 2.0, 3.0, 4.0), 6
                    )
                except TypeError as exc:
                    if "expected 3 arguments, got 4" not in str(exc):
                        raise
                else:
                    raise AssertionError("Too many arguments")

                try:
                    coder.encodeArrayOfObjCType_count_at_("d", 4, (1.0, 2.0, 3.0, 4.0))
                except TypeError as exc:
                    if "a bytes-like object is required, not 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad encoding type")

                try:
                    coder.encodeArrayOfObjCType_count_at_(b"X", 4, (1.0, 2.0, 3.0, 4.0))
                except objc.error as exc:
                    if "type encoding is not valid" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad encoding type")

                try:
                    coder.encodeArrayOfObjCType_count_at_(b"d", 1, 42.5)
                except TypeError as exc:
                    if "need sequence of objects" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad encoding type")

                try:
                    coder.encodeArrayOfObjCType_count_at_(b"d", 1, [42.5, 3])
                except ValueError as exc:
                    if "Inconsistent arguments" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad encoding type")

                try:
                    coder.encodeArrayOfObjCType_count_at_(b"d", 3, [42.5, 3])
                except ValueError as exc:
                    if "Inconsistent arguments" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad encoding type")

                try:
                    coder.encodeArrayOfObjCType_count_at_(b"d", 2, [42.5, "a"])
                except ValueError as exc:
                    if "depythonifying 'double', got 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad encoding type")

                try:
                    coder.encodeBytes_length_(b"hello", 4, 7)
                except TypeError as exc:
                    if "expected 2 arguments, got 3" not in str(exc):
                        raise
                else:
                    raise AssertionError("Too many arguments")

                try:
                    coder.encodeBytes_length_(b"hello")
                except TypeError as exc:
                    if "expected 2 arguments, got 1" not in str(exc):
                        raise
                else:
                    raise AssertionError("Too few arguments")

                try:
                    coder.encodeBytes_length_("hello", 4)
                except TypeError as exc:
                    if "a bytes-like object is required, not 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("not byte string")

                try:
                    coder.encodeBytes_length_(b"hello", "four")
                except ValueError as exc:
                    if "depythonifying 'unsigned long long', got 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("not byte string")

                try:
                    coder.encodeBytes_length_(b"hello", 99)
                except ValueError as exc:
                    if "length 99 > len(buf) 5" not in str(exc):
                        raise
                else:
                    raise AssertionError("mismatched length")

                try:
                    coder.encodeBytes_length_(None, 42)
                except ValueError as exc:
                    if "length 42 > len(buf) 0" not in str(exc):
                        raise
                else:
                    raise AssertionError("mismatched length")

            def initWithCoder_(self, coder):
                # NSObject does not implement NSCoding, no need to
                # call superclass implementation:
                #    self = super(CodeClass1, self).initWithCoder_(coder)
                self = self.init()
                self.intVal = coder.decodeValueOfObjCType_at_(objc._C_INT, None)
                if objc.macos_available(10, 13):
                    self.intVal2 = coder.decodeValueOfObjCType_at_size_(
                        objc._C_INT, None, 4
                    )
                else:
                    self.intVal2 = coder.decodeValueOfObjCType_at_(objc._C_INT, None)
                imp = coder.methodForSelector_(b"decodeValueOfObjCType:at:")
                self.dblVal = imp(coder, objc._C_DBL, None)
                self.fltVal = coder.decodeValueOfObjCType_at_size_(objc._C_FLT, None, 4)
                imp = coder.methodForSelector_(b"decodeValueOfObjCType:at:size:")
                self.lnglngVal = imp(coder, objc._C_LNG_LNG, None, 8)
                self.dblArray = coder.decodeArrayOfObjCType_count_at_(
                    objc._C_DBL, 4, None
                )
                imp = coder.methodForSelector_(b"decodeArrayOfObjCType:count:at:")
                self.dblArray2 = imp(coder, objc._C_DBL, 2, None)
                self.decodedBytes = coder.decodeBytesWithReturnedLength_(None)

                imp = coder.methodForSelector_(b"decodeBytesWithReturnedLength:")
                self.decodedBytes2 = imp(coder, None)

                self.decodedBytes3 = coder.decodeBytesWithReturnedLength_(None)

                try:
                    coder.decodeValueOfObjCType_at_size_(b"q", None, 4)
                except ValueError as exc:
                    if "Cannot get decode with size 4" not in str(exc):
                        raise
                else:
                    raise AssertionError("bad size")

                try:
                    coder.decodeValueOfObjCType_at_size_(b"q", None, "4")
                except ValueError as exc:
                    if "depythonifying 'long long', got 'str' of 1" not in str(exc):
                        raise
                else:
                    raise AssertionError("bad size")

                try:
                    coder.decodeValueOfObjCType_at_size_("q", None, 4)
                except TypeError as exc:
                    if "a bytes-like object is required, not 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("bad encoding")

                try:
                    coder.decodeValueOfObjCType_at_size_(b"x", None, 4)
                except objc.error as exc:
                    if "type encoding is not valid" not in str(exc):
                        raise
                else:
                    raise AssertionError("bad encoding")

                try:
                    coder.decodeValueOfObjCType_at_size_(b"i", bytearray(4), 4)
                except ValueError as exc:
                    if "buffer must be None" not in str(exc):
                        raise
                else:
                    raise AssertionError("bad encoding")

                try:
                    coder.decodeValueOfObjCType_at_size_(b"q", None, 4, 10)
                except TypeError as exc:
                    if "expected 3 arguments, got 4" not in str(exc):
                        raise
                else:
                    raise AssertionError("too many arguments")

                try:
                    coder.decodeValueOfObjCType_at_size_(b"q")
                except TypeError as exc:
                    if "expected 3 arguments, got 1" not in str(exc):
                        raise
                else:
                    raise AssertionError("too few arguments")

                try:
                    coder.decodeValueOfObjCType_at_(b"q", None, 1)
                except TypeError as exc:
                    if "expected 2 arguments, got 3" not in str(exc):
                        raise
                else:
                    raise AssertionError("too many arguments")

                try:
                    coder.decodeValueOfObjCType_at_(b"q")
                except TypeError as exc:
                    if "expected 2 arguments, got 1" not in str(exc):
                        raise
                else:
                    raise AssertionError("too few arguments")

                try:
                    coder.decodeValueOfObjCType_at_("X", None)
                except TypeError as exc:
                    if "a bytes-like object is required, not 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("type encoding invalid")

                try:
                    coder.decodeValueOfObjCType_at_(b"X", None)
                except objc.error as exc:
                    if "type encoding is not valid" not in str(exc):
                        raise
                else:
                    raise AssertionError("type encoding invalid")

                try:
                    coder.decodeValueOfObjCType_at_(b"q", 42)
                except ValueError as exc:
                    if "buffer must be None" not in str(exc):
                        raise
                else:
                    raise AssertionError("type encoding invalid")

                try:
                    coder.decodeArrayOfObjCType_count_at_(b"q", 42)
                except TypeError as exc:
                    if "expected 3 arguments, got 2" not in str(exc):
                        raise
                else:
                    raise AssertionError("too few arguments")

                try:
                    coder.decodeArrayOfObjCType_count_at_(b"q", 42, None, "foo")
                except TypeError as exc:
                    if "expected 3 arguments, got 4" not in str(exc):
                        raise
                else:
                    raise AssertionError("too many arguments")

                try:
                    coder.decodeArrayOfObjCType_count_at_("d", 42, None)
                except TypeError as exc:
                    if "a bytes-like object is required, not 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("type encoding invalid")

                try:
                    coder.decodeArrayOfObjCType_count_at_(b"X", 42, None)

                except objc.error as exc:
                    if "type encoding is not valid" not in str(exc):
                        raise
                else:
                    raise AssertionError("type encoding invalid")

                try:
                    coder.decodeArrayOfObjCType_count_at_(b"q", "hello", None)

                except ValueError as exc:
                    if "depythonifying 'unsigned long long', got 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("type encoding invalid")

                try:
                    coder.decodeArrayOfObjCType_count_at_(b"q", 1, "buffer")
                except ValueError as exc:
                    if "buffer must be None" not in str(exc):
                        raise
                else:
                    raise AssertionError("type encoding invalid")

                try:
                    coder.decodeBytesWithReturnedLength_()
                except TypeError as exc:
                    if "expected 1 arguments, got 0" not in str(exc):
                        raise
                else:
                    raise AssertionError("too few arguments")

                try:
                    coder.decodeBytesWithReturnedLength_(None, 42)
                except TypeError as exc:
                    if "expected 1 arguments, got 2" not in str(exc):
                        raise
                else:
                    raise AssertionError("too many arguments")

                try:
                    coder.decodeBytesWithReturnedLength_(42)
                except ValueError as exc:
                    if "buffer must be None" not in str(exc):
                        raise
                else:
                    raise AssertionError("bad buffer")

                try:
                    coder.decodeValueOfObjCType_at_size_(b"q", None, 1, 9)
                except TypeError as exc:
                    if "expected 3 arguments, got 4" not in str(exc):
                        raise
                else:
                    raise AssertionError("too many arguments")

                try:
                    coder.decodeValueOfObjCType_at_size_(b"q")
                except TypeError as exc:
                    if "expected 3 arguments, got 1" not in str(exc):
                        raise
                else:
                    raise AssertionError("too few arguments")

                try:
                    coder.decodeValueOfObjCType_at_size_("i", None, 4)
                except TypeError as exc:
                    if "a bytes-like object is required, not 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("type encoding invalid")

                try:
                    coder.decodeValueOfObjCType_at_size_(b"X", None, 4)
                except objc.error as exc:
                    if "type encoding is not valid" not in str(exc):
                        raise
                else:
                    raise AssertionError("type encoding invalid")

                try:
                    coder.decodeValueOfObjCType_at_size_(b"q", 42, 8)
                except ValueError as exc:
                    if "buffer must be None" not in str(exc):
                        raise
                else:
                    raise AssertionError("buffer invalid")

                try:
                    coder.decodeValueOfObjCType_at_size_(b"q", None, "a")
                except ValueError as exc:
                    if "depythonifying 'long long', got 'str' of 1" not in str(exc):
                        raise
                else:
                    raise AssertionError("size invalid")

                try:
                    coder.decodeValueOfObjCType_at_size_(b"q", None, 4)
                except ValueError as exc:
                    if "The type encoded as q is expected to be 8 bytes" not in str(
                        exc
                    ):
                        raise
                else:
                    raise AssertionError("size mismatch")

                coder.decodeValueOfObjCType_at_size_(objc._C_INT, None, 4)
                return self

        origObj = CoderClass1.alloc().init()
        data = NSMutableData.data()
        archiver = NSArchiver.alloc().initForWritingWithMutableData_(data)
        archiver.encodeObject_(origObj)

        archiver = NSUnarchiver.alloc().initForReadingWithData_(data)
        newObj = archiver.decodeObject()

        self.assertEqual(newObj.intVal, 2)
        self.assertEqual(newObj.intVal2, 3)
        self.assertAlmostEqual(newObj.dblVal, 2.0)
        self.assertAlmostEqual(newObj.fltVal, 2.5)
        self.assertEqual(newObj.lnglngVal, 2**62)
        self.assertEqual(len(newObj.dblArray), 4)
        self.assertAlmostEqual(newObj.dblArray[0], 1.0)
        self.assertAlmostEqual(newObj.dblArray[1], 2.0)
        self.assertAlmostEqual(newObj.dblArray[2], 3.0)
        self.assertAlmostEqual(newObj.dblArray[3], 4.0)
        self.assertEqual(len(newObj.dblArray2), 2)
        self.assertEqual(newObj.dblArray2, (42.0, -42.0))
        self.assertEqual(newObj.decodedBytes[0], b"hello")
        self.assertEqual(newObj.decodedBytes[1], 5)
        self.assertEqual(newObj.decodedBytes2[0], b"moonbase a")
        self.assertEqual(newObj.decodedBytes2[1], 10)
        self.assertEqual(newObj.decodedBytes3[0], b"")
        self.assertEqual(newObj.decodedBytes3[1], 0)

    def test_keyed_archiver(self):
        class CoderClass2(NSObject):
            def encodeWithCoder_(self, coder):
                coder.encodeBytes_length_forKey_(b"hello there", 11, "message")
                imp = coder.methodForSelector_(b"encodeBytes:length:forKey:")
                imp(coder, b"abdce", 5, "letters")

                with warnings.catch_warnings():
                    warnings.simplefilter("error", category=DeprecationWarning)
                    try:
                        coder.encodeBytes_length_forKey_(b"moon base", "location")
                    except DeprecationWarning as exc:
                        if (
                            "using two arguments for 'encodeBytes_length_forKey_' will be removed in PyObjC 13"
                            not in str(exc)
                        ):
                            raise
                    else:
                        raise AssertionError("Too few arguments")

                    warnings.simplefilter("ignore", category=DeprecationWarning)
                    coder.encodeBytes_length_forKey_(b"moon base", "location")

                try:
                    coder.encodeBytes_length_forKey_(b"hello there")
                except TypeError as exc:
                    if "expected between 2 and 3 arguments, got 1" not in str(exc):
                        raise
                else:
                    raise AssertionError("Too few arguments")

                try:
                    coder.encodeBytes_length_forKey_(b"hello there", 12, "key", 99)
                except TypeError as exc:
                    if "expected between 2 and 3 arguments, got 4" not in str(exc):
                        raise
                else:
                    raise AssertionError("Too many arguments")

                try:
                    coder.encodeBytes_length_forKey_("hello there", 12, "key")
                except TypeError as exc:
                    if "a bytes-like object is required, not 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad buffer")

                try:
                    coder.encodeBytes_length_forKey_(b"hello there", "12", "key")
                except ValueError as exc:
                    if "depythonifying 'unsigned long long', got 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad size")

                try:
                    coder.encodeBytes_length_forKey_(b"hello there", 20, "key")
                except ValueError as exc:
                    if "passed in count 20 is larger than input size 11" not in str(
                        exc
                    ):
                        raise
                else:
                    raise AssertionError("Bad size")

                try:
                    coder.encodeBytes_length_forKey_(b"hello there", 5, NoObjCClass())
                except TypeError as exc:
                    if "Cannot proxy" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad size")

                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", category=DeprecationWarning)
                    try:
                        coder.encodeBytes_length_forKey_("moon base", "location")
                    except TypeError as exc:
                        if "a bytes-like object is required, not 'str'" not in str(exc):
                            raise
                    else:
                        raise AssertionError("Bad size")

                    try:
                        coder.encodeBytes_length_forKey_(b"moon base", NoObjCClass())
                    except TypeError as exc:
                        if "Cannot proxy" not in str(exc):
                            raise
                    else:
                        raise AssertionError("Bad size")

            def initWithCoder_(self, coder):
                self = self.init()
                self.message = coder.decodeBytesForKey_returnedLength_("message", None)

                imp = coder.methodForSelector_(b"decodeBytesForKey:returnedLength:")
                self.letters = imp(coder, "letters", None)

                self.location = coder.decodeBytesForKey_returnedLength_(
                    "location", None
                )
                self.invalid = coder.decodeBytesForKey_returnedLength_("invalid", None)

                try:
                    coder.decodeBytesForKey_returnedLength_("hello there")
                except TypeError as exc:
                    if "expected 2 arguments, got 1" not in str(exc):
                        raise
                else:
                    raise AssertionError("too few arguments")

                try:
                    coder.decodeBytesForKey_returnedLength_("hello there", None, 4)
                except TypeError as exc:
                    if "expected 2 arguments, got 3" not in str(exc):
                        raise
                else:
                    raise AssertionError("too many arguments")

                try:
                    coder.decodeBytesForKey_returnedLength_("hello there", 4)
                except ValueError as exc:
                    if "buffer must be None" not in str(exc):
                        raise
                else:
                    raise AssertionError("bad buffer")

                try:
                    coder.decodeBytesForKey_returnedLength_(NoObjCClass(), None)
                except TypeError as exc:
                    if "proxy" not in str(exc):
                        raise
                else:
                    raise AssertionError("bad key")

                return self

        origObj = CoderClass2.alloc().init()
        data = NSKeyedArchiver.archivedDataWithRootObject_(origObj)

        newObj = NSKeyedUnarchiver.unarchiveObjectWithData_(data)
        self.assertEqual(newObj.message, (b"hello there", 11))
        self.assertEqual(newObj.letters, (b"abdce", 5))
        self.assertEqual(newObj.location, (b"moon base", 9))
        self.assertEqual(newObj.invalid, (None, 0))

    def test_coder_raises(self):
        coder = OC_RaisingCoder.alloc().init()
        with self.assertRaisesRegex(objc.error, "raising coder"):
            coder.encodeArrayOfObjCType_count_at_(b"f", 10, [1.0] * 10)

        with self.assertRaisesRegex(objc.error, "raising coder"):
            coder.encodeBytes_length_(b"foobar", 3)

        with self.assertRaisesRegex(objc.error, "raising coder"):
            coder.encodeBytes_length_forKey_(b"foobar", 3, "key")

        with self.assertRaisesRegex(objc.error, "raising coder"):
            coder.encodeValueOfObjCType_at_(b"q", 42)

        with self.assertRaisesRegex(
            TypeError, "Cannot call 'encodeValuesOfObjCTypes:'"
        ):
            coder.encodeValuesOfObjCTypes_(b"qfi", 42, 3.5, 0)

        with self.assertRaisesRegex(objc.error, "raising coder"):
            coder.decodeValueOfObjCType_at_size_(b"f", None, 4)

        with self.assertRaisesRegex(objc.error, "raising coder"):
            coder.decodeValueOfObjCType_at_(b"f", None)

        with self.assertRaisesRegex(
            TypeError, "Cannot call 'decodeValuesOfObjCTypes:'"
        ):
            coder.decodeValuesOfObjCTypes_(b"qfi", None)

        with self.assertRaisesRegex(objc.error, "raising coder"):
            coder.decodeArrayOfObjCType_count_at_(b"q", 10, None)

        with self.assertRaisesRegex(objc.error, "raising coder"):
            coder.decodeBytesWithReturnedLength_(None)

        with self.assertRaisesRegex(objc.error, "raising coder"):
            coder.decodeBytesForKey_returnedLength_("key", None)

    def test_nil_bytes(self):
        coder = OC_NilBytes.alloc().init()

        data, length = coder.decodeBytesWithReturnedLength_(None)
        self.assertEqual(data, None)
        self.assertEqual(length, 42)

        data, length = coder.decodeBytesForKey_returnedLength_("key", None)
        self.assertEqual(data, None)
        self.assertEqual(length, 21)


class MyCoder(NSCoder):
    def init(self):
        self = super().init()
        if self is None:
            return None
        self.coded = []
        return self

    def encodeValueOfObjCType_at_(self, tp, value):
        self.coded.append(("value", tp, value))

    def encodeArrayOfObjCType_count_at_(self, tp, cnt, value):
        self.coded.append(("array", tp, cnt, value))

    def encodeBytes_length_(self, value, length):
        self.coded.append(("bytes", value, length))

    def encodeBytes_length_forKey_(self, value, length, key):
        self.coded.append(("bytes", value, length, key))

    def decodeValueOfObjCType_at_(self, tp, at):
        if tp == b"i":
            return 42
        elif tp == b"d":
            return 1.5

    def decodeValueOfObjCType_at_size_(self, tp, at, size):
        if tp == b"i":
            return -42
        elif tp == b"d":
            return -1.5

    def decodeArrayOfObjCType_count_at_(self, tp, cnt, at):
        return range(cnt)

    def decodeBytesWithReturnedLength_(self, value):
        return (b"ABCDEabcde", 10)

    def decodeBytesForKey_returnedLength_(self, key, value):
        if key == "name":
            return (b"python", 6)
        elif key == "error":
            raise RuntimeError("error")
        elif key == "missing":
            return (None, 0)
        elif key == "invald-tuple":
            return (b"hello", 5, 6)
        elif key == "no-tuple":
            return b"hello"
        elif key == "invalid-len":
            return (b"hello", "five")
        elif key == "invalid-buffer":
            return ("hello", 5)
        elif key == "long-buffer":
            return (b"hello world", 5)
        elif key == "short-buffer":
            return (b"help", 5)


class MyCoderNotNone(NSCoder):
    def init(self):
        return self.initWithScenario_(0)

    def initWithScenario_(self, scenario):
        self = super().init()
        if self is None:
            return None
        self.coded = []
        self.scenario = scenario
        return self

    def encodeValueOfObjCType_at_(self, tp, value):
        self.coded.append(("value", tp, value))

        if self.scenario == 1:
            return 42
        elif self.scenario == -1:
            raise RuntimeError("error!")

    def encodeArrayOfObjCType_count_at_(self, tp, cnt, value):
        self.coded.append(("array", tp, cnt, value))
        if self.scenario == 2:
            return 42
        elif self.scenario == -2:
            raise RuntimeError("error!")

    def encodeBytes_length_(self, value, length):
        self.coded.append(("bytes", value, length))
        if self.scenario == 3:
            return 42
        elif self.scenario == -3:
            raise RuntimeError("error!")

    def encodeBytes_length_forKey_(self, value, length, key):
        self.coded.append(("bytes", value, length, key))
        if self.scenario == 40:
            return 42
        elif self.scenario == -40:
            raise RuntimeError("error!")

    def decodeValueOfObjCType_at_(self, tp, at):
        if self.scenario == -4:
            raise RuntimeError("error!")

        if tp == b"i":
            return 42
        elif tp == b"d":
            return 1.5

    def decodeArrayOfObjCType_count_at_(self, tp, cnt, at):
        if self.scenario == 5:
            return 42

        elif self.scenario == 6:
            return (1,) * (cnt + 3)

        elif self.scenario == 7:
            return (1,) * (cnt - 1)

        elif self.scenario == -5:
            raise RuntimeError("error!")
        return range(cnt)

    def decodeBytesWithReturnedLength_(self, value):
        if self.scenario == -8:
            raise RuntimeError("error!")
        elif self.scenario == 8:
            return None, 10
        elif self.scenario == 9:
            return b"hello world", 5
        elif self.scenario == 10:
            return b"help", 15
        elif self.scenario == 11:
            return "help", 4
        elif self.scenario == 12:
            return b"help"
        elif self.scenario == 13:
            return b"help", 4, 5
        elif self.scenario == 14:
            return b"help", "4"
        return (b"ABCDEabcde", 10)

    def decodeValueOfObjCType_at_size_(self, tp, at, size):
        if self.scenario == -14:
            raise RuntimeError("error!")
        elif self.scenario == -15:
            return object()

        if tp == b"i":
            return -42
        elif tp == b"d":
            return -1.5


class TestPythonCoder(TestCase):
    #
    # This test accesses a NSCoder implemented in Python from Objective-C
    #
    # The tests only use those methods that require a custom IMP-stub.
    #
    def testNotNone(self):
        o = PyObjC_TestCodingClass.alloc().init()

        for scenario in (1, 2, 3, 40):
            coder = MyCoderNotNone.alloc().initWithScenario_(scenario)
            with self.assertRaisesRegex(TypeError, "did not return None"):
                o.encodeWithCoder_(coder)

    def testRaises(self):
        o = PyObjC_TestCodingClass.alloc().init()

        for scenario in (-1, -2, -3, -40):
            coder = MyCoderNotNone.alloc().initWithScenario_(scenario)
            with self.assertRaisesRegex(RuntimeError, "error!"):
                o.encodeWithCoder_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(-4)
        with self.assertRaisesRegex(RuntimeError, "error!"):
            PyObjC_TestCodingClass.fetchInt_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(-5)
        with self.assertRaisesRegex(RuntimeError, "error!"):
            PyObjC_TestCodingClass.fetchArray_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(-8)
        with self.assertRaisesRegex(RuntimeError, "error!"):
            PyObjC_TestCodingClass.fetchData_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(5)
        with self.assertRaisesRegex(TypeError, "Return-value must be a sequence"):
            PyObjC_TestCodingClass.fetchArray_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(6)
        with self.assertRaisesRegex(
            TypeError, "return value must be a of correct size"
        ):
            PyObjC_TestCodingClass.fetchArray_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(7)
        with self.assertRaisesRegex(
            TypeError, "return value must be a of correct size"
        ):
            PyObjC_TestCodingClass.fetchArray_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(8)
        d = PyObjC_TestCodingClass.fetchData_(coder)
        self.assertEqual(d, (None, 10))

        coder = MyCoderNotNone.alloc().initWithScenario_(9)
        d = PyObjC_TestCodingClass.fetchData_(coder)
        self.assertEqual(d, b"hello")

        coder = MyCoderNotNone.alloc().initWithScenario_(10)
        with self.assertRaisesRegex(
            ValueError, "Buffer length 4 is less than returned length 15"
        ):
            PyObjC_TestCodingClass.fetchData_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(11)
        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'str'"
        ):
            PyObjC_TestCodingClass.fetchData_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(12)
        with self.assertRaisesRegex(ValueError, r"Should return \(bytes, length\)"):
            PyObjC_TestCodingClass.fetchData_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(13)
        with self.assertRaisesRegex(ValueError, r"Should return \(bytes, length\)"):
            PyObjC_TestCodingClass.fetchData_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(14)
        with self.assertRaisesRegex(
            ValueError, r"depythonifying 'unsigned long.*', got 'str'"
        ):
            PyObjC_TestCodingClass.fetchData_(coder)

        coder = MyCoderNotNone.alloc().initWithScenario_(-14)
        with self.assertRaisesRegex(RuntimeError, "error!"):
            print(PyObjC_TestCodingClass.fetchInt_size_(coder, 4))

        coder = MyCoderNotNone.alloc().initWithScenario_(-15)
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'object'"):
            print(PyObjC_TestCodingClass.fetchInt_size_(coder, 4))

    def testEncoding(self):
        coder = MyCoder.alloc().init()
        o = PyObjC_TestCodingClass.alloc().init()
        o.encodeWithCoder_(coder)
        self.assertEqual(
            coder.coded,
            [
                ("value", b"d", 1.5),
                ("array", b"i", 4, (3, 4, 5, 6)),
                ("bytes", b"hello world", 11),
                ("bytes", b"mess", 4, "random-key"),
            ],
        )

    def testDecoding(self):
        coder = MyCoder.alloc().init()
        o = PyObjC_TestCodingClass

        self.assertEqual(o.fetchInt_(coder), 42)
        self.assertEqual(o.fetchDouble_(coder), 1.5)

        self.assertEqual(o.fetchInt_size_(coder, 4), -42)
        self.assertEqual(o.fetchInt_size_(coder, 8), -42)
        with self.assertRaisesRegex(
            ValueError, "provided size 2 is less than actual size 4"
        ):
            self.assertEqual(o.fetchInt_size_(coder, 2), -42)

        d = o.fetchData_(coder)
        self.assertEqual(d.length(), 10)

        b = d.bytes()
        if isinstance(b, memoryview):
            self.assertEqual(b.tobytes(), b"ABCDEabcde")
        else:
            self.assertEqual(bytes(b), b"ABCDEabcde")

        d = o.fetchArray_(coder)
        self.assertEqual(tuple(range(10)), tuple(d))

    def test_decodingkey(self):
        coder = MyCoder.alloc().init()
        o = PyObjC_TestCodingClass

        v = o.fetchData_forKey_(coder, "name")
        self.assertEqual(v, b"python")

        with self.assertRaisesRegex(RuntimeError, "error"):
            o.fetchData_forKey_(coder, "error")

        v = o.fetchData_forKey_(coder, "missing")
        self.assertEqual(v, (None, 0))

        with self.assertRaisesRegex(ValueError, r"Should return \(bytes, length\)"):
            o.fetchData_forKey_(coder, "invalid-tuple")

        with self.assertRaisesRegex(ValueError, r"Should return \(bytes, length\)"):
            o.fetchData_forKey_(coder, "no-tuple")

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            o.fetchData_forKey_(coder, "invalid-len")

        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'str'"
        ):
            o.fetchData_forKey_(coder, "invalid-buffer")

        v = o.fetchData_forKey_(coder, "long-buffer")
        self.assertEqual(v, b"hello")

        with self.assertRaisesRegex(
            ValueError, "Buffer length 4 is less than returned length 5"
        ):
            o.fetchData_forKey_(coder, "short-buffer")


class TestUnsupported(TestCase):
    def test_encodeValuesOfObjCTypes(self):
        with self.assertRaisesRegex(
            TypeError,
            "Implementing encodeValuesOfObjCTypes: in Python is not supported",
        ):

            class MyCoderUnsupported(NSCoder):
                def encodeValuesOfObjCTypes_(self, types, *args):
                    pass
