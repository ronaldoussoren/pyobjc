import CoreWLAN
from PyObjCTools.TestSupport import TestCase


class TestCoreWLANConstants(TestCase):
    def test_constants(self):
        self.assertIsInstance(CoreWLAN.CWErrorDomain, str)
        self.assertIsInstance(CoreWLAN.CWScanCacheDidUpdateNotification, str)
        self.assertIsInstance(CoreWLAN.CWLinkQualityDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.CWLinkQualityNotificationRSSIKey, str)
        self.assertIsInstance(CoreWLAN.CWLinkQualityNotificationTransmitRateKey, str)
        self.assertIsInstance(CoreWLAN.CWServiceDidChangeNotification, str)

        self.assertIsInstance(CoreWLAN.CWPowerDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.CWSSIDDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.CWBSSIDDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.CWLinkDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.CWModeDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.CWCountryCodeDidChangeNotification, str)

        self.assertIsInstance(CoreWLAN.kCWErrorDomain, str)
        self.assertIsInstance(CoreWLAN.kCWPowerDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.kCWSSIDDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.kCWBSSIDDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.kCWLinkDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.kCWModeDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.kCWCountryCodeDidChangeNotification, str)
        self.assertIsInstance(CoreWLAN.kCWAssocKeyPassphrase, str)
        self.assertIsInstance(CoreWLAN.kCWAssocKey8021XProfile, str)
        self.assertIsInstance(CoreWLAN.kCWIBSSKeySSID, str)
        self.assertIsInstance(CoreWLAN.kCWIBSSKeyChannel, str)
        self.assertIsInstance(CoreWLAN.kCWIBSSKeyPassphrase, str)
        self.assertIsInstance(CoreWLAN.kCWScanKeySSID, str)
        self.assertIsInstance(CoreWLAN.kCWScanKeyBSSID, str)
        self.assertIsInstance(CoreWLAN.kCWScanKeyMerge, str)
        self.assertIsInstance(CoreWLAN.kCWScanKeyScanType, str)
        self.assertIsInstance(CoreWLAN.kCWScanKeyDwellTime, str)
        self.assertIsInstance(CoreWLAN.kCWScanKeyRestTime, str)
