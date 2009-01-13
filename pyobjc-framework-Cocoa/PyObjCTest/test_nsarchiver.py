from Foundation import *
from PyObjCTools.TestSupport import *

class TestArchiver (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSInconsistentArchiveException, unicode))


if __name__ == "__main__":
    main()
