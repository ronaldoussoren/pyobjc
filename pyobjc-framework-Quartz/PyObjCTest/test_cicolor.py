from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIColor (TestCase):
    def testMethods(self):
        self.assertResultIsVariableSize(CIColor.components)

if __name__ == "__main__":
    main()
