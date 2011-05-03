'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import unittest
import SearchKit

class TestSearchKit (TestCase):
    def testClasses(self):
        self.assert_( hasattr(SearchKit, 'SKDocumentRef') )
        self.assertIsCFType( SearchKit.SKDocumentRef )

        self.assert_( hasattr(SearchKit, 'SKIndexRef') )
        self.assertIsCFType( SearchKit.SKIndexRef )

    def testValues(self):
        self.assert_( hasattr(SearchKit, 'kSKIndexInverted') )
        self.assert_( isinstance(SearchKit.kSKIndexInverted, (int, long)) )
        self.assertEquals(SearchKit.kSKIndexInverted, 1)
        self.assert_( hasattr(SearchKit, 'kSKIndexInvertedVector') )
        self.assert_( isinstance(SearchKit.kSKIndexInvertedVector, (int, long)) )
        self.assertEquals(SearchKit.kSKIndexInvertedVector, 3)
        self.assert_( hasattr(SearchKit, 'kSKSearchRanked') )
        self.assert_( isinstance(SearchKit.kSKSearchRanked, (int, long)) )
        self.assertEquals(SearchKit.kSKSearchRanked, 0)

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        self.assert_( hasattr(SearchKit, 'kSKEndTermChars') )
        self.assert_( isinstance(SearchKit.kSKEndTermChars, (str, unicode)) )

    def testFunctions(self):
        self.assert_( hasattr(SearchKit, 'SKDocumentCreateWithURL') )
        self.assert_( hasattr(SearchKit, 'SKDocumentCreate') )
        self.assert_( hasattr(SearchKit, 'SKIndexOpenWithURL') )
        self.assert_( hasattr(SearchKit, 'SKLoadDefaultExtractorPlugIns') )


if __name__ == "__main__":
    main()

