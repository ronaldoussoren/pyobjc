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

def main():
    from AppKit import NSApplicationMain, NSRunAlertPanel, NSApp
    import traceback
    import sys
    def unexpectedErrorAlert():
        exceptionInfo = traceback.format_exception_only(*sys.exc_info()[:2])[0].strip()
        return NSRunAlertPanel("An unexpected error has occurred",
                "(%s)" % exceptionInfo,
                "Continue", "Quit", None)
    
    
    mainFunc = NSApplicationMain
    args = (sys.argv,)
    while 1:
        try:
            mainFunc(*args)
        except:
            if not unexpectedErrorAlert():
                raise
            mainFunc = NSApp().run
            args = ()
        else:
            break

if __name__ == '__main__':
    main()