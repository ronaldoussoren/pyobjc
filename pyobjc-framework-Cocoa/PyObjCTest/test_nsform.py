from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSForm (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(NSForm.setBordered_, 0)
        self.assertArgIsBOOL(NSForm.setBezeled_, 0)

if __name__ == "__main__":
    main()
