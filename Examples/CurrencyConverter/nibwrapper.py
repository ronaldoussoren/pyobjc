# THIS FILE IS GENERATED. DO NOT EDIT!!!
# Interface classes for using NIB files

from objc import IBOutlet
from Foundation import NSObject

class ConverterBase (NSObject):
	"Base class for class 'Converter'"
	pass

class ConverterControllerBase (NSObject):
	"Base class for class 'ConverterController'"
	converter = IBOutlet("converter")
	totalField = IBOutlet("totalField")
	rateField = IBOutlet("rateField")
	dollarField = IBOutlet("dollarField")

	def convert_(self, sender): pass


