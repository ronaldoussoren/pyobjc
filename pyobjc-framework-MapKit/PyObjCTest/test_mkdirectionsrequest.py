import sys

try:
    unicode
except NameError:
    unicode = str

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKDirectionsRequest (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKDirectionsRequest, objc.objc_class)

            self.assertArgIsBlock(MapKit.MKDirections.calculateDirectionsWithCompletionHandler_, 0, MKDirectionsHandler)
            self.assertArgIsBlock(MapKit.MKDirections.calculateETAWithCompletionHandler_, 0, MKETAHandler)

            self.assertResultIsBOOL(MapKit.MKDirections.requestsAlternateRoutes)
            self.assertArgIsBOOL(MapKit.MKDirections.setRequestsAlternateRoutes_, 0)

            self.assertResultIsBOOL(MapKit.MKDirections.isDirectionsRequestURL_)

if __name__ == "__main__":
    main()
