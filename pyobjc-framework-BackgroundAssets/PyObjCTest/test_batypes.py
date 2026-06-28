from PyObjCTools.TestSupport import TestCase
import BackgroundAssets


class TestBATypes(TestCase):
    def test_enums(self):
        self.assertIsEnumType(BackgroundAssets.BAContentRequest)
        self.assertEqual(BackgroundAssets.BAContentRequestInstall, 1)
        self.assertEqual(BackgroundAssets.BAContentRequestUpdate, 2)
        self.assertEqual(BackgroundAssets.BAContentRequestPeriodic, 3)
        self.assertEqual(BackgroundAssets.BAContentRequestLanguageChange, 4)
