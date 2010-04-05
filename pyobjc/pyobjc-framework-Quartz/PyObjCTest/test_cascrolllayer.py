
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCAScrollLayer (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(kCAScrollNone, unicode)
        self.assertIsInstance(kCAScrollVertically, unicode)
        self.assertIsInstance(kCAScrollHorizontally, unicode)
        self.assertIsInstance(kCAScrollBoth, unicode)


if __name__ == "__main__":
    main()
