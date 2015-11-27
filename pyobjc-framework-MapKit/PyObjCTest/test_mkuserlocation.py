import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKUserLocation (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKUserLocation, objc.objc_class)

            self.assertResultIsBOOL(MapKit.MKUserLocation.isUpdating)

if __name__ == "__main__":
    main()
