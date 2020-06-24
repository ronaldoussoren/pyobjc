from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import MediaLibrary


class TestMLMediaLibrary(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MediaLibrary.MLMediaLibrary, objc.objc_class)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(MediaLibrary.MLMediaSourcePhotosIdentifier, str)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(MediaLibrary.MLMediaSourceiPhotoIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLMediaSourceiTunesIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLMediaSourceApertureIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLMediaSourceiMovieIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLMediaSourceFinalCutIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLMediaSourceGarageBandIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLMediaSourceLogicIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLMediaSourcePhotoBoothIdentifier, str)

        self.assertIsInstance(MediaLibrary.MLMediaSourceCustomFoldersIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLMediaSourceMoviesFolderIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLMediaSourceAppDefinedFoldersIdentifier, str
        )

        self.assertIsInstance(MediaLibrary.MLMediaLoadSourceTypesKey, str)

        self.assertIsInstance(MediaLibrary.MLMediaLoadIncludeSourcesKey, str)

        self.assertIsInstance(MediaLibrary.MLMediaLoadExcludeSourcesKey, str)

        self.assertIsInstance(MediaLibrary.MLMediaLoadFoldersKey, str)

        self.assertIsInstance(MediaLibrary.MLMediaLoadAppleLoops, str)
        self.assertIsInstance(MediaLibrary.MLMediaLoadMoviesFolder, str)

        self.assertIsInstance(MediaLibrary.MLMediaLoadAppFoldersKey, str)
