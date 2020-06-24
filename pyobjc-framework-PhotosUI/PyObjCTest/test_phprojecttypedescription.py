from PyObjCTools.TestSupport import TestCase, min_os_level
import PhotosUI


class TestPHProjectTypeDescription(TestCase):
    @min_os_level("10.14")
    def testMethods(self):
        self.assertResultIsBOOL(PhotosUI.PHProjectTypeDescription.canProvideSubtypes)
