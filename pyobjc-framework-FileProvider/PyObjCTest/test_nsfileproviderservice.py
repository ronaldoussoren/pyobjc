import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileProviderService(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsOut(
            FileProvider.NSFileProviderExtension.supportedServiceSourcesForItemIdentifier_error_,  # noqa: B950
            1,
        )
