"""
Some simple tests to check that the framework is properly wrapped.
"""

import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestSearchKit(TestCase):
    def testClasses(self):
        self.assertTrue(hasattr(CoreServices, "SKDocumentRef"))
        self.assertIsCFType(CoreServices.SKDocumentRef)

        self.assertTrue(hasattr(CoreServices, "SKIndexRef"))
        self.assertIsCFType(CoreServices.SKIndexRef)

    def testValues(self):
        self.assertTrue(hasattr(CoreServices, "kSKIndexInverted"))
        self.assertTrue(isinstance(CoreServices.kSKIndexInverted, int))
        self.assertEqual(CoreServices.kSKIndexInverted, 1)
        self.assertTrue(hasattr(CoreServices, "kSKIndexInvertedVector"))
        self.assertTrue(isinstance(CoreServices.kSKIndexInvertedVector, int))
        self.assertEqual(CoreServices.kSKIndexInvertedVector, 3)
        self.assertTrue(hasattr(CoreServices, "kSKSearchRanked"))
        self.assertTrue(isinstance(CoreServices.kSKSearchRanked, int))
        self.assertEqual(CoreServices.kSKSearchRanked, 0)

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        self.assertTrue(hasattr(CoreServices, "kSKEndTermChars"))
        self.assertTrue(isinstance(CoreServices.kSKEndTermChars, str))

    def testFunctions(self):
        self.assertTrue(hasattr(CoreServices, "SKDocumentCreateWithURL"))
        self.assertTrue(hasattr(CoreServices, "SKDocumentCreate"))
        self.assertTrue(hasattr(CoreServices, "SKIndexOpenWithURL"))
        self.assertTrue(hasattr(CoreServices, "SKLoadDefaultExtractorPlugIns"))
