from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *
from Quartz import CGRect

class TestCIImageProcessorHelper (NSObject):
    def region(self): return 1
    def bytesPerRow(self): return 1
    def format(self): return 1
    def baseAddress(self): return 1

class TestCIImageProcessor (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertResultIsBOOL(CIImageProcessorKernel.processWithInputs_arguments_output_error_)
        self.assertArgIsOut(CIImageProcessorKernel.processWithInputs_arguments_output_error_, 3)

        self.assertResultHasType(CIImageProcessorKernel.roiForInput_arguments_outputRect_, CGRect.__typestr__)
        self.assertArgHasType(CIImageProcessorKernel.roiForInput_arguments_outputRect_, 2, CGRect.__typestr__)

        self.assertArgIsOut(CIImageProcessorKernel.applyWithExtent_inputs_arguments_error_, 3)


    @min_sdk_level('10.12')
    def testProtocols(self):
        objc.protocolNamed('CIImageProcessorInput')

        self.assertResultHasType(TestCIImageProcessorHelper.region, CGRect.__typestr__)
        self.assertResultHasType(TestCIImageProcessorHelper.bytesPerRow, objc._C_ULNG)
        self.assertResultHasType(TestCIImageProcessorHelper.format, objc._C_NSInteger)
        self.assertResultHasType(TestCIImageProcessorHelper.baseAddress, b'^v')

        objc.protocolNamed('CIImageProcessorOutput')

if __name__ == "__main__":
    main()
