import sys
from Foundation import NSObject
from AppKit import NSApplicationMain
from objc import *
from nibwrapper import ConverterBase, ConverterControllerBase

class Converter (ConverterBase):
	def convertAmount(self, amt, rate):
		return amt*rate
		
class ConverterController (ConverterControllerBase):

	# First define the IB Outlets, the 'ivar' calls below define new
	# instance variables in the objective-C class (e.g. visible
	# for introspection in objective-C)

	def awakeFromNib(self):
		# Provide some defaults for the user...
		self.dollarField.setFloatValue_(2.0)
		self.rateField.setFloatValue_(3.0)

	def convert_(self, sender):
		rate = self.rateField.floatValue()
		amt = self.dollarField.floatValue()

		total = self.converter.convertAmount(rate, amt)
		self.totalField.setFloatValue_(total)
		self.rateField.selectText_(self)


sys.exit(NSApplicationMain(sys.argv))
