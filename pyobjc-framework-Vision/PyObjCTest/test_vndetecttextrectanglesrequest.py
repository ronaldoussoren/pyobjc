from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectTextRectanglesRequest(TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(
            Vision.VNDetectTextRectanglesRequest.reportCharacterBoxes
        )
        self.assertArgIsBOOL(
            Vision.VNDetectTextRectanglesRequest.setReportCharacterBoxes_, 0
        )

    def test_constants(self):
        self.assertEqual(Vision.VNDetectTextRectanglesRequestRevision1, 1)
