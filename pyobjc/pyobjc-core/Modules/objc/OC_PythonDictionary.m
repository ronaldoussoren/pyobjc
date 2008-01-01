/*
 * NOTE: the implementation uses PyDict_* APIs whenever possible and falls
 * back to the generic PyObject_* APIs otherwise. We don't use the PyMapping_*
 * APIs because those are incomplete(!).
 */
#include "pyobjc.h"
#import "OC_PythonDictionary.h"

static PyObject* mapTypes = NULL;

/*
 * OC_PythonDictionaryEnumerator - Enumerator for Python dictionaries
 *
 * This class implements an NSEnumerator for proxied Python dictionaries.
 */
@interface OC_PythonDictionaryEnumerator : NSEnumerator
{
	OC_PythonDictionary* value;
	BOOL valid;
	Py_ssize_t pos;
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
	if (unlikely(self == nil)) return nil;

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

+ depythonifyObject:(PyObject*)object
{
	Py_ssize_t i, len;
	
	if (mapTypes == NULL) return NULL;

	len = PyList_GET_SIZE(mapTypes);

	for (i = 0; i < len; i++) {
		PyObject* tp = PyList_GET_ITEM(mapTypes, i);
		int r = PyObject_IsInstance(object, tp);
		if (r == -1) {
			return NULL;
		}

		if (!r) continue;

		/* Instance of this type should be pythonifyed as a sequence */
		return [OC_PythonArray newWithPythonObject:object];
	}

	return NULL;
}

+ depythonifyTable
{
	NSObject* result; 

	PyObjC_BEGIN_WITH_GIL

		if (mapTypes == NULL) {
			mapTypes = PyList_New(0);
			if (mapTypes == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}
		result = PyObjC_PythonToId(mapTypes);
		if (result == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

	PyObjC_END_WITH_GIL

	return result;
}

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
	if (unlikely(self == nil)) return nil;

	Py_INCREF(v);
	Py_XDECREF(value);
	value = v;
	return self;
}

-(void)release
{
	/* See comment in OC_PythonUnicode */
	PyObjC_BEGIN_WITH_GIL
		[super release];
	PyObjC_END_WITH_GIL
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

-(NSUInteger)count
{
	Py_ssize_t result;

	PyObjC_BEGIN_WITH_GIL
		if (likely(PyDict_CheckExact(value))) {
			result = PyDict_Size(value);
		} else {
			result = PyObject_Length(value);
		}

	PyObjC_END_WITH_GIL

	if (sizeof(Py_ssize_t) > sizeof(NSUInteger)) {
		if (result > (Py_ssize_t)NSUIntegerMax) {
			return NSUIntegerMax;
		}
	}
	return result;
}

-(int)depythonify:(PyObject*)v toId:(id*)datum
{
	if (unlikely(depythonify_c_value(@encode(id), v, datum) == -1)) {
		return -1;
	}
	if (unlikely(*datum == nil)) {
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

		if (unlikely(key == [NSNull null])) {
			Py_INCREF(Py_None);
			k = Py_None;
		} else {
			k = PyObjC_IdToPython(key);
			if (k == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		if (likely(PyDict_CheckExact(value))) {
			v = PyDict_GetItem(value, k);
			Py_XINCREF(v);
		} else {
			v = PyObject_GetItem(value, k);
		}
		Py_DECREF(k);

		if (unlikely(v == NULL)) {
			PyErr_Clear();
			PyObjC_GIL_RETURN(nil);
		}

		if (unlikely([self depythonify:v toId:&result] == -1)) {
			Py_DECREF(v);
			PyObjC_GIL_FORWARD_EXC();
		}
		Py_DECREF(v);
	
	PyObjC_END_WITH_GIL

	return result;
}


-(void)setObject:val forKey:key
{
	PyObject* v = NULL;
	PyObject* k = NULL;
	id null = [NSNull null];

	PyObjC_BEGIN_WITH_GIL
		if (unlikely(val == null)) {
			Py_INCREF(Py_None);
			v = Py_None;
		} else {
			v = PyObjC_IdToPython(val);
			if (unlikely(v == NULL)) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		if (unlikely(key == nil)) {
			Py_INCREF(Py_None);
			k = Py_None;
		} else {
			k = PyObjC_IdToPython(key);
			if (k == NULL) {
				Py_XDECREF(v);
				PyObjC_GIL_FORWARD_EXC();
			}
		}
		
		if (likely(PyDict_CheckExact(value))) {
			if (unlikely(PyDict_SetItem(value, k, v) < 0)) {
				Py_XDECREF(v);
				Py_XDECREF(k);
				PyObjC_GIL_FORWARD_EXC();
			}

		} else {
			if (unlikely(PyObject_SetItem(value, k, v) < 0)) {
				Py_XDECREF(v);
				Py_XDECREF(k);
				PyObjC_GIL_FORWARD_EXC();
			}

		}

		Py_DECREF(v);
		Py_DECREF(k);

	PyObjC_END_WITH_GIL
}

-(BOOL)wrappedKey:(id*)keyPtr value:(id*)valuePtr atPosition:(Py_ssize_t*)positionPtr
{
	PyObject *pykey = NULL;
	PyObject *pyvalue = NULL;
	PyObject **pykeyptr = (keyPtr == nil) ? NULL : &pykey;
	PyObject **pyvalueptr = (valuePtr == nil) ? NULL : &pyvalue;

	PyObjC_BEGIN_WITH_GIL
		if (unlikely(!PyDict_Next(value, positionPtr, pykeyptr, pyvalueptr))) {
			PyObjC_GIL_RETURN(NO);
		}
		if (keyPtr) {
			if (unlikely([self depythonify:pykey toId:keyPtr] == -1)) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}
		if (likely(valuePtr)) {
			if (unlikely([self depythonify:pyvalue toId:valuePtr] == -1)) {
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
		if (unlikely(key == [NSNull null])) {
			Py_INCREF(Py_None);
			k = Py_None;
		} else {
			k = PyObjC_IdToPython(key);
			if (unlikely(k == NULL)) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		if (PyDict_CheckExact(value)) {
			if (unlikely(PyDict_DelItem(value, k) < 0)) {
				Py_DECREF(k);
				PyObjC_GIL_FORWARD_EXC();
			}
		} else {
			if (unlikely(PyObject_DelItem(value, k) < 0)) {
				Py_DECREF(k);
				PyObjC_GIL_FORWARD_EXC();
			}
		}
		Py_DECREF(k);
	
	PyObjC_END_WITH_GIL
}

-(NSEnumerator *)keyEnumerator
{
	if (PyDict_CheckExact(value)) {
		return [OC_PythonDictionaryEnumerator newWithWrappedDictionary:self];
	} else {
		PyObjC_BEGIN_WITH_GIL
			PyObject* keys = PyObject_CallMethod(value, "keys", NULL);
			if (keys == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}

			PyObject* iter = PyObject_GetIter(keys);
			Py_DECREF(keys);
			if (iter == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}

			NSEnumerator* result = [OC_PythonEnumerator newWithPythonObject:iter];
			PyObjC_GIL_RETURN(result);

		PyObjC_END_WITH_GIL
	}
}


- (void)encodeWithCoder:(NSCoder*)coder
{
	/* 
	 * Forcefully disable coding for now, to avoid generating invalid
	 * encoded streams.
	 */        
	[NSException raise:NSInvalidArgumentException format:@"PyObjC: Encoding python objects of type %s is not supported", value->ob_type->tp_name, coder];
}

- initWithCoder:(NSCoder*)coder
{
	[NSException raise:NSInvalidArgumentException format:@"PyObjC: Decoding python objects is not supported", coder];
	return nil;
}

@end  // interface OC_PythonDictionary
