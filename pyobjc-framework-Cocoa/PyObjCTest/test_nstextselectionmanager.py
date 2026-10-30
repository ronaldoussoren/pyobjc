import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSTextSelectionManagerHelper(AppKit.NSObject):
    def selectionManager_shouldBeginSelectionAtPoint_(self, a, b):
        return 1

    def selectionManager_locationOfTextContainerAtPoint_(self, a, b):
        return 1

    def selectionManager_frameOfTextContainerAtPoint_(self, a, b):
        return 1


class TestNSTextSelectionManager(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSTextSelectionMode)
        self.assertEqual(AppKit.NSTextSelectionModeEditable, 0)
        self.assertEqual(AppKit.NSTextSelectionModeSelectable, 1)
        self.assertEqual(AppKit.NSTextSelectionModeNonInteractive, 2)

    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists("NSTextSelectionManagerDelegate", AppKit)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestNSTextSelectionManagerHelper.selectionManager_shouldBeginSelectionAtPoint_
        )
        self.assertArgHasType(
            TestNSTextSelectionManagerHelper.selectionManager_shouldBeginSelectionAtPoint_,
            1,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextSelectionManagerHelper.selectionManager_locationOfTextContainerAtPoint_,
            1,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextSelectionManagerHelper.selectionManager_frameOfTextContainerAtPoint_,
            1,
            AppKit.NSPoint.__typestr__,
        )
