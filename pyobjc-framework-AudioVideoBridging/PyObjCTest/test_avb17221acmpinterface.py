from PyObjCTools.TestSupport import TestCase, min_os_level
import AudioVideoBridging

AVB17221ACMPInterfaceCompletion = b"v@@"


class TestAVB17221ACMPInterfaceHelper(AudioVideoBridging.NSObject):
    def ACMPDidReceiveCommand_onInterface_(self, a, b):
        return 1

    def ACMPDidReceiveResponse_onInterface_(self, a, b):
        return 1


class TestAVB17221ACMPInterface(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("AVB17221ACMPClient")

    def test_methods(self):
        self.assertResultIsBOOL(
            TestAVB17221ACMPInterfaceHelper.ACMPDidReceiveCommand_onInterface_
        )
        self.assertResultIsBOOL(
            TestAVB17221ACMPInterfaceHelper.ACMPDidReceiveResponse_onInterface_
        )

    @min_os_level("10.8")
    def test_methods10_8(self):
        self.assertResultIsBOOL(
            AudioVideoBridging.AVB17221ACMPInterface.sendACMPResponseMessage_error_
        )
        self.assertArgIsOut(
            AudioVideoBridging.AVB17221ACMPInterface.sendACMPResponseMessage_error_, 1
        )

        self.assertResultIsBOOL(
            AudioVideoBridging.AVB17221ACMPInterface.sendACMPCommandMessage_completionHandler_
        )
        self.assertArgIsBlock(
            AudioVideoBridging.AVB17221ACMPInterface.sendACMPCommandMessage_completionHandler_,
            1,
            AVB17221ACMPInterfaceCompletion,
        )

    @min_os_level("10.9")
    def test_methods10_9(self):
        self.assertResultIsBOOL(
            AudioVideoBridging.AVB17221ACMPInterface.setHandler_forEntityID_
        )
