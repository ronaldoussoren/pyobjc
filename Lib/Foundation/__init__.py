import objc as _objc

from _Foundation import *

NSClassFromString = _objc.lookup_class

# Do something smart to collect Foundation classes...

NSBundle = _objc.lookup_class('NSBundle')

# We use strings to represent selectors, therefore 
# NSSelectorFromString and NSStringFromSelector are no-ops (for now)
def NSSelectorFromString(aSelectorName):
	if not isinstance(aSelectorName, str):
		raise TypeError, "aSelector must be string"

	return aSelectorName

NSStringFromSelector = NSSelectorFromString


def NSClassFromString(aClass):
	return aClass.__name__




# Define usefull utility methods here

def load_bundle(path):
	"""
	Load the specified bundle/framework and return a list of classes 
	defined in that bundle/framework
	"""
	bundle_class = _objc.lookup_class('NSBundle')
	print "Bundle-class = ", bundle_class
	bndl = bundle_class.bundleWithPath_(path)
	print "Bundle = ", bndl, path
	bndl.load()
	classes = [ cls 
			for cls in _objc.class_list() 
			if path == bundle_class.bundleForClass_(cls).bundlePath() ]
	return classes

class_list = load_bundle('/System/Library/Frameworks/Foundation.framework')
gl = globals()
for cls in class_list:
	gl[cls.__name__] = cls

del class_list
del cls
del gl

# Define usefull utility methods here
