
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCACIFilterAdditions (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(CIFilter.isEnabled)
        self.failUnlessArgIsBOOL(CIFilter.setEnabled_, 0)

if __name__ == "__main__":
    main()
