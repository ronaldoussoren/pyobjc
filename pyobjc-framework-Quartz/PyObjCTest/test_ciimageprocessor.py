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


class TestCIImageProcessor(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
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

    @min_sdk_level("10.12")
    def testProtocols(self):
        objc.protocolNamed("CIImageProcessorInput")

        self.assertResultHasType(
            TestCIImageProcessorHelper.region, Quartz.CGRect.__typestr__
        )
        self.assertResultHasType(TestCIImageProcessorHelper.bytesPerRow, objc._C_ULNG)
        self.assertResultHasType(TestCIImageProcessorHelper.format, objc._C_NSInteger)
        self.assertResultHasType(TestCIImageProcessorHelper.baseAddress, b"^v")

        objc.protocolNamed("CIImageProcessorOutput")
