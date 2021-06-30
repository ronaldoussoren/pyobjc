from PyObjCTools.TestSupport import TestCase, min_os_level
import AudioVideoBridging


class TestAVB17221Entity(TestCase):
    @min_os_level("10.8")
    def test_methods10_8(self):
        self.assertResultIsBOOL(AudioVideoBridging.AVB17221Entity.isLocalEntity)
        self.assertArgIsBOOL(AudioVideoBridging.AVB17221Entity.setLocalEntity_, 0)
