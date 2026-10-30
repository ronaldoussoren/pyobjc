from PyObjCTools.TestSupport import TestCase
import AudioVideoBridging


class TestAVB17221Entity(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AudioVideoBridging.AVB17221Entity.isLocalEntity)
        self.assertArgIsBOOL(AudioVideoBridging.AVB17221Entity.setLocalEntity_, 0)
