import objc
from PyObjCTools.TestSupport import TestCase
from PyObjCTest.stringint import OC_StringInt, OC_BadString
import pickle

import weakref

NSString = objc.lookUpClass("NSString")


class TestUnicodeProxy(TestCase):
    def test_regr1(self):
        o = NSString.stringWithString_("hello")
        self.assertIsInstance(o.stringByAppendingFormat_, objc.selector)
        self.assertIsInstance(o.nsstring().stringByAppendingFormat_, objc.selector)

        # XXX: Can only test this one when Foundation wrappers are loaded:
        # self.assertEqual(o.stringByAppendingFormat_('foo %d', 42), 'hellofoo 42')

    def test_regr2(self):
        o = NSString.stringWithString_("hello")
        self.assertIsInstance(o.stringByAppendingString_, objc.selector)
        self.assertIsInstance(o.nsstring().stringByAppendingString_, objc.selector)

        self.assertEqual(o.stringByAppendingString_("foo %d"), "hellofoo %d")

    def test_wide_string(self):

        # UCS4 + single surrogate: cannot encode to UTF-8
        strval = "\U000fffff\uDBBB"

        with self.assertRaisesRegex(UnicodeEncodeError, "codec can't encode character"):
            NSString.stringWithString_(strval)

    def test_weakref(self):
        val = NSString.stringWithString_("groceries")

        cleared = []
        wr = weakref.ref(val, lambda x: cleared.append(x))

        self.assertIs(wr(), val)
        self.assertEqual(cleared, [])

        del val
        self.assertEqual(cleared, [wr])

    def test_pickling_restores_to_str(self):
        val = NSString.stringWithString_("cale")

        buf = pickle.dumps(val)
        copy = pickle.loads(buf)

        self.assertIs(type(copy), str)
        self.assertEqual(copy, val)

    def test_cannot_instantiate(self):
        with self.assertRaisesRegex(
            TypeError, "cannot create 'objc.pyobjc_unicode' instances"
        ):
            objc.pyobjc_unicode("foo")

    def test_create_emoji(self):
        o = NSString.stringWithString_("\N{GRINNING FACE}")
        self.assertEqual(o, "\N{GRINNING FACE}")

        # UCS2 in Objective-C land:
        self.assertEqual(o.length(), 2)

        o = NSString.stringWithString_("\N{GRINNING FACE}!")
        self.assertEqual(o, "\N{GRINNING FACE}!")

        # UCS2 in Objective-C land:
        self.assertEqual(o.length(), 3)

    def test_single_surrogate(self):
        o = OC_StringInt.getLowSurrogate()
        self.assertEqual(len(o), 1)
        self.assertEqual(ord(o), 0xDCCC)

        o = OC_StringInt.getHighSurrogate()
        self.assertEqual(len(o), 1)
        self.assertEqual(ord(o), 0xDBBB)

    def test_bad_surrogate_order(self):
        o = OC_StringInt.getBadPair()
        self.assertEqual(len(o), 2)
        self.assertEqual(ord(o[0]), 0xDC0B)
        self.assertEqual(ord(o[1]), 0xDB0B)

    def test_correctsurrogate(self):
        o = OC_StringInt.getCorrectPair()
        self.assertEqual(len(o), 1)
        self.assertEqual(
            ord(o), 0x10000 + ((0xDB0B & 0x03FF) << 10) + (0xDC0B & 0x03FF)
        )

    def test_extremepair(self):
        o = OC_StringInt.getExtremePair()
        self.assertEqual(len(o), 1)
        self.assertEqual(
            ord(o), 0x10000 + ((0xDBFF & 0x03FF) << 10) + (0xDFFF & 0x03FF)
        )

    def test_raising_conversion(self):
        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            OC_BadString.new()
