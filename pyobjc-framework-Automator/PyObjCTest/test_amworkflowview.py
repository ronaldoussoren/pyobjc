
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMWorkflowView (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(AMWorkflowView.isEditable)
        self.assertArgIsBOOL(AMWorkflowView.setEditable_, 0)


if __name__ == "__main__":
    main()
