from PyObjCTools.TestSupport import *

import Foundation

class TestNSDebug (TestCase):
    def testNoUnsupportedSymbols(self):

        self.failIf(hasattr(Foundation, 'NSDebugEnabled'))
        self.failIf(hasattr(Foundation, 'NSZombieEnabled'))
        self.failIf(hasattr(Foundation, 'NSDeallocateZombies'))
        self.failIf(hasattr(Foundation, 'NSHangOnUncaughtException'))

        self.failIf(hasattr(Foundation, 'NSKeepAllocationStatistics'))

        self.failIf(hasattr(Foundation, 'NSFrameAddress'))
        self.failIf(hasattr(Foundation, 'NSReturnAddress'))
        self.failIf(hasattr(Foundation, 'NSCountFrames'))

        self.failUnless(hasattr(Foundation, 'NSIsFreedObject'))
        self.failUnless(hasattr(Foundation, 'NSRecordAllocationEvent'))

    def testConstants(self):
        self.assertEquals(Foundation.NSObjectAutoreleasedEvent, 3)
        self.assertEquals(Foundation.NSObjectExtraRefIncrementedEvent, 4)
        self.assertEquals(Foundation.NSObjectExtraRefDecrementedEvent, 5)
        self.assertEquals(Foundation.NSObjectInternalRefIncrementedEvent, 6)
        self.assertEquals(Foundation.NSObjectInternalRefDecrementedEvent, 7)


if __name__ == "__main__":
    main()
