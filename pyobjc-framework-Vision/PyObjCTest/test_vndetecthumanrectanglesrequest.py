import sys


if sys.maxsize >= 2 ** 32:
    from PyObjCTools.TestSupport import TestCase
    import Vision

    class TestVNDetectHumanRectanglesRequest(TestCase):
        def test_constants(self):
            self.assertEqual(Vision.VNDetectHumanRectanglesRequestRevision1, 1)
