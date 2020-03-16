import JavaScriptCore
from PyObjCTools.TestSupport import TestCase


class TestWebKitAvailability(TestCase):
    def test_constants(self):
        self.assertEqual(JavaScriptCore.WEBKIT_VERSION_1_0, 0x0100)
        self.assertEqual(JavaScriptCore.WEBKIT_VERSION_1_1, 0x0110)
        self.assertEqual(JavaScriptCore.WEBKIT_VERSION_1_2, 0x0120)
        self.assertEqual(JavaScriptCore.WEBKIT_VERSION_1_3, 0x0130)
        self.assertEqual(JavaScriptCore.WEBKIT_VERSION_2_0, 0x0200)
        self.assertEqual(JavaScriptCore.WEBKIT_VERSION_3_0, 0x0300)
        self.assertEqual(JavaScriptCore.WEBKIT_VERSION_3_1, 0x0310)
        self.assertEqual(JavaScriptCore.WEBKIT_VERSION_4_0, 0x0400)
        self.assertEqual(JavaScriptCore.WEBKIT_VERSION_LATEST, 0x9999)
