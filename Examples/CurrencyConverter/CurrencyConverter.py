import time
def before(txt = None):
    global b
    if txt is not None:
        print time.ctime(), txt
    b = time.time()

def after(txt):
    global b
    e = time.time()
    print time.ctime(), txt, e - b
    b = e

before('import sys')
import sys
after('import sys')
from Foundation import NSObject
after('import Foundation')
from AppKit import NSApplicationMain, NibClassBuilder
after('import AppKit')
from objc import *
after('import objc')

NibClassBuilder.extractClasses('MainMenu.nib')
after('extractClasses')

class Converter (NibClassBuilder.AutoBaseClass):
    def convertAmount(self, amt, rate):
        return amt*rate

after('class Converter')
        
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

after('class ConverterController')

sys.exit(NSApplicationMain(sys.argv))

after('NSApplicationMain')
