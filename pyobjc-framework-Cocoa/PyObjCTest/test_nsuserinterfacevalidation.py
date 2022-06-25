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
    def testProtocols(self):
        self.assertProtocolExists("NSValidatedUserInterfaceItem")
        self.assertResultHasType(
            TestNSUserInterfaceValidationHelper.action, objc._C_SEL
        )
        self.assertResultHasType(
            TestNSUserInterfaceValidationHelper.tag, objc._C_NSInteger
        )

        self.assertProtocolExists("NSUserInterfaceValidations")
        self.assertResultIsBOOL(
            TestNSUserInterfaceValidationHelper.validateUserInterfaceItem_
        )
