from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSTask (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTask.suspend)
        self.failUnlessResultIsBOOL(NSTask.resume)
        self.failUnlessResultIsBOOL(NSTask.isRunning)

    def testConstants(self):
        self.failUnlessIsInstance(NSTaskDidTerminateNotification, unicode)


if __name__ == "__main__":
    main()
