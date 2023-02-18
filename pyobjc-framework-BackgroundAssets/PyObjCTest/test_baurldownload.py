from PyObjCTools.TestSupport import TestCase, min_os_level
import BackgroundAssets


class TestBAURLDownload(TestCase):
    @min_os_level("13.3")
    def test_methods13_3(self):
        self.assertArgIsBOOL(
            BackgroundAssets.BAURLDownload.initWithIdentifier_request_essential_fileSize_applicationGroupIdentifier_priority_,
            2,
        )
