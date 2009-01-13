from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSProcessInfo (TestCase):
    def testConstants(self):
        self.assertEquals(NSWindowsNTOperatingSystem, 1)
        self.assertEquals(NSWindows95OperatingSystem, 2)
        self.assertEquals(NSSolarisOperatingSystem, 3)
        self.assertEquals(NSHPUXOperatingSystem, 4)
        self.assertEquals(NSMACHOperatingSystem, 5)
        self.assertEquals(NSSunOSOperatingSystem, 6)
        self.assertEquals(NSOSF1OperatingSystem, 7)


if __name__ == "__main__":
    main()
