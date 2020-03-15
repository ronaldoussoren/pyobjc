import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSDebug(TestCase):
    def testFunctions(self):
        self.assertResultIsBOOL(Foundation.NSIsFreedObject)
        Foundation.NSRecordAllocationEvent
        Foundation.NSFrameAddress
        Foundation.NSReturnAddress
        Foundation.NSCountFrames
        Foundation.NSRecordAllocationEvent

    def testConstants(self):
        self.assertEqual(Foundation.NSObjectAutoreleasedEvent, 3)
        self.assertEqual(Foundation.NSObjectExtraRefIncrementedEvent, 4)
        self.assertEqual(Foundation.NSObjectExtraRefDecrementedEvent, 5)
        self.assertEqual(Foundation.NSObjectInternalRefIncrementedEvent, 6)
        self.assertEqual(Foundation.NSObjectInternalRefDecrementedEvent, 7)

        self.assertIsInstance(Foundation.NSDebugEnabled, bool)
        self.assertIsInstance(Foundation.NSZombieEnabled, bool)
        self.assertIsInstance(Foundation.NSDeallocateZombies, bool)
        self.assertIsInstance(Foundation.NSHangOnUncaughtException, bool)
        self.assertIsInstance(Foundation.NSKeepAllocationStatistics, bool)
