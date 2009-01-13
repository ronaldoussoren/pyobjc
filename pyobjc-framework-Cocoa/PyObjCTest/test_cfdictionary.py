from CoreFoundation import *
from Foundation import NSDictionary, NSMutableDictionary
from PyObjCTools.TestSupport import *

class TestCFDictionary (TestCase):

    def testCreation(self):
        dictionary = CFDictionaryCreate(None,
                ('aap', 'noot', 'mies', 'wim'),
                ('monkey', 'nut', 'missy', 'john'),
                4, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.assert_(isinstance(dictionary, CFDictionaryRef))
        self.assertEquals(dictionary, {
                'aap': 'monkey',
                'noot': 'nut',
                'mies': 'missy',
                'wim': 'john'
            })

        dictionary = CFDictionaryCreateMutable(None, 0, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.assert_(isinstance(dictionary, CFMutableDictionaryRef))
        CFDictionarySetValue(dictionary, 'hello', 'world')
        self.assertEquals(dictionary, {'hello': 'world'})

    def testApplyFunction(self):
        dictionary = CFDictionaryCreate(None,
                ('aap', 'noot', 'mies', 'wim'),
                ('monkey', 'nut', 'missy', 'john'), 4, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)

        context = []

        def function(key, value, context):
            context.append((key, value))

        CFDictionaryApplyFunction(dictionary, function, context)

        context.sort()
        self.failUnless(len(context) == 4)
        self.assertEquals(context,
                [
                    (u'aap', u'monkey'),
                    (u'mies', u'missy'),
                    (u'noot', u'nut'),
                    (u'wim', u'john')
                ])

    def testTypeID(self):
        self.failUnless(isinstance(CFDictionaryGetTypeID(), (int, long)))

    def testCreation(self):
        dct = CFDictionaryCreate(None, [u"key1", u"key2"], [42, 43], 2, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.failUnless(isinstance(dct, CFDictionaryRef))

        dct = CFDictionaryCreateCopy(None, dct)
        self.failUnless(isinstance(dct, CFDictionaryRef))

        dct = CFDictionaryCreateMutable(None, 0, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.failUnless(isinstance(dct, CFDictionaryRef))

        dct = CFDictionaryCreateMutableCopy(None, 0, dct)
        self.failUnless(isinstance(dct, CFDictionaryRef))

    def testInspection(self):
        dct = CFDictionaryCreate(None, [u"key1", u"key2"], [42, 42], 2, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.failUnless(isinstance(dct, CFDictionaryRef))

        self.failUnless(CFDictionaryGetCount(dct) == 2)
        self.failUnless(CFDictionaryGetCountOfKey(dct, u"key1") == 1)
        self.failUnless(CFDictionaryGetCountOfKey(dct, u"key3") == 0)

        self.failUnless(CFDictionaryGetCountOfValue(dct, 42) == 2)
        self.failUnless(CFDictionaryGetCountOfValue(dct, 44) == 0)

        self.failUnless(CFDictionaryContainsKey(dct, u"key1"))
        self.failIf(CFDictionaryContainsKey(dct, u"key3"))

        self.failUnless(CFDictionaryContainsValue(dct, 42))
        self.failIf(CFDictionaryContainsValue(dct, u"key3"))

        self.failUnless(CFDictionaryGetValue(dct, "key2") == 42)
        self.failUnless(CFDictionaryGetValue(dct, "key3") is None)

        ok, value = CFDictionaryGetValueIfPresent(dct, "key2", None)
        self.failUnless(ok)
        self.failUnless(value == 42)

        ok, value = CFDictionaryGetValueIfPresent(dct, "key3", None)
        self.failIf(ok)
        self.failUnless(value is None)


        keys, values = CFDictionaryGetKeysAndValues(dct, None, None)
        self.failUnless(values == (42, 42))
        keys = list(keys)
        keys.sort()
        self.failUnless(keys == ['key1', 'key2'])

    def testMutation(self):
        dct = CFDictionaryCreateMutable(None, 0, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks)
        self.failUnless(CFDictionaryGetCount(dct) == 0)

        CFDictionaryAddValue(dct, u"key1", u"value1")
        self.failUnless(CFDictionaryGetCount(dct) == 1)
        self.failUnless(CFDictionaryContainsKey(dct, u"key1"))

        CFDictionarySetValue(dct, u"key2", u"value2")
        self.failUnless(CFDictionaryGetCount(dct) == 2)
        self.failUnless(CFDictionaryContainsKey(dct, u"key2"))

        CFDictionaryReplaceValue(dct, u"key2", u"value2b")
        self.failUnless(CFDictionaryGetCount(dct) == 2)
        self.failUnless(CFDictionaryContainsKey(dct, u"key2"))
        self.failUnless(CFDictionaryGetValue(dct, "key2") == u"value2b")

        CFDictionaryReplaceValue(dct, u"key3", u"value2b")
        self.failUnless(CFDictionaryGetCount(dct) == 2)
        self.failIf(CFDictionaryContainsKey(dct, u"key3"))

        CFDictionaryRemoveValue(dct, u"key1")
        self.failIf(CFDictionaryContainsKey(dct, u"key1"))

        CFDictionaryRemoveAllValues(dct)
        self.failIf(CFDictionaryContainsKey(dct, u"key2"))
        self.failUnless(CFDictionaryGetCount(dct) == 0)

if __name__ == "__main__":
    main()
