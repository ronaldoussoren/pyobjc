#import "OC_PythonDictionary.h"

static void
nsmaptable_python_retain(NSMapTable *table __attribute__((__unused__)), const void *datum) {
	Py_INCREF((PyObject *)datum);
}

static void
nsmaptable_python_release(NSMapTable *table __attribute__((__unused__)), void *datum) {
	Py_DECREF((PyObject *)datum);
}

static void
nsmaptable_objc_retain(NSMapTable *table __attribute__((__unused__)), const void *datum) {
	[(id)datum retain];
}

static void
nsmaptable_objc_release(NSMapTable *table __attribute__((__unused__)), void *datum) {
	[(id)datum release];
}

static
NSMapTableKeyCallBacks PyObjC_ObjectToIdTable_KeyCallBacks = {
	NULL, // use pointer value for hash
	NULL, // use pointer value for equality
	&nsmaptable_python_retain,
	&nsmaptable_python_release,
	NULL, // generic description
	NULL // not a key
};

static
NSMapTableValueCallBacks PyObjC_ObjectToIdTable_ValueCallBacks = {
	&nsmaptable_objc_retain,
	&nsmaptable_objc_release,
	NULL  // generic description
};




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
	if (table) {
		NSResetMapTable(table);
	} else {
		table = NSCreateMapTable(PyObjC_ObjectToIdTable_KeyCallBacks, PyObjC_ObjectToIdTable_ValueCallBacks, [self count]);
	}
	NSMapInsert(table, (const void *)Py_None, (const void *)[NSNull null]);
	return self;
}

-(void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		Py_XDECREF(value);
		if (table) {
			NSFreeMapTable(table);
		}
	
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
	if (!(*datum = (id)NSMapGet(table, (const void *)v))) {
		if (depythonify_c_value(@encode(id), v, datum) == -1) {
			return -1;
		}
		NSMapInsert(table, (const void *)v, (const void *)*datum);
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

-keyEnumerator
{
	return [OC_PythonDictionaryEnumerator newWithWrappedDictionary:self];
}

@end  // interface OC_PythonDictionary
