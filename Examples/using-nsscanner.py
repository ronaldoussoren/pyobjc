#
# Using NSScanner. This demonstrates pass-by-reference output parameters
#
# TODO: Create a real (more usefull) example out of this.
#
# 

from Foundation import NSScanner

obj = NSScanner.scannerWithString_(u"1.2 2.4")
converted, value =  obj.scanDouble_()
print 'converted: %d, value: %s'%(converted, value)
converted, value =  obj.scanFloat_()
print 'converted: %d, value: %s'%(converted, value)
print 'obj.retainCount:', obj.retainCount()
