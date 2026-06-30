from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEFilterDataProvider(TestCase):
    def test_enums(self):
        self.assertIsEnumType(NetworkExtension.NEFilterDataAttribute)
        self.assertEqual(NetworkExtension.NEFilterDataAttributeHasIPHeader, 0x00000001)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            NetworkExtension.NEFilterDataProvider.applySettings_completionHandler_,
            1,
            b"v@",
        )
