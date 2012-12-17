from Foundation import *

class Converter (NSObject):
    exchangeRate = objc.ivar.double()
    dollarsToConvert = objc.ivar.double()

    def init(self):
        self = super(Converter, self).init()
        self.exchangeRate = 3
        self.dollarsToConvert = 4
        return self

    def amountInOtherCurrency(self):
        return self.dollarsToConvert * self.exchangeRate

Converter.setKeys_triggerChangeNotificationsForDependentKey_(
    [u"dollarsToConvert", u"exchangeRate"],
    u"amountInOtherCurrency"
)
