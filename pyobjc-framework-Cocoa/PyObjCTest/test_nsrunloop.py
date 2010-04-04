from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSRunLoop (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSRunLoop.runMode_beforeDate_)

        self.assertArgIsSEL(NSRunLoop.performSelector_withObject_afterDelay_inModes_, 0, b'v@:@')
        self.assertArgIsSEL(NSRunLoop.performSelector_withObject_afterDelay_, 0, b'v@:@')
        self.assertArgIsSEL(NSRunLoop.performSelector_target_argument_order_modes_, 0, b'v@:@')

if __name__ == "__main__":
    main()
