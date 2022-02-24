from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEFilterDataProvider(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(NetworkExtension.NEFilterDataAttribute)

    def test_constants(self):
        self.assertEqual(NetworkExtension.NEFilterDataAttributeHasIPHeader, 0x00000001)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            NetworkExtension.NEFilterDataProvider.applySettings_completionHandler_,
            1,
            b"v@",
        )
