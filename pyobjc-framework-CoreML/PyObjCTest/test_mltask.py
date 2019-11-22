import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLTask(TestCase):
        def test_constants(self):
            self.assertEqual(CoreML.MLTaskStateSuspended, 1)
            self.assertEqual(CoreML.MLTaskStateRunning, 2)
            self.assertEqual(CoreML.MLTaskStateCancelling, 3)
            self.assertEqual(CoreML.MLTaskStateCompleted, 4)
            self.assertEqual(CoreML.MLTaskStateFailed, 5)


if __name__ == "__main__":
    main()
