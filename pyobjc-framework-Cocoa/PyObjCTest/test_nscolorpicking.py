from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSColorPickingHelper (NSObject):
    def supportsMode_(self, m):
        return 0

    def provideNewView_(self, i):
        return None


class TestNSColorPicking (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(TestNSColorPickingHelper.supportsMode_)
        self.assertArgIsBOOL(TestNSColorPickingHelper.provideNewView_, 0)

if __name__ == "__main__":
    main()
