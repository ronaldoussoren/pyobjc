import os

from CoreLocation import *
from PyObjCTools.TestSupport import *


class TestCLErrorDomain(TestCase):
    def testConstants(self):
        self.assertIsInstance(kCLErrorDomain, unicode)


if __name__ == "__main__":
    main()
