from PyObjCTools.TestSupport import TestCase

import CoreSpotlight


class TestCSSuggestion(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreSpotlight.CSSuggestionKind)
        self.assertEqual(CoreSpotlight.CSSuggestionKindNone, 0)
        self.assertEqual(CoreSpotlight.CSSuggestionKindCustom, 1)
        self.assertEqual(CoreSpotlight.CSSuggestionKindDefault, 2)
