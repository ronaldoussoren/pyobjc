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
                "UINSServiceViewController",
                "IOBluetoothDeviceInquiry",
            },
        )
