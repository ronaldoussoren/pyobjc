import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSFileProviderServiceHelper(FileProvider.NSObject):
    def makeListenerEndpointAndReturnError_(self, a):
        return 1

    def isRestricted(self):
        return 1


class TestNSFileProviderService(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsOut(
            FileProvider.NSFileProviderExtension.supportedServiceSourcesForItemIdentifier_error_,  # noqa: B950
            1,
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            FileProvider.NSFileProviderManager.getServiceWithName_itemIdentifier_completionHandler_,
            2,
            b"v@@",
        )

    @min_sdk_level("11.0")
    def test_protocols(self):
        self.assertProtocolExists("NSFileProviderServiceSource", FileProvider)

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestNSFileProviderServiceHelper.makeListenerEndpointAndReturnError_,
            0,
            b"o^@",
        )
        self.assertResultIsBOOL(TestNSFileProviderServiceHelper.isRestricted)
