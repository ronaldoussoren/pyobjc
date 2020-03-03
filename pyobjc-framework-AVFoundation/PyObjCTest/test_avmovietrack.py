import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVMovieTrack(TestCase):
    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AVFoundation.AVMutableMovieTrack.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVMutableMovieTrack.setEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVMutableMovieTrack.isModified)
        self.assertArgIsBOOL(AVFoundation.AVMutableMovieTrack.setModified_, 0)

        self.assertResultIsBOOL(
            AVFoundation.AVMutableMovieTrack.hasProtectedContent
        )  # noqa: B950

        self.assertResultIsBOOL(
            AVFoundation.AVMutableMovieTrack.insertTimeRange_ofTrack_atTime_copySampleData_error_  # noqa: B950
        )
        self.assertArgIsBOOL(
            AVFoundation.AVMutableMovieTrack.insertTimeRange_ofTrack_atTime_copySampleData_error_,  # noqa: B950
            3,
        )
        self.assertArgIsOut(
            AVFoundation.AVMutableMovieTrack.insertTimeRange_ofTrack_atTime_copySampleData_error_,  # noqa: B950
            4,
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(
            AVFoundation.AVMutableMovieTrack.appendSampleBuffer_decodeTime_presentationTime_error_  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVMutableMovieTrack.appendSampleBuffer_decodeTime_presentationTime_error_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            AVFoundation.AVMutableMovieTrack.appendSampleBuffer_decodeTime_presentationTime_error_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AVFoundation.AVMutableMovieTrack.appendSampleBuffer_decodeTime_presentationTime_error_,  # noqa: B950
            3,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVMutableMovieTrack.insertMediaTimeRange_intoTimeRange_
        )

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(
            AVFoundation.AVFragmentedMovieTrackTimeRangeDidChangeNotification,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVFragmentedMovieTrackSegmentsDidChangeNotification,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVFragmentedMovieTrackTotalSampleDataLengthDidChangeNotification,  # noqa: B950
            str,
        )
