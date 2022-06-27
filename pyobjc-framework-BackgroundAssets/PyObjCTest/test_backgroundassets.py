from PyObjCTools.TestSupport import TestCase
import BackgroundAssets


class TestBackgroundAssets(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(BackgroundAssets)
