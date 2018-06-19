from PyObjCTools.TestSupport import *

import CoreAudio

class TestHostTime (TestCase):
    def testFunctions(self):
        CoreAudio.AudioGetCurrentHostTime
        CoreAudio.AudioGetHostClockFrequency
        CoreAudio.AudioGetHostClockMinimumTimeDelta
        CoreAudio.AudioConvertHostTimeToNanosAudioConvertNanosToHostTime

if __name__ == "__main__":
    main()
