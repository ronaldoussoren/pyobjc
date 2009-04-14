
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *
from Quartz import *

class TestCIKernel (TestCase):
    def testMethods(self):
        self.failUnlessArgIsSEL(CIKernel.setROISelector_, 0, CGRect.__typestr__ + '@:i' + CGRect.__typestr__ + '@')

if __name__ == "__main__":
    main()
