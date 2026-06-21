import AppKit
import objc
from PyObjCTools.TestSupport import TestCase


class TestNSUserInterfaceValidationHelper(AppKit.NSObject):
    def action(self):
        return 1

    def tag(self):
        return 1

    def validateUserInterfaceItem_(self, a):
        return 1


class TestNSUserInterfaceValidation(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("NSValidatedUserInterfaceItem", AppKit)
        self.assertResultHasType(
            TestNSUserInterfaceValidationHelper.action, objc._C_SEL
        )
        self.assertResultHasType(
            TestNSUserInterfaceValidationHelper.tag, objc._C_NSInteger
        )

        self.assertProtocolExists("NSUserInterfaceValidations", AppKit)
        self.assertResultIsBOOL(
            TestNSUserInterfaceValidationHelper.validateUserInterfaceItem_
        )
