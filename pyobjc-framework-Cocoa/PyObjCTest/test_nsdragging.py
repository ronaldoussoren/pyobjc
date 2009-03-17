
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDraggingHelper (NSObject):
    def draggingSourceOperationMask(self): return 1
    def draggingLocation(self): return 1
    def draggedImageLocation(self): return 1
    def draggingSource(self): return 1
    def draggingSequenceNumber(self): return 1
    def slideDraggedImageTo_(self, v): pass

    def draggingEntered_(self, sender): return 1
    def draggingUpdated_(self, sender): return 1
    def draggingExited_(self, sender): pass
    def prepareForDragOperation_(self, sender): return 1
    def performDragOperation_(self, sender): return 1
    def concludeDragOperation_(self, sender): pass
    def draggingEnded_(self, sender): pass
    def wantsPeriodicDraggingUpdates(self): return 1

    def draggingSourceOperationMaskForLocal_(self, v): return 1
    def draggedImage_beganAt_(self, v, v2): pass
    def draggedImage_endedAt_operation_(self, v, v2, v3): pass
    def draggedImage_movedTo_(self, v, v2): pass
    def ignoreModifierKeysWhileDragging(self): return 1
    def draggedImage_endedAt_deposited_(self, i, p, f): pass

class TestNSDragging (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSDragOperationNone, 0)
        self.failUnlessEqual(NSDragOperationCopy, 1)
        self.failUnlessEqual(NSDragOperationLink, 2)
        self.failUnlessEqual(NSDragOperationGeneric, 4)
        self.failUnlessEqual(NSDragOperationPrivate, 8)
        self.failUnlessEqual(NSDragOperationAll_Obsolete, 15)
        self.failUnlessEqual(NSDragOperationMove, 16)
        self.failUnlessEqual(NSDragOperationDelete, 32)
        self.failUnlessEqual(NSDragOperationEvery, -1)

        self.failUnlessEqual(NSDragOperationAll, NSDragOperationAll_Obsolete)

    def testProtocols(self):
        self.failUnlessResultHasType(TestNSDraggingHelper.draggingSourceOperationMask, objc._C_NSUInteger)
        self.failUnlessResultHasType(TestNSDraggingHelper.draggingLocation, NSPoint.__typestr__)
        self.failUnlessResultHasType(TestNSDraggingHelper.draggedImageLocation, NSPoint.__typestr__)
        self.failUnlessResultHasType(TestNSDraggingHelper.draggingSequenceNumber, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSDraggingHelper.slideDraggedImageTo_, 0, NSPoint.__typestr__)

        self.failUnlessResultHasType(TestNSDraggingHelper.draggingEntered_, objc._C_NSUInteger)
        self.failUnlessResultHasType(TestNSDraggingHelper.draggingUpdated_, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestNSDraggingHelper.prepareForDragOperation_)
        self.failUnlessResultIsBOOL(TestNSDraggingHelper.performDragOperation_)
        self.failUnlessResultIsBOOL(TestNSDraggingHelper.wantsPeriodicDraggingUpdates)

        self.failUnlessResultHasType(TestNSDraggingHelper.draggingSourceOperationMaskForLocal_, objc._C_NSUInteger)
        self.failUnlessArgIsBOOL(TestNSDraggingHelper.draggingSourceOperationMaskForLocal_, 0)
        self.failUnlessArgHasType(TestNSDraggingHelper.draggedImage_beganAt_, 1, NSPoint.__typestr__)
        self.failUnlessArgHasType(TestNSDraggingHelper.draggedImage_endedAt_operation_, 1, NSPoint.__typestr__)
        self.failUnlessArgHasType(TestNSDraggingHelper.draggedImage_endedAt_operation_, 2, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSDraggingHelper.draggedImage_movedTo_, 1, NSPoint.__typestr__)
        self.failUnlessResultIsBOOL(TestNSDraggingHelper.ignoreModifierKeysWhileDragging)
        self.failUnlessArgHasType(TestNSDraggingHelper.draggedImage_endedAt_deposited_, 1, NSPoint.__typestr__)
        self.failUnlessArgIsBOOL(TestNSDraggingHelper.draggedImage_endedAt_deposited_, 2)

if __name__ == "__main__":
    main()
