import Automator
from PyObjCTools.TestSupport import TestCase


class TestAMShellScriptAction(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Automator.AMShellScriptAction.remapLineEndings)
