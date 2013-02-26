from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCWNetworkProfile (TestCase):
    @min_os_level('10.7')
    def test_methods10_7(self):
        self.assertResultIsBOOL(CoreWLAN.CWNetworkProfile.isEqualToNetworkProfile_);
        self.assertResultIsBOOL(CoreWLAN.CWNetworkProfile.isEqualToNetwork_);
        self.assertResultIsBOOL(CoreWLAN.CWNetworkProfile.supportsSecurity_);
        self.assertResultIsBOOL(CoreWLAN.CWNetworkProfile.supportsPHYMode_);
        self.assertResultIsBOOL(CoreWLAN.CWNetworkProfile.isIBSS);

if __name__ == "__main__":
    main()
