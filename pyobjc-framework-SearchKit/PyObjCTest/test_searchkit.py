"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
from PyObjCTools.TestSupport import *
import unittest

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import SearchKit


class TestSearchKit(TestCase):
    def testClasses(self):
        self.assertHasAttr(SearchKit, "SKDocumentRef")
        self.assertIsCFType(SearchKit.SKDocumentRef)

        self.assertHasAttr(SearchKit, "SKIndexRef")
        self.assertIsCFType(SearchKit.SKIndexRef)

    def testValues(self):
        self.assertHasAttr(SearchKit, "kSKIndexInverted")
        self.assertIsInstance(SearchKit.kSKIndexInverted, (int, long))
        self.assertEqual(SearchKit.kSKIndexInverted, 1)
        self.assertHasAttr(SearchKit, "kSKIndexInvertedVector")
        self.assertIsInstance(SearchKit.kSKIndexInvertedVector, (int, long))
        self.assertEqual(SearchKit.kSKIndexInvertedVector, 3)
        self.assertHasAttr(SearchKit, "kSKSearchRanked")
        self.assertIsInstance(SearchKit.kSKSearchRanked, (int, long))
        self.assertEqual(SearchKit.kSKSearchRanked, 0)

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        self.assertHasAttr(SearchKit, "kSKEndTermChars")
        self.assertIsInstance(SearchKit.kSKEndTermChars, (str, unicode))

    def testFunctions(self):
        self.assertHasAttr(SearchKit, "SKDocumentCreateWithURL")
        self.assertHasAttr(SearchKit, "SKDocumentCreate")
        self.assertHasAttr(SearchKit, "SKIndexOpenWithURL")
        self.assertHasAttr(SearchKit, "SKLoadDefaultExtractorPlugIns")


if __name__ == "__main__":
    main()
