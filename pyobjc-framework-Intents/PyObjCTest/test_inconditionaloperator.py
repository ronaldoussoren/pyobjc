from PyObjCTools.TestSupport import TestCase
import Intents


class TestINConditionalOperator(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INConditionalOperator)
        self.assertEqual(Intents.INConditionalOperatorAll, 0)
        self.assertEqual(Intents.INConditionalOperatorAny, 1)
        self.assertEqual(Intents.INConditionalOperatorNone, 2)
