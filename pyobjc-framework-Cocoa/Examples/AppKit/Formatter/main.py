from AppKit import NSFormatter, NSString
from PyObjCTools import AppHelper

try:
    unicode
except NameError:
    unicode = str


class MyFormatter(NSFormatter):
    def stringForObjectValue_(self, product):
        if isinstance(product, (str, unicode)):
            return product
        return str(product)

    def getObjectValue_forString_errorDescription_(self, value, upc, error):
        print(self, upc)

        if not upc:
            print("No data")
            return True, None, None

        print("Have data")
        return False, None, NSString.stringWithString_("Foo the {}".format("bar"))


AppHelper.runEventLoop()
