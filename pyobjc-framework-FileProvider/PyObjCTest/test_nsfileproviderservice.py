import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileProviderServiceHelper(FileProvider.NSObject):
    def makeListenerEndpointAndReturnError_(self, a):
        return 1


class TestNSFileProviderService(TestCase):
    def test_methods(self):
        self.assertArgHasType(
            TestNSFileProviderServiceHelper.makeListenerEndpointAndReturnError_,
            0,
            b"o^@",
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsOut(
            FileProvider.NSFileProviderExtension.supportedServiceSourcesForItemIdentifier_error_,  # noqa: B950
            1,
        )
