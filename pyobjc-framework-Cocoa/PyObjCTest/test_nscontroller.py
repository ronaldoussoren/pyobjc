from AppKit import *
from PyObjCTools.TestSupport import *

class  TestNSController (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSController.commitEditing)
        self.assertResultIsBOOL(NSController.isEditing)
        self.assertArgIsSEL(NSController.commitEditingWithDelegate_didCommitSelector_contextInfo_, 1, b'v@:@' + objc._C_NSBOOL + b'^v')
        self.assertArgHasType(NSController.commitEditingWithDelegate_didCommitSelector_contextInfo_, 2, b'^v')

if __name__ == "__main__":
    main()
