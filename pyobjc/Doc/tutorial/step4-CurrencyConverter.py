import objc
from Foundation import *
from AppKit import *
from PyObjCTools import NibClassBuilder, AppHelper


NibClassBuilder.extractClasses("MainMenu")


# class defined in MainMenu.nib
class Converter(NibClassBuilder.AutoBaseClass):
    # the actual base class is NSObject
    pass


# class defined in MainMenu.nib
class ConverterController(NibClassBuilder.AutoBaseClass):
    # the actual base class is NSObject
    # The following outlets are added to the class:
    # converter
    # dollarField
    # rateField
    # totalField

    def convert_(self, sender):
        pass



if __name__ == "__main__":
    AppHelper.runEventLoop()
