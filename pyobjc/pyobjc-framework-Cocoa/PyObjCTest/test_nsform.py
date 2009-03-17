from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSForm (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSForm.setBordered_, 0)
        self.failUnlessArgIsBOOL(NSForm.setBezeled_, 0)

if __name__ == "__main__":
    main()
