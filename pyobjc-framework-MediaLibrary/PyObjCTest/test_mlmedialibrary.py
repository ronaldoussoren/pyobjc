from PyObjCTools.TestSupport import TestCase
import MediaLibrary


class TestMLMediaLibrary(TestCase):
    def test_constants(self):
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
        self.assertIsInstance(MediaLibrary.MLMediaSourcePhotosIdentifier, str)

        self.assertIsInstance(MediaLibrary.MLMediaLoadSourceTypesKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaLoadIncludeSourcesKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaLoadExcludeSourcesKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaLoadFoldersKey, str)

        self.assertIsInstance(MediaLibrary.MLMediaLoadAppleLoops, str)
        self.assertIsInstance(MediaLibrary.MLMediaLoadMoviesFolder, str)

        self.assertIsInstance(MediaLibrary.MLMediaLoadAppFoldersKey, str)
