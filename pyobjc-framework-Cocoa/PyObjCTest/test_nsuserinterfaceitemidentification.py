import AppKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestNSUserInterfaceItemIdentification(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(AppKit.NSUserInterfaceItemIdentifier, str)

    def test_protocols(self):
        self.assertProtocolExists("NSUserInterfaceItemIdentification", AppKit)
