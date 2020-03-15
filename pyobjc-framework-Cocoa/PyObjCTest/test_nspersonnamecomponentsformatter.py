import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPersonNameComponentsFormatter(TestCase):
    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(Foundation.NSPersonNameComponentsFormatterStyleDefault, 0)
        self.assertEqual(Foundation.NSPersonNameComponentsFormatterStyleShort, 1)
        self.assertEqual(Foundation.NSPersonNameComponentsFormatterStyleMedium, 2)
        self.assertEqual(Foundation.NSPersonNameComponentsFormatterStyleLong, 3)
        self.assertEqual(Foundation.NSPersonNameComponentsFormatterStyleAbbreviated, 4)

        self.assertEqual(Foundation.NSPersonNameComponentsFormatterPhonetic, 1 << 1)

        self.assertIsInstance(Foundation.NSPersonNameComponentKey, str)
        self.assertIsInstance(Foundation.NSPersonNameComponentGivenName, str)
        self.assertIsInstance(Foundation.NSPersonNameComponentFamilyName, str)
        self.assertIsInstance(Foundation.NSPersonNameComponentMiddleName, str)
        self.assertIsInstance(Foundation.NSPersonNameComponentPrefix, str)
        self.assertIsInstance(Foundation.NSPersonNameComponentSuffix, str)
        self.assertIsInstance(Foundation.NSPersonNameComponentNickname, str)
        self.assertIsInstance(Foundation.NSPersonNameComponentDelimiter, str)

    @min_os_level("10.11")
    def testOutput(self):
        self.assertResultIsBOOL(
            Foundation.NSPersonNameComponentsFormatter.getObjectValue_forString_errorDescription_  # noqa: B950
        )
        self.assertArgIsOut(
            Foundation.NSPersonNameComponentsFormatter.getObjectValue_forString_errorDescription_,  # noqa: B950
            0,
        )
        self.assertArgIsOut(
            Foundation.NSPersonNameComponentsFormatter.getObjectValue_forString_errorDescription_,  # noqa: B950
            2,
        )

        self.assertResultIsBOOL(Foundation.NSPersonNameComponentsFormatter.isPhonetic)
        self.assertArgIsBOOL(Foundation.NSPersonNameComponentsFormatter.setPhonetic_, 0)
