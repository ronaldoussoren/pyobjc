
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSText (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSEnterCharacter, 0x0003)
        self.failUnlessEqual(NSBackspaceCharacter, 0x0008)
        self.failUnlessEqual(NSTabCharacter, 0x0009)
        self.failUnlessEqual(NSNewlineCharacter, 0x000a)
        self.failUnlessEqual(NSFormFeedCharacter, 0x000c)
        self.failUnlessEqual(NSCarriageReturnCharacter, 0x000d)
        self.failUnlessEqual(NSBackTabCharacter, 0x0019)    
        self.failUnlessEqual(NSDeleteCharacter,  0x007f)
        self.failUnlessEqual(NSLineSeparatorCharacter, 0x2028)
        self.failUnlessEqual(NSParagraphSeparatorCharacter, 0x2029)
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



if __name__ == "__main__":
    main()
