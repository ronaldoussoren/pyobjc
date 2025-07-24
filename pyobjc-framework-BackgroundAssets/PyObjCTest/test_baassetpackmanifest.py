from PyObjCTools.TestSupport import TestCase, min_os_level
import BackgroundAssets


class TestBAAssetPackManifest(TestCase):
    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertArgIsOut(
            BackgroundAssets.BAAssetPackManifest.initWithContentsOfURL_applicationGroupIdentifier_error_,
            2,
        )
        self.assertArgIsOut(
            BackgroundAssets.BAAssetPackManifest.initFromData_applicationGroupIdentifier_error_,
            2,
        )
