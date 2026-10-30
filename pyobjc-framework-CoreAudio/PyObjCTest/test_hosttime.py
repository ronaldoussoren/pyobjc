import CoreAudio
from PyObjCTools.TestSupport import TestCase


class TestHostTime(TestCase):
    def test_functions(self):
        CoreAudio.AudioGetCurrentHostTime
        CoreAudio.AudioGetHostClockFrequency
        CoreAudio.AudioGetHostClockMinimumTimeDelta
        CoreAudio.AudioConvertNanosToHostTime
