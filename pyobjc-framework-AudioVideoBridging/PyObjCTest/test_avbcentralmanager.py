from PyObjCTools.TestSupport import TestCase, min_os_level
import AudioVideoBridging


class TestAVBCentralManager(TestCase):
    def test_constants(self):
        self.assertIsInstance(AudioVideoBridging.AVBNullEUI64, int)

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBOOL(
            AudioVideoBridging.AVBCentralManager.streamingEnabledInterfacesOnly
        )
