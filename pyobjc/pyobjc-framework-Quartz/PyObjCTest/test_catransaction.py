
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCATransaction (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(kCATransactionAnimationDuration, unicode)
        self.failUnlessIsInstance(kCATransactionDisableActions, unicode)


if __name__ == "__main__":
    main()
