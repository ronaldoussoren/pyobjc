import sys
from Foundation import NSObject
from AppKit import NSApplicationMain
from objc import *

class Converter (NSObject):
	def convertAmount(self, amt, rate):
		return amt*rate
		
class ConverterController (NSObject):

	# First define the IB Outlets, the 'ivar' calls below define new
	# instance variables in the objective-C class (e.g. visible
	# for introspection in objective-C)
	converter   = IBOutlet('converter')
	dollarField = IBOutlet('dollarField')
	rateField   = IBOutlet('rateField')
	totalField  = IBOutlet('totalField')
	extraField  = IBOutlet('extraField')

	def dummy(self):
		return "dummy"

	def awakeFromNib(self):
		print "awakeFromNib"

		# Provide some defaults for the user...
		self.dollarField.setFloatValue_(2.0)
		self.rateField.setFloatValue_(3.0)

	def convert_(self, sender):
		print 'DBG PYTHON: ConverterController.convert_(%s, %s)' % (self, sender)
		rate = self.rateField.floatValue()
		print '  rate=', rate
		amt = self.dollarField.floatValue()
		print '  amt=', amt

		total = self.converter.convertAmount(rate, amt)
		print '  total=', total
		self.totalField.setFloatValue_(total)
		self.rateField.selectText_(self)
		print "Done"


sys.exit(NSApplicationMain(sys.argv))
