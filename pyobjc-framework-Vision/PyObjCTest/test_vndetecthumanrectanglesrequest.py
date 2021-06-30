from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectHumanRectanglesRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectHumanRectanglesRequestRevision1, 1)
        self.assertEqual(Vision.VNDetectHumanRectanglesRequestRevision2, 2)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(Vision.VNDetectHumanRectanglesRequest.upperBodyOnly)
        self.assertArgIsBOOL(Vision.VNDetectHumanRectanglesRequest.setUpperBodyOnly_, 0)
