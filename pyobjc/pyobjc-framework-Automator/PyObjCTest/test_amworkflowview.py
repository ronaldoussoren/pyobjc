
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMWorkflowView (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(AMWorkflowView.isEditable)
        self.failUnlessArgIsBOOL(AMWorkflowView.setEditable_, 0)


if __name__ == "__main__":
    main()
