import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import MapKit

    class TestMKAnnotation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKAnnotation, objc.objc_class)

if __name__ == "__main__":
    main()
