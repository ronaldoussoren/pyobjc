from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSRunLoop (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSRunLoop.runMode_beforeDate_)

        self.assertArgIsSEL(NSRunLoop.performSelector_withObject_afterDelay_inModes_, 0, b'v@:@')
        self.assertArgIsSEL(NSRunLoop.performSelector_withObject_afterDelay_, 0, b'v@:@')
        self.assertArgIsSEL(NSRunLoop.performSelector_target_argument_order_modes_, 0, b'v@:@')

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertArgIsBlock(NSRunLoop.performInModes_block_, 1, b'v')
        self.assertArgIsBlock(NSRunLoop.performBlock_, 0, b'v')

    def testConstants(self):
        self.assertIsInstance(NSDefaultRunLoopMode, unicode)
        self.assertIsInstance(NSRunLoopCommonModes, unicode)

if __name__ == "__main__":
    main()
