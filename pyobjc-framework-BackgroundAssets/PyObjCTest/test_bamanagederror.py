from PyObjCTools.TestSupport import TestCase, min_os_level
import BackgroundAssets


class TestBAManagedError(TestCase):
    def test_constants(self):
        self.assertIsEnumType(BackgroundAssets.BAManagedErrorCode)
        self.assertEqual(BackgroundAssets.BAManagedErrorCodeAssetPackNotFound, 0)
        self.assertEqual(BackgroundAssets.BAManagedErrorCodeFileNotFound, 1)

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(BackgroundAssets.BAManagedErrorDomain, str)
