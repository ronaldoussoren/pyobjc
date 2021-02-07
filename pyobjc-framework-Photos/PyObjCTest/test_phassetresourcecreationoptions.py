from PyObjCTools.TestSupport import TestCase, min_os_level
import Photos


class TestPHAssetResourceCreationOptions(TestCase):
    @min_os_level("10.15")
    def testMethods(self):
        self.assertResultIsBOOL(Photos.PHAssetResourceCreationOptions.shouldMoveFile)
        self.assertArgIsBOOL(
            Photos.PHAssetResourceCreationOptions.setShouldMoveFile_, 0
        )

        self.assertResultIsBOOL(
            Photos.PHAssetCreationRequest.supportsAssetResourceTypes_
        )
