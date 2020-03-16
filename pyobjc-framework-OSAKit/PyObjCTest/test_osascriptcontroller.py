import OSAKit
from PyObjCTools.TestSupport import TestCase


class TestOSAScriptController(TestCase):
    def testConstants(self):
        self.assertEqual(OSAKit.OSAScriptStopped, 0)
        self.assertEqual(OSAKit.OSAScriptRunning, 1)
        self.assertEqual(OSAKit.OSAScriptRecording, 2)

    def testMethods(self):
        self.assertResultIsBOOL(OSAKit.OSAScriptController.isCompiling)
