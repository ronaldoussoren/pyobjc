from PyObjCTools.TestSupport import TestCase

import SharedWithYou


class TestSWHighlightChangeEvent(TestCase):
    def test_constants(self):
        self.assertIsEnumType(SharedWithYou.SWHighlightChangeEventTrigger)
        self.assertEqual(SharedWithYou.SWHighlightChangeEventTriggerEdit, 1)
        self.assertEqual(SharedWithYou.SWHighlightChangeEventTriggerComment, 2)
