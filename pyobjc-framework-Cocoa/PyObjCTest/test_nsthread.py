from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSThread (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSThread.isMultiThreaded)
        self.failUnlessArgIsSEL(NSThread.detachNewThreadSelector_toTarget_withObject_, 0, 'v@:@')
        self.failUnlessResultIsBOOL(NSThread.setThreadPriority_)

        self.failUnlessArgIsSEL(NSThread.performSelectorOnMainThread_withObject_waitUntilDone_modes_, 0, 'v@:@')
        self.failUnlessArgIsBOOL(NSThread.performSelectorOnMainThread_withObject_waitUntilDone_modes_, 2)
        self.failUnlessArgIsSEL(NSThread.performSelectorOnMainThread_withObject_waitUntilDone_, 0, 'v@:@')
        self.failUnlessArgIsBOOL(NSThread.performSelectorOnMainThread_withObject_waitUntilDone_, 2)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessArgIsSEL(NSThread.initWithTarget_selector_object_, 1, 'v@:@')
        self.failUnlessResultIsBOOL(NSThread.isExecuting)
        self.failUnlessResultIsBOOL(NSThread.isFinished)
        self.failUnlessResultIsBOOL(NSThread.isCancelled)
        self.failUnlessResultIsBOOL(NSThread.isMainThread)
        self.failUnlessResultIsBOOL(NSThread.mainThread().isMainThread)
        self.failUnlessArgIsSEL(NSThread.performSelector_onThread_withObject_waitUntilDone_modes_, 0, 'v@:@')
        self.failUnlessArgIsBOOL(NSThread.performSelector_onThread_withObject_waitUntilDone_modes_, 3)
        self.failUnlessArgIsSEL(NSThread.performSelector_onThread_withObject_waitUntilDone_, 0, 'v@:@')
        self.failUnlessArgIsBOOL(NSThread.performSelector_onThread_withObject_waitUntilDone_, 3)
        self.failUnlessArgIsSEL(NSThread.performSelectorInBackground_withObject_, 0, 'v@:@')


    def testConstants(self):
        self.failUnlessIsInstance(NSWillBecomeMultiThreadedNotification, unicode)
        self.failUnlessIsInstance(NSDidBecomeSingleThreadedNotification, unicode)
        self.failUnlessIsInstance(NSThreadWillExitNotification, unicode)


if __name__ == "__main__":
    main()
