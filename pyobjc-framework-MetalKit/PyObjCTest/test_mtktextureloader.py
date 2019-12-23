from PyObjCTools.TestSupport import *


import sys

if sys.maxsize > 2 ** 32:
    import MetalKit

    MTKTextureLoaderCallback = b"v@@"
    MTKTextureLoaderArrayCallback = b"v@@"

    class TestMTKTextureLoading(TestCase):
        @min_os_level("10.11")
        def test_constants10_11(self):
            self.assertIsInstance(MetalKit.MTKTextureLoaderErrorDomain, unicode)
            self.assertIsInstance(MetalKit.MTKTextureLoaderErrorKey, unicode)

            self.assertIsInstance(
                MetalKit.MTKTextureLoaderOptionAllocateMipmaps, unicode
            )
            self.assertIsInstance(MetalKit.MTKTextureLoaderOptionSRGB, unicode)
            self.assertIsInstance(MetalKit.MTKTextureLoaderOptionTextureUsage, unicode)
            self.assertIsInstance(
                MetalKit.MTKTextureLoaderOptionTextureCPUCacheMode, unicode
            )

        @min_os_level("10.12")
        def test_constants10_12(self):
            self.assertIsInstance(
                MetalKit.MTKTextureLoaderOptionGenerateMipmaps, unicode
            )
            self.assertIsInstance(
                MetalKit.MTKTextureLoaderOptionTextureStorageMode, unicode
            )
            self.assertIsInstance(MetalKit.MTKTextureLoaderOptionCubeLayout, unicode)
            self.assertIsInstance(MetalKit.MTKTextureLoaderCubeLayoutVertical, unicode)
            self.assertIsInstance(MetalKit.MTKTextureLoaderOptionOrigin, unicode)
            self.assertIsInstance(MetalKit.MTKTextureLoaderOriginTopLeft, unicode)
            self.assertIsInstance(MetalKit.MTKTextureLoaderOriginBottomLeft, unicode)
            self.assertIsInstance(
                MetalKit.MTKTextureLoaderOriginFlippedVertically, unicode
            )

        @min_os_level("10.11")
        def test_methods10_11(self):
            self.assertArgIsBlock(
                MetalKit.MTKTextureLoader.newTextureWithContentsOfURL_options_completionHandler_,
                2,
                MTKTextureLoaderCallback,
            )
            self.assertArgIsBlock(
                MetalKit.MTKTextureLoader.newTextureWithData_options_completionHandler_,
                2,
                MTKTextureLoaderCallback,
            )
            self.assertArgIsBlock(
                MetalKit.MTKTextureLoader.newTextureWithCGImage_options_completionHandler_,
                2,
                MTKTextureLoaderCallback,
            )

            self.assertArgIsOut(
                MetalKit.MTKTextureLoader.newTextureWithContentsOfURL_options_error_, 2
            )
            self.assertArgIsOut(
                MetalKit.MTKTextureLoader.newTextureWithData_options_error_, 2
            )
            self.assertArgIsOut(
                MetalKit.MTKTextureLoader.newTextureWithCGImage_options_error_, 2
            )

        @min_os_level("10.12")
        def test_methods10_12(self):
            self.assertArgIsBlock(
                MetalKit.MTKTextureLoader.newTextureWithName_scaleFactor_bundle_options_completionHandler_,
                4,
                MTKTextureLoaderCallback,
            )
            self.assertArgIsBlock(
                MetalKit.MTKTextureLoader.newTextureWithName_scaleFactor_displayGamut_bundle_options_completionHandler_,
                5,
                MTKTextureLoaderCallback,
            )
            self.assertArgIsBlock(
                MetalKit.MTKTextureLoader.newTexturesWithContentsOfURLs_options_completionHandler_,
                2,
                MTKTextureLoaderArrayCallback,
            )
            self.assertArgIsBlock(
                MetalKit.MTKTextureLoader.newTexturesWithNames_scaleFactor_bundle_options_completionHandler_,
                4,
                MTKTextureLoaderArrayCallback,
            )
            self.assertArgIsBlock(
                MetalKit.MTKTextureLoader.newTexturesWithNames_scaleFactor_displayGamut_bundle_options_completionHandler_,
                5,
                MTKTextureLoaderArrayCallback,
            )
            self.assertArgIsBlock(
                MetalKit.MTKTextureLoader.newTextureWithMDLTexture_options_completionHandler_,
                2,
                MTKTextureLoaderCallback,
            )

            self.assertArgIsOut(
                MetalKit.MTKTextureLoader.newTexturesWithContentsOfURLs_options_error_,
                2,
            )
            self.assertArgIsOut(
                MetalKit.MTKTextureLoader.newTextureWithMDLTexture_options_error_, 2
            )
            self.assertArgIsOut(
                MetalKit.MTKTextureLoader.newTextureWithName_scaleFactor_bundle_options_error_,
                4,
            )
            self.assertArgIsOut(
                MetalKit.MTKTextureLoader.newTextureWithName_scaleFactor_displayGamut_bundle_options_error_,
                5,
            )
