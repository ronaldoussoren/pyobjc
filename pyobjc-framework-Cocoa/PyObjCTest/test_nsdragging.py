
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDraggingHelper (NSObject):
    def draggingFormation(self): return 1
    def setDraggingFormation(self, v): return 1
    def animatesToDestination(self): return 1
    def setAnimatesToDestination_(self, v): return 1
    def numberOfValidItemsForDrop(self): return 1
    def setNumberOfValidItemsForDrop_(self, v): return 1
    def enumerateDraggingItemsWithOptions_forView_classes_searchOptions_usingBlock_(self, a, b, c, d, e): return 1
    def draggingSession_sourceOperationMaskForDraggingContext_(self, a, b): return 1
    def draggingSession_willBeginAtPoint_(self, a, b): pass
    def draggingSession_movedToPoint_(self, a, b): pass
    def draggingSession_endedAtPoint_operation_(self, a, b, c): pass
    def ignoreModifierKeysForDraggingSession_(self, a): return 1



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
        self.assertEqual(NSDragOperationEvery, NSUIntegerMax)

        self.assertEqual(NSDragOperationAll, NSDragOperationAll_Obsolete)

    @min_os_level('10.7')
    def testConstant10_7(self):
        self.assertEqual(NSDraggingFormationDefault, 0)
        self.assertEqual(NSDraggingFormationNone, 1)
        self.assertEqual(NSDraggingFormationPile, 2)
        self.assertEqual(NSDraggingFormationList, 3)
        self.assertEqual(NSDraggingFormationStack, 4)

        self.assertEqual(NSDraggingContextOutsideApplication, 0)
        self.assertEqual(NSDraggingContextWithinApplication, 1)

        self.assertEqual(NSDraggingItemEnumerationClearNonenumeratedImages, 1<<16)


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

    @min_os_level('10.7')
    def testProtocols10_7(self):
        self.assertResultIsBOOL(TestNSDraggingHelper.animatesToDestination)
        self.assertArgIsBOOL(TestNSDraggingHelper.setAnimatesToDestination_, 0)

        self.assertResultIsBOOL(TestNSDraggingHelper.animatesToDestination)
        self.assertArgIsBOOL(TestNSDraggingHelper.setAnimatesToDestination_, 0)

        self.assertResultHasType(TestNSDraggingHelper.numberOfValidItemsForDrop, objc._C_NSInteger)
        self.assertArgHasType(TestNSDraggingHelper.setNumberOfValidItemsForDrop_, 0, objc._C_NSInteger)


        self.assertArgHasType(TestNSDraggingHelper.enumerateDraggingItemsWithOptions_forView_classes_searchOptions_usingBlock_, 0, objc._C_NSUInteger)
        self.assertArgIsBlock(TestNSDraggingHelper.enumerateDraggingItemsWithOptions_forView_classes_searchOptions_usingBlock_, 4, b'v@' + objc._C_NSInteger + b'o^' + objc._C_NSBOOL)

        self.assertArgHasType(TestNSDraggingHelper.draggingSession_willBeginAtPoint_, 1, NSPoint.__typestr__)
        self.assertArgHasType(TestNSDraggingHelper.draggingSession_movedToPoint_, 1, NSPoint.__typestr__)
        self.assertArgHasType(TestNSDraggingHelper.draggingSession_endedAtPoint_operation_, 1, NSPoint.__typestr__)
        self.assertArgHasType(TestNSDraggingHelper.draggingSession_endedAtPoint_operation_, 2, objc._C_NSUInteger)

        self.assertResultIsBOOL(TestNSDraggingHelper.ignoreModifierKeysForDraggingSession_)

if __name__ == "__main__":
    main()
