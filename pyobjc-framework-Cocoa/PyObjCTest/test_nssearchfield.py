import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSSearchField(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSearchField.sendsWholeSearchString)
        self.assertArgIsBOOL(AppKit.NSSearchField.setSendsWholeSearchString_, 0)
        self.assertResultIsBOOL(AppKit.NSSearchField.sendsSearchStringImmediately)
        self.assertArgIsBOOL(AppKit.NSSearchField.setSendsSearchStringImmediately_, 0)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBOOL(AppKit.NSSearchField.rectForSearchTextWhenCentered_, 0)
        self.assertArgIsBOOL(AppKit.NSSearchField.rectForSearchButtonWhenCentered_, 0)
        self.assertArgIsBOOL(AppKit.NSSearchField.rectForCancelButtonWhenCentered_, 0)
        self.assertResultIsBOOL(AppKit.NSSearchField.centersPlaceholder)
        self.assertArgIsBOOL(AppKit.NSSearchField.setCentersPlaceholder_, 0)

    @min_sdk_level("10.11")
    def testProtocols(self):
        objc.protocolNamed("NSSearchFieldDelegate")
