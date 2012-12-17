#
#  TransformerAppDelegate.py
#  Transformer
#
#  Converted by ufiedler@web.de on 03.02.05.
#
#  Value Transformer Example Application
#  Based on Apples FahrenheitToCelsiusTransformer Example
#  file:///Developer/ADC%20Reference%20Library/documentation/Cocoa/Conceptual/ValueTransformers/index.html

from Cocoa import *


class FahrenheitToCelsiusTransformer(NSValueTransformer):
    # While not strictly necessary, because PyObjC can deduce that
    # these selectors should be implemented for the class,
    # declaring them as classmethod helps make this more clear.
    def transformedValueClass(cls):
        return NSNumber
    transformedValueClass = classmethod(transformedValueClass)

    def allowsReverseTransformation(cls):
        return True
    allowsReverseTransformation = classmethod(allowsReverseTransformation)

    def transformedValue_(self, value):
        if value is None:
            return None
        # the forward value is coming from an ivar that's
        # already a number, so we don't need to coerce this...
        # but we do it anyway for
        fahrenheitInputValue = float(value)
        # calculate Celsius value
        celsiusOutputValue = (5.0 / 9.0) * (fahrenheitInputValue - 32.0)
        return celsiusOutputValue

    def reverseTransformedValue_(self, value):
        if value is None:
            return None
        # the reverse value comes from the text field, so it's
        # going to be a string that we need to coerce to float.
        celsiusInputValue = float(value)
        # calculate Fahrenheit value
        fahrenheitOutputValue = ((9.0 / 5.0) * celsiusInputValue) + 32.0
        return fahrenheitOutputValue


class TransformerAppDelegate (NSObject):
    fahrenheit = objc.ivar('fahrenheit', objc._C_DBL)

trans = FahrenheitToCelsiusTransformer.alloc().init()
NSValueTransformer.setValueTransformer_forName_(trans, u"FahrenheitToCelsiusTransformer")
