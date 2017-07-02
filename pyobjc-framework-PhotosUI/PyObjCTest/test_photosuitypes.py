from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import PhotosUI

    class TestPhotosUITypes (TestCase):
        @min_os_level('10.13')
        def testConstants(self):
            self.assertIsInstance(PhotosUI.PHProjectTypeUndefined, unicode)

if __name__ == "__main__":
    main()
