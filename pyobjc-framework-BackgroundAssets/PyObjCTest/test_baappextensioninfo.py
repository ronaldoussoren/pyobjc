from PyObjCTools.TestSupport import TestCase
import BackgroundAssets


class TestBAAppExtensionInfo(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            BackgroundAssets.BAAppExtensionInfo.downloadSizeRestricted
        )
