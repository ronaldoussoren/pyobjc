from PyObjCTools.TestSupport import *

import Foundation

class TestNSDebug (TestCase):
    def testNoUnsupportedSymbols(self):

        self.assertNotHasAttr(Foundation, 'NSDebugEnabled')
        self.assertNotHasAttr(Foundation, 'NSZombieEnabled')
        self.assertNotHasAttr(Foundation, 'NSDeallocateZombies')
        self.assertNotHasAttr(Foundation, 'NSHangOnUncaughtException')
        self.assertNotHasAttr(Foundation, 'NSKeepAllocationStatistics')
        self.assertNotHasAttr(Foundation, 'NSFrameAddress')
        self.assertNotHasAttr(Foundation, 'NSReturnAddress')
        self.assertNotHasAttr(Foundation, 'NSCountFrames')
        self.assertHasAttr(Foundation, 'NSIsFreedObject')
        self.assertHasAttr(Foundation, 'NSRecordAllocationEvent')
    def testConstants(self):
        self.assertEqual(Foundation.NSObjectAutoreleasedEvent, 3)
        self.assertEqual(Foundation.NSObjectExtraRefIncrementedEvent, 4)
        self.assertEqual(Foundation.NSObjectExtraRefDecrementedEvent, 5)
        self.assertEqual(Foundation.NSObjectInternalRefIncrementedEvent, 6)
        self.assertEqual(Foundation.NSObjectInternalRefDecrementedEvent, 7)


if __name__ == "__main__":
    main()
