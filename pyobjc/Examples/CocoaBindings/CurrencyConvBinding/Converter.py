from Foundation import *
from AppKit import *
from PyObjCTools import NibClassBuilder
from objc import ivar

NibClassBuilder.extractClasses("CurrencyConvBindingDocument")


class Converter(NibClassBuilder.AutoBaseClass):
	exchangeRate = ivar('exchangeRate', 'd')
	dollarsToConvert = ivar('dollarsToConvert', 'd')
	
	def init(self):
		self = super(Converter, self).init()
		self.exchangeRate = 3
		self.dollarsToConvert = 4
		return self
		
	def amountInOtherCurrency(self):
		return self.dollarsToConvert * self.exchangeRate
#		return float(self.dollarsToConvert) * float(self.exchangeRate)

Converter.setKeys_triggerChangeNotificationsForDependentKey_(
["dollarsToConvert", "exchangeRate"], "amountInOtherCurrency")

