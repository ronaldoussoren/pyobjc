from Foundation import NSObject, NSObject
from AppKit import NibClassBuilder
from AppKit.NibClassBuilder import AutoBaseClass

NibClassBuilder.extractClasses("MainMenu")


# class defined in MainMenu.nib
class Converter(AutoBaseClass):
    # the actual base class is NSObject
    pass


# class defined in MainMenu.nib
class ConverterController(AutoBaseClass):
    # the actual base class is NSObject
    # The following outlets are added to the class:
    # converter
    # dollarField
    # rateField
    # totalField

    def convert_(self, sender):
        pass


