
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
        self.assertEqual(NSDragOperationNone, 0)
        self.assertEqual(NSDragOperationCopy, 1)
        self.assertEqual(NSDragOperationLink, 2)
        self.assertEqual(NSDragOperationGeneric, 4)
        self.assertEqual(NSDragOperationPrivate, 8)
        self.assertEqual(NSDragOperationAll_Obsolete, 15)
        self.assertEqual(NSDragOperationMove, 16)
        self.assertEqual(NSDragOperationDelete, 32)
        self.assertEqual(NSDragOperationEvery, -1)

        self.assertEqual(NSDragOperationAll, NSDragOperationAll_Obsolete)

    def testProtocols(self):
        self.assertResultHasType(TestNSDraggingHelper.draggingSourceOperationMask, objc._C_NSUInteger)
        self.assertResultHasType(TestNSDraggingHelper.draggingLocation, NSPoint.__typestr__)
        self.assertResultHasType(TestNSDraggingHelper.draggedImageLocation, NSPoint.__typestr__)
        self.assertResultHasType(TestNSDraggingHelper.draggingSequenceNumber, objc._C_NSInteger)
        self.assertArgHasType(TestNSDraggingHelper.slideDraggedImageTo_, 0, NSPoint.__typestr__)

        self.assertResultHasType(TestNSDraggingHelper.draggingEntered_, objc._C_NSUInteger)
        self.assertResultHasType(TestNSDraggingHelper.draggingUpdated_, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestNSDraggingHelper.prepareForDragOperation_)
        self.assertResultIsBOOL(TestNSDraggingHelper.performDragOperation_)
        self.assertResultIsBOOL(TestNSDraggingHelper.wantsPeriodicDraggingUpdates)

        self.assertResultHasType(TestNSDraggingHelper.draggingSourceOperationMaskForLocal_, objc._C_NSUInteger)
        self.assertArgIsBOOL(TestNSDraggingHelper.draggingSourceOperationMaskForLocal_, 0)
        self.assertArgHasType(TestNSDraggingHelper.draggedImage_beganAt_, 1, NSPoint.__typestr__)
        self.assertArgHasType(TestNSDraggingHelper.draggedImage_endedAt_operation_, 1, NSPoint.__typestr__)
        self.assertArgHasType(TestNSDraggingHelper.draggedImage_endedAt_operation_, 2, objc._C_NSUInteger)
        self.assertArgHasType(TestNSDraggingHelper.draggedImage_movedTo_, 1, NSPoint.__typestr__)
        self.assertResultIsBOOL(TestNSDraggingHelper.ignoreModifierKeysWhileDragging)
        self.assertArgHasType(TestNSDraggingHelper.draggedImage_endedAt_deposited_, 1, NSPoint.__typestr__)
        self.assertArgIsBOOL(TestNSDraggingHelper.draggedImage_endedAt_deposited_, 2)

if __name__ == "__main__":
    main()
