#
# Demonstrates that the super-class implementation of an overridden method
# can be called in the same way as with normal objects.
#
# Well almost, the new 'super(MyClass, self).method(...)' convention is not
# supported yet because it looks directly into the __dict__ of classes, and
# that dict is empty for objective-C classes (well, until I find a way to work
# around a feature of Cocoa on MacOS X)
import objc

NSObject = objc.lookUpClass('NSObject')

N = 1

class MyObject (NSObject):
    def init(self):
        global N
        if N == 1:
            print "Calling super.init"
            N = 0

            # Call super-class implementation.
            super(MyObject, self).init()

            # The older convention also works:
            #NSObject.init(self)
        else:
            print "Cyclic call detected"


x = MyObject.alloc().init()
