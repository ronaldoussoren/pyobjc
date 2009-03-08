
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMatrix (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSRadioModeMatrix, 0)
        self.failUnlessEqual(NSHighlightModeMatrix, 1)
        self.failUnlessEqual(NSListModeMatrix, 2)
        self.failUnlessEqual(NSTrackModeMatrix, 3)

    def testMethods(self):
        self.fail("- (void)sortUsingSelector:(SEL)comparator;")
        self.fail("- (void)sortUsingFunction:(NSInteger (*)(id, id, void *))compare context:(void *)context;")
        self.fail("- (void)getNumberOfRows:(NSInteger *)rowCount columns:(NSInteger *)colCount;")

        self.fail("- (BOOL)getRow:(NSInteger *)row column:(NSInteger *)col ofCell:(NSCell *)aCell;")
        self.fail("- (BOOL)getRow:(NSInteger *)row column:(NSInteger *)col forPoint:(NSPoint)aPoint;")
        self.fail("- (void)setDoubleAction:(SEL)aSelector;")




if __name__ == "__main__":
    main()
