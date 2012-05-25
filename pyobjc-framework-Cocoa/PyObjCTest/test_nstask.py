from Foundation import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str

class TestNSTask (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSTask.suspend)
        self.assertResultIsBOOL(NSTask.resume)
        self.assertResultIsBOOL(NSTask.isRunning)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBlock(NSTask.setTerminationHandler_, 0, b'v@')
        self.assertResultIsBlock(NSTask.terminationHandler, b'v@')

    def testConstants(self):
        self.assertIsInstance(NSTaskDidTerminateNotification, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSTaskTerminationReasonExit, 1)
        self.assertEqual(NSTaskTerminationReasonUncaughtSignal, 2)


if __name__ == "__main__":
    main()
