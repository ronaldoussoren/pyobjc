from Quartz import *
from PyObjCTools.TestSupport import *


class TestCAEmitterCell (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(CAEmitterCell.shouldArchiveValueForKey_)
        self.failUnlessResultIsBOOL(CAEmitterCell.isEnabled)
        self.failUnlessArgIsBOOL(CAEmitterCell.setEnabled_, 0)

if __name__ == "__main__":
    main()
