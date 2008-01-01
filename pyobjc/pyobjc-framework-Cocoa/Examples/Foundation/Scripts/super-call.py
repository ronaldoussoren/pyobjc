#
# Demonstrates that the super-class implementation of an overridden method
# can be called in the same way as with normal objects.
#
from Foundation import *

N = 1

class MyObject (NSObject):
    def init(self):
        global N
        if N == 1:
            print "Calling super.init"
            N = 0

            # Call super-class implementation.
            super(MyObject, self).init()

        else:
            print "Cyclic call detected"


x = MyObject.alloc().init()
