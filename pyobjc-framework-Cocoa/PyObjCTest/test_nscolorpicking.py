from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSColorPickingHelper (NSObject):
    def supportsMode_(self, m):
        return 0

    def provideNewView_(self, i):
        return None

    def initWithPickerMask_colorPanel_(self, m, p): return 1


class TestNSColorPicking (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(TestNSColorPickingHelper.supportsMode_)
        self.assertArgIsBOOL(TestNSColorPickingHelper.provideNewView_, 0)

        self.assertArgHasType(TestNSColorPickingHelper.initWithPickerMask_colorPanel_, 0, objc._C_NSUInteger)

    def testProtocols(self):
        objc.protocolNamed('NSColorPickingCustom')
        objc.protocolNamed('NSColorPickingDefault')

if __name__ == "__main__":
    main()
