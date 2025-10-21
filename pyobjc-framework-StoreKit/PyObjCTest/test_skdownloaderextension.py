import StoreKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestSKDownloaderExtension(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("SKDownloaderExtension")
