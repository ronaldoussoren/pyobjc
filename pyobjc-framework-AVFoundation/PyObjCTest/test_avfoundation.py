from PyObjCTools.TestSupport import TestCase

import AVFoundation


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            AVFoundation,
            exclude_attrs={
                "ACDKeychain",
                "ACDLazyArray",
                "BGFastPassSystemTaskRequest",
                "BGNonRepeatingSystemTaskRequest",
                "BGRepeatingSystemTaskRequest",
                "BGSystemTaskRequest",
                "BiometricKit",
                "BiometricKitXPCClient",
                "BKAccessory",
                "BKDevice",
                "BKDeviceManager",
                "BKDevicePearl",
                "BKDeviceTouchID",
                "CKException",
                "CKSignificantIssue",
                "CKSQLite",
                "CKSQLiteDatabase",
                "CKSQLiteStatement",
                "DSSandboxingURLWrapper",
                "IMLogging",
                "LACIOKitHelper",
                "MLModelErrorUtils",
                "NSATSTypesetter",
                "NSConcreteNotifyingMutableAttributedString",
                "NSConcreteTextStorage",
                "NSDocFormatWriter",
                "NSFont",
                "NSLayoutManager",
                "NSStringDrawingTextStorage",
                "NSTextLayoutFragment",
                "NSTextStorage",
                "NSTypesetter",
                "SAException",
                "UAFAssetInfoCache",
                "UAFAssetSetExperiment",
                "VisionCoreValidationUtilities",
            },
        )
