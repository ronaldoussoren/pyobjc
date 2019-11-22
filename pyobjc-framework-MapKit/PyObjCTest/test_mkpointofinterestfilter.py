import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKPointOfInterestFilter(TestCase):
        @min_os_level("10.15")
        def test_methods(self):
            self.assertResultIsBOOL(MapKit.MKPointOfInterestFilter.includesCategory_)
            self.assertResultIsBOOL(MapKit.MKPointOfInterestFilter.excludesCategory_)


if __name__ == "__main__":
    main()
