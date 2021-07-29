from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCIKernel(TestCase):
    def testMethods(self):
        self.assertArgIsSEL(
            Quartz.CIKernel.setROISelector_,
            0,
            Quartz.CGRect.__typestr__ + b"@:i" + Quartz.CGRect.__typestr__ + b"@",
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        CIKernelROICallback = (
            Quartz.CGRect.__typestr__ + objc._C_INT + Quartz.CGRect.__typestr__
        )
        self.assertArgIsBlock(
            Quartz.CIKernel.applyWithExtent_roiCallback_arguments_,
            1,
            CIKernelROICallback,
        )
        self.assertArgIsBlock(
            Quartz.CIWarpKernel.applyWithExtent_roiCallback_inputImage_arguments_,
            1,
            CIKernelROICallback,
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(
            Quartz.CIKernel.kernelWithFunctionName_fromMetalLibraryData_error_, 2
        )
        self.assertArgIsOut(
            Quartz.CIKernel.kernelWithFunctionName_fromMetalLibraryData_outputPixelFormat_error_,
            3,
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertArgIsOut(Quartz.CIKernel.kernelsWithMetalString_error_, 1)
