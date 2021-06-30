import FileProvider  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSFileProviderItemDecoration(TestCase):
    @min_sdk_level("11.0")
    def test_protocols11_0(self):
        objc.protocolNamed("NSFileProviderItemDecorating")
