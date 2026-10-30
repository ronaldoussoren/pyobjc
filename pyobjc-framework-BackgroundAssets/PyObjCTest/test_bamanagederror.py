from PyObjCTools.TestSupport import TestCase, min_os_level
import BackgroundAssets


class TestBAManagedError(TestCase):
    def test_enums(self):
        self.assertIsEnumType(BackgroundAssets.BAManagedErrorCode)
        self.assertEqual(BackgroundAssets.BAManagedErrorCodeAssetPackNotFound, 0)
        self.assertEqual(BackgroundAssets.BAManagedErrorCodeFileNotFound, 1)
        self.assertEqual(BackgroundAssets.BAManagedErrorCodeLocalAvailabilityFailure, 2)

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(BackgroundAssets.BAManagedErrorDomain, str)
        self.assertIsInstance(BackgroundAssets.BAAssetPackIdentifierErrorKey, str)

    @min_os_level("27.0")
    def test_constants27_0(self):
        self.assertIsInstance(BackgroundAssets.BASuccessesErrorKey, str)
        self.assertIsInstance(BackgroundAssets.BAFailuresErrorKey, str)
