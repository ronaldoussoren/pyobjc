from PyObjCTools.TestSupport import *
import VideoToolbox

class TestVTMultiPassStorage (TestCase):
    @expectedFailure
    @min_os_level('10.10')
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTMultiPassStorageRef)

    @min_os_level('10.10')
    def test_constants(self):
        self.assertIsInstance(VideoToolbox.kVTMultiPassStorageCreationOption_DoNotDelete, unicode)

    @min_os_level('10.10')
    def test_functions(self):
        VideoToolbox.VTMultiPassStorageGetTypeID

        self.assertArgIsOut(VideoToolbox.VTMultiPassStorageCreate, 4)
        self.assertArgIsCFRetained(VideoToolbox.VTMultiPassStorageCreate, 4)

        VideoToolbox.VTMultiPassStorageClose




if __name__ == "__main__":
    main()
