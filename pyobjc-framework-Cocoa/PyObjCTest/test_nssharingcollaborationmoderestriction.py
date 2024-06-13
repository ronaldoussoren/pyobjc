import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSSharingCollaborationModeRestriction(TestCase):
    def test_enum(self):
        self.assertIsEnumType(AppKit.NSSharingCollaborationMode)
        self.assertEqual(AppKit.NSSharingCollaborationModeSendCopy, 0)
        self.assertEqual(AppKit.NSSharingCollaborationModeCollaborate, 1)
