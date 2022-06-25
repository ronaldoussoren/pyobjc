from PyObjCTools.TestSupport import TestCase

import SharedWithYou


class TestSWAttributionView(TestCase):
    def test_constants(self):
        self.assertIsEnumType(SharedWithYou.SWAttributionViewDisplayContext)
        self.assertEqual(SharedWithYou.SWAttributionViewDisplayContextSummary, 0)
        self.assertEqual(SharedWithYou.SWAttributionViewDisplayContextDetail, 1)

        self.assertIsEnumType(SharedWithYou.SWAttributionViewHorizontalAlignment)
        self.assertEqual(SharedWithYou.SWAttributionViewHorizontalAlignmentDefault, 0)
        self.assertEqual(SharedWithYou.SWAttributionViewHorizontalAlignmentLeading, 1)
        self.assertEqual(SharedWithYou.SWAttributionViewHorizontalAlignmentCenter, 2)
        self.assertEqual(SharedWithYou.SWAttributionViewHorizontalAlignmentTrailing, 3)

        self.assertIsEnumType(SharedWithYou.SWAttributionViewBackgroundStyle)
        self.assertEqual(SharedWithYou.SWAttributionViewBackgroundStyleDefault, 0)
        self.assertEqual(SharedWithYou.SWAttributionViewBackgroundStyleColor, 1)
        self.assertEqual(SharedWithYou.SWAttributionViewBackgroundStyleMaterial, 2)

    def test_methods(self):
        self.assertResultIsBOOL(SharedWithYou.SWAttributionView.enablesMarquee)
        self.assertArgIsBOOL(SharedWithYou.SWAttributionView.setEnablesMarquee_, 0)
