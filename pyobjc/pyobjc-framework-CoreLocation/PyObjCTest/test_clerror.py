
from PyObjCTools.TestSupport import *
from CoreLocation import *

class TestCLError (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.failUnlessIsInstance(kCLErrorDomain, unicode)

        self.failUnlessEqual(kCLErrorLocationUnknown, 0)
        self.failUnlessEqual(kCLErrorDenied, 1)

if __name__ == "__main__":
    main()
