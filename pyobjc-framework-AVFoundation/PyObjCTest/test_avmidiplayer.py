from PyObjCTools.TestSupport import *

import AVFoundation

AVMIDIPlayerCompletionHandler = b'v'

class TestAVMIDIPlayer (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertArgIsOut(AVFoundation.AVMIDIPlayer.initWithContentsOfURL_soundBankURL_error_, 2)
        self.assertArgIsOut(AVFoundation.AVMIDIPlayer.initWithData_soundBankURL_error_, 2)

        self.assertArgIsBlock(AVFoundation.AVMIDIPlayer.play_, 0, AVMIDIPlayerCompletionHandler)
        self.assertResultIsBOOL(AVFoundation.AVMIDIPlayer.isPlaying)

if __name__ == "__main__":
    main()
