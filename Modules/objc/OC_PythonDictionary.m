#include "pyobjc.h"

#import <Foundation/NSEnumerator.h>

/*
 * OC_PythonDictionaryEnumerator - Enumerator for Python dictionaries
 *
 * This class implements an NSEnumerator for proxied Python dictionaries.
 */
@interface OC_PythonDictionaryEnumerator  : NSEnumerator
{
	PyObject* value;
	int       cur;
	int       len;
}
+ newWithPythonObject:(PyObject*)value;
- initWithPythonObject:(PyObject*)value;
-(void)dealloc;

-(id)nextObject;

@end /* interface OC_PythonDictionaryEnumerator */



@implementation OC_PythonDictionaryEnumerator

+newWithPythonObject:(PyObject*)v;
{
	OC_PythonDictionaryEnumerator* res;

	res = [[OC_PythonDictionaryEnumerator alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

-initWithPythonObject:(PyObject*)v;
{
	self = [super init];
	if (!self) return nil;

	value = PySequence_Fast(v, 
		"pyObject of OC_PythonDictionaryEnumerator must be a sequence");
	cur   = 0;
	len = PySequence_Fast_GET_SIZE(value);
	return self;
}

-(void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		Py_XDECREF(value);

	PyObjC_END_WITH_GIL
}

-(id)nextObject
{
	PyObject* v;
	id result;
	int err;

	PyObjC_BEGIN_WITH_GIL

		do {
			if (cur >= len) {
				PyObjC_GIL_RETURN(nil);
			}

			v = PySequence_Fast_GET_ITEM(value, cur++);
			err = depythonify_c_value("@", v, &result);
			if (err == -1) {
				PyObjC_GIL_FORWARD_EXC();
			}

			if (result == nil) {
				NSLog(@"OC_PythonDictionaryEnumerator: Python dict with None as key, skipping this key");
				continue;
			}

		} while (result == nil);

	PyObjC_END_WITH_GIL

	return result;
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
		Py_XDECREF(value);
		value = NULL;
	
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

-objectForKey:key
{
	PyObject* v;
	PyObject* k;
	id result;
	int err;

	PyObjC_BEGIN_WITH_GIL

		k = pythonify_c_value("@", &key);
		if (k == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		v = PyDict_GetItem(value, k);
		Py_DECREF(k);

		if (!v) {
			PyErr_Clear();
			PyObjC_GIL_RETURN(nil);
		}

		err = depythonify_c_value("@", v, &result);
		if (err == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}
	
	PyObjC_END_WITH_GIL

	return result;
}


-(void)setObject:val forKey:key
{
	PyObject* v = NULL;
	PyObject* k = NULL;

	PyObjC_BEGIN_WITH_GIL
		v = PyObjC_IdToPython(val);
		if (v == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		k = PyObjC_IdToPython(key);
		if (k == NULL) {
			Py_XDECREF(v);
			PyObjC_GIL_FORWARD_EXC();
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

-(void)removeObjectForKey:key
{
	PyObject* k;

	PyObjC_BEGIN_WITH_GIL
		k = PyObjC_IdToPython(key);
		if (k == NULL) {
			PyObjC_GIL_FORWARD_EXC();
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
	PyObject* keys;
	id result;

	PyObjC_BEGIN_WITH_GIL
		keys = PyDict_Keys(value);
		if (keys == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}
		result = [OC_PythonDictionaryEnumerator 
				newWithPythonObject:keys];
		Py_DECREF(keys);

	PyObjC_END_WITH_GIL

	return result;
}

@end  // interface OC_PythonDictionary
