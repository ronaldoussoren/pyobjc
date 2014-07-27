import sys

try:
    unicode
except NameError:
    unicode = str

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBService (TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(CoreBleutooth.CBService, objc.objc_class)
        self.assertIsInstance(CoreBleutooth.CBMutableService, objc.objc_class)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(CoreBleutooth.CBService.isPrimary)
        self.assertResultIsBOOL(CoreBleutooth.CBMutableService.isPrimary)
        self.assertArgIsBOOL(CoreBleutooth.CBMutableService.setPrimary_, 0)
        self.assertArgIsBOOL(CoreBleutooth.CBMutableService.initWithType_primary_, 1)

if __name__ == "__main__":
    main()
