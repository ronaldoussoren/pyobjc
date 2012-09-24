from PyObjCTools.TestSupport import *

import SystemConfiguration
import objc

class TestCaptiveNework (TestCase):
    @min_os_level('10.8')
    def testFunctions10_8(self):
        self.assertResultHasType(SystemConfiguration.CNSetSupportedSSIDs, objc._C_NSBOOL)
        self.assertResultHasType(SystemConfiguration.CNMarkPortalOnline, objc._C_NSBOOL)
        self.assertResultHasType(SystemConfiguration.CNMarkPortalOffline, objc._C_NSBOOL)
        self.assertResultIsCFRetained(SystemConfiguration.CNCopySupportedInterfaces)

if __name__ == "__main__":
    main()
