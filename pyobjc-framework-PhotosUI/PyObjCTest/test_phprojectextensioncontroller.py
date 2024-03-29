from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import PhotosUI


class TestPHProjectExtensionControllerHelper(PhotosUI.NSObject):
    def beginProjectWithExtensionContext_projectInfo_completion_(self, ec, pi, c):
        pass

    def resumeProjectWithExtensionContext_completion_(self, ec, c):
        pass

    def finishProjectWithCompletionHandler_(self, c):
        pass


class TestPHProjectExtensionController(TestCase):
    @min_sdk_level("10.13")
    def testProtocols(self):
        self.assertProtocolExists("PHProjectExtensionController")

    @min_os_level("10.11")
    def testMethods(self):
        self.assertArgIsBlock(
            TestPHProjectExtensionControllerHelper.beginProjectWithExtensionContext_projectInfo_completion_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPHProjectExtensionControllerHelper.resumeProjectWithExtensionContext_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPHProjectExtensionControllerHelper.finishProjectWithCompletionHandler_,
            0,
            b"v@",
        )
