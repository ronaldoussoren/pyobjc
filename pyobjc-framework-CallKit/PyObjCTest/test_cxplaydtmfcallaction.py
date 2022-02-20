from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXPlayDTMFCallAction(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CallKit.CXPlayDTMFCallActionType)

    def test_constants(self):
        self.assertEqual(CallKit.CXPlayDTMFCallActionTypeSingleTone, 1)
        self.assertEqual(CallKit.CXPlayDTMFCallActionTypeSoftPause, 2)
        self.assertEqual(CallKit.CXPlayDTMFCallActionTypeHardPause, 3)
