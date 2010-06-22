from CoreFoundation import *
from Foundation import NSDictionary, NSMutableDictionary, NSCFDictionary
from PyObjCTools.TestSupport import *

class TestCFDictionary (TestCase):

    def testTypes(self):
        self.assertIs(CFDictionaryRef, NSCFDictionary)
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
                    (u'aap', u'monkey'),
                    (u'mies', u'missy'),
                    (u'noot', u'nut'),
                    (u'wim', u'john')
                ])

    def testTypeID(self):
        self.assertIsInstance(CFDictionaryGetTypeID(), (int, long))
    def testCreation(self):
        dct = CFDictionaryCreate(None, [u"key1", u"key2"], [42, 43], 2, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.assertIsInstance(dct, CFDictionaryRef)
        dct = CFDictionaryCreateCopy(None, dct)
        self.assertIsInstance(dct, CFDictionaryRef)
        dct = CFDictionaryCreateMutable(None, 0, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.assertIsInstance(dct, CFDictionaryRef)
        dct = CFDictionaryCreateMutableCopy(None, 0, dct)
        self.assertIsInstance(dct, CFDictionaryRef)
    def testInspection(self):
        dct = CFDictionaryCreate(None, [u"key1", u"key2"], [42, 42], 2, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.assertIsInstance(dct, CFDictionaryRef)
        self.assertEqual(CFDictionaryGetCount(dct) , 2)
        self.assertEqual(CFDictionaryGetCountOfKey(dct, u"key1") , 1)
        self.assertEqual(CFDictionaryGetCountOfKey(dct, u"key3") , 0)
        self.assertEqual(CFDictionaryGetCountOfValue(dct, 42) , 2)
        self.assertEqual(CFDictionaryGetCountOfValue(dct, 44) , 0)
        self.assertResultHasType(CFDictionaryContainsKey, objc._C_NSBOOL)
        self.assertTrue(CFDictionaryContainsKey(dct, u"key1"))
        self.assertFalse(CFDictionaryContainsKey(dct, u"key3"))

        self.assertResultHasType(CFDictionaryContainsValue, objc._C_NSBOOL)
        self.assertTrue(CFDictionaryContainsValue(dct, 42))
        self.assertFalse(CFDictionaryContainsValue(dct, u"key3"))

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
        CFDictionaryAddValue(dct, u"key1", u"value1")
        self.assertEqual(CFDictionaryGetCount(dct) , 1)
        self.assertTrue(CFDictionaryContainsKey(dct, u"key1"))

        CFDictionarySetValue(dct, u"key2", u"value2")
        self.assertEqual(CFDictionaryGetCount(dct) , 2)
        self.assertTrue(CFDictionaryContainsKey(dct, u"key2"))

        CFDictionaryReplaceValue(dct, u"key2", u"value2b")
        self.assertEqual(CFDictionaryGetCount(dct) , 2)
        self.assertTrue(CFDictionaryContainsKey(dct, u"key2"))
        self.assertEqual(CFDictionaryGetValue(dct, "key2") , u"value2b")
        CFDictionaryReplaceValue(dct, u"key3", u"value2b")
        self.assertEqual(CFDictionaryGetCount(dct) , 2)
        self.assertFalse(CFDictionaryContainsKey(dct, u"key3"))

        CFDictionaryRemoveValue(dct, u"key1")
        self.assertFalse(CFDictionaryContainsKey(dct, u"key1"))

        CFDictionaryRemoveAllValues(dct)
        self.assertFalse(CFDictionaryContainsKey(dct, u"key2"))
        self.assertEqual(CFDictionaryGetCount(dct) , 0)
if __name__ == "__main__":
    main()
