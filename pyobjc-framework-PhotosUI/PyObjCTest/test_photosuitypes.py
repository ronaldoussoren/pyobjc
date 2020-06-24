from PyObjCTools.TestSupport import TestCase, min_os_level
import PhotosUI


class TestPhotosUITypes(TestCase):
    @min_os_level("10.13")
    def testConstants(self):
        self.assertIsInstance(PhotosUI.PHProjectTypeUndefined, str)

    @min_os_level("10.14")
    def test_constants_10_14(self):
        self.assertIsInstance(PhotosUI.PHProjectCategoryBook, str)
        self.assertIsInstance(PhotosUI.PHProjectCategoryCalendar, str)
        self.assertIsInstance(PhotosUI.PHProjectCategoryCard, str)
        self.assertIsInstance(PhotosUI.PHProjectCategoryPrints, str)
        self.assertIsInstance(PhotosUI.PHProjectCategorySlideshow, str)
        self.assertIsInstance(PhotosUI.PHProjectCategoryWallDecor, str)
        self.assertIsInstance(PhotosUI.PHProjectCategoryOther, str)

    @min_os_level("10.14.2")
    def test_constants_10_14_4(self):
        self.assertIsInstance(PhotosUI.PHProjectCategoryUndefined, str)
