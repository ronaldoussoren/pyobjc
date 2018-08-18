from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVAudioFile (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertArgIsOut(AVFoundation.AVAudioFile.initForReading_error_, 1)

        self.assertArgIsBOOL(AVFoundation.AVAudioFile.initForReading_commonFormat_interleaved_error_, 2)
        self.assertArgIsOut(AVFoundation.AVAudioFile.initForReading_commonFormat_interleaved_error_, 3)

        self.assertArgIsOut(AVFoundation.AVAudioFile.initForWriting_settings_error_, 2)

        self.assertArgIsBOOL(AVFoundation.AVAudioFile.initForWriting_settings_commonFormat_interleaved_error_, 3)
        self.assertArgIsOut(AVFoundation.AVAudioFile.initForWriting_settings_commonFormat_interleaved_error_, 4)

        self.assertResultIsBOOL(AVFoundation.AVAudioFile.readIntoBuffer_error_)
        self.assertArgIsOut(AVFoundation.AVAudioFile.readIntoBuffer_error_, 1)

        self.assertResultIsBOOL(AVFoundation.AVAudioFile.readIntoBuffer_frameCount_error_)
        self.assertArgIsOut(AVFoundation.AVAudioFile.readIntoBuffer_frameCount_error_, 2)

        self.assertResultIsBOOL(AVFoundation.AVAudioFile.writeFromBuffer_error_)
        self.assertArgIsOut(AVFoundation.AVAudioFile.writeFromBuffer_error_, 1)

if __name__ == "__main__":
    main()
