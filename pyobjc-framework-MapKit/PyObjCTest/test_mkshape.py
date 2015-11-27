import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKShape (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKShape, objc.objc_class)

if __name__ == "__main__":
    main()
