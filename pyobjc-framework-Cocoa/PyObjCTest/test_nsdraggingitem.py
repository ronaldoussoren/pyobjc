import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSDraggingItem(TestCase):
    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AppKit.NSDraggingImageComponentIconKey, str)
        self.assertIsInstance(AppKit.NSDraggingImageComponentLabelKey, str)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBlock(
            AppKit.NSDraggingItem.setImageComponentsProvider_, 0, b"@"
        )
        self.assertResultIsBlock(AppKit.NSDraggingItem.imageComponentsProvider, b"@")
