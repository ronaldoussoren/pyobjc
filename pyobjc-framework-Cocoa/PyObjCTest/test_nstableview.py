
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTableView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTableViewDropOn, 0)
        self.failUnlessEqual(NSTableViewDropAbove, 1)

        self.failUnlessEqual(NSTableViewNoColumnAutoresizing, 0)
        self.failUnlessEqual(NSTableViewUniformColumnAutoresizingStyle, 1)
        self.failUnlessEqual(NSTableViewSequentialColumnAutoresizingStyle, 2)
        self.failUnlessEqual(NSTableViewReverseSequentialColumnAutoresizingStyle, 3)
        self.failUnlessEqual(NSTableViewLastColumnOnlyAutoresizingStyle, 4)
        self.failUnlessEqual(NSTableViewFirstColumnOnlyAutoresizingStyle, 5)

        self.failUnlessEqual(NSTableViewGridNone, 0)
        self.failUnlessEqual(NSTableViewSolidVerticalGridLineMask, 1 << 0)
        self.failUnlessEqual(NSTableViewSolidHorizontalGridLineMask, 1 << 1)

        self.failUnlessEqual(NSTableViewSelectionHighlightStyleRegular, 0)
        self.failUnlessEqual(NSTableViewSelectionHighlightStyleSourceList, 1)

        self.failUnlessIsInstance(NSTableViewSelectionDidChangeNotification, unicode)
        self.failUnlessIsInstance(NSTableViewColumnDidMoveNotification, unicode)
        self.failUnlessIsInstance(NSTableViewColumnDidResizeNotification, unicode)
        self.failUnlessIsInstance(NSTableViewSelectionIsChangingNotification, unicode)


    def testMethods(self):
        self.fail("- (NSString *)tableView:(NSTableView *)tableView toolTipForCell:(NSCell *)cell rect:(NSRectPointer)rect tableColumn:(NSTableColumn *)tableColumn row:(NSInteger)row mouseLocation:(NSPoint)mouseLocation;")



if __name__ == "__main__":
    main()
