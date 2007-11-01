from CoreFoundation import *
from Foundation import NSDictionary, NSMutableDictionary
import unittest

class TestCFDictionary (unittest.TestCase):
    def testCreation(self):
        dictionary = NSDictionary.dictionaryWithDictionary_(
                { 'aap': 'monkey', 'noot': 'nut', 'mies': 'missy',
                  'wim': 'john' })
        #dictionary = CFDictionaryCreate(None,
        #        ('aap', 'noot', 'mies', 'wim'),
        #        ('monkey', 'nut', 'missy', 'john'),
        #        4,
        #        kCFTypeDictionaryKeyCallBacks,
        #         kCFTypeDictionaryValueCallBacks)
        self.assert_(isinstance(dictionary, CFDictionaryRef))
        self.assertEquals(dictionary, {
                'aap': 'monkey',
                'noot': 'nut',
                'mies': 'missy',
                'wim': 'john'
            })

        #dictionary = CFDictionaryCreateMutable(
        #        None, 0, 
        #        kCFTypeDictionaryKeyCallBacks,
        #         kCFTypeDictionaryValueCallBacks)
        dictionary = NSMutableDictionary.dictionary()
        self.assert_(isinstance(dictionary, CFMutableDictionaryRef))
        CFDictionarySetValue(dictionary, 'hello', 'world')
        self.assertEquals(dictionary, {'hello': 'world'})

    def testApplyFunction(self):
        dictionary = NSDictionary.dictionaryWithDictionary_({
                'foo': 'bar',
                40: 42,
            })

if __name__ == "__main__":
    unittest.main()
