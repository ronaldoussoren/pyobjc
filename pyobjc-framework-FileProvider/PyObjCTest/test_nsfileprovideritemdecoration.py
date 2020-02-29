import FileProvider
from PyObjCTools.TestSupport import *


class TestNSFileProviderItemDecoration(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("NSFileProviderItemDecorating")
