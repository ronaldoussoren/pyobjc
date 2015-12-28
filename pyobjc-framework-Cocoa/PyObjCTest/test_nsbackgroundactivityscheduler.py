from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSBackgroundActivityScheduler (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSBackgroundActivityResultFinished, 1)
        self.assertEqual(NSBackgroundActivityResultDeferred, 2)

    @min_os_level('10.10')
    def testMethods10_10(self):
        NSBackgroundActivityCompletionHandler = b'v' + objc._C_NSInteger

        self.assertResultIsBOOL(NSBackgroundActivityScheduler.repeats)
        self.assertArgIsBOOL(NSBackgroundActivityScheduler.setRepeats_, 0)
        self.assertArgIsBlock(NSBackgroundActivityScheduler.scheduleWithBlock_, 0, NSBackgroundActivityCompletionHandler)
        self.assertResultIsBOOL(NSBackgroundActivityScheduler.shouldDefer)


if __name__ == "__main__":
    main()
