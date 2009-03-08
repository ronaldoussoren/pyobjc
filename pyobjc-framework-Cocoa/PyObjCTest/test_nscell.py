from PyObjCTools.TestSupport import *
import objc

from AppKit import *

class TestNSCell(TestCase):
    def testUnicode(self):
        u = u'\xc3\xbc\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8d\xc3\xa8'
        cell = NSCell.alloc().initTextCell_(u)
        cell.setStringValue_(u)
        self.assertEquals(cell.stringValue(), u)

    def testInt(self):
        i = 17
        cell = NSCell.alloc().initTextCell_(u"")
        cell.setIntValue_(i)
        self.assertEquals(cell.intValue(), i)

    def testFloat(self):
        f = 3.125
        cell = NSCell.alloc().initTextCell_(u"")
        cell.setFloatValue_(f)
        self.assertEquals(cell.floatValue(), f)

    def testMethods(self):
        self.fail("- (void)setAction:(SEL)aSelector;")

    def testFunctions(self):
        self.fail("APPKIT_EXTERN void NSDrawThreePartImage(NSRect frame, NSImage *startCap, NSImage *centerFill, NSImage *endCap, BOOL vertical, NSCompositingOperation op, CGFloat alphaFraction, BOOL flipped) AVAILABLE_MAC_OS_X_VERSION_10_5_AND_LATER;")

        self.fail("APPKIT_EXTERN void NSDrawNinePartImage(NSRect frame, NSImage *topLeftCorner, NSImage *topEdgeFill, NSImage *topRightCorner, NSImage *leftEdgeFill, NSImage *centerFill, NSImage *rightEdgeFill, NSImage *bottomLeftCorner, NSImage *bottomEdgeFill, NSImage *bottomRightCorner, NSCompositingOperation op, CGFloat alphaFraction, BOOL flipped) AVAILABLE_MAC_OS_X_VERSION_10_5_AND_LATER;")


    def testConstants(self):
        self.failUnlessIsInstance(NSControlTintDidChangeNotification, unicode)

        self.failUnlessEqual(NSAnyType, 0)
        self.failUnlessEqual(NSIntType, 1)
        self.failUnlessEqual(NSPositiveIntType, 2)
        self.failUnlessEqual(NSFloatType, 3)
        self.failUnlessEqual(NSPositiveFloatType, 4)
        self.failUnlessEqual(NSDoubleType, 6)
        self.failUnlessEqual(NSPositiveDoubleType, 7)
        self.failUnlessEqual(NSNullCellType, 0)
        self.failUnlessEqual(NSTextCellType, 1)
        self.failUnlessEqual(NSImageCellType, 2)
        self.failUnlessEqual(NSCellDisabled, 0)
        self.failUnlessEqual(NSCellState, 1)
        self.failUnlessEqual(NSPushInCell, 2)
        self.failUnlessEqual(NSCellEditable, 3)
        self.failUnlessEqual(NSChangeGrayCell, 4)
        self.failUnlessEqual(NSCellHighlighted, 5)
        self.failUnlessEqual(NSCellLightsByContents, 6)
        self.failUnlessEqual(NSCellLightsByGray, 7)
        self.failUnlessEqual(NSChangeBackgroundCell, 8)
        self.failUnlessEqual(NSCellLightsByBackground, 9)
        self.failUnlessEqual(NSCellIsBordered, 10)
        self.failUnlessEqual(NSCellHasOverlappingImage, 11)
        self.failUnlessEqual(NSCellHasImageHorizontal, 12)
        self.failUnlessEqual(NSCellHasImageOnLeftOrBottom, 13)
        self.failUnlessEqual(NSCellChangesContents, 14)
        self.failUnlessEqual(NSCellIsInsetButton, 15)
        self.failUnlessEqual(NSCellAllowsMixedState, 16)
        self.failUnlessEqual(NSNoImage, 0)
        self.failUnlessEqual(NSImageOnly, 1)
        self.failUnlessEqual(NSImageLeft, 2)
        self.failUnlessEqual(NSImageRight, 3)
        self.failUnlessEqual(NSImageBelow, 4)
        self.failUnlessEqual(NSImageAbove, 5)
        self.failUnlessEqual(NSImageOverlaps, 6)
        self.failUnlessEqual(NSScaleProportionally, 0)
        self.failUnlessEqual(NSScaleToFit, 1)
        self.failUnlessEqual(NSScaleNone, 2)
        self.failUnlessEqual(NSImageScaleProportionallyDown, 0)
        self.failUnlessEqual(NSImageScaleAxesIndependently,1)
        self.failUnlessEqual(NSImageScaleNone, 2)
        self.failUnlessEqual(NSImageScaleProportionallyUpOrDown, 3)
        self.failUnlessEqual(NSMixedState, -1)
        self.failUnlessEqual(NSOffState,  0)
        self.failUnlessEqual(NSOnState,  1)
        self.failUnlessEqual(NSNoCellMask, 0)
        self.failUnlessEqual(NSContentsCellMask, 1)
        self.failUnlessEqual(NSPushInCellMask, 2)
        self.failUnlessEqual(NSChangeGrayCellMask, 4)
        self.failUnlessEqual(NSChangeBackgroundCellMask, 8)
        self.failUnlessEqual(NSDefaultControlTint, 0)
        self.failUnlessEqual(NSBlueControlTint, 1)
        self.failUnlessEqual(NSGraphiteControlTint, 6)
        self.failUnlessEqual(NSClearControlTint, 7)
        self.failUnlessEqual(NSRegularControlSize, 0)
        self.failUnlessEqual(NSSmallControlSize, 1)
        self.failUnlessEqual(NSMiniControlSize, 2)
        self.failUnlessEqual(NSCellHitNone, 0)
        self.failUnlessEqual(NSCellHitContentArea, 1 << 0)
        self.failUnlessEqual(NSCellHitEditableTextArea, 1 << 1)
        self.failUnlessEqual(NSCellHitTrackableArea, 1 << 2)
        self.failUnlessEqual(NSBackgroundStyleLight, 0)
        self.failUnlessEqual(NSBackgroundStyleDark, 1)
        self.failUnlessEqual(NSBackgroundStyleRaised, 2)
        self.failUnlessEqual(NSBackgroundStyleLowered, 3)


if __name__ == '__main__':
    main( )
