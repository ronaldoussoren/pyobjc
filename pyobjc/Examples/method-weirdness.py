# 
# This is not really an example, but a tale about a weird feature of the Cocoa
# library on MacOS X.
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
import objc

# NSButtonCell is one of the classes that acts like this, NSTextView is
# another one (both detected accidently while debugging a problem with the
# Todo example)
NSButtonCell = objc.lookup_class('NSButtonCell')

before =  NSButtonCell.setEnabled_
b = NSButtonCell.alloc()
after = NSButtonCell.setEnabled_

if before == after:
	print "No weirdness present"
else:
	print "Method weirdness detected"
	print "before:", before
	print "after:", after
