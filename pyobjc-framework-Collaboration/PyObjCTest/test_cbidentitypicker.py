import Collaboration
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBIdentityPicker(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            Collaboration.CBIdentityPicker.setAllowsMultipleSelection_, 0
        )
        self.assertResultIsBOOL(Collaboration.CBIdentityPicker.allowsMultipleSelection)

        self.assertArgIsSEL(
            Collaboration.CBIdentityPicker.runModalForWindow_modalDelegate_didEndSelector_contextInfo_,  # noqa: B950
            2,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgHasType(
            Collaboration.CBIdentityPicker.runModalForWindow_modalDelegate_didEndSelector_contextInfo_,  # noqa: B950
            3,
            b"^v",
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBlock(
            Collaboration.CBIdentityPicker.runModalForWindow_completionHandler_,
            1,
            b"vI",
        )
