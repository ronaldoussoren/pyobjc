from Foundation import *
from AppKit import *
from PyObjCTools import NibClassBuilder
from objc import ivar

NibClassBuilder.extractClasses("CurrencyConvBindingDocument")


class Converter(NibClassBuilder.AutoBaseClass):

        # The input fields have formatters that convert the text
        # value to a number. If we wouldn't do that, exchangeRate
        # and dollarsToConvert would be set to strings.
        #
        # The alternative is using objc instance variables of the
        # right type (in this case doubles) and let the Cocoa 
        # implementation worry about the conversion:
	#   exchangeRate = ivar('exchangeRate', 'd')
	#   dollarsToConvert = ivar('dollarsToConvert', 'd')
	
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

