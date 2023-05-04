from PyObjCTools.TestSupport import TestCase

import Cocoa


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            Cocoa,
            exclude_cocoa=False,
            exclude_attrs={
                (
                    "NSFileSubarbitrationClaim",
                    "forwardReacquisitionForWritingClaim_withID_toPresenterForID_usingReplySender_",
                ),
                (
                    "DSPDelegateDouble",
                    "adaptToConfigurationChange_",
                ),
                (
                    "IKGLSharedContextRegistry",
                    "declareContext_isSharedWith_",
                ),
                (
                    "IKGLSharedContextRegistry",
                    "isContext_sharedWith_",
                ),
                ("CMIOGraphService", "setMonitoring_forNodes_"),
                ("CMIOGraphService", "initiateConnectionWithClient_"),
                ("CMIOGraphService", "setMonitoringForAllNodes_"),
                ("IOBluetoothDevice", "updateName_lastUpdate_"),
                ("IOBluetoothDevice", "updateServices_lastUpdate_"),
                ("IOBluetoothDevice", "updateInquiryInfo_lastUpdate_"),
                ("IOBluetoothDevice", "updateServicesArchive_lastUpdate_"),
                ("SDPQueryCallbackDispatcher", "sdpQueryComplete_status_"),
                "UINSServiceViewController",
                "IOBluetoothDeviceInquiry",
            },
        )
