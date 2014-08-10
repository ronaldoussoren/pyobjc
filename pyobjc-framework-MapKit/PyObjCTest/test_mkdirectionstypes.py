import sys

try:
    unicode
except NameError:
    unicode = str

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKDirectionsTypes (TestCase):
        @min_os_level("10.9")
        def testConstants(self):
            self.assertEqual(MapKit.MKDirectionsTransportTypeAutomobile, 1 << 0)
            self.assertEqual(MapKit.MKDirectionsTransportTypeWalking, 1 << 1)
            self.assertEqual(MapKit.MKDirectionsTransportTypeAny, 0x0FFFFFFF)

if __name__ == "__main__":
    main()
