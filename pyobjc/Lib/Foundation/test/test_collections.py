import unittest
import objc

from Foundation import *

samplePropertyList = '{ "" = 1; "x" = "2"; 1 = "one";}'

class TestCollections( unittest.TestCase ):
    def assertSameArrayContents(self, a1, a2):
        self.assertEqual(len(a1), len(a2))

        if isinstance(a2, NSArray):
            for o in a1:
                self.assert_( a2.indexOfObject_(o) != NSNotFound )
        else:
            for o in a1:
                a2.index(o)

        if isinstance(a1, NSArray):
            for o in a2:
                self.assert_( a1.indexOfObject_(o) != NSNotFound )
        else:
            for o in a2:
                a1.index(o)
    
    def assertSameDictionaryContents(self, d1, d2):
        self.assertEqual(len(d1), len(d2))

        self.assertSameArrayContents(d1.keys(), d2.keys())

        for k in d1:
            self.assertEqual(d1[k], d2[k],
                             "assertSameDictionary() failed for key '%s'." % k)
        for k in d2:
            self.assertEqual(d1[k], d2[k],
                             "assertSameDictionary() failed for key '%s'." % k)
                             
    def testConversion(self):
        originalNSDictionary = NSString.propertyList(samplePropertyList)
        aPythonDictionary = pythonCollectionFromPropertyList(originalNSDictionary)
        convertedNSDictionary = propertyListFromPythonCollection(aPythonDictionary)

        self.assertSameDictionaryContents(originalNSDictionary, originalNSDictionary)
        self.assertSameDictionaryContents(aPythonDictionary, aPythonDictionary)
        self.assertSameDictionaryContents(originalNSDictionary, aPythonDictionary)
        self.assertSameDictionaryContents(originalNSDictionary, convertedNSDictionary)
        self.assertSameDictionaryContents(convertedNSDictionary, aPythonDictionary)

def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestCollections ) )
    return suite

if __name__ == '__main__':
    try:
        unittest.main( )
    except SystemExit :
        pass
