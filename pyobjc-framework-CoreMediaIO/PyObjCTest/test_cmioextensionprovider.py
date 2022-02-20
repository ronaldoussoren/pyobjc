import CoreMediaIO
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level


class TestCMIOExtensionProviderHelper(CoreMediaIO.NSObject):
    def connectClient_error_(self, a, b):
        return 1

    def providerPropertiesForProperties_error_(self, a, b):
        return 1

    def setProviderProperties_error_(self, a, b):
        return 1


class TestCMIOExtensionProvider(TestCase):
    @min_os_level("12.3")
    def test_constants(self):
        self.assertIsInstance(CoreMediaIO.CMIOExtensionInfoDictionaryKey, str)
        self.assertIsInstance(CoreMediaIO.CMIOExtensionMachServiceNameKey, str)

    @min_sdk_level("12.3")
    def test_protocols(self):
        objc.protocolNamed("CMIOExtensionProviderSource")

    def test_methods(self):
        self.assertResultIsBOOL(TestCMIOExtensionProviderHelper.connectClient_error_)
        self.assertArgHasType(
            TestCMIOExtensionProviderHelper.connectClient_error_, 1, b"o^@"
        )

        self.assertArgHasType(
            TestCMIOExtensionProviderHelper.providerPropertiesForProperties_error_,
            1,
            b"o^@",
        )

        self.assertResultIsBOOL(
            TestCMIOExtensionProviderHelper.setProviderProperties_error_
        )
        self.assertArgHasType(
            TestCMIOExtensionProviderHelper.setProviderProperties_error_, 1, b"o^@"
        )

    @min_os_level("12.3")
    def test_methods12_3(self):
        self.assertResultIsBOOL(CoreMediaIO.CMIOExtensionProvider.addDevice_error_)
        self.assertArgIsOut(CoreMediaIO.CMIOExtensionProvider.addDevice_error_, 1)

        self.assertResultIsBOOL(CoreMediaIO.CMIOExtensionProvider.removeDevice_error_)
        self.assertArgIsOut(CoreMediaIO.CMIOExtensionProvider.removeDevice_error_, 1)
