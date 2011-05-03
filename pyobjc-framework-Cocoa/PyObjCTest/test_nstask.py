from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSTask (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSTask.suspend)
        self.assertResultIsBOOL(NSTask.resume)
        self.assertResultIsBOOL(NSTask.isRunning)

    def testConstants(self):
        self.assertIsInstance(NSTaskDidTerminateNotification, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSTaskTerminationReasonExit, 1)
        self.assertEqual(NSTaskTerminationReasonUncaughtSignal, 2)


if __name__ == "__main__":
    main()
