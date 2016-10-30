from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHLivePhotoEditingContextHelper (Photos.NSObject):
        def time(self): return 1
        def type(self): return 1
        def renderScale(self): return 1


    class TestPHLivePhotoEditingContext (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            PHLivePhotoFrameProcessingBlock = b'@@o^@'

            self.assertResultIsBlock(Photos.PHLivePhotoEditingContext.frameProcessor, PHLivePhotoFrameProcessingBlock)
            self.assertArgIsBlock(Photos.PHLivePhotoEditingContext.setFrameProcessor_, 0, PHLivePhotoFrameProcessingBlock)

            self.assertArgIsBlock(Photos.PHLivePhotoEditingContext.prepareLivePhotoForPlaybackWithTargetSize_options_completionHandler_, 2, b'vZ@')
            self.assertArgIsBlock(Photos.PHLivePhotoEditingContext.saveLivePhotoToOutput_options_completionHandler_, 2, b'vZ@')

            self.assertResultHasType(TestPHLivePhotoEditingContextHelper.time, b'{_CMTime=qiIq}') # Photos.CMTime.__typestr__
            self.assertResultHasType(TestPHLivePhotoEditingContextHelper.type, objc._C_NSInteger)
            self.assertResultHasType(TestPHLivePhotoEditingContextHelper.renderScale, objc._C_CGFloat)


        @min_os_level('10.12')
        def testContants(self):
            self.assertEqual(Photos.PHLivePhotoFrameTypePhoto, 0)
            self.assertEqual(Photos.PHLivePhotoFrameTypeVideo, 1)

            self.assertIsInstance(Photos.PHLivePhotoEditingErrorDomain, unicode)
            self.assertIsInstance(Photos.PHLivePhotoShouldRenderAtPlaybackTime, unicode)

            self.assertEqual(Photos.PHLivePhotoEditingErrorCodeUnknown, 0)
            self.assertEqual(Photos.PHLivePhotoEditingErrorCodeAborted, 1)


        @min_sdk_level('10.12')
        def testProtocols(self):
            objc.protocolNamed('PHLivePhotoFrame')



if __name__ == "__main__":
    main()
