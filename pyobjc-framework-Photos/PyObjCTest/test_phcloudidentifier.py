from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHCloudIdentifier (TestCase):
        @min_os_level('10.13')
        def testConstants(self):
            self.assertIsInstance(Photos.PHLocalIdentifierNotFound, unicode)

if __name__ == "__main__":
    main()
