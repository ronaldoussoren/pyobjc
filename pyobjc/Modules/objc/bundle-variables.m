/*
 * This module exports a function to load variables in a bundle
 *
 * NOTE: The interface is specified with NSBundles, but we have to 
 * use CFBundles in the implementation. This is not portable to GNUstep :-(
 */
#include "pyobjc.h"

#include <CoreFoundation/CoreFoundation.h>
#import <Foundation/NSBundle.h>
#import <Foundation/NSURL.h>

/* XXX: this should be somewhere else */
static int
PyObjCObject_Convert(PyObject* object, void* pvar)
{
	id* pid = (id*)pvar;

	*pid = PyObjC_PythonToId(object);

	if (PyErr_Occurred()) {
		return 0;
	} 
	return 1;
}


static CFBundleRef 
NSBundle2CFBundle(NSBundle* bundle)
{
	CFURLRef bundleURL;

	bundleURL = (CFURLRef)[NSURL fileURLWithPath:[bundle bundlePath]];
	return CFBundleCreate(
			kCFAllocatorDefault,
			bundleURL);
}


PyObject* PyObjC_loadBundleVariables(PyObject* self __attribute__((__unused__)),
		PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "bundle", "module_globals", "variableInfo", "skip_undefined", NULL };
	NSBundle*	bundle;
	PyObject*	module_globals;
	PyObject*	variableInfo;
	int		skip_undefined = 1;
	CFBundleRef	cfBundle;
	PyObject*       seq;
	int		i, len;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&OO|i",
			keywords, PyObjCObject_Convert, &bundle,
			&module_globals, &variableInfo, &skip_undefined)) {
		return NULL;
	}


	NS_DURING
		cfBundle = NSBundle2CFBundle(bundle);	
	
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		NS_VALUERETURN(NULL, PyObject*);

	NS_ENDHANDLER

	if (cfBundle == NULL) {
		PyErr_Format(PyObjCExc_Error, 
			"Cannot convert NSBundle to CFBundle");
		return NULL;
	}

	seq = PySequence_Fast(variableInfo, "variableInfo not a sequence");
	if (seq == NULL) {
		return NULL;
	}

	len = PySequence_Fast_GET_SIZE(seq);
	for (i = 0; i < len; i++) {
		PyObject* item = PySequence_Fast_GET_ITEM(seq, i);
		void*		value;
		char*		signature;
		NSString*	name;

		if (!PyTuple_Check(item)) {
			PyErr_Format(PyExc_TypeError,
				"item %d has type %s not tuple",
				i, item->ob_type->tp_name);
			Py_DECREF(seq);
			return NULL;
		}

		if (!PyArg_ParseTuple(item, "O&s:variableInfo", 
				PyObjCObject_Convert, &name, &signature)) {
			Py_DECREF(seq);
			return NULL;
		}

		if (![name isKindOfClass:[NSString class]]) {
			PyErr_SetString(PyExc_TypeError,
					"variable name not a string");
			Py_DECREF(seq);
			return NULL;
		}

		value = CFBundleGetDataPointerForName(cfBundle, 
				(CFStringRef)name);
		if (value == NULL) {
			if (!skip_undefined) {
				PyErr_SetString(PyObjCExc_Error,
					"cannot find a variable"); // XXX
				Py_DECREF(seq);
				return NULL;
			}
		} else {
			PyObject* pyVal = pythonify_c_value(signature, value);
			if (pyVal == NULL) {
				Py_DECREF(seq);
				return NULL;
			}

			if (PyDict_SetItemString(module_globals, 
					[name UTF8String], pyVal) == -1) {
				Py_DECREF(seq);
				Py_DECREF(pyVal);
				return NULL;
			}
			Py_DECREF(pyVal);
		}
	}
	Py_DECREF(seq);
	Py_INCREF(Py_None);
	return Py_None;
}

PyObject* PyObjC_loadBundleFunctions(PyObject* self __attribute__((__unused__)),
		PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "bundle", "module_globals", "variableInfo", "skip_undefined", NULL };
	NSBundle*	bundle;
	PyObject*	module_globals;
	PyObject*	functionInfo;
	int		skip_undefined = 1;
	CFBundleRef	cfBundle;
	PyObject*       seq;
	int		i, len;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&OO|i",
			keywords, PyObjCObject_Convert, &bundle,
			&module_globals, &functionInfo, &skip_undefined)) {
		return NULL;
	}


	NS_DURING
		cfBundle = NSBundle2CFBundle(bundle);	
	
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		NS_VALUERETURN(NULL, PyObject*);

	NS_ENDHANDLER

	if (cfBundle == NULL) {
		PyErr_Format(PyObjCExc_Error, 
			"Cannot convert NSBundle to CFBundle");
		return NULL;
	}

	seq = PySequence_Fast(functionInfo, "functionInfo not a sequence");
	if (seq == NULL) {
		return NULL;
	}

	len = PySequence_Fast_GET_SIZE(seq);
	for (i = 0; i < len; i++) {
		PyObject* item = PySequence_Fast_GET_ITEM(seq, i);
		void*		value;
		char*		signature;
		NSString*	name;
		PyObject*	doc;
		PyObject*	py_name;

		if (!PyTuple_Check(item)) {
			PyErr_Format(PyExc_TypeError,
				"item %d has type %s not tuple",
				i, item->ob_type->tp_name);
			Py_DECREF(seq);
			return NULL;
		}

		doc = NULL;
		if (!PyArg_ParseTuple(item, "Ss|S:functionInfo", 
				&py_name, &signature, &doc)){
			Py_DECREF(seq);
			return NULL;
		}

		name = PyObjC_PythonToId(py_name);
		if (name == NULL) {
			Py_DECREF(seq);
			return NULL;
		}


		if (![name isKindOfClass:[NSString class]]) {
			PyErr_SetString(PyExc_TypeError,
					"functionInfo name not a string");
			Py_DECREF(seq);
			return NULL;
		}

		value = CFBundleGetFunctionPointerForName(cfBundle, 
				(CFStringRef)name);
		if (value == NULL) {
			if (!skip_undefined) {
				PyErr_SetString(PyObjCExc_Error,
					"cannot find a function"); // XXX
				Py_DECREF(seq);
				return NULL;
			}
		} else {
			PyObject* pyVal = PyObjCFunc_New(
					name,
					value,
					signature,
					doc);
			if (pyVal == NULL) {
				Py_DECREF(seq);
				return NULL;
			}

			if (PyDict_SetItemString(module_globals, 
					[name UTF8String], pyVal) == -1) {
				Py_DECREF(seq);
				Py_DECREF(pyVal);
				return NULL;
			}
			Py_DECREF(pyVal);


		}
	}
	Py_DECREF(seq);
	Py_INCREF(Py_None);
	return Py_None;
}
