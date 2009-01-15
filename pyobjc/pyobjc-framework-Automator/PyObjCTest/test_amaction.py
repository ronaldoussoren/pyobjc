
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMAction (TestCase):
    @min_os_level("10.5")
    def testMethods10_5(self):
        self.failUnlessArgIsOut(AMAction.initWithContentsOfURL_error_, 1)
        self.failUnlessArgIsBOOL(AMAction.initWithDefinition_fromArchive_, 1)

    def testMethods(self):
        self.failUnlessArgIsOut(AMAction.runWithInput_fromAction_error_, 2)

if __name__ == "__main__":
    main()
