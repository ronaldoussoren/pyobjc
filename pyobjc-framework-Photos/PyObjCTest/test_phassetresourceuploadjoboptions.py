from PyObjCTools.TestSupport import TestCase, min_os_level
import Photos


class TestPHAssetResourceUploadJobOptions(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Photos.PHAssetResourceUploadJobOptions.preventsExpensiveNetworkAccess
        )
        self.assertArgIsBOOL(
            Photos.PHAssetResourceUploadJobOptions.setPreventsExpensiveNetworkAccess_, 0
        )
