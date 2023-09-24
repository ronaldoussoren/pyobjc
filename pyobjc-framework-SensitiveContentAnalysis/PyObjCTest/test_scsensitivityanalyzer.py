from PyObjCTools.TestSupport import TestCase

import SensitiveContentAnalysis


class TestSCSensitivityAnalyzer(TestCase):
    def test_constants(self):
        self.assertIsEnumType(SensitiveContentAnalysis.SCSensitivityAnalysisPolicy)

        self.assertEqual(
            SensitiveContentAnalysis.SCSensitivityAnalysisPolicyDisabled, 0
        )
        self.assertEqual(
            SensitiveContentAnalysis.SCSensitivityAnalysisPolicySimpleInterventions, 1
        )
        self.assertEqual(
            SensitiveContentAnalysis.SCSensitivityAnalysisPolicyDescriptiveInterventions,
            2,
        )

    def test_methods(self):
        self.assertResultIsBOOL(
            SensitiveContentAnalysis.SCSensitivityAnalysis.isSensitive
        )

        self.assertArgIsBlock(
            SensitiveContentAnalysis.SCSensitivityAnalyzer.analyzeImageFile_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            SensitiveContentAnalysis.SCSensitivityAnalyzer.analyzeCGImage_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            SensitiveContentAnalysis.SCSensitivityAnalyzer.analyzeVideoFile_completionHandler_,
            1,
            b"v@@",
        )
