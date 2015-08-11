from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSStatusBarButton (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertResultIsBOOL(NSStatusBarButton.appearsDisabled)
        self.assertArgIsBOOL(NSStatusBarButton.setAppearsDisabled_, 0)

if __name__ == "__main__":
    main()
