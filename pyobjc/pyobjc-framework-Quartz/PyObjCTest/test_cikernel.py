
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *
from Quartz import *

class TestCIKernel (TestCase):
    def testMethods(self):
        self.assertArgIsSEL(CIKernel.setROISelector_, 0, CGRect.__typestr__ + b'@:i' + CGRect.__typestr__ + b'@')

if __name__ == "__main__":
    main()
