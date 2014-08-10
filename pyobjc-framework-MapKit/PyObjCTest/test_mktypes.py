import sys

try:
    unicode
except NameError:
    unicode = str

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKCircle (TestCase):
        @min_os_level("10.9")
        def testConstants(self):
            self.assertEqual(MapKit.MKMapTypeStandard, 0)
            self.assertEqual(MapKit.MKMapTypeSatellite, 1)
            self.assertEqual(MapKit.MKMapTypeHybrid, 2)

            self.assertIsInstance(MapKit.MKErrorDomain, unicode)

            self.assertEqual(MapKit.MKErrorUnknown, 1)
            self.assertEqual(MapKit.MKErrorServerFailure, 2)
            self.assertEqual(MapKit.MKErrorLoadingThrottled, 3)
            self.assertEqual(MapKit.MKErrorPlacemarkNotFound, 4)
            self.assertEqual(MapKit.MKErrorDirectionsNotFound, 5)

if __name__ == "__main__":
    main()
