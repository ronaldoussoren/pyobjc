import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSScriptStandardSuiteCommands(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSSaveOptions)

    def testCommands(self):
        self.assertEqual(Foundation.NSSaveOptionsYes, 0)
        self.assertEqual(Foundation.NSSaveOptionsNo, 1)
        self.assertEqual(Foundation.NSSaveOptionsAsk, 2)
