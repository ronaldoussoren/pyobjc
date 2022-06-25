import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSTextHelper(AppKit.NSObject):
    def textShouldBeginEditing_(self, t):
        return 1

    def textShouldEndEditing_(self, t):
        return 1


class TestNSText(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTextAlignment)
        self.assertIsEnumType(AppKit.NSTextMovement)
        self.assertIsEnumType(AppKit.NSWritingDirection)

    def testConstants(self):
        self.assertEqual(AppKit.NSEnterCharacter, chr(0x0003))
        self.assertEqual(AppKit.NSBackspaceCharacter, chr(0x0008))
        self.assertEqual(AppKit.NSTabCharacter, chr(0x0009))
        self.assertEqual(AppKit.NSNewlineCharacter, chr(0x000A))
        self.assertEqual(AppKit.NSFormFeedCharacter, chr(0x000C))
        self.assertEqual(AppKit.NSCarriageReturnCharacter, chr(0x000D))
        self.assertEqual(AppKit.NSBackTabCharacter, chr(0x0019))
        self.assertEqual(AppKit.NSDeleteCharacter, chr(0x007F))
        self.assertEqual(AppKit.NSLineSeparatorCharacter, chr(0x2028))
        self.assertEqual(AppKit.NSParagraphSeparatorCharacter, chr(0x2029))

        self.assertEqual(AppKit.NSLeftTextAlignment, 0)
        self.assertEqual(AppKit.NSJustifiedTextAlignment, 3)
        self.assertEqual(AppKit.NSNaturalTextAlignment, 4)

        self.assertEqual(AppKit.NSTextAlignmentLeft, 0)
        if objc.arch == "x86_64":
            self.assertEqual(AppKit.NSTextAlignmentRight, 1)
            self.assertEqual(AppKit.NSTextAlignmentCenter, 2)
        else:
            self.assertEqual(AppKit.NSTextAlignmentCenter, 1)
            self.assertEqual(AppKit.NSTextAlignmentRight, 2)

        self.assertEqual(AppKit.NSRightTextAlignment, AppKit.NSTextAlignmentRight)
        self.assertEqual(AppKit.NSCenterTextAlignment, AppKit.NSTextAlignmentCenter)

        self.assertEqual(AppKit.NSTextAlignmentJustified, 3)
        self.assertEqual(AppKit.NSTextAlignmentNatural, 4)

        self.assertEqual(AppKit.NSWritingDirectionNatural, -1)
        self.assertEqual(AppKit.NSWritingDirectionLeftToRight, 0)
        self.assertEqual(AppKit.NSWritingDirectionRightToLeft, 1)

        self.assertEqual(AppKit.NSIllegalTextMovement, 0)
        self.assertEqual(AppKit.NSReturnTextMovement, 0x10)
        self.assertEqual(AppKit.NSTabTextMovement, 0x11)
        self.assertEqual(AppKit.NSBacktabTextMovement, 0x12)
        self.assertEqual(AppKit.NSLeftTextMovement, 0x13)
        self.assertEqual(AppKit.NSRightTextMovement, 0x14)
        self.assertEqual(AppKit.NSUpTextMovement, 0x15)
        self.assertEqual(AppKit.NSDownTextMovement, 0x16)
        self.assertEqual(AppKit.NSCancelTextMovement, 0x17)
        self.assertEqual(AppKit.NSOtherTextMovement, 0)

        self.assertIsInstance(AppKit.NSTextDidBeginEditingNotification, str)
        self.assertIsInstance(AppKit.NSTextDidEndEditingNotification, str)
        self.assertIsInstance(AppKit.NSTextDidChangeNotification, str)

        self.assertEqual(AppKit.NSTextMovementReturn, 0x10)
        self.assertEqual(AppKit.NSTextMovementTab, 0x11)
        self.assertEqual(AppKit.NSTextMovementBacktab, 0x12)
        self.assertEqual(AppKit.NSTextMovementLeft, 0x13)
        self.assertEqual(AppKit.NSTextMovementRight, 0x14)
        self.assertEqual(AppKit.NSTextMovementUp, 0x15)
        self.assertEqual(AppKit.NSTextMovementDown, 0x16)
        self.assertEqual(AppKit.NSTextMovementCancel, 0x17)
        self.assertEqual(AppKit.NSTextMovementOther, 0)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(AppKit.NSTextWritingDirectionEmbedding, 0 << 1)
        self.assertEqual(AppKit.NSTextWritingDirectionOverride, 1 << 1)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AppKit.NSTextMovementUserInfoKey, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSText.writeRTFDToFile_atomically_)
        self.assertArgIsBOOL(AppKit.NSText.writeRTFDToFile_atomically_, 1)
        self.assertResultIsBOOL(AppKit.NSText.readRTFDFromFile_)
        self.assertResultIsBOOL(AppKit.NSText.isEditable)
        self.assertArgIsBOOL(AppKit.NSText.setEditable_, 0)
        self.assertResultIsBOOL(AppKit.NSText.isSelectable)
        self.assertArgIsBOOL(AppKit.NSText.setSelectable_, 0)
        self.assertResultIsBOOL(AppKit.NSText.isRichText)
        self.assertArgIsBOOL(AppKit.NSText.setRichText_, 0)
        self.assertResultIsBOOL(AppKit.NSText.importsGraphics)
        self.assertArgIsBOOL(AppKit.NSText.setImportsGraphics_, 0)
        self.assertResultIsBOOL(AppKit.NSText.isFieldEditor)
        self.assertArgIsBOOL(AppKit.NSText.setFieldEditor_, 0)
        self.assertResultIsBOOL(AppKit.NSText.usesFontPanel)
        self.assertArgIsBOOL(AppKit.NSText.setUsesFontPanel_, 0)
        self.assertResultIsBOOL(AppKit.NSText.drawsBackground)
        self.assertArgIsBOOL(AppKit.NSText.setDrawsBackground_, 0)
        self.assertResultIsBOOL(AppKit.NSText.isRulerVisible)
        self.assertResultIsBOOL(AppKit.NSText.isHorizontallyResizable)
        self.assertArgIsBOOL(AppKit.NSText.setHorizontallyResizable_, 0)
        self.assertResultIsBOOL(AppKit.NSText.isVerticallyResizable)
        self.assertArgIsBOOL(AppKit.NSText.setVerticallyResizable_, 0)

    @min_sdk_level("10.6")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSTextDelegate")

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSTextHelper.textShouldBeginEditing_)
        self.assertResultIsBOOL(TestNSTextHelper.textShouldEndEditing_)
