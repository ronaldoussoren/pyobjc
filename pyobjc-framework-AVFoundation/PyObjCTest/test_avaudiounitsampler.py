import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVUnitSampler(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAudioUnitSampler.loadSoundBankInstrumentAtURL_program_bankMSB_bankLSB_error_  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioUnitSampler.loadSoundBankInstrumentAtURL_program_bankMSB_bankLSB_error_,  # noqa: B950
            4,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVAudioUnitSampler.loadInstrumentAtURL_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioUnitSampler.loadInstrumentAtURL_error_, 1
        )

        self.assertResultIsBOOL(
            AVFoundation.AVAudioUnitSampler.loadAudioFilesAtURLs_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioUnitSampler.loadAudioFilesAtURLs_error_, 1
        )
