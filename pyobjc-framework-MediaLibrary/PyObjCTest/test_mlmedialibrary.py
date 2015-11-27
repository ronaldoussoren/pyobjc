import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import MediaLibrary

    class TestMLMediaLibrary (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MediaLibrary.MLMediaLibrary, objc.objc_class)

        @min_os_level("10.10")
        def testConstants10_10(self):
            self.assertIsInstance(MediaLibrary.MLMediaSourcePhotosIdentifier, unicode)

        @min_os_level("10.9")
        def testConstants(self):
            self.assertIsInstance(MediaLibrary.MLMediaSourceiPhotoIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaSourceiTunesIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaSourceApertureIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaSourceiMovieIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaSourceFinalCutIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaSourceGarageBandIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaSourceLogicIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaSourcePhotoBoothIdentifier, unicode)

            self.assertIsInstance(MediaLibrary.MLMediaSourceCustomFoldersIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaSourceMoviesFolderIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaSourceAppDefinedFoldersIdentifier, unicode)

            self.assertIsInstance(MediaLibrary.MLMediaLoadSourceTypesKey, unicode)

            self.assertIsInstance(MediaLibrary.MLMediaLoadIncludeSourcesKey, unicode)

            self.assertIsInstance(MediaLibrary.MLMediaLoadExcludeSourcesKey, unicode)

            self.assertIsInstance(MediaLibrary.MLMediaLoadFoldersKey, unicode)

            self.assertIsInstance(MediaLibrary.MLMediaLoadAppleLoops, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaLoadMoviesFolder, unicode)

            self.assertIsInstance(MediaLibrary.MLMediaLoadAppFoldersKey, unicode)

if __name__ == "__main__":
    main()
