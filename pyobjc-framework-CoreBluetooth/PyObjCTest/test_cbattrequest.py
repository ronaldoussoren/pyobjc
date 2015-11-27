import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestFinderSync (TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertHasAttr(CoreBluetooth, "CBATTRequest")
        self.assertIsInstance(CoreBluetooth.CBATTRequest, objc.objc_class)

if __name__ == "__main__":
    main()
