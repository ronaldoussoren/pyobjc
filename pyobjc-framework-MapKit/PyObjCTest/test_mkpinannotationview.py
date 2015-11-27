import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKPinAnnotationView (TestCase):
        @min_os_level("10.9")
        def testConstants(self):
            self.assertEqual(MapKit.MKPinAnnotationColorRed, 0)
            self.assertEqual(MapKit.MKPinAnnotationColorGreen, 1)
            self.assertEqual(MapKit.MKPinAnnotationColorPurple, 2)

        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKPinAnnotationView, objc.objc_class)

            self.assertResultIsBOOL(MapKit.MKPinAnnotationView.animatesDrop)
            self.assertArgIsBOOL(MapKit.MKPinAnnotationView.setAnimatesDrop_, 0)

if __name__ == "__main__":
    main()
