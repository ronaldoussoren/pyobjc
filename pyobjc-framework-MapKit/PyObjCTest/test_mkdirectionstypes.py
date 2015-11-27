import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKDirectionsTypes (TestCase):
        @min_os_level("10.9")
        def testConstants(self):
            self.assertEqual(MapKit.MKDirectionsTransportTypeAutomobile, 1 << 0)
            self.assertEqual(MapKit.MKDirectionsTransportTypeWalking, 1 << 1)
            self.assertEqual(MapKit.MKDirectionsTransportTypeAny, 0x0FFFFFFF)

        @min_os_level("10.11")
        def testConstants10_11(self):
            self.assertEqual(MapKit.MKDirectionsTransportTypeTransit, 1 << 2)

if __name__ == "__main__":
    main()
