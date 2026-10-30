import BrowserEngineKit
from PyObjCTools.TestSupport import TestCase


class TestBEWebContentFilter(TestCase):
    def test_enums(self):
        self.assertIsEnumType(BrowserEngineKit.BEWebContentFilterPermissionDecision)
        self.assertEqual(BrowserEngineKit.BEWebContentFilterPermissionDecisionError, 0)
        self.assertEqual(
            BrowserEngineKit.BEWebContentFilterPermissionDecisionAllowed, 1
        )
        self.assertEqual(BrowserEngineKit.BEWebContentFilterPermissionDecisionDenied, 2)
        self.assertEqual(
            BrowserEngineKit.BEWebContentFilterPermissionDecisionPending, 3
        )
