import time
import sys
from Foundation import NSObject
from AppKit import NSApplicationMain
from PyObjCTools import NibClassBuilder
from AppKit import NSRunAlertPanel
from objc import *

NibClassBuilder.extractClasses('MainMenu.nib')

class Converter (NibClassBuilder.AutoBaseClass):
    def convertAmount(self, amt, rate):
        return amt*rate


class ConverterController (NibClassBuilder.AutoBaseClass):

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

        x = NSRunAlertPanel("Calculation Result",
            "The result is %s"%(total), "OK", None, None)


sys.exit(NSApplicationMain(sys.argv))
