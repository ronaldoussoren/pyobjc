import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSDraggingItem(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(AppKit.NSDraggingImageComponentKey, str)

    def test_constants(self):
        self.assertIsInstance(AppKit.NSDraggingImageComponentIconKey, str)
        self.assertIsInstance(AppKit.NSDraggingImageComponentLabelKey, str)

    def test_methods(self):
        self.assertArgIsBlock(
            AppKit.NSDraggingItem.setImageComponentsProvider_, 0, b"@"
        )
        self.assertResultIsBlock(AppKit.NSDraggingItem.imageComponentsProvider, b"@")
