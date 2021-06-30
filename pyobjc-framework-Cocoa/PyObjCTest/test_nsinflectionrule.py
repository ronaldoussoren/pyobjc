import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSInflectionRule(TestCase):
    @min_os_level("12.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Foundation.NSInflectionRule.canInflectPreferredLocalization
        )
