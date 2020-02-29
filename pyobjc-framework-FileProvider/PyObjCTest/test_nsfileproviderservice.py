import FileProvider
from PyObjCTools.TestSupport import *


class TestNSFileProviderService(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(
            FileProvider.NSFileProviderExtension.supportedServiceSourcesForItemIdentifier_error_,
            1,
        )
