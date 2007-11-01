'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import DictionaryServices

class TestDictionaryServices (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(DictionaryServices, 'DCSDictionaryRef') )
        self.assert_( issubclass(DictionaryServices.DCSDictionaryRef, objc.lookUpClass('NSCFType')) )
        self.assert_( DictionaryServices.DCSDictionaryRef is not objc.lookUpClass('NSCFType') )



    def testFunctions(self):
        self.assert_( hasattr(DictionaryServices, 'DCSGetTermRangeInString') )
        self.assert_( hasattr(DictionaryServices, 'DCSCopyTextDefinition') )


if __name__ == "__main__":
    unittest.main()

