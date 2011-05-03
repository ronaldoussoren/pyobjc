
from PyObjCTools.TestSupport import *
from CoreLocation import *

class TestCLError (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.assertIsInstance(kCLErrorDomain, unicode)

        self.assertEqual(kCLErrorLocationUnknown, 0)
        self.assertEqual(kCLErrorDenied, 1)

if __name__ == "__main__":
    main()
