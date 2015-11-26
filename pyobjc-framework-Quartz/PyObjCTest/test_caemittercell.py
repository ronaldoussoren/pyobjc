import Quartz
from PyObjCTools.TestSupport import *


class TestCAEmitterCell (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(Quartz.CAEmitterCell.shouldArchiveValueForKey_)
        self.assertResultIsBOOL(Quartz.CAEmitterCell.isEnabled)
        self.assertArgIsBOOL(Quartz.CAEmitterCell.setEnabled_, 0)

if __name__ == "__main__":
    main()
