from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSDate (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSDate.isEqualToDate_)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSSystemClockDidChangeNotification, unicode)


if __name__ == "__main__":
    main()
