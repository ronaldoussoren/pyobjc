from PyObjCTools.TestSupport import TestCase, min_os_level
import ServiceManagement


class TestSMAppService(TestCase):
    def test_constants(self):
        self.assertIsEnumType(ServiceManagement.SMAppServiceStatus)
        self.assertEqual(ServiceManagement.SMAppServiceStatusNotRegistered, 0)
        self.assertEqual(ServiceManagement.SMAppServiceStatusEnabled, 1)
        self.assertEqual(ServiceManagement.SMAppServiceStatusRequiresApproval, 2)
        self.assertEqual(ServiceManagement.SMAppServiceStatusNotFound, 3)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(ServiceManagement.SMAppService.registerAndReturnError_)
        self.assertArgIsOut(ServiceManagement.SMAppService.registerAndReturnError_, 0)

        self.assertResultIsBOOL(
            ServiceManagement.SMAppService.unregisterAndReturnError_
        )
        self.assertArgIsOut(ServiceManagement.SMAppService.unregisterAndReturnError_, 0)

        self.assertArgIsBlock(
            ServiceManagement.SMAppService.unregisterWithCompletionHandler_, 0, b"v@"
        )
