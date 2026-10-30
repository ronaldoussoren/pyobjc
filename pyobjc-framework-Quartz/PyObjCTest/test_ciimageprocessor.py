from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import Quartz
import objc


class TestCIImageProcessorHelper(Quartz.NSObject):
    def region(self):
        return 1

    def bytesPerRow(self):
        return 1

    def format(self):  # noqa: A003
        return 1

    def baseAddress(self):
        return 1

    def temporarySurfaceWithIdentifier_format_width_height_(self, a, b, c, d):
        return 1

    def temporaryPixelBufferWithIdentifier_format_width_height_attributes_(
        self, a, b, c, d, e
    ):
        return 1


class TestCIImageProcessor(TestCase):
    @min_os_level("10.12")
    def test_methods(self):
        self.assertResultIsBOOL(
            Quartz.CIImageProcessorKernel.processWithInputs_arguments_output_error_
        )
        self.assertArgIsOut(
            Quartz.CIImageProcessorKernel.processWithInputs_arguments_output_error_, 3
        )

        self.assertResultHasType(
            Quartz.CIImageProcessorKernel.roiForInput_arguments_outputRect_,
            Quartz.CGRect.__typestr__,
        )
        self.assertArgHasType(
            Quartz.CIImageProcessorKernel.roiForInput_arguments_outputRect_,
            2,
            Quartz.CGRect.__typestr__,
        )

        self.assertArgIsOut(
            Quartz.CIImageProcessorKernel.applyWithExtent_inputs_arguments_error_, 3
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(
            Quartz.CIImageProcessorKernel.processWithInputs_arguments_outputs_error_
        )
        self.assertArgIsOut(
            Quartz.CIImageProcessorKernel.processWithInputs_arguments_outputs_error_, 3
        )

        self.assertArgIsOut(
            Quartz.CIImageProcessorKernel.applyWithExtents_inputs_arguments_error_, 3
        )

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertArgIsOut(
            Quartz.CIImageProcessorKernel.applyWithTiledExtent_inputs_arguments_error_,
            3,
        )

    @min_sdk_level("10.12")
    def test_protocols(self):
        self.assertProtocolExists(
            "CIImageProcessorInput", Quartz, "CIImageProcessorInputProtocol"
        )
        self.assertProtocolExists(
            "CIImageProcessorOutput", Quartz, "CIImageProcessorOutputProtocol"
        )

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestCIImageProcessorHelper.region, Quartz.CGRect.__typestr__
        )
        self.assertResultHasType(TestCIImageProcessorHelper.bytesPerRow, objc._C_ULNG)
        self.assertResultHasType(TestCIImageProcessorHelper.format, objc._C_NSInteger)
        self.assertResultHasType(TestCIImageProcessorHelper.baseAddress, b"^v")

        self.assertArgHasType(
            TestCIImageProcessorHelper.temporarySurfaceWithIdentifier_format_width_height_,
            1,
            objc._C_INT,
        )
        self.assertArgHasType(
            TestCIImageProcessorHelper.temporarySurfaceWithIdentifier_format_width_height_,
            2,
            objc._C_ULNG_LNG,
        )
        self.assertArgHasType(
            TestCIImageProcessorHelper.temporarySurfaceWithIdentifier_format_width_height_,
            3,
            objc._C_ULNG_LNG,
        )

        self.assertArgHasType(
            TestCIImageProcessorHelper.temporaryPixelBufferWithIdentifier_format_width_height_attributes_,
            1,
            objc._C_INT,
        )
        self.assertArgHasType(
            TestCIImageProcessorHelper.temporaryPixelBufferWithIdentifier_format_width_height_attributes_,
            2,
            objc._C_ULNG_LNG,
        )
        self.assertArgHasType(
            TestCIImageProcessorHelper.temporaryPixelBufferWithIdentifier_format_width_height_attributes_,
            3,
            objc._C_ULNG_LNG,
        )
