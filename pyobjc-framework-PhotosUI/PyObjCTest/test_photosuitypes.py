from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import PhotosUI

    class TestPhotosUITypes(TestCase):
        @min_os_level("10.13")
        def testConstants(self):
            self.assertIsInstance(PhotosUI.PHProjectTypeUndefined, unicode)

        @min_os_level("10.14")
        def test_constants_10_14(self):
            self.assertIsInstance(PhotosUI.PHProjectCategoryBook, unicode)
            self.assertIsInstance(PhotosUI.PHProjectCategoryCalendar, unicode)
            self.assertIsInstance(PhotosUI.PHProjectCategoryCard, unicode)
            self.assertIsInstance(PhotosUI.PHProjectCategoryPrints, unicode)
            self.assertIsInstance(PhotosUI.PHProjectCategorySlideshow, unicode)
            self.assertIsInstance(PhotosUI.PHProjectCategoryWallDecor, unicode)
            self.assertIsInstance(PhotosUI.PHProjectCategoryOther, unicode)

        @min_os_level("10.14.2")
        def test_constants_10_14_4(self):
            self.assertIsInstance(PhotosUI.PHProjectCategoryUndefined, unicode)


if __name__ == "__main__":
    main()
