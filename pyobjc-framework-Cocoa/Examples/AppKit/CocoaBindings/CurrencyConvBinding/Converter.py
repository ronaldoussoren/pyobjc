import objc
from Foundation import NSObject
from objc import super


class Converter(NSObject):
    exchangeRate = objc.ivar.double()
    dollarsToConvert = objc.ivar.double()

    def init(self):
        self = super().init()
        self.exchangeRate = 3
        self.dollarsToConvert = 4
        return self

    def amountInOtherCurrency(self):
        return self.dollarsToConvert * self.exchangeRate


Converter.setKeys_triggerChangeNotificationsForDependentKey_(
    ["dollarsToConvert", "exchangeRate"], "amountInOtherCurrency"
)
