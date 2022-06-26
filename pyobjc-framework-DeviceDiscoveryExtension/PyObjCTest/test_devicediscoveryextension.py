from PyObjCTools.TestSupport import TestCase
import DeviceDiscoveryExtension


class TestDeviceDiscoveryExtension(TestCase):
    def test_metadata_sane(self):
        self.assertCallableMetadataIsSane(DeviceDiscoveryExtension)
