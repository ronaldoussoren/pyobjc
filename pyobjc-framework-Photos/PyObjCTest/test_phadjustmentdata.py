from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHAdjustmentData (TestCase):
        @min_os_level('10.11')
        def testClasses(self):
            self.assertIsInstance(Photos.PHAdjustmentData, objc.objc_class)

if __name__ == "__main__":
    main()
