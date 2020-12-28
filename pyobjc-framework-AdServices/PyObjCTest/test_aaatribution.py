import AdServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAAAtribution(TestCase):
    def test_constants(self):
        self.assertEqual(AdServices.AAAttributionErrorCodeNetworkError, 1)
        self.assertEqual(AdServices.AAAttributionErrorCodeInternalError, 2)
        self.assertEqual(AdServices.AAAttributionErrorCodePlatformNotSupported, 3)

    @min_os_level("10.16.1")
    def test_methods10_16_1(self):
        self.assertArgIsOut(AdServices.AAAttribution.attributionTokenWithError_, 0)
