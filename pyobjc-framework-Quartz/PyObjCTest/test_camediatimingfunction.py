
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

try:
    unicode
except NameError:
    unicode = str

class TestCAMediaTimingFunction (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(kCAMediaTimingFunctionLinear, unicode)
        self.assertIsInstance(kCAMediaTimingFunctionEaseIn, unicode)
        self.assertIsInstance(kCAMediaTimingFunctionEaseOut, unicode)
        self.assertIsInstance(kCAMediaTimingFunctionEaseInEaseOut, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCAMediaTimingFunctionDefault, unicode)

if __name__ == "__main__":
    main()
