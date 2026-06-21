import OSAKit
from PyObjCTools.TestSupport import TestCase


class TestOSAScriptController(TestCase):
    def test_constants(self):
        self.assertEqual(OSAKit.OSAScriptStopped, 0)
        self.assertEqual(OSAKit.OSAScriptRunning, 1)
        self.assertEqual(OSAKit.OSAScriptRecording, 2)

    def test_methods(self):
        self.assertResultIsBOOL(OSAKit.OSAScriptController.isCompiling)
