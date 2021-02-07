import FileProvider  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSFileProviderItemDecoration(TestCase):
    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("NSFileProviderItemDecorating")
