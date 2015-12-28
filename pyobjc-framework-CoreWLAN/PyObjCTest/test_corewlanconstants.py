from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCoreWLANConstants (TestCase):
    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(CoreWLAN.CWErrorDomain, unicode)
        self.assertIsInstance(CoreWLAN.CWScanCacheDidUpdateNotification, unicode)
        self.assertIsInstance(CoreWLAN.CWLinkQualityDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.CWLinkQualityNotificationRSSIKey, unicode)
        self.assertIsInstance(CoreWLAN.CWLinkQualityNotificationTransmitRateKey, unicode)
        self.assertIsInstance(CoreWLAN.CWServiceDidChangeNotification, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(CoreWLAN.kCWErrorDomain, unicode)
        self.assertIsInstance(CoreWLAN.kCWPowerDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.kCWSSIDDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.kCWBSSIDDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.kCWLinkDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.kCWModeDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.kCWCountryCodeDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.kCWAssocKeyPassphrase, unicode)
        self.assertIsInstance(CoreWLAN.kCWAssocKey8021XProfile, unicode)
        self.assertIsInstance(CoreWLAN.kCWIBSSKeySSID, unicode)
        self.assertIsInstance(CoreWLAN.kCWIBSSKeyChannel, unicode)
        self.assertIsInstance(CoreWLAN.kCWIBSSKeyPassphrase, unicode)
        self.assertIsInstance(CoreWLAN.kCWScanKeySSID, unicode)
        self.assertIsInstance(CoreWLAN.kCWScanKeyBSSID, unicode)
        self.assertIsInstance(CoreWLAN.kCWScanKeyMerge, unicode)
        self.assertIsInstance(CoreWLAN.kCWScanKeyScanType, unicode)
        self.assertIsInstance(CoreWLAN.kCWScanKeyDwellTime, unicode)
        self.assertIsInstance(CoreWLAN.kCWScanKeyRestTime, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(CoreWLAN.CWPowerDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.CWSSIDDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.CWBSSIDDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.CWLinkDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.CWModeDidChangeNotification, unicode)
        self.assertIsInstance(CoreWLAN.CWCountryCodeDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
