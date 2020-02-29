from Automator import *
from PyObjCTools.TestSupport import *


class TestAMShellScriptAction(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AMShellScriptAction.remapLineEndings)


if __name__ == "__main__":
    main()
