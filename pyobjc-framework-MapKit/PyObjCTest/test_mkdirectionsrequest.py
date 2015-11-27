import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKDirectionsRequest (TestCase):

        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKDirectionsRequest, objc.objc_class)

            self.assertResultIsBOOL(MapKit.MKDirectionsRequest.requestsAlternateRoutes)
            self.assertArgIsBOOL(MapKit.MKDirectionsRequest.setRequestsAlternateRoutes_, 0)

            self.assertResultIsBOOL(MapKit.MKDirectionsRequest.isDirectionsRequestURL_)

if __name__ == "__main__":
    main()
