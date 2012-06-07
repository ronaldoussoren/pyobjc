from PyObjCTools.TestSupport import *
from Quartz import *

try:
    long
except NameError:
    long = int

class TestCVHostTime (TestCase):
    def testFunctions(self):
        v = CVGetCurrentHostTime()
        self.assertIsInstance(v, (int, long))

        v = CVGetHostClockFrequency()
        self.assertIsInstance(v, float)

        v = CVGetHostClockMinimumTimeDelta()
        self.assertIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
