from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalKit

MTKTextureLoaderCallback = b"v@@"
MTKTextureLoaderArrayCallback = b"v@@"


class TestMTKTextureLoading(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(MetalKit.MTKTextureLoaderCubeLayout, str)
        self.assertIsTypedEnum(MetalKit.MTKTextureLoaderError, str)
        self.assertIsTypedEnum(MetalKit.MTKTextureLoaderOption, str)
        self.assertIsTypedEnum(MetalKit.MTKTextureLoaderOrigin, str)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(MetalKit.MTKTextureLoaderErrorDomain, str)
        self.assertIsInstance(MetalKit.MTKTextureLoaderErrorKey, str)

        self.assertIsInstance(MetalKit.MTKTextureLoaderOptionAllocateMipmaps, str)
        self.assertIsInstance(MetalKit.MTKTextureLoaderOptionSRGB, str)
        self.assertIsInstance(MetalKit.MTKTextureLoaderOptionTextureUsage, str)
        self.assertIsInstance(MetalKit.MTKTextureLoaderOptionTextureCPUCacheMode, str)

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(MetalKit.MTKTextureLoaderOptionGenerateMipmaps, str)
        self.assertIsInstance(MetalKit.MTKTextureLoaderOptionTextureStorageMode, str)
        self.assertIsInstance(MetalKit.MTKTextureLoaderOptionCubeLayout, str)
        self.assertIsInstance(MetalKit.MTKTextureLoaderCubeLayoutVertical, str)
        self.assertIsInstance(MetalKit.MTKTextureLoaderOptionOrigin, str)
        self.assertIsInstance(MetalKit.MTKTextureLoaderOriginTopLeft, str)
        self.assertIsInstance(MetalKit.MTKTextureLoaderOriginBottomLeft, str)
        self.assertIsInstance(MetalKit.MTKTextureLoaderOriginFlippedVertically, str)

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertArgIsBlock(
            MetalKit.MTKTextureLoader.newTextureWithContentsOfURL_options_completionHandler_,  # noqa: B950
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
            MetalKit.MTKTextureLoader.newTextureWithName_scaleFactor_bundle_options_completionHandler_,  # noqa: B950
            4,
            MTKTextureLoaderCallback,
        )
        self.assertArgIsBlock(
            MetalKit.MTKTextureLoader.newTextureWithName_scaleFactor_displayGamut_bundle_options_completionHandler_,  # noqa: B950
            5,
            MTKTextureLoaderCallback,
        )
        self.assertArgIsBlock(
            MetalKit.MTKTextureLoader.newTexturesWithContentsOfURLs_options_completionHandler_,  # noqa: B950
            2,
            MTKTextureLoaderArrayCallback,
        )
        self.assertArgIsBlock(
            MetalKit.MTKTextureLoader.newTexturesWithNames_scaleFactor_bundle_options_completionHandler_,  # noqa: B950
            4,
            MTKTextureLoaderArrayCallback,
        )
        self.assertArgIsBlock(
            MetalKit.MTKTextureLoader.newTexturesWithNames_scaleFactor_displayGamut_bundle_options_completionHandler_,  # noqa: B950
            5,
            MTKTextureLoaderArrayCallback,
        )
        self.assertArgIsBlock(
            MetalKit.MTKTextureLoader.newTextureWithMDLTexture_options_completionHandler_,
            2,
            MTKTextureLoaderCallback,
        )

        self.assertArgIsOut(
            MetalKit.MTKTextureLoader.newTexturesWithContentsOfURLs_options_error_, 2
        )
        self.assertArgIsOut(
            MetalKit.MTKTextureLoader.newTextureWithMDLTexture_options_error_, 2
        )
        self.assertArgIsOut(
            MetalKit.MTKTextureLoader.newTextureWithName_scaleFactor_bundle_options_error_,
            4,
        )
        self.assertArgIsOut(
            MetalKit.MTKTextureLoader.newTextureWithName_scaleFactor_displayGamut_bundle_options_error_,  # noqa: B950
            5,
        )
