
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCACIFilterAdditions (TestCase):

    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessResultIsBOOL(CIFilter.isEnabled)
        self.failUnlessArgIsBOOL(CIFilter.setEnabled_, 0)

if __name__ == "__main__":
    main()
