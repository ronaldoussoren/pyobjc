from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIColor (TestCase):
    def testMethods(self):
        self.failUnlessResultIsVariableSize(CIColor.components)

if __name__ == "__main__":
    main()
