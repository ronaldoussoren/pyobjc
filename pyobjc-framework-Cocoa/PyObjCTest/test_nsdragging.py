import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSDraggingHelper(AppKit.NSObject):
    def draggingFormation(self):
        return 1

    def setDraggingFormation_(self, v):
        return 1

    def animatesToDestination(self):
        return 1

    def setAnimatesToDestination_(self, v):
        return 1

    def numberOfValidItemsForDrop(self):
        return 1

    def setNumberOfValidItemsForDrop_(self, v):
        return 1

    def enumerateDraggingItemsWithOptions_forView_classes_searchOptions_usingBlock_(
        self, a, b, c, d, e
    ):
        return 1

    def draggingSession_sourceOperationMaskForDraggingContext_(self, a, b):
        return 1

    def draggingSession_willBeginAtPoint_(self, a, b):
        pass

    def draggingSession_movedToPoint_(self, a, b):
        pass

    def draggingSession_endedAtPoint_operation_(self, a, b, c):
        pass

    def ignoreModifierKeysForDraggingSession_(self, a):
        return 1

    def draggingSourceOperationMask(self):
        return 1

    def draggingLocation(self):
        return 1

    def draggedImageLocation(self):
        return 1

    def draggingSource(self):
        return 1

    def draggingSequenceNumber(self):
        return 1

    def slideDraggedImageTo_(self, v):
        pass

    def draggingEntered_(self, sender):
        return 1

    def draggingUpdated_(self, sender):
        return 1

    def draggingExited_(self, sender):
        pass

    def prepareForDragOperation_(self, sender):
        return 1

    def performDragOperation_(self, sender):
        return 1

    def concludeDragOperation_(self, sender):
        pass

    def draggingEnded_(self, sender):
        pass

    def wantsPeriodicDraggingUpdates(self):
        return 1

    def draggingSourceOperationMaskForLocal_(self, v):
        return 1

    def draggedImage_beganAt_(self, v, v2):
        pass

    def draggedImage_endedAt_operation_(self, v, v2, v3):
        pass

    def draggedImage_movedTo_(self, v, v2):
        pass

    def ignoreModifierKeysWhileDragging(self):
        return 1

    def draggedImage_endedAt_deposited_(self, i, p, f):
        pass

    def springLoadingActivated_draggingInfo_(self, a, i):
        pass

    def springLoadingEntered_(self, a):
        pass

    def springLoadingUpdated_(self, a):
        pass


class TestNSDragging(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSDragOperationNone, 0)
        self.assertEqual(AppKit.NSDragOperationCopy, 1)
        self.assertEqual(AppKit.NSDragOperationLink, 2)
        self.assertEqual(AppKit.NSDragOperationGeneric, 4)
        self.assertEqual(AppKit.NSDragOperationPrivate, 8)
        self.assertEqual(AppKit.NSDragOperationAll_Obsolete, 15)
        self.assertEqual(AppKit.NSDragOperationMove, 16)
        self.assertEqual(AppKit.NSDragOperationDelete, 32)
        self.assertEqual(AppKit.NSDragOperationEvery, AppKit.NSUIntegerMax)

        self.assertEqual(AppKit.NSDragOperationAll, AppKit.NSDragOperationAll_Obsolete)

    @min_os_level("10.7")
    def testConstant10_7(self):
        self.assertEqual(AppKit.NSDraggingFormationDefault, 0)
        self.assertEqual(AppKit.NSDraggingFormationNone, 1)
        self.assertEqual(AppKit.NSDraggingFormationPile, 2)
        self.assertEqual(AppKit.NSDraggingFormationList, 3)
        self.assertEqual(AppKit.NSDraggingFormationStack, 4)

        self.assertEqual(AppKit.NSDraggingContextOutsideApplication, 0)
        self.assertEqual(AppKit.NSDraggingContextWithinApplication, 1)

        self.assertEqual(
            AppKit.NSDraggingItemEnumerationConcurrent, AppKit.NSEnumerationConcurrent
        )
        self.assertEqual(
            AppKit.NSDraggingItemEnumerationClearNonenumeratedImages, 1 << 16
        )

    @min_os_level("10.11")
    def testConstant10_11(self):
        self.assertEqual(AppKit.NSSpringLoadingHighlightNone, 0)
        self.assertEqual(AppKit.NSSpringLoadingHighlightStandard, 1)
        self.assertEqual(AppKit.NSSpringLoadingHighlightEmphasized, 2)

        self.assertEqual(AppKit.NSSpringLoadingDisabled, 0)
        self.assertEqual(AppKit.NSSpringLoadingEnabled, 1)
        self.assertEqual(AppKit.NSSpringLoadingContinuousActivation, 2)
        self.assertEqual(AppKit.NSSpringLoadingNoHover, 4)

    @min_sdk_level("10.7")
    def testProtocols(self):
        objc.protocolNamed("NSDraggingDestination")
        objc.protocolNamed("NSDraggingSource")

    @min_sdk_level("10.11")
    def testProtocols10_11(self):
        objc.protocolNamed("NSSpringLoadingDestination")

    def testProtocolImplementations(self):
        self.assertResultHasType(
            TestNSDraggingHelper.draggingSourceOperationMask, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestNSDraggingHelper.draggingLocation, AppKit.NSPoint.__typestr__
        )
        self.assertResultHasType(
            TestNSDraggingHelper.draggedImageLocation, AppKit.NSPoint.__typestr__
        )
        self.assertResultHasType(
            TestNSDraggingHelper.draggingSequenceNumber, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSDraggingHelper.slideDraggedImageTo_, 0, AppKit.NSPoint.__typestr__
        )

        self.assertResultHasType(
            TestNSDraggingHelper.draggingEntered_, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestNSDraggingHelper.draggingUpdated_, objc._C_NSUInteger
        )
        self.assertResultIsBOOL(TestNSDraggingHelper.prepareForDragOperation_)
        self.assertResultIsBOOL(TestNSDraggingHelper.performDragOperation_)
        self.assertResultIsBOOL(TestNSDraggingHelper.wantsPeriodicDraggingUpdates)

        self.assertResultHasType(
            TestNSDraggingHelper.draggingSourceOperationMaskForLocal_,
            objc._C_NSUInteger,
        )
        self.assertArgIsBOOL(
            TestNSDraggingHelper.draggingSourceOperationMaskForLocal_, 0
        )
        self.assertArgHasType(
            TestNSDraggingHelper.draggedImage_beganAt_, 1, AppKit.NSPoint.__typestr__
        )
        self.assertArgHasType(
            TestNSDraggingHelper.draggedImage_endedAt_operation_,
            1,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSDraggingHelper.draggedImage_endedAt_operation_, 2, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestNSDraggingHelper.draggedImage_movedTo_, 1, AppKit.NSPoint.__typestr__
        )
        self.assertResultIsBOOL(TestNSDraggingHelper.ignoreModifierKeysWhileDragging)
        self.assertArgHasType(
            TestNSDraggingHelper.draggedImage_endedAt_deposited_,
            1,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgIsBOOL(TestNSDraggingHelper.draggedImage_endedAt_deposited_, 2)

        self.assertResultHasType(
            TestNSDraggingHelper.draggingSession_sourceOperationMaskForDraggingContext_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSDraggingHelper.draggingSession_sourceOperationMaskForDraggingContext_,
            1,
            objc._C_NSInteger,
        )

    @min_os_level("10.7")
    def testProtocols10_7(self):
        self.assertResultIsBOOL(TestNSDraggingHelper.animatesToDestination)
        self.assertArgIsBOOL(TestNSDraggingHelper.setAnimatesToDestination_, 0)

        self.assertResultIsBOOL(TestNSDraggingHelper.animatesToDestination)
        self.assertArgIsBOOL(TestNSDraggingHelper.setAnimatesToDestination_, 0)

        self.assertResultHasType(
            TestNSDraggingHelper.numberOfValidItemsForDrop, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSDraggingHelper.setNumberOfValidItemsForDrop_, 0, objc._C_NSInteger
        )

        self.assertArgHasType(
            TestNSDraggingHelper.enumerateDraggingItemsWithOptions_forView_classes_searchOptions_usingBlock_,  # noqa: B950
            0,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestNSDraggingHelper.enumerateDraggingItemsWithOptions_forView_classes_searchOptions_usingBlock_,  # noqa: B950
            4,
            b"v@" + objc._C_NSInteger + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgHasType(
            TestNSDraggingHelper.draggingSession_willBeginAtPoint_,
            1,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSDraggingHelper.draggingSession_movedToPoint_,
            1,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSDraggingHelper.draggingSession_endedAtPoint_operation_,
            1,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSDraggingHelper.draggingSession_endedAtPoint_operation_,
            2,
            objc._C_NSUInteger,
        )

        self.assertResultIsBOOL(
            TestNSDraggingHelper.ignoreModifierKeysForDraggingSession_
        )

    @min_os_level("10.11")
    def testProtocolMethods10_11(self):
        self.assertArgIsBOOL(
            TestNSDraggingHelper.springLoadingActivated_draggingInfo_, 0
        )
        self.assertResultHasType(
            TestNSDraggingHelper.springLoadingEntered_, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestNSDraggingHelper.springLoadingUpdated_, objc._C_NSUInteger
        )
