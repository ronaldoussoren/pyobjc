import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKDirectionsRequest (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKDirectionsResponse, objc.objc_class)
            self.assertIsInstance(MapKit.MKRoute, objc.objc_class)
            self.assertIsInstance(MapKit.MKRouteStep, objc.objc_class)
            self.assertIsInstance(MapKit.MKETAResponse, objc.objc_class)

if __name__ == "__main__":
    main()
