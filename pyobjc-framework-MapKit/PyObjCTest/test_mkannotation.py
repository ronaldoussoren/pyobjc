import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKAnnotationHelper (MapKit.NSObject):
        def coordinate(self):
            return 1
        def setCoordinate_(self, value):
            pass

    class TestMKAnnotation (TestCase):
        @min_os_level("10.9")
        def testProtocols(self):
            self.assertIsInstance(objc.protocolNamed("MKAnnotation"), objc.formal_protocol)

            self.assertResultHasType(TestMKAnnotationHelper.coordinate, MapKit.CLLocationCoordinate2D.__typestr__)
            self.assertArgHasType(TestMKAnnotationHelper.setCoordinate_, 0, MapKit.CLLocationCoordinate2D.__typestr__)



if __name__ == "__main__":
    main()
