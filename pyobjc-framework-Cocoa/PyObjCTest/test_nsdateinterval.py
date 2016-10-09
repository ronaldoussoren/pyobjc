from PyObjCTools.TestSupport import *
import sys
from Foundation import *



class TestNSDateInterval (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertResultIsBOOL(NSDateInterval.isEqualToDateInterval_)
        self.assertResultIsBOOL(NSDateInterval.intersectsDateInterval_)
        self.assertResultIsBOOL(NSDateInterval.containsDate_)


if __name__ == "__main__":
    main()
