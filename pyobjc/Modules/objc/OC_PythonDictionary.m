#import "OC_PythonDictionary.h"

/*
 * OC_PythonDictionaryEnumerator - Enumerator for Python dictionaries
 *
 * This class implements an NSEnumerator for proxied Python dictionaries.
 */
@interface OC_PythonDictionaryEnumerator  : NSEnumerator
{
	OC_PythonDictionary* value;
	BOOL valid;
	int pos;
}
+ newWithWrappedDictionary:(OC_PythonDictionary*)value;
- initWithWrappedDictionary:(OC_PythonDictionary*)value;
-(void)dealloc;

-(id)nextObject;

@end /* interface OC_PythonDictionaryEnumerator */



@implementation OC_PythonDictionaryEnumerator

+newWithWrappedDictionary:(OC_PythonDictionary*)v;
{
	return [[[self alloc] initWithWrappedDictionary:v] autorelease];
}

-initWithWrappedDictionary:(OC_PythonDictionary*)v;
{
	self = [super init];
	if (!self) return nil;

	value = [v retain];
	valid = YES;
	pos = 0;
	return self;
}

-(void)dealloc
{
	[value release];
	[super dealloc];
}

-(id)nextObject
{
	id key = nil;
	if (valid) {
		valid = [value wrappedKey:&key value:nil atPosition:&pos];
	}
	return key;
}

@end // implementation OC_PythonDictionaryEnumerator


@implementation OC_PythonDictionary 

+newWithPythonObject:(PyObject*)v;
{
	OC_PythonDictionary* res = 
		[[OC_PythonDictionary alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

-initWithPythonObject:(PyObject*)v;
{
	self = [super init];
	if (!self) return nil;

	Py_INCREF(v);
	Py_XDECREF(value);
	value = v;
	return self;
}

-(void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		PyObjC_UnregisterObjCProxy(value, self);
		Py_XDECREF(value);
	
	PyObjC_END_WITH_GIL

	[super dealloc];
}

-(PyObject*)__pyobjc_PythonObject__
{
	Py_INCREF(value);
	return value;
}

-(int)count
{
	int result;

	PyObjC_BEGIN_WITH_GIL
		result = PyDict_Size(value);

	PyObjC_END_WITH_GIL

	return result;
}

-(int)depythonify:(PyObject*)v toId:(id*)datum
{
	if (depythonify_c_value(@encode(id), v, datum) == -1) {
		return -1;
	}
	if (*datum == nil) {
		*datum = [NSNull null];
	}
	return 0;
}

-objectForKey:key
{
	PyObject* v;
	PyObject* k;
	id result;

	PyObjC_BEGIN_WITH_GIL

		if (key == [NSNull null]) {
			Py_INCREF(Py_None);
			k = Py_None;
		} else {
			k = PyObjC_IdToPython(key);
			if (k == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		v = PyDict_GetItem(value, k);
		Py_DECREF(k);

		if (!v) {
			PyErr_Clear();
			PyObjC_GIL_RETURN(nil);
		}

		if ([self depythonify:v toId:&result] == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}
	
	PyObjC_END_WITH_GIL

	return result;
}


-(void)setObject:val forKey:key
{
	PyObject* v = NULL;
	PyObject* k = NULL;
	id null = [NSNull null];

	PyObjC_BEGIN_WITH_GIL
		if (val == null) {
			Py_INCREF(Py_None);
			v = Py_None;
		} else {
			v = PyObjC_IdToPython(val);
			if (v == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		if (key == null) {
			Py_INCREF(Py_None);
			k = Py_None;
		} else {
			k = PyObjC_IdToPython(key);
			if (k == NULL) {
				Py_XDECREF(v);
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		if (PyDict_SetItem(value, k, v) < 0) {
			Py_XDECREF(v);
			Py_XDECREF(k);
			PyObjC_GIL_FORWARD_EXC();
		}

		Py_DECREF(v);
		Py_DECREF(k);

	PyObjC_END_WITH_GIL
}

-(BOOL)wrappedKey:(id*)keyPtr value:(id*)valuePtr atPosition:(int*)positionPtr
{
	PyObject *pykey = NULL;
	PyObject *pyvalue = NULL;
	PyObject **pykeyptr = (keyPtr == nil) ? NULL : &pykey;
	PyObject **pyvalueptr = (valuePtr == nil) ? NULL : &pyvalue;
	PyObjC_BEGIN_WITH_GIL
		if (!PyDict_Next(value, positionPtr, pykeyptr, pyvalueptr)) {
			PyObjC_GIL_RETURN(NO);
		}
		if (keyPtr) {
			if ([self depythonify:pykey toId:keyPtr] == -1) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}
		if (valuePtr) {
			if ([self depythonify:pyvalue toId:valuePtr] == -1) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}
	PyObjC_END_WITH_GIL
	return YES;
}

-(void)removeObjectForKey:key
{
	PyObject* k;

	PyObjC_BEGIN_WITH_GIL
		if (key == [NSNull null]) {
			Py_INCREF(Py_None);
			k = Py_None;
		} else {
			k = PyObjC_IdToPython(key);
			if (k == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		if (PyDict_DelItem(value, k) < 0) {
			Py_DECREF(k);
			PyObjC_GIL_FORWARD_EXC();
		}
		Py_DECREF(k);
	
	PyObjC_END_WITH_GIL
}

-(NSEnumerator *)keyEnumerator
{
	return [OC_PythonDictionaryEnumerator newWithWrappedDictionary:self];
}

@end  // interface OC_PythonDictionary
