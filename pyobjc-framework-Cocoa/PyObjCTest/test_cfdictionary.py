from CoreFoundation import *
from Foundation import NSDictionary, NSMutableDictionary, NSCFDictionary
from PyObjCTools.TestSupport import *

try:
    long
except NameError:
    long = int


class TestCFDictionary (TestCase):

    def testCreation(self):
        dictionary = CFDictionaryCreate(None,
                ('aap', 'noot', 'mies', 'wim'),
                ('monkey', 'nut', 'missy', 'john'),
                4, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.assert_(isinstance(dictionary, CFDictionaryRef))
        self.assertEqual(dictionary, {
                'aap': 'monkey',
                'noot': 'nut',
                'mies': 'missy',
                'wim': 'john'
            })

        dictionary = CFDictionaryCreateMutable(None, 0, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.assert_(isinstance(dictionary, CFMutableDictionaryRef))
        CFDictionarySetValue(dictionary, 'hello', 'world')
        self.assertEqual(dictionary, {'hello': 'world'})

    def testApplyFunction(self):
        dictionary = CFDictionaryCreate(None,
                ('aap', 'noot', 'mies', 'wim'),
                ('monkey', 'nut', 'missy', 'john'), 4, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)

        context = []

        def function(key, value, context):
            context.append((key, value))

        self.assertArgIsFunction(CFDictionaryApplyFunction, 1, b'v@@@', False)
        self.assertArgHasType(CFDictionaryApplyFunction, 2, b'@')
        CFDictionaryApplyFunction(dictionary, function, context)

        context.sort()
        self.assertEqual(len(context) , 4)
        self.assertEqual(context,
                [
                    (b'aap'.decode('ascii'), b'monkey'.decode('ascii')),
                    (b'mies'.decode('ascii'), b'missy'.decode('ascii')),
                    (b'noot'.decode('ascii'), b'nut'.decode('ascii')),
                    (b'wim'.decode('ascii'), b'john'.decode('ascii'))
                ])

    def testTypeID(self):
        self.assertIsInstance(CFDictionaryGetTypeID(), (int, long))
    def testCreation(self):
        dct = CFDictionaryCreate(None, [b"key1".decode('ascii'), b"key2".decode('ascii')], [42, 43], 2, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.assertIsInstance(dct, CFDictionaryRef)
        dct = CFDictionaryCreateCopy(None, dct)
        self.assertIsInstance(dct, CFDictionaryRef)
        dct = CFDictionaryCreateMutable(None, 0, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.assertIsInstance(dct, CFDictionaryRef)
        dct = CFDictionaryCreateMutableCopy(None, 0, dct)
        self.assertIsInstance(dct, CFDictionaryRef)
    def testInspection(self):
        dct = CFDictionaryCreate(None, [b"key1".decode('ascii'), b"key2".decode('ascii')], [42, 42], 2, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.assertIsInstance(dct, CFDictionaryRef)
        self.assertEqual(CFDictionaryGetCount(dct) , 2)
        self.assertEqual(CFDictionaryGetCountOfKey(dct, b"key1".decode('ascii')) , 1)
        self.assertEqual(CFDictionaryGetCountOfKey(dct, b"key3".decode('ascii')) , 0)
        self.assertEqual(CFDictionaryGetCountOfValue(dct, 42) , 2)
        self.assertEqual(CFDictionaryGetCountOfValue(dct, 44) , 0)
        self.assertResultHasType(CFDictionaryContainsKey, objc._C_NSBOOL)
        self.assertTrue(CFDictionaryContainsKey(dct, b"key1".decode('ascii')))
        self.assertFalse(CFDictionaryContainsKey(dct, b"key3".decode('ascii')))

        self.assertResultHasType(CFDictionaryContainsValue, objc._C_NSBOOL)
        self.assertTrue(CFDictionaryContainsValue(dct, 42))
        self.assertFalse(CFDictionaryContainsValue(dct, b"key3".decode('ascii')))

        self.assertEqual(CFDictionaryGetValue(dct, "key2") , 42)
        self.assertIs(CFDictionaryGetValue(dct, "key3"), None)
        self.assertResultHasType(CFDictionaryGetValueIfPresent, objc._C_NSBOOL)
        self.assertArgIsOut(CFDictionaryGetValueIfPresent, 2)
        ok, value = CFDictionaryGetValueIfPresent(dct, "key2", None)
        self.assertTrue(ok)
        self.assertEqual(value , 42)
        ok, value = CFDictionaryGetValueIfPresent(dct, "key3", None)
        self.assertFalse(ok)
        self.assertIs(value, None)
        keys, values = CFDictionaryGetKeysAndValues(dct, None, None)
        self.assertEqual(values , (42, 42))
        keys = list(keys)
        keys.sort()
        self.assertEqual(keys , ['key1', 'key2'])
    def testMutation(self):
        dct = CFDictionaryCreateMutable(None, 0, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.assertEqual(CFDictionaryGetCount(dct) , 0)
        CFDictionaryAddValue(dct, b"key1".decode('ascii'), b"value1".decode('ascii'))
        self.assertEqual(CFDictionaryGetCount(dct) , 1)
        self.assertTrue(CFDictionaryContainsKey(dct, b"key1".decode('ascii')))

        CFDictionarySetValue(dct, b"key2".decode('ascii'), b"value2".decode('ascii'))
        self.assertEqual(CFDictionaryGetCount(dct) , 2)
        self.assertTrue(CFDictionaryContainsKey(dct, b"key2".decode('ascii')))

        CFDictionaryReplaceValue(dct, b"key2".decode('ascii'), b"value2b".decode('ascii'))
        self.assertEqual(CFDictionaryGetCount(dct) , 2)
        self.assertTrue(CFDictionaryContainsKey(dct, b"key2".decode('ascii')))
        self.assertEqual(CFDictionaryGetValue(dct, "key2") , b"value2b".decode('ascii'))
        CFDictionaryReplaceValue(dct, b"key3".decode('ascii'), b"value2b".decode('ascii'))
        self.assertEqual(CFDictionaryGetCount(dct) , 2)
        self.assertFalse(CFDictionaryContainsKey(dct, b"key3".decode('ascii')))

        CFDictionaryRemoveValue(dct, b"key1".decode('ascii'))
        self.assertFalse(CFDictionaryContainsKey(dct, b"key1".decode('ascii')))

        CFDictionaryRemoveAllValues(dct)
        self.assertFalse(CFDictionaryContainsKey(dct, b"key2".decode('ascii')))
        self.assertEqual(CFDictionaryGetCount(dct) , 0)
if __name__ == "__main__":
    main()
