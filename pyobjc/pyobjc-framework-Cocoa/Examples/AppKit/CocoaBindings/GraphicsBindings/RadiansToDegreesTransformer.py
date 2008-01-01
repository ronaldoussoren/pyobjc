#
#  RadiansToDegreesTransformer.py
#  GraphicsBindings
#
#  Converted by u.fiedler on feb 2005
#  with great help from Bob Ippolito - Thank you Bob!
#
#  The original version was written in Objective-C by Malcolm Crawford
#  http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from Foundation import *

class RadiansToDegreesTransformer(NSValueTransformer):

    def transformedValueClass(cls):
        return NSNumber
    transformedValueClass = classmethod(transformedValueClass)
        
    def allowsReverseTransformation(cls):
        return True
    allowsReverseTransformation = classmethod(allowsReverseTransformation)
        
    def transformedValue_(self, radians):
        return radians / (3.1415927/180.0)
        
    def reverseTransformedValue_(self, degrees):
        if type(degrees) == type(1.2):
            # when using jostickview we get a value of type float()
            return degrees * (3.1415927/180.0)
        else:
            # we get a decimalNumber when entering a value in the textfield
            return degrees.doubleValue() * (3.1415927/180.0)
