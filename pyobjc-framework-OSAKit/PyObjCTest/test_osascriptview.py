import OSAKit
from PyObjCTools.TestSupport import TestCase


class TestOSAScriptView(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(OSAKit.OSAScriptView.usesScriptAssistant)
        self.assertArgIsBOOL(OSAKit.OSAScriptView.setUsesScriptAssistant_, 0)
        self.assertResultIsBOOL(OSAKit.OSAScriptView.usesTabs)
        self.assertArgIsBOOL(OSAKit.OSAScriptView.setUsesTabs_, 0)
        self.assertResultIsBOOL(OSAKit.OSAScriptView.wrapsLines)
        self.assertArgIsBOOL(OSAKit.OSAScriptView.setWrapsLines_, 0)
        self.assertResultIsBOOL(OSAKit.OSAScriptView.indentsWrappedLines)
        self.assertArgIsBOOL(OSAKit.OSAScriptView.setIndentsWrappedLines_, 0)
