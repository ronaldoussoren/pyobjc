
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMShellScriptAction (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AMShellScriptAction.remapLineEndings)

if __name__ == "__main__":
    main()
