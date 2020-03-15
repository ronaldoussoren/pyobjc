import CoreAudio
from PyObjCTools.TestSupport import TestCase


class TestHostTime(TestCase):
    def testFunctions(self):
        CoreAudio.AudioGetCurrentHostTime
        CoreAudio.AudioGetHostClockFrequency
        CoreAudio.AudioGetHostClockMinimumTimeDelta
        CoreAudio.AudioConvertNanosToHostTime
