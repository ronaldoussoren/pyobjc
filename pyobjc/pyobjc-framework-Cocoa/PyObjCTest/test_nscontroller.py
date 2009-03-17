from AppKit import *
from PyObjCTools.TestSupport import *

class  TestNSController (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSController.commitEditing)
        self.failUnlessResultIsBOOL(NSController.isEditing)
        self.failUnlessArgIsSEL(NSController.commitEditingWithDelegate_didCommitSelector_contextInfo_, 1, 'v@:@' + objc._C_NSBOOL + '^v')
        self.failUnlessArgHasType(NSController.commitEditingWithDelegate_didCommitSelector_contextInfo_, 2, '^v')

if __name__ == "__main__":
    main()
