from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIRenderDestination (TestCase):
    @min_os_level('10.13')
    def testMethods(self):
        self.assertArgIsBlock(CIRenderDestination.initWithWidth_height_pixelFormat_commandBuffer_mtlTextureProvider_, 4, b'@')

        self.assertResultIsBOOL(CIRenderDestination.isFlipped)
        self.assertArgIsBOOL(CIRenderDestination.setFlipped_, 0)

        self.assertResultIsBOOL(CIRenderDestination.isDithered)
        self.assertArgIsBOOL(CIRenderDestination.setDithered_, 0)

        self.assertResultIsBOOL(CIRenderDestination.isClamped)
        self.assertArgIsBOOL(CIRenderDestination.setClamped_, 0)

        self.assertResultIsBOOL(CIRenderDestination.blendsInDestinationColorSpace)
        self.assertArgIsBOOL(CIRenderDestination.setBlendsInDestinationColorSpace_, 0)

        self.assertArgIsOut(CIRenderTask.waitUntilCompletedAndReturnError_, 0)

        self.assertArgIsOut(CIContext.startTaskToRender_fromRect_toDestination_atPoint_error_, 4)
        self.assertArgIsOut(CIContext.startTaskToRender_toDestination_error_, 2)

        self.assertResultIsBOOL(CIContext.prepareRender_fromRect_toDestination_atPoint_error_)
        self.assertArgIsOut(CIContext.prepareRender_fromRect_toDestination_atPoint_error_, 4)

        self.assertArgIsOut(CIContext.startTaskToClear_error_, 1)

    def testConstants(self):
        self.assertEqual(CIRenderDestinationAlphaNone, 0)
        self.assertEqual(CIRenderDestinationAlphaPremultiplied, 1)
        self.assertEqual(CIRenderDestinationAlphaUnpremultiplied, 2)

if __name__ == "__main__":
    main()
