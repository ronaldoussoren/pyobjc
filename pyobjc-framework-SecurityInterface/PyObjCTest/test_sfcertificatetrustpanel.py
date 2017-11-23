from PyObjCTools.TestSupport import *

import SecurityInterface

class TestSFCertificateTrustPanel (TestCase):
    def test_classes(self):
        SecurityInterface.SFCertificateTrustPanel

    def test_methods(self):
        self.assertArgIsSEL(SecurityInterface.SFCertificateTrustPanel.beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_trust_message_, 2, b'v@:@' + objc._C_NSInteger + b'^v')

if __name__ == "__main__":
    main()
