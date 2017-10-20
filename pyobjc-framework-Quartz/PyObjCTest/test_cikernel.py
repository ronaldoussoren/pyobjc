
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *
from Quartz import *

class TestCIKernel (TestCase):
    def testMethods(self):
        self.assertArgIsSEL(CIKernel.setROISelector_, 0, CGRect.__typestr__ + b'@:i' + CGRect.__typestr__ + b'@')


    @min_os_level('10.11')
    def testMethods(self):
        CIKernelROICallback = CGRect.__typestr__ + objc._C_INT + CGRect.__typestr__
        self.assertArgIsBlock(CIKernel.applyWithExtent_roiCallback_arguments_, 1, CIKernelROICallback)
        self.assertArgIsBlock(CIWarpKernel.applyWithExtent_roiCallback_inputImage_arguments_, 1, CIKernelROICallback)

    @min_os_level('10.13')
    def testMethods(self):
        self.assertArgIsOut(CIKernel.kernelWithFunctionName_fromMetalLibraryData_error_, 2)
        self.assertArgIsOut(CIKernel.kernelWithFunctionName_fromMetalLibraryData_outputPixelFormat_error_, 3)

if __name__ == "__main__":
    main()
