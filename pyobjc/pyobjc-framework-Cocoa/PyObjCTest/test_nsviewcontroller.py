from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSViewController (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessArgIsSEL(NSViewController.commitEditingWithDelegate_didCommitSelector_contextInfo_, 1, 'v@:@'+objc._C_NSBOOL + '^v')
        self.failUnlessArgHasType(NSViewController.commitEditingWithDelegate_didCommitSelector_contextInfo_, 2, '^v')

        self.failUnlessResultIsBOOL(NSViewController.commitEditing)

if __name__ == "__main__":
    main()
