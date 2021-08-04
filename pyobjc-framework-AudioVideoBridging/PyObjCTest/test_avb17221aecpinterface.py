from PyObjCTools.TestSupport import TestCase, min_os_level
import AudioVideoBridging
import objc

AVB17221AECPInterfaceCompletion = b"v@@"


class TestAVB17221AECPInterfaceHelper(AudioVideoBridging.NSObject):
    def AECPDidReceiveCommand_onInterface_(self, a, b):
        return 1

    def AECPDidReceiveResponse_onInterface_(self, a, b):
        return 1


class TestAVB17221AECPInterface(TestCase):
    def test_protocols(self):
        objc.protocolNamed("AVB17221AECPClient")

    def test_methods(self):
        self.assertResultIsBOOL(
            TestAVB17221AECPInterfaceHelper.AECPDidReceiveCommand_onInterface_
        )
        self.assertResultIsBOOL(
            TestAVB17221AECPInterfaceHelper.AECPDidReceiveResponse_onInterface_
        )

    @min_os_level("10.8")
    def test_methods10_8(self):
        self.assertResultIsBOOL(
            AudioVideoBridging.AVB17221AECPInterface.sendCommand_toMACAddress_completionHandler_
        )
        self.assertArgIsBlock(
            AudioVideoBridging.AVB17221AECPInterface.sendCommand_toMACAddress_completionHandler_,
            2,
            AVB17221AECPInterfaceCompletion,
        )

        self.assertResultIsBOOL(
            AudioVideoBridging.AVB17221AECPInterface.sendResponse_toMACAddress_error_
        )
        self.assertArgIsOut(
            AudioVideoBridging.AVB17221AECPInterface.sendResponse_toMACAddress_error_, 2
        )

        self.assertResultIsBOOL(AudioVideoBridging.AVB17221AECPAEMMessage.isUnsolicited)
        self.assertArgIsBOOL(
            AudioVideoBridging.AVB17221AECPAEMMessage.setUnsolicited_, 0
        )

        self.assertResultIsBOOL(
            AudioVideoBridging.AVB17221AECPAEMMessage.isControllerRequest
        )
        self.assertArgIsBOOL(
            AudioVideoBridging.AVB17221AECPAEMMessage.setControllerRequest_, 0
        )
