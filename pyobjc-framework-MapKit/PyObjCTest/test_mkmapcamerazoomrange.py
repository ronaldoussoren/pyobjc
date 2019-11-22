import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKMapCameraZoomRange(TestCase):
        @min_os_level("10.15")
        def test_constants(self):
            self.assertIsInstance(MapKit.MKMapCameraZoomDefault, float)


if __name__ == "__main__":
    main()
