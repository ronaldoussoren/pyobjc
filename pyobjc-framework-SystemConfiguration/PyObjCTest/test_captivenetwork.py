from PyObjCTools.TestSupport import *

import SystemConfiguration
import objc

class TestCaptiveNework (TestCase):
    @min_os_level('10.8')
    def testFunctions10_8(self):
        self.assertResultIsBOOL(SystemConfiguration.CNSetSupportedSSIDs)
        self.assertResultIsBOOL(SystemConfiguration.CNMarkPortalOnline)
        self.assertResultIsBOOL(SystemConfiguration.CNMarkPortalOffline)
        self.assertResultIsCFRetained(SystemConfiguration.CNCopySupportedInterfaces)

if __name__ == "__main__":
    main()
