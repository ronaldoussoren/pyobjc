from PyObjCTools.TestSupport import TestCase, min_os_level
import PhotosUI


class TestPHProjectInfo(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(PhotosUI.PHProjectCreationSource)
        self.assertIsEnumType(PhotosUI.PHProjectSectionType)
        self.assertIsEnumType(PhotosUI.PHProjectTextElementType)

    def testConstants(self):
        self.assertEqual(PhotosUI.PHProjectCreationSourceUndefined, 0)
        self.assertEqual(PhotosUI.PHProjectCreationSourceUserSelection, 1)
        self.assertEqual(PhotosUI.PHProjectCreationSourceAlbum, 2)
        self.assertEqual(PhotosUI.PHProjectCreationSourceMemory, 3)
        self.assertEqual(PhotosUI.PHProjectCreationSourceMoment, 4)
        self.assertEqual(PhotosUI.PHProjectCreationSourceProject, 20)
        self.assertEqual(PhotosUI.PHProjectCreationSourceProjectBook, 21)
        self.assertEqual(PhotosUI.PHProjectCreationSourceProjectCalendar, 22)
        self.assertEqual(PhotosUI.PHProjectCreationSourceProjectCard, 23)
        self.assertEqual(PhotosUI.PHProjectCreationSourceProjectPrintOrder, 24)
        self.assertEqual(PhotosUI.PHProjectCreationSourceProjectSlideshow, 25)
        self.assertEqual(PhotosUI.PHProjectCreationSourceProjectExtension, 26)

        self.assertEqual(PhotosUI.PHProjectSectionTypeUndefined, 0)
        self.assertEqual(PhotosUI.PHProjectSectionTypeCover, 1)
        self.assertEqual(PhotosUI.PHProjectSectionTypeContent, 2)
        self.assertEqual(PhotosUI.PHProjectSectionTypeAuxiliary, 3)

        self.assertEqual(PhotosUI.PHProjectTextElementTypeBody, 0)
        self.assertEqual(PhotosUI.PHProjectTextElementTypeTitle, 1)
        self.assertEqual(PhotosUI.PHProjectTextElementTypeSubtitle, 2)

    @min_os_level("10.14")
    def testMethods(self):
        self.assertResultIsBOOL(PhotosUI.PHProjectInfo.brandingEnabled)
        self.assertResultIsBOOL(PhotosUI.PHProjectInfo.pageNumbersEnabled)
        self.assertResultIsBOOL(PhotosUI.PHProjectAssetElement.horizontallyFlipped)
        self.assertResultIsBOOL(PhotosUI.PHProjectAssetElement.verticallyFlipped)
