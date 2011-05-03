import unittest
import objc

from Foundation import *
from PyObjCTools.Conversion import *

samplePropertyList = u'{ "" = 1; "x" = "2"; 1 = "one";}'

class TestCollections(unittest.TestCase):
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
            self.assert_(d1.has_key(k), "Missing key %s in %s"%(`k`, `d1`))
            self.assert_(d2.has_key(k), "Missing key %s in %s"%(`k`, `d2`))
            self.assertEqual(d1[k], d2[k],
                             "assertSameDictionary() failed for key '%s'. [%s != %s]" % (k, d1[k], d2[k]))
        for k in d2:
            self.assert_(d1.has_key(k), "Missing key %s in %s"%(`k`, `d1`))
            self.assert_(d2.has_key(k), "Missing key %s in %s"%(`k`, `d2`))
            self.assertEqual(d1[k], d2[k],
                             "assertSameDictionary() failed for key '%s'. [%s != %s]" % (k, d1[k], d2[k]))

    def testConversion(self):
        originalNSDictionary = NSString.propertyList(samplePropertyList)
        aPythonDictionary = pythonCollectionFromPropertyList(originalNSDictionary)
        convertedNSDictionary = propertyListFromPythonCollection(aPythonDictionary)

        self.assertSameDictionaryContents(originalNSDictionary, originalNSDictionary)
        self.assertSameDictionaryContents(aPythonDictionary, aPythonDictionary)
        self.assertSameDictionaryContents(originalNSDictionary, aPythonDictionary)
        self.assertSameDictionaryContents(originalNSDictionary, convertedNSDictionary)
        self.assertSameDictionaryContents(convertedNSDictionary, aPythonDictionary)

    def testIntegerConversion(self):
        x = NSArray.arrayWithArray_([1,2,3,4])
        y = pythonCollectionFromPropertyList(x)
        z = propertyListFromPythonCollection(y)

        self.assertSameArrayContents(x,y)
        self.assertSameArrayContents(x,z)
        self.assertSameArrayContents(z,y)

    def testHelpers(self):
        def conversionHelper(anObject):
            return anObject

        self.assertRaises(TypeError, propertyListFromPythonCollection, { u'1' : type([]) })
        propertyListFromPythonCollection({u'1' : type([])}, conversionHelper)

        d = NSDictionary.dictionaryWithDictionary_( {u'1' : NSObject.alloc().init() })
        # was: NSBundle.bundleForClass_(NSObject)} )
        # XXX: using NSBundle doesn't work on GNUstep

        self.assertRaises(TypeError, pythonCollectionFromPropertyList, d)
        pythonCollectionFromPropertyList(d, conversionHelper)


if __name__ == '__main__':
    try:
        unittest.main( )
    except SystemExit :
        pass
    objc.recycleAutoreleasePool()
