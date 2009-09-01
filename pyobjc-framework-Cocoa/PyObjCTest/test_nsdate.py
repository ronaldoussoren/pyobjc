from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSDate (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSDate.isEqualToDate_)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(NSSystemClockDidChangeNotification, unicode)


if __name__ == "__main__":
    main()
