from PyObjCTools.TestSupport import TestCase, min_os_level

import DeviceCheck


class TestDCAppAttestService(TestCase):
    @min_os_level("11.0")
    def test_methods(self):
        self.assertResultIsBOOL(DeviceCheck.DCAppAttestService.isSupported)

        self.assertArgIsBlock(
            DeviceCheck.DCAppAttestService.generateKeyWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            DeviceCheck.DCAppAttestService.attestKey_clientDataHash_completionHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            DeviceCheck.DCAppAttestService.generateAssertion_clientDataHash_completionHandler_,
            2,
            b"v@@",
        )
