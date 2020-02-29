import CoreAudio
from PyObjCTools.TestSupport import *


class TestHostTime(TestCase):
    def testFunctions(self):
        CoreAudio.AudioGetCurrentHostTime
        CoreAudio.AudioGetHostClockFrequency
        CoreAudio.AudioGetHostClockMinimumTimeDelta
        CoreAudio.AudioConvertNanosToHostTime


if __name__ == "__main__":
    main()
