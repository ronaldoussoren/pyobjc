from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSDateIntervalFormatter (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSDateIntervalFormatterNoStyle, 0)
        self.assertEqual(NSDateIntervalFormatterShortStyle, 1)
        self.assertEqual(NSDateIntervalFormatterMediumStyle, 2)
        self.assertEqual(NSDateIntervalFormatterLongStyle, 3)
        self.assertEqual(NSDateIntervalFormatterFullStyle, 4)

if __name__ == "__main__":
    main()
