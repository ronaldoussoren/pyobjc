'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import unittest
import CoreServices

class TestSearchKit (TestCase):
    def testClasses(self):
        self.assert_( hasattr(CoreServices, 'SKDocumentRef') )
        self.assertIsCFType( CoreServices.SKDocumentRef )

        self.assert_( hasattr(CoreServices, 'SKIndexRef') )
        self.assertIsCFType( CoreServices.SKIndexRef )

    def testValues(self):
        self.assert_( hasattr(CoreServices, 'kSKIndexInverted') )
        self.assert_( isinstance(CoreServices.kSKIndexInverted, (int, long)) )
        self.assertEquals(CoreServices.kSKIndexInverted, 1)
        self.assert_( hasattr(CoreServices, 'kSKIndexInvertedVector') )
        self.assert_( isinstance(CoreServices.kSKIndexInvertedVector, (int, long)) )
        self.assertEquals(CoreServices.kSKIndexInvertedVector, 3)
        self.assert_( hasattr(CoreServices, 'kSKSearchRanked') )
        self.assert_( isinstance(CoreServices.kSKSearchRanked, (int, long)) )
        self.assertEquals(CoreServices.kSKSearchRanked, 0)

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        self.assert_( hasattr(CoreServices, 'kSKEndTermChars') )
        self.assert_( isinstance(CoreServices.kSKEndTermChars, (str, unicode)) )

    def testFunctions(self):
        self.assert_( hasattr(CoreServices, 'SKDocumentCreateWithURL') )
        self.assert_( hasattr(CoreServices, 'SKDocumentCreate') )
        self.assert_( hasattr(CoreServices, 'SKIndexOpenWithURL') )
        self.assert_( hasattr(CoreServices, 'SKLoadDefaultExtractorPlugIns') )


if __name__ == "__main__":
    main()
