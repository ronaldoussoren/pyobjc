import CoreFoundation
import objc
from PyObjCTools.TestSupport import TestCase


class TestCFDictionary(TestCase):
    def testCreation(self):
        dictionary = CoreFoundation.CFDictionaryCreate(
            None,
            ("aap", "noot", "mies", "wim"),
            ("monkey", "nut", "missy", "john"),
            4,
            CoreFoundation.kCFTypeDictionaryKeyCallBacks,
            CoreFoundation.kCFTypeDictionaryValueCallBacks,
        )
        self.assertIsInstance(dictionary, CoreFoundation.CFDictionaryRef)
        self.assertEqual(
            dictionary, {"aap": "monkey", "noot": "nut", "mies": "missy", "wim": "john"}
        )

        dictionary = CoreFoundation.CFDictionaryCreateMutable(
            None,
            0,
            CoreFoundation.kCFTypeDictionaryKeyCallBacks,
            CoreFoundation.kCFTypeDictionaryValueCallBacks,
        )
        self.assertIsInstance(dictionary, CoreFoundation.CFMutableDictionaryRef)
        CoreFoundation.CFDictionarySetValue(dictionary, "hello", "world")
        self.assertEqual(dictionary, {"hello": "world"})

    def testApplyFunction(self):
        dictionary = CoreFoundation.CFDictionaryCreate(
            None,
            ("aap", "noot", "mies", "wim"),
            ("monkey", "nut", "missy", "john"),
            4,
            CoreFoundation.kCFTypeDictionaryKeyCallBacks,
            CoreFoundation.kCFTypeDictionaryValueCallBacks,
        )

        context = []

        def function(key, value, context):
            context.append((key, value))

        self.assertArgIsFunction(
            CoreFoundation.CFDictionaryApplyFunction, 1, b"v@@@", False
        )
        self.assertArgHasType(CoreFoundation.CFDictionaryApplyFunction, 2, b"@")
        CoreFoundation.CFDictionaryApplyFunction(dictionary, function, context)

        context.sort()
        self.assertEqual(len(context), 4)
        self.assertEqual(
            context,
            [("aap", "monkey"), ("mies", "missy"), ("noot", "nut"), ("wim", "john")],
        )

    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFDictionaryGetTypeID(), int)

    def testCreation2(self):  # XXX
        dct = CoreFoundation.CFDictionaryCreate(
            None,
            ["key1" "key2"],
            [42, 43],
            2,
            CoreFoundation.kCFTypeDictionaryKeyCallBacks,
            CoreFoundation.kCFTypeDictionaryValueCallBacks,
        )
        self.assertIsInstance(dct, CoreFoundation.CFDictionaryRef)
        dct = CoreFoundation.CFDictionaryCreateCopy(None, dct)
        self.assertIsInstance(dct, CoreFoundation.CFDictionaryRef)
        dct = CoreFoundation.CFDictionaryCreateMutable(
            None,
            0,
            CoreFoundation.kCFTypeDictionaryKeyCallBacks,
            CoreFoundation.kCFTypeDictionaryValueCallBacks,
        )
        self.assertIsInstance(dct, CoreFoundation.CFDictionaryRef)
        dct = CoreFoundation.CFDictionaryCreateMutableCopy(None, 0, dct)
        self.assertIsInstance(dct, CoreFoundation.CFDictionaryRef)

    def testInspection(self):
        dct = CoreFoundation.CFDictionaryCreate(
            None,
            ["key1", "key2"],
            [42, 42],
            2,
            CoreFoundation.kCFTypeDictionaryKeyCallBacks,
            CoreFoundation.kCFTypeDictionaryValueCallBacks,
        )
        self.assertIsInstance(dct, CoreFoundation.CFDictionaryRef)
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 2)
        self.assertEqual(CoreFoundation.CFDictionaryGetCountOfKey(dct, "key1"), 1)
        self.assertEqual(CoreFoundation.CFDictionaryGetCountOfKey(dct, "key3"), 0)
        self.assertEqual(CoreFoundation.CFDictionaryGetCountOfValue(dct, 42), 2)
        self.assertEqual(CoreFoundation.CFDictionaryGetCountOfValue(dct, 44), 0)
        self.assertResultHasType(CoreFoundation.CFDictionaryContainsKey, objc._C_NSBOOL)
        self.assertTrue(CoreFoundation.CFDictionaryContainsKey(dct, "key1"))
        self.assertFalse(CoreFoundation.CFDictionaryContainsKey(dct, "key3"))

        self.assertResultHasType(
            CoreFoundation.CFDictionaryContainsValue, objc._C_NSBOOL
        )
        self.assertTrue(CoreFoundation.CFDictionaryContainsValue(dct, 42))
        self.assertFalse(CoreFoundation.CFDictionaryContainsValue(dct, "key3"))

        self.assertEqual(CoreFoundation.CFDictionaryGetValue(dct, "key2"), 42)
        self.assertIs(CoreFoundation.CFDictionaryGetValue(dct, "key3"), None)
        self.assertResultHasType(
            CoreFoundation.CFDictionaryGetValueIfPresent, objc._C_NSBOOL
        )
        self.assertArgIsOut(CoreFoundation.CFDictionaryGetValueIfPresent, 2)
        ok, value = CoreFoundation.CFDictionaryGetValueIfPresent(dct, "key2", None)
        self.assertTrue(ok)
        self.assertEqual(value, 42)
        ok, value = CoreFoundation.CFDictionaryGetValueIfPresent(dct, "key3", None)
        self.assertFalse(ok)
        self.assertIs(value, None)
        keys, values = CoreFoundation.CFDictionaryGetKeysAndValues(dct, None, None)
        self.assertEqual(values, (42, 42))
        keys = list(keys)
        keys.sort()
        self.assertEqual(keys, ["key1", "key2"])

    def testMutation(self):
        dct = CoreFoundation.CFDictionaryCreateMutable(
            None,
            0,
            CoreFoundation.kCFTypeDictionaryKeyCallBacks,
            CoreFoundation.kCFTypeDictionaryValueCallBacks,
        )
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 0)
        CoreFoundation.CFDictionaryAddValue(dct, "key1", "value1")
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 1)
        self.assertTrue(CoreFoundation.CFDictionaryContainsKey(dct, "key1"))

        CoreFoundation.CFDictionarySetValue(dct, "key2", "value2")
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 2)
        self.assertTrue(CoreFoundation.CFDictionaryContainsKey(dct, "key2"))

        CoreFoundation.CFDictionaryReplaceValue(dct, "key2", "value2b")
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 2)
        self.assertTrue(CoreFoundation.CFDictionaryContainsKey(dct, "key2"))
        self.assertEqual(CoreFoundation.CFDictionaryGetValue(dct, "key2"), "value2b")
        CoreFoundation.CFDictionaryReplaceValue(dct, "key3", "value2b")
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 2)
        self.assertFalse(CoreFoundation.CFDictionaryContainsKey(dct, "key3"))

        CoreFoundation.CFDictionaryRemoveValue(dct, "key1")
        self.assertFalse(CoreFoundation.CFDictionaryContainsKey(dct, "key1"))

        CoreFoundation.CFDictionaryRemoveAllValues(dct)
        self.assertFalse(CoreFoundation.CFDictionaryContainsKey(dct, "key2"))
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 0)
