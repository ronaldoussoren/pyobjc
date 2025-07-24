from PyObjCTools.TestSupport import TestCase, min_os_level

import SensitiveContentAnalysis

SCVideoStreamAnalysisChangeHandler = b"v@@"


class TestSCVideoStreamAnalyzer(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            SensitiveContentAnalysis.SCVideoStreamAnalyzerStreamDirection
        )
        self.assertEqual(
            SensitiveContentAnalysis.SCVideoStreamAnalyzerStreamDirectionOutgoing, 1
        )
        self.assertEqual(
            SensitiveContentAnalysis.SCVideoStreamAnalyzerStreamDirectionIncoming, 2
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBlock(
            SensitiveContentAnalysis.SCVideoStreamAnalyzer.analysisChangedHandler,
            SCVideoStreamAnalysisChangeHandler,
        )
        self.assertArgIsBlock(
            SensitiveContentAnalysis.SCVideoStreamAnalyzer.setAnalysisChangedHandler_,
            0,
            SCVideoStreamAnalysisChangeHandler,
        )

        self.assertArgIsOut(
            SensitiveContentAnalysis.SCVideoStreamAnalyzer.initWithParticipantUUID_streamDirection_error_,
            2,
        )

        self.assertResultIsBOOL(
            SensitiveContentAnalysis.SCVideoStreamAnalyzer.beginAnalysisOfDecompressionSession_error_
        )
        self.assertArgIsOut(
            SensitiveContentAnalysis.SCVideoStreamAnalyzer.beginAnalysisOfDecompressionSession_error_,
            1,
        )

        self.assertResultIsBOOL(
            SensitiveContentAnalysis.SCVideoStreamAnalyzer.beginAnalysisOfCaptureDeviceInput_error_
        )
        self.assertArgIsOut(
            SensitiveContentAnalysis.SCVideoStreamAnalyzer.beginAnalysisOfCaptureDeviceInput_error_,
            1,
        )

        self.assertResultIsBOOL(
            SensitiveContentAnalysis.SCVideoStreamAnalyzer.shouldInterruptVideo
        )
        self.assertResultIsBOOL(
            SensitiveContentAnalysis.SCVideoStreamAnalyzer.shouldIndicateSensitivity
        )
        self.assertResultIsBOOL(
            SensitiveContentAnalysis.SCVideoStreamAnalyzer.shouldMuteAudio
        )
