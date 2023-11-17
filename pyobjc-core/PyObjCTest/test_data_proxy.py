from PyObjCTools.TestSupport import (
    TestCase,
    pyobjc_options,
    os_level_key,
    os_release,
    min_os_level,
)
from PyObjCTest.dataint import OC_DataInt
from PyObjCTest.pythonset import OC_TestSet
from itertools import count
import array
import objc

NSKeyedArchiver = objc.lookUpClass("NSKeyedArchiver")
NSKeyedUnarchiver = objc.lookUpClass("NSKeyedUnarchiver")
NSArchiver = objc.lookUpClass("NSArchiver")
NSUnarchiver = objc.lookUpClass("NSUnarchiver")
NSData = objc.lookUpClass("NSData")
NSMutableData = objc.lookUpClass("NSMutableData")
OC_PythonData = objc.lookUpClass("OC_PythonData")
OC_BuiltinPythonData = objc.lookUpClass("OC_BuiltinPythonData")

# XXX: Move register calls to utility module
objc.registerMetaDataForSelector(
    b"NSKeyedArchiver",
    b"archivedDataWithRootObject:requiringSecureCoding:error:",
    {
        "arguments": {
            2 + 1: {"type": objc._C_NSBOOL},
            2 + 2: {"type_modifier": objc._C_OUT},
        }
    },
)
objc.registerMetaDataForSelector(
    b"NSKeyedUnarchiver",
    b"unarchivedObjectOfClass:fromData:error:",
    {"arguments": {2 + 2: {"type_modifier": objc._C_OUT}}},
)
objc.registerMetaDataForSelector(
    b"NSKeyedUnarchiver",
    b"unarchivedObjectOfClasses:fromData:error:",
    {"arguments": {2 + 2: {"type_modifier": objc._C_OUT}}},
)

_counter = count()


class SomeBytes(bytes):
    def __init__(self, value=None):
        self.x = next(_counter)

    def __eq__(self, other):
        if not isinstance(other, SomeBytes):
            return False
        r = super().__eq__(other)
        if r:
            return other.x == self.x
        return r

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f"{super().__repr__()} x={self.x}"

    __str__ = __repr__


class TestDataReading(TestCase):
    bytes_class = bytes

    def test_get_bytes(self):
        data = self.bytes_class(b"hello world")

        v = OC_DataInt.getBytes_length_(data, 8)
        self.assertEqual(v, b"hello wo")

    def test_length(self):
        data = self.bytes_class(b"hello world")
        self.assertEqual(OC_DataInt.lengthOf_(data), len(data))

    def test_coderClass(self):
        data = self.bytes_class(b"hello")
        cls = OC_DataInt.coderClassFor_(data)
        if type(data) is bytes:
            self.assertIs(cls, NSData)
        elif type(data) is bytearray:
            self.assertIs(cls, NSMutableData)
        else:
            self.assertIs(cls, OC_PythonData)

    def test_keyedArchiverClass(self):
        data = self.bytes_class(b"hello")
        cls = OC_DataInt.keyedArchiverClassFor_(data)
        if self.bytes_class in (bytes, bytearray):
            self.assertIs(cls, OC_BuiltinPythonData)
        else:
            self.assertIs(cls, OC_PythonData)

    def test_roundtrip_through_keyedarchive(self):
        data = self.bytes_class(b"hello to you too")

        if os_level_key(os_release()) >= os_level_key("10.13"):
            (
                blob,
                err,
            ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                data, False, None
            )
        else:
            blob = NSKeyedArchiver.archivedDataWithRootObject_(data)
            err = None
        self.assertIs(err, None)
        self.assertIsInstance(blob, NSData)

        copy = NSKeyedUnarchiver.unarchiveObjectWithData_(blob)
        self.assertIsInstance(copy, self.bytes_class)
        self.assertEqual(copy, data)

    def test_roundtrip_through_archive(self):
        data = self.bytes_class(b"hello to you too")

        blob = NSArchiver.archivedDataWithRootObject_(data)
        self.assertIsInstance(blob, NSData)

        copy = NSUnarchiver.unarchiveObjectWithData_(blob)
        self.assertEqual(copy, data)

        if self.bytes_class in (bytes, bytearray):
            # For interoperability with Objective-C code
            # bytes and bytearray are encoded as
            # NS(Mutable)Data in non-keyed archvies
            self.assertIsInstance(copy, NSMutableData)
        else:
            self.assertIsInstance(copy, self.bytes_class)


class TestReadingNonBytes(TestDataReading):
    bytes_class = SomeBytes

    def test_non_equal_defaults(self):
        v1 = self.bytes_class(b"hello")
        v2 = self.bytes_class(b"hello")

        self.assertIsInstance(v1.x, int)
        self.assertIsInstance(v2.x, int)

        self.assertNotEqual(v1.x, v2.x)
        self.assertNotEqual(v1, v2)
        self.assertEqual(bytes(v1), b"hello")


class TestDataWriting(TestDataReading):
    bytes_class = bytearray

    def test_set_bytes(self):
        data = self.bytes_class(b"hello world")

        OC_DataInt.setBytes_new_length_(data, b"12345678", 8)
        self.assertEqual(data, b"12345678rld")

    def test_cannot_set_readonly_bytes(self):
        data = b"hello world"

        # Copy of "data" in a way that not just an alias
        data2 = b"hello"
        data2 += b" world"

        self.assertIsNot(data, data2)

        with self.assertRaisesRegex(BufferError, "Object is not writable."):
            OC_DataInt.setBytes_new_length_(data, b"12345678", 8)

        # Make sure the buffer didn't change:
        self.assertEqual(data, data2)


class TestMisc(TestCase):
    # XXX: Create a custom helper class that will cause
    #      an error  in OCReleasedBuffer

    def test_using_array_array(self):
        for code, itemsize in (("b", 1), ("h", 2), ("i", 4), ("l", 8)):
            with self.subTest(code=code):
                a = array.array(code, [1, 2, 3, 4, 5])

                v = OC_DataInt.lengthOf_(a)
                self.assertEqual(v, 5 * itemsize)

                data = OC_DataInt.getBytes_length_(a, 5)
                if code == "b":
                    # XXX: Would be nice to test other codes as well,
                    # but this is good enough for now.
                    self.assertEqual(data, b"\x01\x02\x03\x04\x05")

                OC_DataInt.setBytes_new_length_(a, b"\x0a\x0b", 2)
                n = a[0]

                # XXX: As with getting it would be nice to test settting
                # with other values as well, but this is good enough.
                if code == "b":
                    self.assertEqual(n, 10)
                elif code == "h":
                    self.assertEqual(n, 11 << 8 | 10)

    def test_encoding_raises(self):
        data = SomeBytes(b"world")

        def raise_exception(coder, value):
            raise RuntimeError("Cannot encode")

        with pyobjc_options(_nscoding_encoder=raise_exception):
            with self.assertRaisesRegex(RuntimeError, "Cannot encode"):
                NSKeyedArchiver.archivedDataWithRootObject_(data)

    @min_os_level("10.12")
    def test_decoding_raises(self):
        # This is a known failure on macOS 10.11 due to behaviour of NSArchiver
        data = SomeBytes(b"world")

        def raise_exception(coder, value):
            raise RuntimeError("Cannot decode")

        with pyobjc_options(_nscoding_decoder=raise_exception):
            blob = NSKeyedArchiver.archivedDataWithRootObject_(data)

            with self.assertRaisesRegex(RuntimeError, "Cannot decode"):
                NSKeyedUnarchiver.unarchiveObjectWithData_(blob)

    def test_proxy_class(self):
        with self.subTest(bytes):
            self.assertIs(OC_TestSet.classOf_(b""), OC_BuiltinPythonData)
        with self.subTest(bytearray):
            self.assertIs(OC_TestSet.classOf_(bytearray()), OC_BuiltinPythonData)
        with self.subTest(SomeBytes):
            self.assertIs(OC_TestSet.classOf_(SomeBytes()), OC_PythonData)

    @min_os_level("10.13")
    def test_secure_coding(self):
        for cls in (bytes, bytearray):
            with self.subTest(cls):
                data = cls(b"hello")
                (
                    blob,
                    err,
                ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                    data, True, None
                )
                self.assertIs(err, None)
                self.assertIsInstance(blob, NSData)

                copy = NSKeyedUnarchiver.unarchiveObjectWithData_(blob)
                self.assertIs(err, None)
                self.assertIsInstance(copy, cls)
                self.assertEqual(copy, data)

        with self.subTest(SomeBytes):
            data = SomeBytes(b"hello")
            (
                blob,
                err,
            ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                data, True, None
            )
            self.assertIs(blob, None)
        self.assertIsInstance(err, objc.lookUpClass("NSError"))
