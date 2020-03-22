import SoundAnalysis
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSNAnalyzer(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            SoundAnalysis.SNAudioStreamAnalyzer.addRequest_withObserver_error_
        )
        self.assertArgIsOut(
            SoundAnalysis.SNAudioStreamAnalyzer.addRequest_withObserver_error_, 2
        )

        self.assertArgIsOut(SoundAnalysis.SNAudioFileAnalyzer.initWithURL_error_, 1)

        self.assertResultIsBOOL(
            SoundAnalysis.SNAudioStreamAnalyzer.addRequest_withObserver_error_
        )
        self.assertArgIsOut(
            SoundAnalysis.SNAudioStreamAnalyzer.addRequest_withObserver_error_, 2
        )

        self.assertArgIsBlock(
            SoundAnalysis.SNAudioFileAnalyzer.analyzeWithCompletionHandler_, 0, b"v@"
        )
