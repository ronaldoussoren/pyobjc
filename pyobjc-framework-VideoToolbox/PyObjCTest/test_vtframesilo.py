from PyObjCTools.TestSupport import *
import VideoToolbox

class TestVTFrameSilo (TestCase):
    @expectedFailure
    @min_os_level('10.10')
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTFrameSiloRef)

    @min_os_level('10.10')
    def test_functions(self):
        VideoToolbox.VTFrameSiloGetTypeID

        self.assertArgIsOut(VideoToolbox.VTFrameSiloCreate, 4)
        self.assertArgIsCFRetained(VideoToolbox.VTFrameSiloCreate, 4)

        VideoToolbox.VTFrameSiloAddSampleBuffer

        self.assertArgIsIn(VideoToolbox.VTFrameSiloSetTimeRangesForNextPass, 2)
        self.assertArgSizeInArg(VideoToolbox.VTFrameSiloSetTimeRangesForNextPass, 2, 1)

        self.assertArgIsOut(VideoToolbox.VTFrameSiloGetProgressOfCurrentPass, 1)

        self.assertArgIsFunction(VideoToolbox.VTFrameSiloCallFunctionForEachSampleBuffer, 3, b'i^v^{opaqueCMSampleBuffer=}', False)

        self.assertArgIsBlock(VideoToolbox.VTFrameSiloCallBlockForEachSampleBuffer, 2, b'i^{opaqueCMSampleBuffer=}')


if __name__ == "__main__":
    main()
