from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCWWirelessProfile (TestCase):
    @min_os_level('10.6')
    def test_methods10_6(self):
        self.assertResultIsBOOL(CoreWLAN.CWWirelessProfile.isEqualToProfile_);

if __name__ == "__main__":
    main()
