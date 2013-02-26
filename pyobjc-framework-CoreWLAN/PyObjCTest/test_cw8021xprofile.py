from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCW8021XProfile (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(CoreWLAN.CW8021XProfile.alwaysPromptForPassword)
        self.assertArgIsBOOL(CoreWLAN.CW8021XProfile.setAlwaysPromptForPassword_, 0)
        self.assertResultIsBOOL(CoreWLAN.CW8021XProfile.isEqualToProfile_)

if __name__ == "__main__":
    main()
