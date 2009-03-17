from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDatePicker (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSDatePicker.isBezeled)
        self.failUnlessArgIsBOOL(NSDatePicker.setBezeled_, 0)
        
        self.failUnlessResultIsBOOL(NSDatePicker.isBordered)
        self.failUnlessArgIsBOOL(NSDatePicker.setBordered_, 0)

        self.failUnlessResultIsBOOL(NSDatePicker.drawsBackground)
        self.failUnlessArgIsBOOL(NSDatePicker.setDrawsBackground_, 0)

if __name__ == "__main__":
    main()
