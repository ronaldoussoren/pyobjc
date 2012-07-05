from PyObjCTools.TestSupport import *
from CoreLocation import *

CLGeocodeCompletionHandler = b'v@@'

class TestCLGeocoder (TestCase):
    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertArgIsBlock(CLGeocoder.geocodeAddressDictionary_completionHandler_, 1, CLGeocodeCompletionHandler)
        self.assertArgIsBlock(CLGeocoder.geocodeAddressString_completionHandler_, 1, CLGeocodeCompletionHandler)
        self.assertArgIsBlock(CLGeocoder.geocodeAddressString_inRegion_completionHandler_, 2, CLGeocodeCompletionHandler)
        self.assertArgIsBlock(CLGeocoder.reverseGeocodeLocation_completionHandler_, 1, CLGeocodeCompletionHandler)

        self.assertResultIsBOOL(CLGeocoder.isGeocoding)

if __name__ == "__main__":
    main()
