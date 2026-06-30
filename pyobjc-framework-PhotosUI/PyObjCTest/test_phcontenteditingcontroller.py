from PyObjCTools.TestSupport import TestCase, min_sdk_level
import PhotosUI


class TestPHContentEditingControllerHelper(PhotosUI.NSObject):
    def canHandleAdjustmentData_(self, d):
        return True

    def finishContentEditingWithCompletionHandler_(self, handler):
        pass

    def shouldShowCancelConfirmation(self):
        return True


class TestPHContentEditingController(TestCase):
    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("PHContentEditingController", PhotosUI)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestPHContentEditingControllerHelper.canHandleAdjustmentData_
        )
        self.assertArgIsBlock(
            TestPHContentEditingControllerHelper.finishContentEditingWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertResultIsBOOL(
            TestPHContentEditingControllerHelper.shouldShowCancelConfirmation
        )
