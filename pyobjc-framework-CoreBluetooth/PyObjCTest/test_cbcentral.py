import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBCentral (TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertHasAttr(CoreBluetooth, "CBCentral")
        self.assertIsInstance(CoreBluetooth.CBCentral, objc.objc_class)

if __name__ == "__main__":
    main()
