from Quartz import *
from PyObjCTools.TestSupport import *


class TestCAEmitterCell (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(CAEmitterCell.shouldArchiveValueForKey_)
        self.assertResultIsBOOL(CAEmitterCell.isEnabled)
        self.assertArgIsBOOL(CAEmitterCell.setEnabled_, 0)

if __name__ == "__main__":
    main()
