from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *

class TestCVHostTime (TestCase):
    def testFunctions(self):
        v = CVGetCurrentHostTime()
        self.failUnlessIsInstance(v, (int, long))

        v = CVGetHostClockFrequency()
        self.failUnlessIsInstance(v, float)

        v = CVGetHostClockMinimumTimeDelta()
        self.failUnlessIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
