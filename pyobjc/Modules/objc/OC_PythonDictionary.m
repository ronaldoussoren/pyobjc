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
	value = PySequence_Fast(v, 
		"pyObject of OC_PythonDictionaryEnumerator must be a sequence");
	cur   = 0;
	len = PySequence_Fast_GET_SIZE(value);
	return self;
}

-(void)dealloc
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_XDECREF(value);
	PyGILState_Release(state);
}

-(id)nextObject
{
	PyObject* v;
	id result;
	int err;

	PyGILState_STATE state = PyGILState_Ensure();

	do {
		if (cur >= len) {
			PyGILState_Release(state);
			return nil;
		}

		v = PySequence_Fast_GET_ITEM(value, cur++);
		err = depythonify_c_value("@", v, &result);
		if (err == -1) {
			PyObjCErr_ToObjCWithGILState(&state);
			return nil;
		}

		if (result == nil) {
			NSLog(@"OC_PythonDictionaryEnumerator: Python dict with None as key, skipping this key");
			continue;
		}

	} while (result == nil);

	PyGILState_Release(state);

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
	value = v;
	Py_INCREF(v);
	return self;
}

-(void)dealloc
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_XDECREF(value);
	value = NULL;
	PyGILState_Release(state);

	[super dealloc];
}

-(PyObject*)__pyobjc_PythonObject__
{
	Py_INCREF(value);
	return value;
}

-(int)count
{
	PyGILState_STATE state = PyGILState_Ensure();
	int result = PyDict_Size(value);
	PyGILState_Release(state);
	return result;
}

-objectForKey:key
{
	PyObject* v;
	PyObject* k;
	id result;
	int err;
	PyGILState_STATE state = PyGILState_Ensure();

	k = pythonify_c_value("@", &key);
	if (k == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	v = PyDict_GetItem(value, k);

	if (!v) {
		Py_DECREF(k);
		PyErr_Clear();
		PyGILState_Release(state);
		return nil;
	}

	err = depythonify_c_value("@", v, &result);
	Py_DECREF(k);
	if (err == -1) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}
	PyGILState_Release(state);
	return result;
}


-(void)setObject:val forKey:key
{
	PyObject* v = NULL;
	PyObject* k = NULL;
	PyGILState_STATE state = PyGILState_Ensure();

	v = pythonify_c_value("@", &val);
	if (v == NULL) goto error;

	k = pythonify_c_value("@", &key);
	if (k == NULL) goto error;

	if (PyDict_SetItem(value, k, v) < 0) goto error;

	Py_DECREF(v);
	Py_DECREF(k);
	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(v);
	Py_XDECREF(k);
	PyObjCErr_ToObjCWithGILState(&state);
}

-(void)removeObjectForKey:key
{
	PyObject* k;
	PyGILState_STATE state = PyGILState_Ensure();

	k = pythonify_c_value("@", &key);
	if (k == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	if (PyDict_DelItem(value, k) < 0) {
		Py_DECREF(k);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	Py_DECREF(k);
	PyGILState_Release(state);
}

-keyEnumerator
{
	PyObject* keys;
	id result;
	PyGILState_STATE state = PyGILState_Ensure();

	keys = PyDict_Keys(value);
	result = [OC_PythonDictionaryEnumerator newWithPythonObject:keys];
	Py_DECREF(keys);

	PyGILState_Release(state);

	return result;
}

@end  // interface OC_PythonDictionary
