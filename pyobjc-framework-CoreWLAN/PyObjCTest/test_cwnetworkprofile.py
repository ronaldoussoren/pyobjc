from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCWNetworkProfile (TestCase):
    @min_os_level('10.7')
    def test_methods10_7(self):
        self.assertResultIsBOOL(CoreWLAN.CWNetworkProfile.isEqualToNetworkProfile_);

if __name__ == "__main__":
    main()
