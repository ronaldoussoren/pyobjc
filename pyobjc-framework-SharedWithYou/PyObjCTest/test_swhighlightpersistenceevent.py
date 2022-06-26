from PyObjCTools.TestSupport import TestCase

import SharedWithYou


class TestSWHighlightPersistenceEvent(TestCase):
    def test_constants(self):
        self.assertIsEnumType(SharedWithYou.SWHighlightPersistenceEventTrigger)
        self.assertEqual(SharedWithYou.SWHighlightPersistenceEventTriggerCreated, 1)
        self.assertEqual(SharedWithYou.SWHighlightPersistenceEventTriggerDeleted, 2)
        self.assertEqual(SharedWithYou.SWHighlightPersistenceEventTriggerRenamed, 3)
        self.assertEqual(SharedWithYou.SWHighlightPersistenceEventTriggerMoved, 4)
