import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLUpdateProgressEvent(TestCase):
        def test_constants(self):
            self.assertEqual(CoreML.MLUpdateProgressEventTrainingBegin, 1 << 0)
            self.assertEqual(CoreML.MLUpdateProgressEventEpochEnd, 1 << 1)
            self.assertEqual(CoreML.MLUpdateProgressEventMiniBatchEnd, 1 << 2)


if __name__ == "__main__":
    main()
