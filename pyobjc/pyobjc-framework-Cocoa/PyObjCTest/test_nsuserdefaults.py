from Foundation import *
from PyObjCTools.TestSupport import *

class PythonListAsValue (TestCase):

    def testSettingPythonList(self):
        defaults = NSUserDefaults.standardUserDefaults()
        defaults.setObject_forKey_([u'a', u'b', u'c'], u'randomKey')

        self.assertEquals(defaults.arrayForKey_(u'randomKey'), [u'a', u'b', u'c'])

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSUserDefaults.boolForKey_)
        self.failUnlessArgIsBOOL(NSUserDefaults.setBool_forKey_, 0)
        self.failUnlessResultIsBOOL(NSUserDefaults.synchronize)
        self.failUnlessResultIsBOOL(NSUserDefaults.objectIsForcedForKey_)
        self.failUnlessResultIsBOOL(NSUserDefaults.objectIsForcedForKey_inDomain_)


    def testConstants(self):
        self.failUnless(isinstance(NSGlobalDomain, unicode))
        self.failUnless(isinstance(NSArgumentDomain, unicode))
        self.failUnless(isinstance(NSRegistrationDomain, unicode))

        self.failUnless(isinstance(NSUserDefaultsDidChangeNotification, unicode))

        self.failUnless(isinstance(NSWeekDayNameArray, unicode))
        self.failUnless(isinstance(NSShortWeekDayNameArray, unicode))
        self.failUnless(isinstance(NSMonthNameArray, unicode))

        self.failUnless(isinstance(NSShortMonthNameArray, unicode))
        self.failUnless(isinstance(NSTimeFormatString, unicode))
        self.failUnless(isinstance(NSDateFormatString, unicode))
        self.failUnless(isinstance(NSTimeDateFormatString, unicode))
        self.failUnless(isinstance(NSShortTimeDateFormatString, unicode))
        self.failUnless(isinstance(NSCurrencySymbol, unicode))
        self.failUnless(isinstance(NSDecimalSeparator, unicode))
        self.failUnless(isinstance(NSThousandsSeparator, unicode))
        self.failUnless(isinstance(NSDecimalDigits, unicode))
        self.failUnless(isinstance(NSAMPMDesignation, unicode))
        self.failUnless(isinstance(NSHourNameDesignations, unicode))
        self.failUnless(isinstance(NSYearMonthWeekDesignations, unicode))
        self.failUnless(isinstance(NSEarlierTimeDesignations, unicode))
        self.failUnless(isinstance(NSLaterTimeDesignations, unicode))
        self.failUnless(isinstance(NSThisDayDesignations, unicode))
        self.failUnless(isinstance(NSNextDayDesignations, unicode))
        self.failUnless(isinstance(NSNextNextDayDesignations, unicode))
        self.failUnless(isinstance(NSPriorDayDesignations, unicode))
        self.failUnless(isinstance(NSDateTimeOrdering, unicode))
        self.failUnless(isinstance(NSInternationalCurrencyString, unicode))
        self.failUnless(isinstance(NSShortDateFormatString, unicode))
        self.failUnless(isinstance(NSPositiveCurrencyFormatString, unicode))
        self.failUnless(isinstance(NSNegativeCurrencyFormatString, unicode))




if __name__ == "__main__":
    main()
