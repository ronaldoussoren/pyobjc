
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextHelper (NSObject):
    def textShouldBeginEditing_(self, t): return 1
    def textShouldEndEditing_(self, t): return 1

class TestNSText (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSEnterCharacter, unichr(0x0003))
        self.failUnlessEqual(NSBackspaceCharacter, unichr(0x0008))
        self.failUnlessEqual(NSTabCharacter, unichr(0x0009))
        self.failUnlessEqual(NSNewlineCharacter, unichr(0x000a))
        self.failUnlessEqual(NSFormFeedCharacter, unichr(0x000c))
        self.failUnlessEqual(NSCarriageReturnCharacter, unichr(0x000d))
        self.failUnlessEqual(NSBackTabCharacter, unichr(0x0019))
        self.failUnlessEqual(NSDeleteCharacter,  unichr(0x007f))
        self.failUnlessEqual(NSLineSeparatorCharacter, unichr(0x2028))
        self.failUnlessEqual(NSParagraphSeparatorCharacter, unichr(0x2029))
        self.failUnlessEqual(NSLeftTextAlignment, 0)
        self.failUnlessEqual(NSRightTextAlignment, 1)
        self.failUnlessEqual(NSCenterTextAlignment, 2)
        self.failUnlessEqual(NSJustifiedTextAlignment, 3)
        self.failUnlessEqual(NSNaturalTextAlignment, 4)

        self.failUnlessEqual(NSWritingDirectionNatural, -1)
        self.failUnlessEqual(NSWritingDirectionLeftToRight, 0)
        self.failUnlessEqual(NSWritingDirectionRightToLeft, 1)

        self.failUnlessEqual(NSIllegalTextMovement, 0)
        self.failUnlessEqual(NSReturnTextMovement, 0x10)
        self.failUnlessEqual(NSTabTextMovement, 0x11)
        self.failUnlessEqual(NSBacktabTextMovement, 0x12)
        self.failUnlessEqual(NSLeftTextMovement, 0x13)
        self.failUnlessEqual(NSRightTextMovement, 0x14)
        self.failUnlessEqual(NSUpTextMovement, 0x15)
        self.failUnlessEqual(NSDownTextMovement, 0x16)
        self.failUnlessEqual(NSCancelTextMovement, 0x17)
        self.failUnlessEqual(NSOtherTextMovement, 0)

        self.failUnlessIsInstance(NSTextDidBeginEditingNotification, unicode)
        self.failUnlessIsInstance(NSTextDidEndEditingNotification, unicode)
        self.failUnlessIsInstance(NSTextDidChangeNotification, unicode)

    def testMehods(self):
        self.failUnlessResultIsBOOL(NSText.writeRTFDToFile_atomically_)
        self.failUnlessArgIsBOOL(NSText.writeRTFDToFile_atomically_, 1)
        self.failUnlessResultIsBOOL(NSText.readRTFDFromFile_)
        self.failUnlessResultIsBOOL(NSText.isEditable)
        self.failUnlessArgIsBOOL(NSText.setEditable_, 0)
        self.failUnlessResultIsBOOL(NSText.isSelectable)
        self.failUnlessArgIsBOOL(NSText.setSelectable_, 0)
        self.failUnlessResultIsBOOL(NSText.isRichText)
        self.failUnlessArgIsBOOL(NSText.setRichText_, 0)
        self.failUnlessResultIsBOOL(NSText.importsGraphics)
        self.failUnlessArgIsBOOL(NSText.setImportsGraphics_, 0)
        self.failUnlessResultIsBOOL(NSText.isFieldEditor)
        self.failUnlessArgIsBOOL(NSText.setFieldEditor_, 0)
        self.failUnlessResultIsBOOL(NSText.usesFontPanel)
        self.failUnlessArgIsBOOL(NSText.setUsesFontPanel_, 0)
        self.failUnlessResultIsBOOL(NSText.drawsBackground)
        self.failUnlessArgIsBOOL(NSText.setDrawsBackground_, 0)
        self.failUnlessResultIsBOOL(NSText.isRulerVisible)
        self.failUnlessResultIsBOOL(NSText.isHorizontallyResizable)
        self.failUnlessArgIsBOOL(NSText.setHorizontallyResizable_, 0)
        self.failUnlessResultIsBOOL(NSText.isVerticallyResizable)
        self.failUnlessArgIsBOOL(NSText.setVerticallyResizable_, 0)

    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestNSTextHelper.textShouldBeginEditing_)
        self.failUnlessResultIsBOOL(TestNSTextHelper.textShouldEndEditing_)

if __name__ == "__main__":
    main()
