from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSPersonNameComponentsFormatter (TestCase):
    @min_os_level('10.11')
    def testConstants(self):
        self.assertEqual(NSPersonNameComponentsFormatterStyleDefault, 0)
        self.assertEqual(NSPersonNameComponentsFormatterStyleShort, 1)
        self.assertEqual(NSPersonNameComponentsFormatterStyleMedium, 2)
        self.assertEqual(NSPersonNameComponentsFormatterStyleLong, 3)
        self.assertEqual(NSPersonNameComponentsFormatterStyleAbbreviated, 4)

        self.assertEqual(NSPersonNameComponentsFormatterPhonetic, 1<<1)

        self.assertIsInstance(NSPersonNameComponentKey, unicode)
        self.assertIsInstance(NSPersonNameComponentGivenName, unicode)
        self.assertIsInstance(NSPersonNameComponentFamilyName, unicode)
        self.assertIsInstance(NSPersonNameComponentMiddleName, unicode)
        self.assertIsInstance(NSPersonNameComponentPrefix, unicode)
        self.assertIsInstance(NSPersonNameComponentSuffix, unicode)
        self.assertIsInstance(NSPersonNameComponentNickname, unicode)
        self.assertIsInstance(NSPersonNameComponentDelimiter, unicode)

    @min_os_level('10.11')
    def testOutput(self):
        self.assertResultIsBOOL(NSPersonNameComponentsFormatter.getObjectValue_forString_errorDescription_)
        self.assertArgIsOut(NSPersonNameComponentsFormatter.getObjectValue_forString_errorDescription_, 0)
        self.assertArgIsOut(NSPersonNameComponentsFormatter.getObjectValue_forString_errorDescription_, 2)

        self.assertResultIsBOOL(NSPersonNameComponentsFormatter.isPhonetic)
        self.assertArgIsBOOL(NSPersonNameComponentsFormatter.setPhonetic_, 0)

if __name__ == "__main__":
    main()
