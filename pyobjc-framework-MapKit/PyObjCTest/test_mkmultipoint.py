import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKMultiPoint (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKMultiPoint, objc.objc_class)

            self.assertResultIsVariableSize(MapKit.MKMultiPoint.points) #  XXX: Gone in 10.11 SDK headers?

            self.assertArgSizeInArg(MapKit.MKMultiPoint.getCoordinates_range_, 0, 1)
            self.assertArgIsOut(MapKit.MKMultiPoint.getCoordinates_range_, 0)

if __name__ == "__main__":
    main()
