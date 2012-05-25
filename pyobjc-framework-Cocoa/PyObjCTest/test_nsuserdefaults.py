from Foundation import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str

class PythonListAsValue (TestCase):

    def testSettingPythonList(self):
        defaults = NSUserDefaults.standardUserDefaults()
        defaults.setObject_forKey_([b'a'.decode('ascii'), b'b'.decode('ascii'), b'c'.decode('ascii')], b'randomKey'.decode('ascii'))

        self.assertEqual(defaults.arrayForKey_(b'randomKey'.decode('ascii')), [b'a'.decode('ascii'), b'b'.decode('ascii'), b'c'.decode('ascii')])

    def testMethods(self):
        self.assertResultIsBOOL(NSUserDefaults.boolForKey_)
        self.assertArgIsBOOL(NSUserDefaults.setBool_forKey_, 0)
        self.assertResultIsBOOL(NSUserDefaults.synchronize)
        self.assertResultIsBOOL(NSUserDefaults.objectIsForcedForKey_)
        self.assertResultIsBOOL(NSUserDefaults.objectIsForcedForKey_inDomain_)


    def testConstants(self):
        self.assertIsInstance(NSGlobalDomain, unicode)
        self.assertIsInstance(NSArgumentDomain, unicode)
        self.assertIsInstance(NSRegistrationDomain, unicode)
        self.assertIsInstance(NSUserDefaultsDidChangeNotification, unicode)
        self.assertIsInstance(NSWeekDayNameArray, unicode)
        self.assertIsInstance(NSShortWeekDayNameArray, unicode)
        self.assertIsInstance(NSMonthNameArray, unicode)
        self.assertIsInstance(NSShortMonthNameArray, unicode)
        self.assertIsInstance(NSTimeFormatString, unicode)
        self.assertIsInstance(NSDateFormatString, unicode)
        self.assertIsInstance(NSTimeDateFormatString, unicode)
        self.assertIsInstance(NSShortTimeDateFormatString, unicode)
        self.assertIsInstance(NSCurrencySymbol, unicode)
        self.assertIsInstance(NSDecimalSeparator, unicode)
        self.assertIsInstance(NSThousandsSeparator, unicode)
        self.assertIsInstance(NSDecimalDigits, unicode)
        self.assertIsInstance(NSAMPMDesignation, unicode)
        self.assertIsInstance(NSHourNameDesignations, unicode)
        self.assertIsInstance(NSYearMonthWeekDesignations, unicode)
        self.assertIsInstance(NSEarlierTimeDesignations, unicode)
        self.assertIsInstance(NSLaterTimeDesignations, unicode)
        self.assertIsInstance(NSThisDayDesignations, unicode)
        self.assertIsInstance(NSNextDayDesignations, unicode)
        self.assertIsInstance(NSNextNextDayDesignations, unicode)
        self.assertIsInstance(NSPriorDayDesignations, unicode)
        self.assertIsInstance(NSDateTimeOrdering, unicode)
        self.assertIsInstance(NSInternationalCurrencyString, unicode)
        self.assertIsInstance(NSShortDateFormatString, unicode)
        self.assertIsInstance(NSPositiveCurrencyFormatString, unicode)
        self.assertIsInstance(NSNegativeCurrencyFormatString, unicode)

if __name__ == "__main__":
    main()
