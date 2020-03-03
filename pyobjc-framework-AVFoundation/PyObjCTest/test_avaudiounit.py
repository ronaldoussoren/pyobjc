import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioUnit(TestCase):
    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioUnit.instantiateWithComponentDescription_options_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

        self.assertResultIsBOOL(
            AVFoundation.AVAudioUnit.loadAudioUnitPresetAtURL_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioUnit.loadAudioUnitPresetAtURL_error_, 1
        )  # noqa: B950
