from PyObjCTools.TestSupport import TestCase

import MediaExtension


class TestMEExtensionPlugin(TestCase):
    def test_constants(self):
        self.assertEqual(
            MediaExtension.kMEFormatReaderExtensionPointName,
            "com.apple.mediaextension.formatreader",
        )
        self.assertEqual(
            MediaExtension.kMEVideoDecoderExtensionPointName,
            "com.apple.mediaextension.videodecoder",
        )
        self.assertEqual(
            MediaExtension.kMEFormatReaderClassImplementationIDKey,
            "ClassImplementationID",
        )
        self.assertEqual(MediaExtension.kMEFormatReaderUTTypeArrayKey, "MTUTTypeArray")
        self.assertEqual(
            MediaExtension.kMEFormatReaderFileNameExtensionArrayKey,
            "MTFileNameExtensionArray",
        )
        self.assertEqual(MediaExtension.kMEFormatReaderObjectNameKey, "ObjectName")
        self.assertEqual(
            MediaExtension.kMEVideoDecoderClassImplementationIDKey,
            "ClassImplementationID",
        )
        self.assertEqual(MediaExtension.kMEVideoDecoderCodecTypeKey, "CodecType")
        self.assertEqual(MediaExtension.kMEVideoDecoderObjectNameKey, "ObjectName")
