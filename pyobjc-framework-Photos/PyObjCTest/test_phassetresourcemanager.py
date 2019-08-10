from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    PHAssetResourceProgressHandler = b"vd"

    class TestPHAssetResourceManager(TestCase):
        @min_os_level("10.15")
        def testMethods(self):
            self.assertResultIsBOOL(
                Photos.PHContentEditingInputRequestOptions.isNetworkAccessAllowed
            )
            self.assertArgIsBOOL(
                Photos.PHContentEditingInputRequestOptions.setNetworkAccessAllowed_, 0
            )

            self.assertArgIsBlock(
                Photos.PHAssetResourceManager.requestDataForAssetResource_options_dataReceivedHandler_completionHandler_,
                2,
                b"v@",
            )
            self.assertArgIsBlock(
                Photos.PHAssetResourceManager.requestDataForAssetResource_options_dataReceivedHandler_completionHandler_,
                3,
                b"v@",
            )

            self.assertArgIsBlock(
                Photos.PHAssetResourceManager.writeDataForAssetResource_toFile_options_completionHandler_,
                3,
                b"v@",
            )


if __name__ == "__main__":
    main()
