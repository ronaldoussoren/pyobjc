import CoreFoundation
import objc
from PyObjCTools.TestSupport import TestCase


class TestAttributedString(TestCase):
    def testTypes(self):
        try:
            NSCFAttributedString = objc.lookUpClass("__NSCFAttributedString")
        except objc.error:
            NSCFAttributedString = objc.lookUpClass("NSCFAttributedString")

        self.assertIs(CoreFoundation.CFAttributedStringRef, NSCFAttributedString)
        self.assertIs(CoreFoundation.CFMutableAttributedStringRef, NSCFAttributedString)

    def testTypeID(self):
        v = CoreFoundation.CFAttributedStringGetTypeID()
        self.assertIsInstance(v, int)

    def testCreate(self):
        val = CoreFoundation.CFAttributedStringCreate(None, "hello", {"foo": 42})
        self.assertIsInstance(val, CoreFoundation.CFAttributedStringRef)
        val = CoreFoundation.CFAttributedStringCreateWithSubstring(None, val, (1, 2))
        self.assertIsInstance(val, CoreFoundation.CFAttributedStringRef)
        val2 = CoreFoundation.CFAttributedStringCreateCopy(None, val)
        self.assertIs(val2, val)

    def testGetting(self):
        val = CoreFoundation.CFAttributedStringCreate(
            None, "hello", {"foo": 42, "bar": b"baz"}
        )
        self.assertIsInstance(val, CoreFoundation.CFAttributedStringRef)
        dta = CoreFoundation.CFAttributedStringGetString(val)
        self.assertEqual(dta, "hello")
        length = CoreFoundation.CFAttributedStringGetLength(val)
        self.assertEqual(length, 5)
        v, rng = CoreFoundation.CFAttributedStringGetAttributes(val, 1, None)
        self.assertEqual(v, {"foo": 42, "bar": b"baz"})
        self.assertEqual(rng, (0, 5))
        v, rng = CoreFoundation.CFAttributedStringGetAttributes(val, 1, objc.NULL)
        self.assertEqual(v, {"foo": 42, "bar": b"baz"})
        self.assertEqual(rng, objc.NULL)
        v, rng = CoreFoundation.CFAttributedStringGetAttribute(val, 1, "foo", None)
        self.assertEqual(v, 42)
        self.assertEqual(rng, (0, 5))
        v, rng = CoreFoundation.CFAttributedStringGetAttribute(val, 1, "foo", objc.NULL)
        self.assertEqual(v, 42)
        self.assertEqual(rng, objc.NULL)
        v, rng = CoreFoundation.CFAttributedStringGetAttributesAndLongestEffectiveRange(
            val, 1, (0, 5), None
        )
        self.assertEqual(v, {"foo": 42, "bar": b"baz"})
        self.assertEqual(rng, (0, 5))
        v, rng = CoreFoundation.CFAttributedStringGetAttributesAndLongestEffectiveRange(
            val, 1, (0, 5), objc.NULL
        )
        self.assertEqual(v, {"foo": 42, "bar": b"baz"})
        self.assertEqual(rng, objc.NULL)
        v, rng = CoreFoundation.CFAttributedStringGetAttributeAndLongestEffectiveRange(
            val, 1, "bar", (0, 5), None
        )
        self.assertEqual(v, b"baz")
        self.assertEqual(rng, (0, 5))
        v, rng = CoreFoundation.CFAttributedStringGetAttributeAndLongestEffectiveRange(
            val, 1, "bar", (0, 5), objc.NULL
        )
        self.assertEqual(v, b"baz")
        self.assertEqual(rng, objc.NULL)

    def testMutableCopy(self):
        val = CoreFoundation.CFAttributedStringCreateMutable(None, 0)
        self.assertIsInstance(val, CoreFoundation.CFAttributedStringRef)
        orig = CoreFoundation.CFAttributedStringCreate(
            None, "hello", {"foo": 42, "bar": "baz"}
        )
        self.assertIsInstance(orig, CoreFoundation.CFAttributedStringRef)
        val = CoreFoundation.CFAttributedStringCreateMutableCopy(None, 0, orig)
        self.assertIsInstance(orig, CoreFoundation.CFAttributedStringRef)
        self.assertIsNot(val, orig)
        CoreFoundation.CFAttributedStringReplaceString(val, (0, 3), "Hal")
        dta = CoreFoundation.CFAttributedStringGetString(val)
        self.assertEqual(dta, "Hallo")
        v = CoreFoundation.CFAttributedStringGetMutableString(val)
        self.assertIs(v, None)
        CoreFoundation.CFAttributedStringSetAttributes(
            val, (0, 2), {"ronald": 99}, False
        )
        v, rng = CoreFoundation.CFAttributedStringGetAttributes(val, 1, None)
        self.assertEqual(v, {"ronald": 99, "foo": 42, "bar": "baz"})
        self.assertEqual(rng, (0, 2))
        v, rng = CoreFoundation.CFAttributedStringGetAttributes(val, 3, None)
        self.assertEqual(v, {"foo": 42, "bar": "baz"})
        self.assertEqual(rng, (2, 3))
        self.assertIsInstance(rng, CoreFoundation.CFRange)
        CoreFoundation.CFAttributedStringSetAttributes(
            val, (0, 2), {"ronald": 99}, True
        )
        v, rng = CoreFoundation.CFAttributedStringGetAttributes(val, 1, None)
        self.assertEqual(v, {"ronald": 99})
        self.assertEqual(rng, (0, 2))
        CoreFoundation.CFAttributedStringSetAttribute(val, (1, 3), "color", "blue")
        v, rng = CoreFoundation.CFAttributedStringGetAttributes(val, 1, None)
        self.assertEqual(v, {"ronald": 99, "color": "blue"})
        self.assertEqual(rng, (1, 1))
        CoreFoundation.CFAttributedStringRemoveAttribute(val, (1, 3), "color")
        v, rng = CoreFoundation.CFAttributedStringGetAttributes(val, 3, None)
        self.assertEqual(v, {"foo": 42, "bar": "baz"})
        self.assertEqual(rng, (2, 2))
        rep = CoreFoundation.CFAttributedStringCreate(None, "dummy", {"attrib": 99})
        CoreFoundation.CFAttributedStringReplaceAttributedString(val, (1, 3), rep)
        self.assertEqual(CoreFoundation.CFAttributedStringGetString(val), "Hdummyo")

    def testEditing(self):
        val = CoreFoundation.CFAttributedStringCreateMutable(None, 0)
        self.assertIsInstance(val, CoreFoundation.CFAttributedStringRef)
        CoreFoundation.CFAttributedStringBeginEditing(val)
        CoreFoundation.CFAttributedStringEndEditing(val)
