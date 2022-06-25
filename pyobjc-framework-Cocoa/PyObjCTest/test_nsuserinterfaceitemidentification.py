import AppKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSUserInterfaceItemIdentification(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSUserInterfaceItemIdentifier, str)

    @min_os_level("10.7")
    def testProtocols(self):
        self.assertProtocolExists("NSUserInterfaceItemIdentification")
