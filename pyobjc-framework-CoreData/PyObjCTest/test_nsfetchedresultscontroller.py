import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSFetchedResultsControllerHelper(CoreData.NSObject):
    def controller_didChangeObject_atIndexPath_forChangeType_newIndexPath_(
        self, c, o, p, t, np
    ):
        pass

    def controller_didChangeSection_atIndex_forChangeType_(self, c, o, p, t):
        pass


class TestNSFetchedResultsController(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(CoreData.NSFetchedResultsController.performFetch_)
        self.assertArgIsOut(CoreData.NSFetchedResultsController.performFetch_, 0)

    @min_sdk_level("10.12")
    def testProtocols(self):
        objc.protocolNamed("NSFetchedResultsControllerDelegate")
        self.assertArgHasType(
            TestNSFetchedResultsControllerHelper.controller_didChangeObject_atIndexPath_forChangeType_newIndexPath_,
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSFetchedResultsControllerHelper.controller_didChangeSection_atIndex_forChangeType_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSFetchedResultsControllerHelper.controller_didChangeSection_atIndex_forChangeType_,
            3,
            objc._C_NSUInteger,
        )

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(CoreData.NSFetchedResultsChangeInsert, 1)
        self.assertEqual(CoreData.NSFetchedResultsChangeDelete, 2)
        self.assertEqual(CoreData.NSFetchedResultsChangeMove, 3)
        self.assertEqual(CoreData.NSFetchedResultsChangeUpdate, 4)
