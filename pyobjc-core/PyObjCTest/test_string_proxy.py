from PyObjCTools.TestSupport import TestCase, pyobjc_options, min_os_level
from PyObjCTest.objectint import OC_ObjectInt
from PyObjCTest.stringint import OC_StringInt

import objc

NSData = objc.lookUpClass("NSData")
NSError = objc.lookUpClass("NSError")
NSArchiver = objc.lookUpClass("NSArchiver")
NSKeyedArchiver = objc.lookUpClass("NSKeyedArchiver")
NSUnarchiver = objc.lookUpClass("NSUnarchiver")
NSKeyedUnarchiver = objc.lookUpClass("NSKeyedUnarchiver")

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


class MyString(str):
    def __init__(self, *args, **kwds):
        super().__init__()
        self.attr = "attribute"


class TestString(TestCase):
    # XXX: Most of the functionality of
    # OC_PythonUnicode is covered by other
    # tests, move those to this file.
    test_value = "hello"

    def test_archiving(self):
        blob = NSArchiver.archivedDataWithRootObject_(self.test_value)
        self.assertIsInstance(blob, NSData)

        copy = NSUnarchiver.unarchiveObjectWithData_(blob)
        self.assertEqual(copy, self.test_value)
        self.assertIsInstance(copy, type(self.test_value))

    def test_keyedarchiving(self):
        blob = NSKeyedArchiver.archivedDataWithRootObject_(self.test_value)
        self.assertIsInstance(blob, NSData)

        copy = NSKeyedUnarchiver.unarchiveObjectWithData_(blob)
        self.assertEqual(copy, self.test_value)
        self.assertIsInstance(copy, type(self.test_value))

    @min_os_level("10.13")
    def test_secure_keyedarchiving(self):
        (
            blob,
            error,
        ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
            self.test_value, True, None
        )
        if type(self.test_value) is str:
            self.assertIs(error, None)
            self.assertIsInstance(blob, NSData)

            copy = NSKeyedUnarchiver.unarchiveObjectWithData_(blob)
            self.assertEqual(copy, self.test_value)
            self.assertIsInstance(copy, type(self.test_value))

        else:
            self.assertIs(blob, None)
            self.assertIsInstance(error, NSError)
            self.assertIn("disallows secure coding", str(error))

    def test_replacementobject(self):
        self.assertIs(
            self.test_value,
            OC_ObjectInt.replacementObjectForArchiver_of_(None, self.test_value),
        )
        self.assertIs(
            self.test_value,
            OC_ObjectInt.replacementObjectForKeyedArchiver_of_(None, self.test_value),
        )
        self.assertIs(
            self.test_value,
            OC_ObjectInt.replacementObjectForCoder_of_(None, self.test_value),
        )
        self.assertIs(
            self.test_value,
            OC_ObjectInt.replacementObjectForPortCoder_of_(None, self.test_value),
        )


class TestStringSubclass(TestString):
    test_value = MyString("hello")


class TestMisc(TestCase):
    def test_alternate_creation(self):
        value = OC_StringInt.createNonUTF8WithClass_(objc.lookUpClass("NSString"))
        self.assertIsInstance(value, objc.pyobjc_unicode)
        self.assertEqual(value, "hello world")

        value = OC_StringInt.createNonUTF8WithClass_(
            objc.lookUpClass("OC_PythonUnicode")
        )
        self.assertIs(type(value), str)
        self.assertEqual(value, "hello world")

    def test_keyedarchiving(self):
        def failed(*args, **kwds):
            raise TypeError("Cannot encode")

        with pyobjc_options(_nscoding_encoder=failed):
            with self.assertRaisesRegex(TypeError, "Cannot encode"):
                NSKeyedArchiver.archivedDataWithRootObject_(MyString("jojo"))

            # This should not fail:
            NSKeyedArchiver.archivedDataWithRootObject_("putty")

        blob = NSKeyedArchiver.archivedDataWithRootObject_(MyString("jojo"))

        with pyobjc_options(_nscoding_decoder=None):
            with self.assertRaisesRegex(
                ValueError,
                "decoding Python objects is not supported",
            ):
                NSKeyedUnarchiver.unarchiveObjectWithData_(blob)

        with pyobjc_options(_nscoding_encoder=None):
            with self.assertRaisesRegex(
                ValueError,
                "encoding Python objects is not supported",
            ):
                NSKeyedArchiver.archivedDataWithRootObject_(MyString("jojo"))

            # This should not fail:
            NSKeyedArchiver.archivedDataWithRootObject_("putty")

    @min_os_level("10.12")
    def test_keyedarchiving_raises(self):
        # Known error on macOS 10.11 due to behaviour of NSCoder
        def failed(*args, **kwds):
            raise TypeError("Cannot encode")

        blob = NSKeyedArchiver.archivedDataWithRootObject_(MyString("jojo"))
        with pyobjc_options(_nscoding_decoder=failed):
            with self.assertRaisesRegex(TypeError, "Cannot encode"):
                NSKeyedUnarchiver.unarchiveObjectWithData_(blob)
