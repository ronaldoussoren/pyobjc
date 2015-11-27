from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTError (TestCase):
    @min_os_level('10.9')
    def testConstants(self):
        self.assertEqual(QTMovieModernizerStatusUnknown, 0)
        self.assertEqual(QTMovieModernizerStatusPreparing, 1)
        self.assertEqual(QTMovieModernizerStatusRunning, 2)
        self.assertEqual(QTMovieModernizerStatusCancelled, 3)
        self.assertEqual(QTMovieModernizerStatusFailed, 4)
        self.assertEqual(QTMovieModernizerStatusCompletedWithSuccess, 5)
        self.assertEqual(QTMovieModernizerStatusNotRequired, 6)

        self.assertIsInstance(QTMovieModernizerOutputFormat_H264, unicode)
        self.assertIsInstance(QTMovieModernizerOutputFormat_AppleProRes422, unicode)
        self.assertIsInstance(QTMovieModernizerOutputFormat_AppleProRes4444, unicode)

    @min_os_level('10.9')
    def testMethods(self):
        self.assertResultIsBOOL(QTMovieModernizer.requiresModernization_error_)
        self.assertArgIsOut(QTMovieModernizer.requiresModernization_error_, 1)

        self.assertArgIsBlock(QTMovieModernizer.modernizeWithCompletionHandler_, 0, b'v')


if __name__ == "__main__":
    main()
