import CoreMediaIO
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level


class TestCMIOExtensionDeviceHelper(CoreMediaIO.NSObject):
    def devicePropertiesForProperties_error_(self, a, b):
        return 1

    def setDeviceProperties_error_(self, a, b):
        return 1


class TestCMIOExtensionDevice(TestCase):
    @min_sdk_level("12.3")
    def test_protocols(self):
        objc.protocolNamed("CMIOExtensionDeviceSource")

    def test_methods(self):
        self.assertArgHasType(
            TestCMIOExtensionDeviceHelper.devicePropertiesForProperties_error_,
            1,
            b"o^@",
        )

        self.assertResultIsBOOL(
            TestCMIOExtensionDeviceHelper.setDeviceProperties_error_
        )
        self.assertArgHasType(
            TestCMIOExtensionDeviceHelper.setDeviceProperties_error_, 1, b"o^@"
        )

    @min_os_level("12.3")
    def test_methods12_3(self):
        self.assertResultIsBOOL(CoreMediaIO.CMIOExtensionDevice.addStream_error_)
        self.assertArgIsOut(CoreMediaIO.CMIOExtensionDevice.addStream_error_, 1)

        self.assertResultIsBOOL(CoreMediaIO.CMIOExtensionDevice.removeStream_error_)
        self.assertArgIsOut(CoreMediaIO.CMIOExtensionDevice.removeStream_error_, 1)
