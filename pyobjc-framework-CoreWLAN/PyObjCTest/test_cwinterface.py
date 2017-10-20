from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCWInterface (TestCase):
    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertArgIsBOOL(CoreWLAN.CWInterface.scanForNetworksWithName_includeHidden_error_, 1)
        self.assertArgIsOut(CoreWLAN.CWInterface.scanForNetworksWithName_includeHidden_error_, 2)

        self.assertArgIsBOOL(CoreWLAN.CWInterface.scanForNetworksWithSSID_includeHidden_error_, 1)
        self.assertArgIsOut(CoreWLAN.CWInterface.scanForNetworksWithSSID_includeHidden_error_, 2)

    @min_os_level('10.7')
    def test_methods10_7(self):
        self.assertResultIsBOOL(CoreWLAN.CWInterface.powerOn);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.deviceAttached);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.serviceActive);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.setPower_error_);
        self.assertArgIsBOOL(CoreWLAN.CWInterface.setPower_error_, 0);
        self.assertArgIsOut(CoreWLAN.CWInterface.setPower_error_, 1);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.setWLANChannel_error_);
        self.assertArgIsOut(CoreWLAN.CWInterface.setWLANChannel_error_, 1);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.setPairwiseMasterKey_error_);
        self.assertArgIsOut(CoreWLAN.CWInterface.setPairwiseMasterKey_error_, 1);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.setWEPKey_flags_index_error_);
        self.assertArgIsOut(CoreWLAN.CWInterface.setWEPKey_flags_index_error_, 3);

        self.assertArgIsOut(CoreWLAN.CWInterface.scanForNetworksWithSSID_error_, 1);
        self.assertArgIsOut(CoreWLAN.CWInterface.scanForNetworksWithName_error_, 1);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.associateToNetwork_password_error_);
        self.assertArgIsOut(CoreWLAN.CWInterface.associateToNetwork_password_error_, 2);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.associateToEnterpriseNetwork_identity_username_password_error_);
        self.assertArgIsOut(CoreWLAN.CWInterface.associateToEnterpriseNetwork_identity_username_password_error_, 4);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.startIBSSModeWithSSID_security_channel_password_error_);
        self.assertArgIsOut(CoreWLAN.CWInterface.startIBSSModeWithSSID_security_channel_password_error_, 4);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.commitConfiguration_authorization_error_);
        self.assertArgIsOut(CoreWLAN.CWInterface.commitConfiguration_authorization_error_, 2);

    @os_level_between('10.6', '10.8')
    def testMethods10_6(self):
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsWoW);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsWEP);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsAES_CCM);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsIBSS);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsTKIP);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsPMGT);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsHostAP);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsMonitorMode);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsWPA);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsWPA2);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsWME);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsShortGI40MHz);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsShortGI20MHz);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.supportsTSN);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.power);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.powerSave);
        self.assertResultIsBOOL(CoreWLAN.CWInterface.isEqualToInterface_);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.setChannel_error_);
        self.assertArgIsOut(CoreWLAN.CWInterface.setChannel_error_, 1);

        self.assertArgIsOut(CoreWLAN.CWInterface.scanForNetworksWithParameters_error_, 1);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.associateToNetwork_parameters_error_);
        self.assertArgIsOut(CoreWLAN.CWInterface.associateToNetwork_parameters_error_, 2);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.enableIBSSWithParameters_error_);
        self.assertArgIsOut(CoreWLAN.CWInterface.enableIBSSWithParameters_error_, 1);

        self.assertResultIsBOOL(CoreWLAN.CWInterface.commitConfiguration_error_);
        self.assertArgIsOut(CoreWLAN.CWInterface.commitConfiguration_error_, 1);

if __name__ == "__main__":
    main()
