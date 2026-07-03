from PyObjCTools.TestSupport import TestCase

import AVFoundation


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            AVFoundation,
            exclude_attrs={
                "ACDLazyArray",
                "BGFastPassSystemTaskRequest",
                "BGNonRepeatingSystemTaskRequest",
                "BGRepeatingSystemTaskRequest",
                "BGSystemTaskRequest",
                "CKException",
                "CKSQLite",
                "CKSQLiteDatabase",
                "CKSQLiteStatement",
                "CKSignificantIssue",
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
            },
        )
