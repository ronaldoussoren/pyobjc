from AppKit import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str

class TestNSDate (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSDate.isEqualToDate_)

    def testConstants(self):
        self.assertEqual(NSTimeIntervalSince1970, 978307200.0)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSSystemClockDidChangeNotification, unicode)


if __name__ == "__main__":
    main()
