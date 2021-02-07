import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level

CLGeocodeCompletionHandler = b"v@@"


class TestCLGeocoder(TestCase):
    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertArgIsBlock(
            CoreLocation.CLGeocoder.geocodeAddressDictionary_completionHandler_,
            1,
            CLGeocodeCompletionHandler,
        )
        self.assertArgIsBlock(
            CoreLocation.CLGeocoder.geocodeAddressString_completionHandler_,
            1,
            CLGeocodeCompletionHandler,
        )
        self.assertArgIsBlock(
            CoreLocation.CLGeocoder.geocodeAddressString_inRegion_completionHandler_,
            2,
            CLGeocodeCompletionHandler,
        )
        self.assertArgIsBlock(
            CoreLocation.CLGeocoder.reverseGeocodeLocation_completionHandler_,
            1,
            CLGeocodeCompletionHandler,
        )

        self.assertResultIsBOOL(CoreLocation.CLGeocoder.isGeocoding)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            CoreLocation.CLGeocoder.reverseGeocodeLocation_preferredLocale_completionHandler_,
            2,
            CLGeocodeCompletionHandler,
        )
        self.assertArgIsBlock(
            CoreLocation.CLGeocoder.geocodeAddressString_inRegion_preferredLocale_completionHandler_,
            3,
            CLGeocodeCompletionHandler,
        )
        self.assertArgIsBlock(
            CoreLocation.CLGeocoder.geocodePostalAddress_completionHandler_,
            1,
            CLGeocodeCompletionHandler,
        )
        self.assertArgIsBlock(
            CoreLocation.CLGeocoder.geocodePostalAddress_preferredLocale_completionHandler_,
            2,
            CLGeocodeCompletionHandler,
        )
