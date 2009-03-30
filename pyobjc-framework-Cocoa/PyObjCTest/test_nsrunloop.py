from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSRunLoop (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSRunLoop.runMode_beforeDate_)

        self.failUnlessArgIsSEL(NSRunLoop.performSelector_withObject_afterDelay_inModes_, 0, 'v@:@')
        self.failUnlessArgIsSEL(NSRunLoop.performSelector_withObject_afterDelay_, 0, 'v@:@')
        self.failUnlessArgIsSEL(NSRunLoop.performSelector_target_argument_order_modes_, 0, 'v@:@')

if __name__ == "__main__":
    main()
