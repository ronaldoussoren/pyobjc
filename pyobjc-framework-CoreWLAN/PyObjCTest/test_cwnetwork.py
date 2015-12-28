
from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCWNetwork (TestCase):
    @min_os_level('10.7')
    def test_methods10_7(self):
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.ibss);

    @min_os_level('10.6')
    def test_methods10_6(self):
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.isEqualToNetwork_);
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.isIBSS);

    @min_os_level('10.7')
    def test_methods10_7(self):
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.supportsSecurity_);
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.supportsPHYMode_);


if __name__ == "__main__":
    main()
