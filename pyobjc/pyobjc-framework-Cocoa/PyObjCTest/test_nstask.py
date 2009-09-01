from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSTask (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTask.suspend)
        self.failUnlessResultIsBOOL(NSTask.resume)
        self.failUnlessResultIsBOOL(NSTask.isRunning)

    def testConstants(self):
        self.failUnlessIsInstance(NSTaskDidTerminateNotification, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(NSTaskTerminationReasonExit, 1)
        self.failUnlessEqual(NSTaskTerminationReasonUncaughtSignal, 2)


if __name__ == "__main__":
    main()
