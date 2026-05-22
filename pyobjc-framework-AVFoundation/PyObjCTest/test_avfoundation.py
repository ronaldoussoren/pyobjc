from PyObjCTools.TestSupport import TestCase

import AVFoundation


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            AVFoundation,
            exclude_attrs={
                "CKException",
                "CKSQLite",
                "CKSQLiteDatabase",
                "CKSignificantIssue",
                "IMLogging",
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
