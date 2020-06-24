from PyObjCTools.TestSupport import TestCase, min_os_level
import QTKit


class TestQTError(TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(QTKit.QTMovieModernizerStatusUnknown, 0)
        self.assertEqual(QTKit.QTMovieModernizerStatusPreparing, 1)
        self.assertEqual(QTKit.QTMovieModernizerStatusRunning, 2)
        self.assertEqual(QTKit.QTMovieModernizerStatusCancelled, 3)
        self.assertEqual(QTKit.QTMovieModernizerStatusFailed, 4)
        self.assertEqual(QTKit.QTMovieModernizerStatusCompletedWithSuccess, 5)
        self.assertEqual(QTKit.QTMovieModernizerStatusNotRequired, 6)

        self.assertIsInstance(QTKit.QTMovieModernizerOutputFormat_H264, str)
        self.assertIsInstance(QTKit.QTMovieModernizerOutputFormat_AppleProRes422, str)
        self.assertIsInstance(QTKit.QTMovieModernizerOutputFormat_AppleProRes4444, str)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTMovieModernizer.requiresModernization_error_)
        self.assertArgIsOut(QTKit.QTMovieModernizer.requiresModernization_error_, 1)

        self.assertArgIsBlock(
            QTKit.QTMovieModernizer.modernizeWithCompletionHandler_, 0, b"v"
        )
