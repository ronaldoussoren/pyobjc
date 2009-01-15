
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMBundleAction (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(AMBundleAction.initWithDefinition_fromArchive_, 1)
        self.failUnlessResultIsBOOL(AMBundleAction.hasView)

if __name__ == "__main__":
    main()
