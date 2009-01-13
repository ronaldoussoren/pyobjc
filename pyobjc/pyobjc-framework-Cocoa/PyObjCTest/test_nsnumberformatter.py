from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSNumberFormatter (TestCase):
    def testConstants(self):
        self.assertEquals(NSNumberFormatterNoStyle, kCFNumberFormatterNoStyle)
        self.assertEquals(NSNumberFormatterDecimalStyle, kCFNumberFormatterDecimalStyle)
        self.assertEquals(NSNumberFormatterCurrencyStyle, kCFNumberFormatterCurrencyStyle)
        self.assertEquals(NSNumberFormatterPercentStyle, kCFNumberFormatterPercentStyle)
        self.assertEquals(NSNumberFormatterScientificStyle, kCFNumberFormatterScientificStyle)
        self.assertEquals(NSNumberFormatterSpellOutStyle, kCFNumberFormatterSpellOutStyle)

        self.assertEquals(NSNumberFormatterBehaviorDefault, 0)
        self.assertEquals(NSNumberFormatterBehavior10_0, 1000)
        self.assertEquals(NSNumberFormatterBehavior10_4, 1040)

        self.assertEquals(NSNumberFormatterPadBeforePrefix, kCFNumberFormatterPadBeforePrefix)
        self.assertEquals(NSNumberFormatterPadAfterPrefix, kCFNumberFormatterPadAfterPrefix)
        self.assertEquals(NSNumberFormatterPadBeforeSuffix, kCFNumberFormatterPadBeforeSuffix)
        self.assertEquals(NSNumberFormatterPadAfterSuffix, kCFNumberFormatterPadAfterSuffix)

        self.assertEquals(NSNumberFormatterRoundCeiling, kCFNumberFormatterRoundCeiling)
        self.assertEquals(NSNumberFormatterRoundFloor, kCFNumberFormatterRoundFloor)
        self.assertEquals(NSNumberFormatterRoundDown, kCFNumberFormatterRoundDown)
        self.assertEquals(NSNumberFormatterRoundUp, kCFNumberFormatterRoundUp)
        self.assertEquals(NSNumberFormatterRoundHalfEven, kCFNumberFormatterRoundHalfEven)
        self.assertEquals(NSNumberFormatterRoundHalfDown, kCFNumberFormatterRoundHalfDown)
        self.assertEquals(NSNumberFormatterRoundHalfUp, kCFNumberFormatterRoundHalfUp)


    def testOutput(self):
        o = NSNumberFormatter.alloc().init()
        m = o.getObjectValue_forString_range_error_.__metadata__()
        self.assertEquals(m['arguments'][2]['type'], 'o^@')
        self.failUnless(m['arguments'][4]['type'].startswith('N^'))
        self.failUnless(m['arguments'][5]['type'].startswith('o^'))




if __name__ == "__main__":
    main()
