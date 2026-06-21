import Automator
from PyObjCTools.TestSupport import TestCase


class TestAMShellScriptAction(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Automator.AMShellScriptAction.remapLineEndings)
