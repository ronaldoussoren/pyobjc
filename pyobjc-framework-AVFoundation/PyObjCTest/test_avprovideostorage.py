import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVProVideoStorage(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVProVideoStorage.isSupported)
        self.assertResultIsBOOL(AVFoundation.AVProVideoStorage.isBusy)
