from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVMovie (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVMovieReferenceRestrictionsKey, unicode)

        self.assertEqual(AVFoundation.AVMovieWritingAddMovieHeaderToDestination, 0)
        self.assertEqual(AVFoundation.AVMovieWritingTruncateDestinationToMovieHeaderOnly, 1<<0)

        self.assertIsInstance(AVFoundation.AVFragmentedMovieContainsMovieFragmentsDidChangeNotification, unicode)
        self.assertIsInstance(AVFoundation.AVFragmentedMovieDurationDidChangeNotification, unicode)
        self.assertIsInstance(AVFoundation.AVFragmentedMovieWasDefragmentedNotification, unicode)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVMovie.canContainMovieFragments)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(AVFoundation.AVMovie.isCompatibleWithFileType_)

        self.assertResultIsBOOL(AVFoundation.AVMovie.containsMovieFragments)
        self.assertArgIsOut(AVFoundation.AVMovie.movieHeaderWithFileType_error_, 1)

        self.assertResultIsBOOL(AVFoundation.AVMovie.writeMovieHeaderToURL_fileType_options_error_)
        self.assertArgIsOut(AVFoundation.AVMovie.writeMovieHeaderToURL_fileType_options_error_, 3)

        self.assertArgIsOut(AVFoundation.AVMutableMovie.movieWithURL_options_error_, 2)
        self.assertArgIsOut(AVFoundation.AVMutableMovie.initWithURL_options_error_, 2)
        self.assertArgIsOut(AVFoundation.AVMutableMovie.movieWithData_options_error_, 2)
        self.assertArgIsOut(AVFoundation.AVMutableMovie.initWithData_options_error_, 2)
        self.assertArgIsOut(AVFoundation.AVMutableMovie.movieWithSettingsFromMovie_options_error_, 2)
        self.assertArgIsOut(AVFoundation.AVMutableMovie.initWithSettingsFromMovie_options_error_, 2)

        self.assertResultIsBOOL(AVFoundation.AVMutableMovie.isModified)
        self.assertArgIsBOOL(AVFoundation.AVMutableMovie.setModified_, 0)

        self.assertResultIsBOOL(AVFoundation.AVMutableMovie.insertTimeRange_ofAsset_atTime_copySampleData_error_)
        self.assertArgIsBOOL(AVFoundation.AVMutableMovie.insertTimeRange_ofAsset_atTime_copySampleData_error_, 3)
        self.assertArgIsOut(AVFoundation.AVMutableMovie.insertTimeRange_ofAsset_atTime_copySampleData_error_, 4)

if __name__ == "__main__":
    main()
