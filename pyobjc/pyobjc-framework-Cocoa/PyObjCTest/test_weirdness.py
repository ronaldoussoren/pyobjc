# This is not a real test, but more documentation of a strange feature of
# the Cocoa runtime.
#
# A number of classes in Cocoa grow new methods if you instantiate them. We
# work around this feature by rescanning the method table after calling a
# class-method.
#
# We need to do this to reliably detect calls to the superclass implementation
# of a method. Without the workaround, calls to NSButtonCell.isEnabled_ (one
# of the magical classes) would be interpreted as calls to
# NSActionCell.isEnabled_, which is wrong.
#

import sys
from PyObjCTools.TestSupport import *

import objc

if sys.platform == 'darwin':
    import AppKit

    class TestWeirdness(TestCase):

        def doWeirdness(self, className, methodToTest):
            c = objc.lookUpClass(className)
            before = getattr(c, methodToTest)
            b = c.alloc().init()
            after = getattr(c, methodToTest)

            self.assert_(before != after, "No weirdness present on %s.%s"%(
                className, methodToTest))


        def testWeirdness1(self):
            self.doWeirdness("NSButtonCell", "setEnabled_")

        def testWeirdness2(self):
            self.doWeirdness("NSTextView", "setEditable_")


if __name__ == '__main__':
    main()
