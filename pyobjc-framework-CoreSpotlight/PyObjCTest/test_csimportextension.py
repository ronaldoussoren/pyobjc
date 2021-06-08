from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreSpotlight


class TestCSImportExtension(TestCase):
    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(
            CoreSpotlight.CSImportExtension.updateAttributes_forFileAtURL_error_
        )
        self.assertArgIsOut(
            CoreSpotlight.CSImportExtension.updateAttributes_forFileAtURL_error_, 2
        )
