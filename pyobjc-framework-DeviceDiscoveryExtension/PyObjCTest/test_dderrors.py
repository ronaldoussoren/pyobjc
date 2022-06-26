from PyObjCTools.TestSupport import TestCase
import DeviceDiscoveryExtension


class TesetDDErrors(TestCase):
    def test_constants(self):
        self.assertIsInstance(DeviceDiscoveryExtension.DDErrorDomain, str)
        self.assertEqual(DeviceDiscoveryExtension.DDErrorCodeSuccess, 0)
        self.assertEqual(DeviceDiscoveryExtension.DDErrorCodeUnknown, 350000)
        self.assertEqual(DeviceDiscoveryExtension.DDErrorCodeBadParameter, 350001)
        self.assertEqual(DeviceDiscoveryExtension.DDErrorCodeUnsupported, 350002)
        self.assertEqual(DeviceDiscoveryExtension.DDErrorCodeTimeout, 350003)
        self.assertEqual(DeviceDiscoveryExtension.DDErrorCodeInternal, 350004)
        self.assertEqual(DeviceDiscoveryExtension.DDErrorCodeMissingEntitlement, 350005)
        self.assertEqual(DeviceDiscoveryExtension.DDErrorCodePermission, 350006)

        self.assertNotHasAttr(DeviceDiscoveryExtension, "DDErrorCodeNext")
