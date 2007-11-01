from Foundation import NSObject, NSObject
from PyObjCTools import NibClassBuilder, AppHelper

NibClassBuilder.extractClasses("MainMenu")


# class defined in MainMenu.nib
class Converter(NibClassBuilder.AutoBaseClass):
    # the actual base class is NSObject

    def convertAmount(self, amt, rate):
        return amt * rate

# class defined in MainMenu.nib
class ConverterController(NibClassBuilder.AutoBaseClass):
    # the actual base class is NSObject
    # The following outlets are added to the class:
    # converter
    # dollarField
    # rateField
    # totalField

    def convert_(self, sender):
        amt = self.dollarField.floatValue()
        rate = self.rateField.floatValue()

        total = self.converter.convertAmount(rate, amt)
        self.totalField.setFloatValue_(total)
        self.rateField.selectText_(self)

    def awakeFromNib(self):
        self.rateField.window().makeKeyAndOrderFront_(self)
        self.rateField.selectText_(self)

    def invertRate_(self, sender):
        rate = self.rateField.floatValue()
        if rate != 0.0:
            rate = 1.0 / rate
        self.rateField.setFloatValue_(rate)

if __name__ == "__main__":
    AppHelper.runEventLoop()
