from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSViewController (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertArgIsSEL(NSViewController.commitEditingWithDelegate_didCommitSelector_contextInfo_, 1, b'v@:@'+objc._C_NSBOOL + b'^v')
        self.assertArgHasType(NSViewController.commitEditingWithDelegate_didCommitSelector_contextInfo_, 2, b'^v')

        self.assertResultIsBOOL(NSViewController.commitEditing)


if __name__ == "__main__":
    main()
