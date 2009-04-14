
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIVector (TestCase):
    def testMethods(self):
        self.failUnlessArgIsIn(CIVector.vectorWithValues_count_, 0)
        self.failUnlessArgSizeInArg(CIVector.vectorWithValues_count_, 0, 1)
        self.failUnlessArgIsIn(CIVector.initWithValues_count_, 0)
        self.failUnlessArgSizeInArg(CIVector.initWithValues_count_, 0, 1)

if __name__ == "__main__":
    main()
