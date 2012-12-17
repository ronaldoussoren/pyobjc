import time
import sys
from AppKit import *


class Converter (NSObject):
    def convertAmount(self, amt, rate):
        return amt*rate


class ConverterController (NSObject):

    # First define the IB Outlets, the 'ivar' calls below define new
    # instance variables in the objective-C class (e.g. visible
    # for introspection in objective-C)
    converter = objc.IBOutlet()
    dollarField = objc.IBOutlet()
    rateField = objc.IBOutlet()
    totalField = objc.IBOutlet()

    def awakeFromNib(self):
        # Provide some defaults for the user...
        self.dollarField.setFloatValue_(2.0)
        self.rateField.setFloatValue_(3.0)

    @objc.IBAction
    def convert_(self, sender):
        rate = self.rateField.floatValue()
        amt = self.dollarField.floatValue()

        total = self.converter.convertAmount(rate, amt)
        self.totalField.setFloatValue_(total)
        self.rateField.selectText_(self)

        #x = NSRunAlertPanel("Calculation Result",
        #    "The result is %s"%(total), "OK", None, None)


sys.exit(NSApplicationMain(sys.argv))
