from __future__ import generators

"""
This module implements a callback function that is used by the C code to
add Python special methods to Objective-C classes with a suitable interface.

This module contains no user callable code.

TODO:
- Add external interface: Framework specific modules may want to add to this.
"""
from objc import set_class_extender, selector, runtime

CONVENIENCE_METHODS = {}
CLASS_METHODS = {}

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
			for name, value in v:
				type_dict[name] = value
	
	if CLASS_METHODS.has_key(name):
		for name, value in CLASS_METHODS[name]:
			type_dict[name] = value

set_class_extender(add_convenience_methods)

# NOTE: the '!= 0' in the definition of the comparison function
# is there to force conversion to type 'bool' on Python releases
# that have such a type.

def __getitem__objectForKey(self, key):
	res = self.objectForKey_(key)
	if res is None:
		raise KeyError, key
	return res
def has_key_objectForKey(self, key):
	res = self.objectForKey_(key)
	return not (res is None)
def get_objectForKey(self, key, dflt=None):
	res = self.objectForKey_(key)
	if res is None: 
		res = dflt
	return res
CONVENIENCE_METHODS['objectForKey:'] = (('__getitem__', __getitem__objectForKey),
					('has_key', has_key_objectForKey),
					('get', get_objectForKey),
					('__contains__', lambda self, elem: (self.objectForKey_(elem) != None)
					 ))

CONVENIENCE_METHODS['removeObjectForKey:'] = (('__delitem__',
					       lambda self, key: self.removeObjectForKey_( key ) ), )

CONVENIENCE_METHODS['setObject:forKey:'] = (('__setitem__',
					     lambda self, key, value: self.setObject_forKey_( value, key ) ), )

CONVENIENCE_METHODS['count'] = (('__len__',
				 lambda self: self.count() ),)

CONVENIENCE_METHODS['description'] = (('__repr__',
				       lambda self: self.description() ),)

CONVENIENCE_METHODS['containsObject:'] = (('__contains__',
					   lambda self, elem: (self.containsObject_(elem) != 0)),)

CONVENIENCE_METHODS['hash'] = (('__hash__',
				lambda self: self.hash() ),)

CONVENIENCE_METHODS['isEqualTo:'] = (('__eq__',
				      lambda self, other: self.isEqualTo_( other ) ),)

CONVENIENCE_METHODS['isEqual:'] = (('__eq__',
				    lambda self, other: self.isEqual_( other ) ),)

CONVENIENCE_METHODS['isGreaterThan:'] = (('__gt__',
					  lambda self, other: self.isGreaterThan_( other ) ),)

CONVENIENCE_METHODS['isGreaterThanOrEqualTo:'] = (('__ge__',
						   lambda self, other: self.isGreaterThanOrEqualTo_( other ) ),)

CONVENIENCE_METHODS['isLessThan:'] = (('__lt__',
				       lambda self, other: self.isLessThan_( other ) ),)

CONVENIENCE_METHODS['isLessThanOrEqualTo:'] = (('__le__',
						lambda self, other: self.isLessThanOrEqualTo_( other ) ),)

CONVENIENCE_METHODS['isNotEqualTo:'] = (('__ne__',
					 lambda self, other: self.isNotEqualTo_( other ) ),)

CONVENIENCE_METHODS['length'] = (('__len__',
				  lambda self: self.length() ),)

def __getitem__objectAtIndexWithSlice(self, x, y):
	l = len(self)
	r = y - x
	if r < 0:
		return []
	if (r - x) > l:
		r = l - x
	return self.subarrayWithRange_( (x, r) )
CONVENIENCE_METHODS['objectAtIndex:'] = (('__getitem__', lambda self, index: self.objectAtIndex_( index )),
					 ('__getslice__', __getitem__objectAtIndexWithSlice) )

def __delslice__removeObjectAtIndex(self, x, y):
	l = len(self)
	r = y - x
	if r < 0:
		return
	if (r - x) > l:
		r = l - x
	return self.removeObjectsInRange_( (x, r) )
	
CONVENIENCE_METHODS['removeObjectAtIndex:'] = (('__delitem__', lambda self, index: self.removeObjectAtIndex_( index )),
					       ('__delslice__', __delslice__removeObjectAtIndex ) )

CONVENIENCE_METHODS['replaceObjectAtIndex:withObject:'] = (('__setitem__',
							    lambda self, index, anObject: self.replaceObjectAtIndex_withObject_( index, anObject) ),)

def __setslice__replaceObjectAtIndex_withObject(self, x, y, v):
	l = len(self)
	r = y - x
	if r < 0:
		return
	if (r - x) > l:
		r = l - x
	return self.replaceObjectsInRange_withObjectsFromArray_( (x, r), v )
CONVENIENCE_METHODS['replaceObjectsInRange:withObjectsFromArray:'] = (('__setslice__', __setslice__replaceObjectAtIndex_withObject), )

# Mapping protocol

# Mappings (e.g. like dict)
# TODO (not all are needed or even possible): 
#   iter*, update, pop, popitem, setdefault
# __str__ would be nice (as obj.description()),

def enumeratorGenerator(anEnumerator):
	nextObject = anEnumerator.nextObject()
	while (nextObject):
		yield nextObject
		nextObject = anEnumerator.nextObject()

CONVENIENCE_METHODS['keyEnumerator'] = (('keys',
					 lambda self: self.allKeys()),

					('__iter__',
					 lambda self: enumeratorGenerator( self.keyEnumerator() ) ),

					('iterkeys',
					 lambda self: enumeratorGenerator( self.keyEnumerator() ) ) )

CONVENIENCE_METHODS['objectEnumerator'] = (('values', lambda self: self.allValues()),)
CONVENIENCE_METHODS['removeAllObjects'] = (('clear', lambda self: self.removeAllObjects()),)
CONVENIENCE_METHODS['dictionaryWithDictionary:'] = (('copy', lambda self: type(self).dictionaryWithDictionary_(self)),)
