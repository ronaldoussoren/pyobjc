from PyObjCTools.TestSupport import TestCase, min_os_level
import PhotosUI


class TestPHProjectExtensionContext(TestCase):
    @min_os_level("10.14")
    def testMethods(self):
        self.assertArgIsBlock(
            PhotosUI.PHProjectExtensionContext.updatedProjectInfoFromProjectInfo_completion_,
            1,
            b"v@",
        )
