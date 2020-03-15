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
            [
                (b"aap".decode("ascii"), b"monkey".decode("ascii")),
                (b"mies".decode("ascii"), b"missy".decode("ascii")),
                (b"noot".decode("ascii"), b"nut".decode("ascii")),
                (b"wim".decode("ascii"), b"john".decode("ascii")),
            ],
        )

    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFDictionaryGetTypeID(), int)

    def testCreation2(self):  # XXX
        dct = CoreFoundation.CFDictionaryCreate(
            None,
            [b"key1".decode("ascii"), b"key2".decode("ascii")],
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
            [b"key1".decode("ascii"), b"key2".decode("ascii")],
            [42, 42],
            2,
            CoreFoundation.kCFTypeDictionaryKeyCallBacks,
            CoreFoundation.kCFTypeDictionaryValueCallBacks,
        )
        self.assertIsInstance(dct, CoreFoundation.CFDictionaryRef)
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 2)
        self.assertEqual(
            CoreFoundation.CFDictionaryGetCountOfKey(dct, b"key1".decode("ascii")), 1
        )
        self.assertEqual(
            CoreFoundation.CFDictionaryGetCountOfKey(dct, b"key3".decode("ascii")), 0
        )
        self.assertEqual(CoreFoundation.CFDictionaryGetCountOfValue(dct, 42), 2)
        self.assertEqual(CoreFoundation.CFDictionaryGetCountOfValue(dct, 44), 0)
        self.assertResultHasType(CoreFoundation.CFDictionaryContainsKey, objc._C_NSBOOL)
        self.assertTrue(
            CoreFoundation.CFDictionaryContainsKey(dct, b"key1".decode("ascii"))
        )
        self.assertFalse(
            CoreFoundation.CFDictionaryContainsKey(dct, b"key3".decode("ascii"))
        )

        self.assertResultHasType(
            CoreFoundation.CFDictionaryContainsValue, objc._C_NSBOOL
        )
        self.assertTrue(CoreFoundation.CFDictionaryContainsValue(dct, 42))
        self.assertFalse(
            CoreFoundation.CFDictionaryContainsValue(dct, b"key3".decode("ascii"))
        )

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
        CoreFoundation.CFDictionaryAddValue(
            dct, b"key1".decode("ascii"), b"value1".decode("ascii")
        )
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 1)
        self.assertTrue(
            CoreFoundation.CFDictionaryContainsKey(dct, b"key1".decode("ascii"))
        )

        CoreFoundation.CFDictionarySetValue(
            dct, b"key2".decode("ascii"), b"value2".decode("ascii")
        )
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 2)
        self.assertTrue(
            CoreFoundation.CFDictionaryContainsKey(dct, b"key2".decode("ascii"))
        )

        CoreFoundation.CFDictionaryReplaceValue(
            dct, b"key2".decode("ascii"), b"value2b".decode("ascii")
        )
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 2)
        self.assertTrue(
            CoreFoundation.CFDictionaryContainsKey(dct, b"key2".decode("ascii"))
        )
        self.assertEqual(
            CoreFoundation.CFDictionaryGetValue(dct, "key2"), b"value2b".decode("ascii")
        )
        CoreFoundation.CFDictionaryReplaceValue(
            dct, b"key3".decode("ascii"), b"value2b".decode("ascii")
        )
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 2)
        self.assertFalse(
            CoreFoundation.CFDictionaryContainsKey(dct, b"key3".decode("ascii"))
        )

        CoreFoundation.CFDictionaryRemoveValue(dct, b"key1".decode("ascii"))
        self.assertFalse(
            CoreFoundation.CFDictionaryContainsKey(dct, b"key1".decode("ascii"))
        )

        CoreFoundation.CFDictionaryRemoveAllValues(dct)
        self.assertFalse(
            CoreFoundation.CFDictionaryContainsKey(dct, b"key2".decode("ascii"))
        )
        self.assertEqual(CoreFoundation.CFDictionaryGetCount(dct), 0)
