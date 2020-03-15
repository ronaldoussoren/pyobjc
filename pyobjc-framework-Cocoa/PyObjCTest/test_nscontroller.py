import AppKit
from PyObjCTools.TestSupport import TestCase
import objc


class TestNSController(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSController.commitEditing)
        self.assertResultIsBOOL(AppKit.NSController.isEditing)
        self.assertArgIsSEL(
            AppKit.NSController.commitEditingWithDelegate_didCommitSelector_contextInfo_,
            1,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSController.commitEditingWithDelegate_didCommitSelector_contextInfo_,
            2,
            b"^v",
        )
