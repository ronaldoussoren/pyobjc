"""
This module implements a callback function that is used by the C code to
add Python special methods to Objective-C classes with a suitable interface.

This module contains no user callable code.

TODO:
- Add external interface: Framework specific modules may want to add to this.
"""
from objc import set_class_extender, selector

CONVENIENCE_METHODS = {}


CLASS_METHODS = { }

def add_convenience_methods(super_class, name, type_dict):
	"""
	Add additional methods to the type-dict of subclass 'name' of 
	'super_class'. 
	
	CONVENIENCE_METHODS is a global variable containing a mapping from
	an Objective-C selector to a Python method name and implementation.
	
	CLASS_METHODS is a global variable containing a mapping from 
	class name to a list of Python method names and implementation.

	Matching entries from both mappings are added to the 'type_dict'.
	"""
	for sel in type_dict.values():
		if not isinstance(sel, selector):
			continue
		sel = sel.selector

		if CONVENIENCE_METHODS.has_key(sel):
			v = CONVENIENCE_METHODS[sel]
			type_dict[v[0]] = v[1]
	
	if CLASS_METHODS.has_key(name):
		for name, value in CLASS_METHODS[name]:
			type_dict[name] = value

set_class_extender(add_convenience_methods)

# NOTE: the '!= 0' in the definition of the comparison function
# is there to force conversion to type 'bool' on Python releases
# that have such a type.
def __contains__(self, elem):
	print "doesContain_", elem
	return self.doesContain_(elem) != 0
def __eq__1(self, other):
	return self.isEqualTo_(other) != 0
def __eq__2(self, other):
	return self.isEqual_(other) != 0
def __ne__(self, other):
	return not (self.isEqual_(other) != 0)
def __gt__(self, other):
	return self.isGreaterThan_(other) != 0
def __ge__(self, other):
	return self.isGreaterThanOrEqualTo_(other) != 0
def __lt__(self, other):
	return self.isLessThan_(other) != 0
def __le__(self, other):
	return self.isLessThanOrEqualTo_(other) != 0
def __repr__(self):
	return self.description()
def __len__1(self):
	return self.count()
def __len__2(self):
	return self.length()
def __getitem__1(self, key):
	res = self.objectForKey_(key)
	if res == None:
		raise KeyError, key
	return res
def __delitem__1(self, key):
	self.removeObjectForKey_(key)
def __setitem__1(self, key, value):
	self.setObject_forKey_(value, key)
def __getitem__2(self, idx):
	res = self.objectAtIndex_(idx)
	if res == None:
		raise IndexError, idx
	return res
def __delitem__2(self, idx):
	self.removeObjectAtIndex_(idx)
def __setitem__2(self, idx, value):
	self.replaceObjectAtIndex_withObject_(idx, value)
def __hash__(self):
	return self.hash()
		

CONVENIENCE_METHODS['objectForKey:'] = ('__getitem__', __getitem__1)
CONVENIENCE_METHODS['removeObjectForKey:'] = ('__delitem__', __delitem__1)
CONVENIENCE_METHODS['setObject:forKey:'] = ('__setitem__', __setitem__1)
CONVENIENCE_METHODS['count'] = ('__len__', __len__1)
CONVENIENCE_METHODS['description'] = ('__repr__', __repr__)
CONVENIENCE_METHODS['doesContain:'] = ('__contains__', __contains__)
CONVENIENCE_METHODS['hash'] = ('__hash__', __hash__)
CONVENIENCE_METHODS['isEqualTo:'] = ('__eq__', __eq__1)
CONVENIENCE_METHODS['isEqual:'] = ('__eq__', __eq__2)
CONVENIENCE_METHODS['isGreaterThan:'] = ('__gt__', __gt__)
CONVENIENCE_METHODS['isGreaterThanOrEqualTo:'] = ('__ge__', __ge__)
CONVENIENCE_METHODS['isLessThan:'] = ('__lt__', __lt__)
CONVENIENCE_METHODS['isLessThanOrEqualTo:'] = ('__le__', __le__)
CONVENIENCE_METHODS['isNotEqualTo:'] = ('__ne__', __ne__)
CONVENIENCE_METHODS['lenght'] = ('__len__', __len__2)
CONVENIENCE_METHODS['objectAtIndex:'] = ('__getitem__', __getitem__2)
CONVENIENCE_METHODS['removeObjectAtIndex:'] = ('__detitem__', __delitem__2)
CONVENIENCE_METHODS['replaceObjectAtIndex:withObject:'] = ('__setitem__', __setitem__2)



# Mapping protocol


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

# Mappings (e.g. like dict)
# TODO (not all are needed or even possible): 
#   iter*, update, pop, popitem, setdefault
# __str__ would be nice (as obj.description()),
CONVENIENCE_METHODS['keyEnumerator'] = ('keys', mapping_keys)
CONVENIENCE_METHODS['objectEnumerator'] = ('values', mapping_values)
CONVENIENCE_METHODS['removeAllObjects'] = ('clear', lambda self: self.removeAllObjects())
CONVENIENCE_METHODS['dictionaryWithDictionary:'] = ('copy', lambda self: type(self).dictionaryWithDictionary_(self))
