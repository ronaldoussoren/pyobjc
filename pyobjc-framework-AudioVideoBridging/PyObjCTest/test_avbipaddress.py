from PyObjCTools.TestSupport import TestCase
import AudioVideoBridging


class TestAVBIPAddress(TestCase):
    def test_methods(self):
        self.assertArgIsIn(AudioVideoBridging.AVBIPAddress.initWithIPv6Address_, 0)
        self.assertArgSizeIs(
            AudioVideoBridging.AVBIPAddress.initWithIPv6Address_, 0, 16
        )

        self.assertResultIsBOOL(AudioVideoBridging.AVBIPAddress.representsIPv4Address)
