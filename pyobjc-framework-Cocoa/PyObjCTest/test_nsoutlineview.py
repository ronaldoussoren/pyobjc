
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSOutlineView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSOutlineViewDropOnItemIndex, -1)

        self.failUnlessIsInstance(NSOutlineViewSelectionDidChangeNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewColumnDidMoveNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewColumnDidResizeNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewSelectionIsChangingNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewItemWillExpandNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewItemDidExpandNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewItemWillCollapseNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewItemDidCollapseNotification, unicode)


    def testMethods(self):
        self.fail("- (NSString *)outlineView:(NSOutlineView *)outlineView toolTipForCell:(NSCell *)cell rect:(NSRectPointer)rect tableColumn:(NSTableColumn *)tableColumn item:(id)item mouseLocation:(NSPoint)mouseLocation;")


if __name__ == "__main__":
    main()
