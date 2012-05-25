from Foundation import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str


class TestNSThread (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSThread.isMultiThreaded)
        self.assertArgIsSEL(NSThread.detachNewThreadSelector_toTarget_withObject_, 0, b'v@:@')
        self.assertResultIsBOOL(NSThread.setThreadPriority_)

        self.assertArgIsSEL(NSThread.performSelectorOnMainThread_withObject_waitUntilDone_modes_, 0, b'v@:@')
        self.assertArgIsBOOL(NSThread.performSelectorOnMainThread_withObject_waitUntilDone_modes_, 2)
        self.assertArgIsSEL(NSThread.performSelectorOnMainThread_withObject_waitUntilDone_, 0, b'v@:@')
        self.assertArgIsBOOL(NSThread.performSelectorOnMainThread_withObject_waitUntilDone_, 2)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertArgIsSEL(NSThread.initWithTarget_selector_object_, 1, b'v@:@')
        self.assertResultIsBOOL(NSThread.isExecuting)
        self.assertResultIsBOOL(NSThread.isFinished)
        self.assertResultIsBOOL(NSThread.isCancelled)
        self.assertResultIsBOOL(NSThread.isMainThread)
        self.assertResultIsBOOL(NSThread.mainThread().isMainThread)
        self.assertArgIsSEL(NSThread.performSelector_onThread_withObject_waitUntilDone_modes_, 0, b'v@:@')
        self.assertArgIsBOOL(NSThread.performSelector_onThread_withObject_waitUntilDone_modes_, 3)
        self.assertArgIsSEL(NSThread.performSelector_onThread_withObject_waitUntilDone_, 0, b'v@:@')
        self.assertArgIsBOOL(NSThread.performSelector_onThread_withObject_waitUntilDone_, 3)
        self.assertArgIsSEL(NSThread.performSelectorInBackground_withObject_, 0, b'v@:@')


    def testConstants(self):
        self.assertIsInstance(NSWillBecomeMultiThreadedNotification, unicode)
        self.assertIsInstance(NSDidBecomeSingleThreadedNotification, unicode)
        self.assertIsInstance(NSThreadWillExitNotification, unicode)


if __name__ == "__main__":
    main()
