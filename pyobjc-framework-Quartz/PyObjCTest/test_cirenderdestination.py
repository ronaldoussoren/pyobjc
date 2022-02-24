from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCIRenderDestination(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Quartz.CIRenderDestinationAlphaMode)

    @min_os_level("10.13")
    def testMethods(self):
        self.assertArgIsBlock(
            Quartz.CIRenderDestination.initWithWidth_height_pixelFormat_commandBuffer_mtlTextureProvider_,
            4,
            b"@",
        )

        self.assertResultIsBOOL(Quartz.CIRenderDestination.isFlipped)
        self.assertArgIsBOOL(Quartz.CIRenderDestination.setFlipped_, 0)

        self.assertResultIsBOOL(Quartz.CIRenderDestination.isDithered)
        self.assertArgIsBOOL(Quartz.CIRenderDestination.setDithered_, 0)

        self.assertResultIsBOOL(Quartz.CIRenderDestination.isClamped)
        self.assertArgIsBOOL(Quartz.CIRenderDestination.setClamped_, 0)

        self.assertResultIsBOOL(
            Quartz.CIRenderDestination.blendsInDestinationColorSpace
        )
        self.assertArgIsBOOL(
            Quartz.CIRenderDestination.setBlendsInDestinationColorSpace_, 0
        )

        self.assertArgIsOut(Quartz.CIRenderTask.waitUntilCompletedAndReturnError_, 0)

        self.assertArgIsOut(
            Quartz.CIContext.startTaskToRender_fromRect_toDestination_atPoint_error_, 4
        )
        self.assertArgIsOut(Quartz.CIContext.startTaskToRender_toDestination_error_, 2)

        self.assertResultIsBOOL(
            Quartz.CIContext.prepareRender_fromRect_toDestination_atPoint_error_
        )
        self.assertArgIsOut(
            Quartz.CIContext.prepareRender_fromRect_toDestination_atPoint_error_, 4
        )

        self.assertArgIsOut(Quartz.CIContext.startTaskToClear_error_, 1)

    def testConstants(self):
        self.assertEqual(Quartz.CIRenderDestinationAlphaNone, 0)
        self.assertEqual(Quartz.CIRenderDestinationAlphaPremultiplied, 1)
        self.assertEqual(Quartz.CIRenderDestinationAlphaUnpremultiplied, 2)
