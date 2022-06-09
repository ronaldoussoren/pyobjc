from PyObjCTools.TestSupport import TestCase, min_os_level

import AudioVideoBridging


class TestAVBIPAddress(TestCase):
    @min_os_level("12.0")
    def test_methods(self):
        self.assertArgIsIn(AudioVideoBridging.AVBIPAddress.initWithIPv6Address_)
        self.assertArgSizeIs(
            AudioVideoBridging.AVBIPAddress.initWithIPv6Address_, 0, 16
        )

        self.assertResultIsBOOL(AudioVideoBridging.AVBIPAddress.representsIPv4Address)
