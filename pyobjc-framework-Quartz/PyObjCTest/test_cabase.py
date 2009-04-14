
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCABase (TestCase):
    @min_os_level('10.5')
    def testFunctions(self):
        v = CACurrentMediaTime()
        self.failUnlessIsInstance(v, float)

if __name__ == "__main__":
    main()
