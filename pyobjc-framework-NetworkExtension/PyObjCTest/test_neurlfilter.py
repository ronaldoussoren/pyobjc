from PyObjCTools.TestSupport import TestCase
import NetworkExtension


class TestNEURLFilter(TestCase):
    def test_constants(self):
        self.assertIsEnumType(NetworkExtension.NEURLFilterVerdict)
        self.assertEqual(NetworkExtension.NEURLFilterVerdictUnknown, 1)
        self.assertEqual(NetworkExtension.NEURLFilterVerdictAllow, 2)
        self.assertEqual(NetworkExtension.NEURLFilterVerdictDeny, 3)
