from PyObjCTools.TestSupport import *

import AVFoundation

try:
    unicode
except NameError:
    unicode = str


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
        self.asssertResultIsBOOL(AVFoundation.AVMovie.canContainMovieFragments)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.asssertResultIsBOOL(AVFoundation.AVMovie.containsMovieFragments)
        self.assertArgIsOut(AVFoundation.AVMovie.movieHeaderWithFileType_error_, 1)

        self.asssertResultIsBOOL(AVFoundation.AVMovie.writeMovieHeaderToURL_options_error_)
        self.assertArgIsOut(AVFoundation.AVMovie.writeMovieHeaderToURL_options_error_, 2)

        self.assertArgIsOut(AVFoundation.AVMutableMovie.movieWithURL_options_error_, 2)
        self.assertArgIsOut(AVFoundation.AVMutableMovie.initWithURL_options_error_, 2)
        self.assertArgIsOut(AVFoundation.AVMutableMovie.movieWithData_options_error_, 2)
        self.assertArgIsOut(AVFoundation.AVMutableMovie.initWithData_options_error_, 2)
        self.assertArgIsOut(AVFoundation.AVMutableMovie.movieWithSettingsFromMovie_options_error_, 2)
        self.assertArgIsOut(AVFoundation.AVMutableMovie.initWithSettingsFromMovie_options_error_, 2)

        self.asssertResultIsBOOL(AVFoundation.AVMutableMovie.isModified)
        self.asssertArgIsBOOL(AVFoundation.AVMutableMovie.setModified_, 0)

        self.asssertResultIsBOOL(AVFoundation.AVMutableMovie.insertTimeRange_ofAsset_atTime_copySampleData_error_)
        self.asssertArgIsBOOL(AVFoundation.AVMutableMovie.insertTimeRange_ofAsset_atTime_copySampleData_error_, 3)
        self.asssertArgIsOut(AVFoundation.AVMutableMovie.insertTimeRange_ofAsset_atTime_copySampleData_error_, 4)

if __name__ == "__main__":
    main()
