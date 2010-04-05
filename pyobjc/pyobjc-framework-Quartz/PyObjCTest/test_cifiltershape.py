
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIFilterShape (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(CIFilterShape.transformBy_interior_, 1)

if __name__ == "__main__":
    main()
