from Foundation import *
from AppKit import *
from PyObjCTools import NibClassBuilder

NibClassBuilder.extractClasses("CurrencyConvBindingDocument")

class CurrencyConvBindingDocument(NibClassBuilder.AutoBaseClass):
    def windowNibName(self):
        return "CurrencyConvBindingDocument"
