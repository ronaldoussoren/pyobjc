#include "OC_PythonDictionary.h"
#include "OC_PythonArray.h"
#include "pyobjc.h"
#include "objc_support.h"

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
+newWithPythonObject:(PyObject*)value;
-initWithPythonObject:(PyObject*)value;
-(void)dealloc;

-(id)nextObject;

@end /* interface OC_PythonDictionaryEnumerator */

@implementation OC_PythonDictionaryEnumerator

+newWithPythonObject:(PyObject*)v;
{
	OC_PythonDictionaryEnumerator* res = 
		[[OC_PythonDictionaryEnumerator alloc] initWithPythonObject:v];
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
	Py_XDECREF(value);
}

-(id)nextObject
{
	PyObject* v;
	id result;
	int err;

	do {
		if (cur >= len) return nil;

		v = PySequence_Fast_GET_ITEM(value, cur++);
		err = depythonify_c_value("@", v, &result);
		if (err == -1) {
			PyObjCErr_ToObjC();
			return NULL;
		}

		if (result == nil) {
			NSLog(@"OC_PythonDictionaryEnumerator: Python dict with None as key");
		}

	} while (result == nil);

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
	Py_XDECREF(value);
}

-(PyObject*)__pyobjc_PythonObject__
{
	Py_INCREF(value);
	return value;
}

-(int)count
{
	return PyDict_Size(value);
}

-objectForKey:key
{
	PyObject* v;
	PyObject* k;
	id result;
	int err;

	k = pythonify_c_value("@", &key);
	if (k == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	v = PyDict_GetItem(value, k);

	if (!v) {
	  Py_DECREF(k);
	  return nil;
	}

	err = depythonify_c_value("@", v, &result);
	Py_DECREF(k);
	if (err == -1) {
		PyObjCErr_ToObjC();
		return nil;
	}
	return result;
}


-(void)setObject:val forKey:key
{
	PyObject* v;
	PyObject* k;

	v = pythonify_c_value("@", &val);
	if (v == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	k = pythonify_c_value("@", &key);
	if (k == NULL) {
		Py_DECREF(v);
		PyObjCErr_ToObjC();
		return;
	}

	if (PyDict_SetItem(value, k, v) < 0) {
		Py_DECREF(v);
		Py_DECREF(k);
		PyObjCErr_ToObjC();
		return;
	}
	Py_DECREF(v);
	Py_DECREF(k);
}

-(void)removeObjectForKey:key
{
	PyObject* k;

	k = pythonify_c_value("@", &key);
	if (k == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	if (PyDict_DelItem(value, k) < 0) {
		Py_DECREF(k);
		PyObjCErr_ToObjC();
		return;
	}
	Py_DECREF(k);
}

-keyEnumerator
{
	PyObject* keys = PyDict_Keys(value);
	id result = [OC_PythonDictionaryEnumerator newWithPythonObject:keys];
	Py_DECREF(keys);

	return result;
}

@end  // interface OC_PythonDictionary
