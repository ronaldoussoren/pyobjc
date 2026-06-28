import OSAKit
from PyObjCTools.TestSupport import TestCase


class TestOSALanguage(TestCase):
    def test_enums(self):
        self.assertIsEnumType(OSAKit.OSALanguageFeatures)
        self.assertEqual(OSAKit.OSASupportsCompiling, 0x0002)
        self.assertEqual(OSAKit.OSASupportsGetSource, 0x0004)
        self.assertEqual(OSAKit.OSASupportsAECoercion, 0x0008)
        self.assertEqual(OSAKit.OSASupportsAESending, 0x0010)
        self.assertEqual(OSAKit.OSASupportsRecording, 0x0020)
        self.assertEqual(OSAKit.OSASupportsConvenience, 0x0040)
        self.assertEqual(OSAKit.OSASupportsDialects, 0x0080)
        self.assertEqual(OSAKit.OSASupportsEventHandling, 0x0100)

    def test_methods(self):
        self.assertResultIsBOOL(OSAKit.OSALanguage.isThreadSafe)
