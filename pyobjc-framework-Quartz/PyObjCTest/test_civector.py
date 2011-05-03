
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIVector (TestCase):
    def testMethods(self):
        self.assertArgIsIn(CIVector.vectorWithValues_count_, 0)
        self.assertArgSizeInArg(CIVector.vectorWithValues_count_, 0, 1)
        self.assertArgIsIn(CIVector.initWithValues_count_, 0)
        self.assertArgSizeInArg(CIVector.initWithValues_count_, 0, 1)

if __name__ == "__main__":
    main()
