from PyObjCTools.TestSupport import *
from CoreLocation import *
import os

try:
    unicode
except NameError:
    unicode = str

class TestCLErrorDomain (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCLErrorDomain, unicode)

if __name__ == "__main__":
    main()
