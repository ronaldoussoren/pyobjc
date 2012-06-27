
from PyObjCTools.TestSupport import *
from CoreLocation import *

try:
    unicode
except NameError:
    unicode = str

class TestCLHeading (TestCase):
    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(kCLHeadingFilterNone, float)


if __name__ == "__main__":
    main()
