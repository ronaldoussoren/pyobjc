from PyObjCTools.TestSupport import TestCase

import SharedWithYou


class TestSWHighlightMembershipEvent(TestCase):
    def test_constants(self):
        self.assertIsEnumType(SharedWithYou.SWHighlightMembershipEventTrigger)
        self.assertEqual(
            SharedWithYou.SWHighlightMembershipEventTriggerAddedCollaborator, 1
        )
        self.assertEqual(
            SharedWithYou.SWHighlightMembershipEventTriggerRemovedCollaborator, 2
        )
