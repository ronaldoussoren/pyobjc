"""
new-style pyobjc
"""
from _objc import *
from _objc import __version__

# Backward compat stuff, Python 2.2.0 doesn't have 'True' and 'False'
try:
	getattr(__builtins__, 'True')
except AttributeError:
	True=1
	False=0

# This is a hack, should probably patch python:
# - We want the resources directory to be on the python search-path
# - It must be at the start of the path
# - The CWD must not be on the path
b = lookup_class('NSBundle').mainBundle()
if b:
	import sys
	sys.path.insert(0, '%s/Contents/Resources'%str(b.bundlePath()))
	try:
		del sys.path[sys.path.index('')]
	except ValueError:
		pass
	del sys
del b


#
# Administration of methods that transfer ownership of objects to the
# caller. This list is used by the runtime to automaticly correct the
# refcount to the object.
#
# These must be set before any proxy classes are created.
#
# These 5 are documented in Apple's Objective-C book, in theory these
# are the only methods that transfer ownership.
ALLOCATOR_METHODS['alloc'] = True
ALLOCATOR_METHODS['allocWithZone:'] = True
ALLOCATOR_METHODS['copy'] = True
ALLOCATOR_METHODS['copyWithZone:'] = True
ALLOCATOR_METHODS['mutableCopyWithZone:'] = True

# Some special modules needed to correctly wrap all
# methods in the Foundation framework. Doing it here
# is ugly, but it is also something that would be very
# hard to avoid...
try:
	import _FoundationSignatures
	del _FoundationSignatures
except ImportError:
	pass

try:
	import _FoundationMapping
	del _FoundationMapping
except ImportError:
	pass


# Add usefull utility functions below


class _runtime:
	"""
	Backward compatibility interface.
	"""
	def __getattr__(self, name):
		if name == '__objc_classes__':
			return class_list()
		elif name == '__kind__':
			return 'python'

		return lookup_class(name)

	def __eq__(self, other):
		if self is other:
			return True
		return False

	def __repr__(self):
		return "objc.runtime"
runtime = _runtime()

# Outlets in Interface Builder are instance variables
IBOutlet = ivar

# Signature for an action in Interface Builder
#IBAction = "v@:"
def IBAction(func):
	return selector(func, signature="v@:@")

# Aliases for Objective-C lovers...
YES=True
NO=False
nil=None



#
# Below here are definitions of convenience methods
# for Objective-C classes. The C-code uses 'CONVENIENCE_METHODS' to
# locate methods it should add to newly constructed class-wrappers.
#
# This is basically used to map objective-C methodnames to corresponding
# python method names.
#
# TODO: Change interfaces, we sometimes want to add more than one wrapper
# method if a method is present (like dict.keys and dict.iterkeys)
#

def mapping_keys(self):
	"""
	NSDictionary.keys()
	"""
	enum = self.keyEnumerator()
	result = []
	key = enum.nextObject()
	while key:
		result.append(key)
		key = enum.nextObject()
	return result

def mapping_values(self):
	"""
	NSDictionary.values()
	"""
	enum = self.objectEnumerator()
	result = []
	value = enum.nextObject()
	while value:
		result.append(value)
		value = enum.nextObject()
	return result

#CONVENIENCE_METHODS['description'] = ('__repr__', lambda self: self.description())
# Mappings (e.g. like dict)
# TODO (not all are needed or even possible): 
#   iter*, update, pop, popitem, setdefault
# __str__ would be nice (as obj.description()),
CONVENIENCE_METHODS['objectForKey:'] = ('__getitem__', lambda self, arg: self.objectForKey_(arg))
CONVENIENCE_METHODS['removeObjectForKey:'] = ('__delitem__', lambda self, arg: self.removeObjectForKey_(arg))
CONVENIENCE_METHODS['setObject:forKey:'] = ('__setitem__', lambda self, key, value: self.setObject_forKey_(value, key))
CONVENIENCE_METHODS['hash'] = ('__hash__', lambda self: self.hash())
CONVENIENCE_METHODS['keyEnumerator'] = ('keys', mapping_keys)
CONVENIENCE_METHODS['objectEnumerator'] = ('values', mapping_values)
CONVENIENCE_METHODS['removeAllObjects'] = ('clear', lambda self: self.removeAllObjects())
CONVENIENCE_METHODS['dictionaryWithDictionary:'] = ('copy', lambda self: self.isa.dictionaryWithDictionary_(self))

CONVENIENCE_METHODS['objectAtIndex:'] = ('__getitem__', lambda self, arg: self.objectAtIndex_(arg))
CONVENIENCE_METHODS['count'] = ('__len__', lambda self: self.count())
CONVENIENCE_METHODS['lenght'] = ('__len__', lambda self: self.length())

del mapping_keys, mapping_values


# From 'ComparisonMethods' protocol
CONVENIENCE_METHODS['doesContain:'] = ('__contains__', lambda self, elem: self.doesContain_(elem))
def eq_func(self, other):
	print "eq_func(%s, %s)"%(self, other)
	if self is other: return True
	return self.isEqualTo_(other)

CONVENIENCE_METHODS['isEqualTo:'] = ('__eq__', eq_func) # lambda self, other: self.isEqualTo_(other))
CONVENIENCE_METHODS['isGreaterThan:'] = ('__gt__', lambda self, other: self.isGreaterThan(other))
CONVENIENCE_METHODS['isGreaterThanOrEqualTo:'] = ('__ge__', None)
CONVENIENCE_METHODS['isLessThan:'] = ('__lt__', None)
CONVENIENCE_METHODS['isLessThanOrEqualTo:'] = ('__le__', None)
CONVENIENCE_METHODS['isNotEqualTo:'] = ('__ne__', None)


# Extra for strings, we'll probably provide C functions to do this
# correctly (dealing correctly with Unicode)
CONVENIENCE_METHODS['cString'] = (
	'__str__', lambda self: self.cString()
)

