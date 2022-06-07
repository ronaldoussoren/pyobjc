from PyObjCTools.TestSupport import TestCase

import SharedWithYou


class TestSWErrors(TestCase):
    def test_constants(self):
        self.assertIsEnumType(SharedWithYou.SWHighlightCenterErrorCode)
        self.assertEqual(SharedWithYou.SWHighlightCenterErrorCodeNoError, 0)
        self.assertEqual(SharedWithYou.SWHighlightCenterErrorCodeInternalError, 1)
        self.assertEqual(SharedWithYou.SWHighlightCenterErrorCodeInvalidURL, 2)
        self.assertEqual(SharedWithYou.SWHighlightCenterErrorCodeAccessDenied, 3)
