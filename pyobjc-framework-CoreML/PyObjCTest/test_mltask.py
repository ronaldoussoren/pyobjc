from PyObjCTools.TestSupport import TestCase
import CoreML


class TestMLTask(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreML.MLTaskState)

    def test_constants(self):
        self.assertEqual(CoreML.MLTaskStateSuspended, 1)
        self.assertEqual(CoreML.MLTaskStateRunning, 2)
        self.assertEqual(CoreML.MLTaskStateCancelling, 3)
        self.assertEqual(CoreML.MLTaskStateCompleted, 4)
        self.assertEqual(CoreML.MLTaskStateFailed, 5)
