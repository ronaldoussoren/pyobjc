from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNWPath(TestCase):
    def test_enums(self):
        self.assertIsEnumType(NetworkExtension.NWPathStatus)
        self.assertEqual(NetworkExtension.NWPathStatusInvalid, 0)
        self.assertEqual(NetworkExtension.NWPathStatusSatisfied, 1)
        self.assertEqual(NetworkExtension.NWPathStatusUnsatisfied, 2)
        self.assertEqual(NetworkExtension.NWPathStatusSatisfiable, 3)

    @min_os_level("10.11")
    def test_methods(self):
        self.assertResultIsBOOL(NetworkExtension.NWPath.isExpensive)
        self.assertResultIsBOOL(NetworkExtension.NWPath.isEqualToPath_)
