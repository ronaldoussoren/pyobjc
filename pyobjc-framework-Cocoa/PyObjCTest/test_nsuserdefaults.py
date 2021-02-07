import Foundation
from PyObjCTools.TestSupport import TestCase


class PythonListAsValue(TestCase):
    def testSettingPythonList(self):
        defaults = Foundation.NSUserDefaults.standardUserDefaults()
        defaults.setObject_forKey_(["a", "b", "c"], "randomKey")

        self.assertEqual(defaults.arrayForKey_("randomKey"), ["a", "b", "c"])

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSUserDefaults.boolForKey_)
        self.assertArgIsBOOL(Foundation.NSUserDefaults.setBool_forKey_, 0)
        self.assertResultIsBOOL(Foundation.NSUserDefaults.synchronize)
        self.assertResultIsBOOL(Foundation.NSUserDefaults.objectIsForcedForKey_)
        self.assertResultIsBOOL(
            Foundation.NSUserDefaults.objectIsForcedForKey_inDomain_
        )

    def testConstants(self):
        self.assertIsInstance(Foundation.NSGlobalDomain, str)
        self.assertIsInstance(Foundation.NSArgumentDomain, str)
        self.assertIsInstance(Foundation.NSRegistrationDomain, str)

        self.assertIsInstance(Foundation.NSUserDefaultsDidChangeNotification, str)

        self.assertIsInstance(Foundation.NSWeekDayNameArray, str)
        self.assertIsInstance(Foundation.NSShortWeekDayNameArray, str)
        self.assertIsInstance(Foundation.NSMonthNameArray, str)
        self.assertIsInstance(Foundation.NSShortMonthNameArray, str)
        self.assertIsInstance(Foundation.NSTimeFormatString, str)
        self.assertIsInstance(Foundation.NSDateFormatString, str)
        self.assertIsInstance(Foundation.NSTimeDateFormatString, str)
        self.assertIsInstance(Foundation.NSShortTimeDateFormatString, str)
        self.assertIsInstance(Foundation.NSCurrencySymbol, str)
        self.assertIsInstance(Foundation.NSDecimalSeparator, str)
        self.assertIsInstance(Foundation.NSThousandsSeparator, str)
        self.assertIsInstance(Foundation.NSDecimalDigits, str)
        self.assertIsInstance(Foundation.NSAMPMDesignation, str)
        self.assertIsInstance(Foundation.NSHourNameDesignations, str)
        self.assertIsInstance(Foundation.NSYearMonthWeekDesignations, str)
        self.assertIsInstance(Foundation.NSEarlierTimeDesignations, str)
        self.assertIsInstance(Foundation.NSLaterTimeDesignations, str)
        self.assertIsInstance(Foundation.NSThisDayDesignations, str)
        self.assertIsInstance(Foundation.NSNextDayDesignations, str)
        self.assertIsInstance(Foundation.NSNextNextDayDesignations, str)
        self.assertIsInstance(Foundation.NSPriorDayDesignations, str)
        self.assertIsInstance(Foundation.NSDateTimeOrdering, str)
        self.assertIsInstance(Foundation.NSInternationalCurrencyString, str)
        self.assertIsInstance(Foundation.NSShortDateFormatString, str)
        self.assertIsInstance(Foundation.NSPositiveCurrencyFormatString, str)
        self.assertIsInstance(Foundation.NSNegativeCurrencyFormatString, str)
