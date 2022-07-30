from PyObjCTools.TestSupport import TestCase
import BackgroundAssets


class TestBAApplicationExtensionInfo(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            BackgroundAssets.BAApplicationExtensionInfo.downloadSizeRestricted
        )
