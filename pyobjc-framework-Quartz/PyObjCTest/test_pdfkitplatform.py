from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFKitPlatform(TestCase):
    def testAliases(self):
        self.assertIs(Quartz.PDFKitPlatformView, Quartz.NSView)
        self.assertIs(Quartz.PDFKitPlatformViewController, Quartz.NSViewController)
        self.assertIs(Quartz.PDFKitPlatformScrollView, Quartz.NSScrollView)
        self.assertIs(Quartz.PDFKitPlatformColor, Quartz.NSColor)
        self.assertIs(Quartz.PDFKitPlatformBezierPath, Quartz.NSBezierPath)
        self.assertIs(
            Quartz.PDFKitPlatformBezierPathElement, Quartz.NSBezierPathElement
        )
        self.assertIs(Quartz.PDFKitPlatformImage, Quartz.NSImage)
        self.assertIs(Quartz.PDFKitPlatformImageView, Quartz.NSImageView)
        self.assertIs(Quartz.PDFKitPlatformEvent, Quartz.NSEvent)
        self.assertIs(Quartz.PDFKitPlatformFont, Quartz.NSFont)
        self.assertIs(Quartz.PDFKitPlatformColor, Quartz.NSColor)
        self.assertIs(Quartz.PDFKitPlatformControl, Quartz.NSControl)
        self.assertIs(Quartz.PDFKitPlatformTextField, Quartz.NSTextField)
        self.assertIs(Quartz.PDFKitPlatformTextView, Quartz.NSTextView)

        # @protocol:
        # self.assertIs(Quartz.PDFKitPlatformTextViewDelegate, Quartz.NSTextViewDelegate)
        self.assertIs(
            Quartz.PDFKitPlatformChoiceWidgetComboBoxView, Quartz.NSPopUpButton
        )
        self.assertIs(Quartz.PDFKitPlatformChoiceWidgetListView, Quartz.NSTableView)
        self.assertIs(Quartz.PDFKitPlatformButton, Quartz.NSButton)
        self.assertIs(Quartz.PDFKitPlatformButtonCell, Quartz.NSButtonCell)
        self.assertIs(Quartz.PDFKitResponder, Quartz.NSResponder)
        self.assertIs(Quartz.PDFKitTextContentType, Quartz.NSTextContentType)
        self.assertIs(Quartz.PDFKitPlatformTextContentType, Quartz.NSTextContentType)
        self.assertIs(Quartz.PDFPoint, Quartz.NSPoint)
        self.assertIs(Quartz.PDFRect, Quartz.NSRect)
        self.assertIs(Quartz.PDFSize, Quartz.NSSize)
        self.assertIs(Quartz.PDFEdgeInsets, Quartz.NSEdgeInsets)
        self.assertIs(Quartz.PDFPointZero, Quartz.NSZeroPoint)
        self.assertIs(Quartz.PDFSizeZero, Quartz.NSZeroSize)
        self.assertIs(Quartz.PDFRectZero, Quartz.NSZeroRect)
        self.assertIs(Quartz.PDFEdgeInsetsZero, Quartz.NSEdgeInsetsZero)
        self.assertIs(Quartz.PDFTrackingRunLoopMode, Quartz.NSEventTrackingRunLoopMode)

    @min_os_level("10.10")
    def test_aliases10_10(self):
        self.assertIs(
            Quartz.PDFKitPlatformAccessibilityElement, Quartz.NSAccessibilityElement
        )

    @min_os_level("10.11")
    def test_aliases10_11(self):
        self.assertIs(
            Quartz.PDFKitPlatformFontWeightRegular, Quartz.NSFontWeightRegular
        )
