import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVMovie(TestCase):
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVMovieReferenceRestrictionsKey, str)

        self.assertEqual(
            AVFoundation.AVMovieWritingAddMovieHeaderToDestination, 0
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVMovieWritingTruncateDestinationToMovieHeaderOnly,
            1 << 0,  # noqa: B950
        )

        self.assertIsInstance(
            AVFoundation.AVFragmentedMovieContainsMovieFragmentsDidChangeNotification,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVFragmentedMovieDurationDidChangeNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVFragmentedMovieWasDefragmentedNotification, str
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVMovie.canContainMovieFragments)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AVFoundation.AVMovie.isCompatibleWithFileType_)

        self.assertResultIsBOOL(AVFoundation.AVMovie.containsMovieFragments)
        self.assertArgIsOut(
            AVFoundation.AVMovie.movieHeaderWithFileType_error_, 1
        )  # noqa: B950

        self.assertResultIsBOOL(
            AVFoundation.AVMovie.writeMovieHeaderToURL_fileType_options_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVMovie.writeMovieHeaderToURL_fileType_options_error_,
            3,  # noqa: B950
        )

        self.assertArgIsOut(
            AVFoundation.AVMutableMovie.movieWithURL_options_error_, 2
        )  # noqa: B950
        self.assertArgIsOut(
            AVFoundation.AVMutableMovie.initWithURL_options_error_, 2
        )  # noqa: B950
        self.assertArgIsOut(
            AVFoundation.AVMutableMovie.movieWithData_options_error_, 2
        )  # noqa: B950
        self.assertArgIsOut(
            AVFoundation.AVMutableMovie.initWithData_options_error_, 2
        )  # noqa: B950
        self.assertArgIsOut(
            AVFoundation.AVMutableMovie.movieWithSettingsFromMovie_options_error_,
            2,  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVMutableMovie.initWithSettingsFromMovie_options_error_,
            2,  # noqa: B950
        )

        self.assertResultIsBOOL(AVFoundation.AVMutableMovie.isModified)
        self.assertArgIsBOOL(AVFoundation.AVMutableMovie.setModified_, 0)

        self.assertResultIsBOOL(
            AVFoundation.AVMutableMovie.insertTimeRange_ofAsset_atTime_copySampleData_error_  # noqa: B950
        )
        self.assertArgIsBOOL(
            AVFoundation.AVMutableMovie.insertTimeRange_ofAsset_atTime_copySampleData_error_,  # noqa: B950
            3,
        )
        self.assertArgIsOut(
            AVFoundation.AVMutableMovie.insertTimeRange_ofAsset_atTime_copySampleData_error_,  # noqa: B950
            4,
        )
