
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIFilterShape (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(CIFilterShape.transformBy_interior_, 1)

if __name__ == "__main__":
    main()
