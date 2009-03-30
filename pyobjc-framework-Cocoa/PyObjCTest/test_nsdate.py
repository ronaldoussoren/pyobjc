from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSDate (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSDate.isEqualToDate_)


if __name__ == "__main__":
    main()
