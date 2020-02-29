from Automator import *
from PyObjCTools.TestSupport import *


class TestAMBundleAction(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(AMBundleAction.initWithDefinition_fromArchive_, 1)
        self.assertResultIsBOOL(AMBundleAction.hasView)


if __name__ == "__main__":
    main()
