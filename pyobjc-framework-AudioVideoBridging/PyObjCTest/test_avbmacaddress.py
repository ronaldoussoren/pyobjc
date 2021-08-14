from PyObjCTools.TestSupport import TestCase
import AudioVideoBridging


class TestAVBMACAddress(TestCase):
    def test_methods(self):
        self.assertArgIsIn(AudioVideoBridging.AVBMACAddress.initWithBytes_, 0)
        self.assertArgIsFixedSize(AudioVideoBridging.AVBMACAddress.initWithBytes_, 0, 6)

        self.assertResultIsFixedSize(AudioVideoBridging.AVBMACAddress.bytes, 6)

        self.assertResultIsBOOL(AudioVideoBridging.AVBMACAddress.isMulticast)
        self.assertArgIsBOOL(AudioVideoBridging.AVBMACAddress.setMulticast_, 0)
