from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSMeasurement (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertResultIsBOOL(NSMeasurement.canBeConvertedToUnit_)

if __name__ == "__main__":
    main()
