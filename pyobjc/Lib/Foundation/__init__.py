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


def NSStringFromClass(aClass):
	return aClass.__name__

# Define usefull utility methods here

def load_bundle(path):
	"""
	Load the specified bundle/framework and return a list of classes 
	defined in that bundle/framework
	"""
	bundle_class = _objc.lookup_class('NSBundle')
	# print "Bundle-class = ", bundle_class
	bndl = bundle_class.bundleWithPath_(path)
	# print "Bundle = ", bndl, path
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

from types import *
def propertyListFromPythonCollection(aPyCollection, conversionHelper=None):
	containerType = type(aPyCollection)
	if containerType == DictType:
		collection = NSMutableDictionary.dictionary()
		for aKey in aPyCollection:
			convertedValue = propertyListFromPythonCollection( aPyCollection[aKey], conversionHelper=conversionHelper )
			collection.setObject_forKey_( convertedValue , aKey )
		return collection
	elif containerType in [TupleType, ListType]:
		collection = NSMutableArray.array()
		for aValue in aPyCollection:
			convertedValue = propertyListFromPythonCollection( aValue, conversionHelper=conversionHelper )
			collection.addObject_( convertedValue  )
		return collection
	elif containerType in StringTypes:
		return aPyCollection # bridge will convert to NSString
	elif containerType == IntType:
		return NSNumber.numberWithInt_( aPyCollection )
	elif containerType == LongType:
		return NSNumber.numberWithLong_( aPyCollection )
	elif containerType == FloatType:
		return NSNumber.numberWithFloat_( aPyCollection )
	elif containerType == NoneType:
		return NSNull.null()
	else:
		if conversionHelper:
			return conversionHelper(aPyCollection)
		raise "UnrecognizedTypeException", "Type %s encountered in python collection;  don't know how to convert." % containerType

# def pythonCollectionFromPropertyList(aPropertyList):
#	elementClass = aPropertyList.
#
# How do I figure out if [aPropertyList isKindOfClass: [NSDictionary class]]??
