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

def testClass( className, methodToTest ):
	c = objc.lookUpClass( className )
	mE = 'c.%s' % methodToTest
	before =  eval(mE)
	#before = getattr(c, methodToTest)
	b = c.alloc().init()
	after = eval(mE)
	#after = getattr(c, methodToTest)

	if before == after:
		print "No weirdness present on %s.%s()" % (className, methodToTest)
	else:
		print "Method weirdness detected on %s.%s()" % (className, methodToTest)
		print "\tbefore alloc(): ", before
		print "\tafter  alloc(): ", after


testClass( "NSButtonCell", "setEnabled_" )
testClass( "NSTextView", "setEditable_" )

