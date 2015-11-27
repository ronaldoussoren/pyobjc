from PyObjCTools.TestSupport import *
from CoreLocation import *
import os

class TestCLErrorDomain (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCLErrorDomain, unicode)

if __name__ == "__main__":
    main()
