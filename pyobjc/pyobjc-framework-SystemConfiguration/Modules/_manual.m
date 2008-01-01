#include <Python.h>
#include "pyobjc-api.h"

#import <SystemConfiguration/SystemConfiguration.h>

/*
 * Context definitions 
 */

static const void*
mod_retain(const void* info)
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_XINCREF((PyObject*)info);
	PyGILState_Release(state);
	return info;
}

static void
mod_release(const void* info)
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_XDECREF((PyObject*)info);
	PyGILState_Release(state);
}


static SCDynamicStoreContext mod_SCDynamicStoreContext = {
	0,			/* version */
	NULL,			/* info */
	mod_retain,		/* retain */
	mod_release,		/* release */
	NULL			/* copyDescription */
};

static SCPreferencesContext mod_SCPreferencesContext = {
	0,			/* version */
	NULL,			/* info */
	mod_retain,		/* retain */
	mod_release,		/* release */
	NULL			/* copyDescription */
};

static SCNetworkConnectionContext mod_SCNetworkConnectionContext = {
	0,			/* version */
	NULL,			/* info */
	mod_retain,		/* retain */
	mod_release,		/* release */
	NULL			/* copyDescription */
};

static SCNetworkReachabilityContext mod_SCNetworkReachabilityContext = {
	0,			/* version */
	NULL,			/* info */
	mod_retain,		/* retain */
	mod_release,		/* release */
	NULL			/* copyDescription */
};


/* Callback implementations */


static void
mod_SCDynamicStoreCallBack(
		SCDynamicStoreRef store,
		CFArrayRef changedKeys,
		void* _info)
{
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* info = (PyObject*)_info;
	PyObject* callable = PyTuple_GET_ITEM(info, 0);	
	PyObject* real_info = PyTuple_GET_ITEM(info, 1);	
	PyObject* py_store = PyObjC_ObjCToPython(@encode(SCDynamicStoreRef), &store);
	if (py_store == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}

	PyObject* py_keys = PyObjC_ObjCToPython(@encode(CFArrayRef), &changedKeys);
	if (py_keys == NULL) {
		Py_DECREF(py_store);
		PyObjCErr_ToObjCWithGILState(&state);
	}


	PyObject* result = PyObject_CallFunction(callable, "NNO", py_store, py_keys, real_info);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static void
mod_SCPreferencesCallBack(
		SCPreferencesRef prefs,
		SCPreferencesNotification notificationType,
		void* _info)
{
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* info = (PyObject*)_info;
	PyObject* callable = PyTuple_GET_ITEM(info, 0);	
	PyObject* real_info = PyTuple_GET_ITEM(info, 1);	
	PyObject* py_prefs = PyObjC_ObjCToPython(@encode(SCPreferencesRef), &prefs);
	if (py_prefs == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	PyObject* py_type = PyObjC_ObjCToPython(@encode(SCPreferencesNotification), &notificationType);
	if (py_type == NULL) {
		Py_DECREF(py_prefs);
		PyObjCErr_ToObjCWithGILState(&state);
	}

	PyObject* result = PyObject_CallFunction(callable, "NNO", py_prefs, py_type, real_info);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static void mod_SCNetworkConnectionCallBack(
		SCNetworkConnectionRef connection,
		SCNetworkConnectionStatus status,
		void* _info)
{
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* info = (PyObject*)_info;
	PyObject* callable = PyTuple_GET_ITEM(info, 0);	
	PyObject* real_info = PyTuple_GET_ITEM(info, 1);	
	PyObject* py_connection = PyObjC_ObjCToPython(@encode(SCNetworkConnectionRef), &connection);
	if (py_connection == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	PyObject* py_status = PyObjC_ObjCToPython(@encode(SCNetworkConnectionStatus), &status);
	if (py_status == NULL) {
		Py_DECREF(py_connection);
		PyObjCErr_ToObjCWithGILState(&state);
	}

	PyObject* result = PyObject_CallFunction(callable, "NNO", 
			py_connection, py_status, real_info);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static void mod_SCNetworkReachabilityCallBack(
		SCNetworkReachabilityRef target,
		SCNetworkConnectionFlags flags,
		void* _info)
{
	PyGILState_STATE state = PyGILState_Ensure();

	printf("mod_SCNetworkReachabilityCallBack\n");

	PyObject* info = (PyObject*)_info;
	PyObject* callable = PyTuple_GET_ITEM(info, 0);	
	PyObject* real_info = PyTuple_GET_ITEM(info, 1);	
	PyObject* py_target = PyObjC_ObjCToPython(@encode(SCNetworkReachabilityRef), &target);
	if (py_target == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	PyObject* py_flags = PyObjC_ObjCToPython(@encode(SCNetworkConnectionFlags), &flags);
	if (py_flags == NULL) {
		Py_DECREF(py_target);
		PyObjCErr_ToObjCWithGILState(&state);
	}

	PyObject* result = PyObject_CallFunction(callable, "NNO", 
			py_target, py_flags, real_info);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

/* And finally the function wrappers */


static PyObject*
mod_SCDynamicStoreCreate(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_name;
	PyObject* callout;
	PyObject* context;
	CFAllocatorRef allocator;
	CFStringRef name;

	if (!PyArg_ParseTuple(args, "OOOO", &py_allocator, &py_name, &callout, &context)) {
		return NULL;
	}
	
	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFStringRef), py_name, &name) < 0) {
		return NULL;
	}

	PyObject* real_info = Py_BuildValue("OO", callout, context);
	if (real_info == NULL) {
		return NULL;
	}

	SCDynamicStoreRef store = NULL;
	SCDynamicStoreContext real_context;
	real_context = mod_SCDynamicStoreContext;
	real_context.info = real_info;

	PyObjC_DURING
		store = SCDynamicStoreCreate(
				allocator,
				name,
				mod_SCDynamicStoreCallBack,
				&real_context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		store = NULL;

	PyObjC_ENDHANDLER
	Py_DECREF(real_info);

	if (store == NULL) {

		if (PyErr_Occurred()) {
			return NULL;
		} else {
			Py_INCREF(Py_None);
			return Py_None;
		}
	}

	PyObject* result = PyObjC_ObjCToPython(
			@encode(SCDynamicStoreRef), &store);
	CFRelease(store);

	return result;
}


static PyObject*
mod_SCDynamicStoreCreateWithOptions(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_name;
	PyObject* py_options;
	PyObject* callout;
	PyObject* context;
	CFAllocatorRef allocator;
	CFDictionaryRef storeOptions;
	CFStringRef name;

	if (!PyArg_ParseTuple(args, "OOOOO", &py_allocator, &py_name, &py_options, &callout, &context)) {
		return NULL;
	}
	
	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFDictionaryRef), py_options, &storeOptions) < 0) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFStringRef), py_name, &name) < 0) {
		return NULL;
	}

	PyObject* real_info = Py_BuildValue("OO", callout, context);
	if (real_info == NULL) {
		return NULL;
	}

	SCDynamicStoreRef store = NULL;
	SCDynamicStoreContext real_context;
	real_context = mod_SCDynamicStoreContext;
	real_context.info = real_info;

	PyObjC_DURING
		store = SCDynamicStoreCreateWithOptions(
				allocator,
				name,
				storeOptions,
				mod_SCDynamicStoreCallBack,
				&real_context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		store = NULL;

	PyObjC_ENDHANDLER
	Py_DECREF(real_info);

	if (store == NULL) {

		if (PyErr_Occurred()) {
			return NULL;
		} else {
			Py_INCREF(Py_None);
			return Py_None;
		}
	}

	PyObject* result = PyObjC_ObjCToPython(
			@encode(SCDynamicStoreRef), &store);
	if (store != NULL) {
		CFRelease(store);
	}

	return result;
}



static PyObject*
mod_SCPreferencesSetCallback(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_prefs;
	PyObject* callout;
	PyObject* context;
	SCPreferencesRef prefs;

	if (!PyArg_ParseTuple(args, "OOO", &py_prefs, &callout, &context)) {
		return NULL;
	}
	
	if (PyObjC_PythonToObjC(@encode(SCPreferencesRef), py_prefs, &prefs) < 0) {
		return NULL;
	}

	PyObject* real_info = Py_BuildValue("OO", callout, context);
	if (real_info == NULL) {
		return NULL;
	}

	SCPreferencesContext real_context;
	real_context = mod_SCPreferencesContext;
	real_context.info = real_info;

	Boolean result = FALSE;
	PyObjC_DURING
		result = SCPreferencesSetCallback(
				prefs,
				mod_SCPreferencesCallBack,
				&real_context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = FALSE;

	PyObjC_ENDHANDLER

	if (!result) {
		Py_DECREF(real_info);

		if (PyErr_Occurred()) {
			return NULL;
		}
	}

	return PyBool_FromLong(result);
}

static PyObject*
mod_SCNetworkConnectionCreateWithServiceID(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_serviceID;
	PyObject* callout;
	PyObject* context;
	CFAllocatorRef allocator;
	CFStringRef serviceID;

	if (!PyArg_ParseTuple(args, "OOOO", &py_allocator, &py_serviceID, &callout, &context)) {
		return NULL;
	}
	
	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFStringRef), py_serviceID, &serviceID) < 0) {
		return NULL;
	}

	PyObject* real_info = Py_BuildValue("OO", callout, context);
	if (real_info == NULL) {
		return NULL;
	}

	SCNetworkConnectionContext real_context;
	real_context = mod_SCNetworkConnectionContext;
	real_context.info = real_info;

	SCNetworkConnectionRef result = NULL;
	PyObjC_DURING
		result = SCNetworkConnectionCreateWithServiceID(
				allocator,
				serviceID,
				mod_SCNetworkConnectionCallBack,
				&real_context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;

	PyObjC_ENDHANDLER

	Py_DECREF(real_info);

	if (result == NULL) {

		if (PyErr_Occurred()) {
			return NULL;
		}
	}

	PyObject* rv = PyObjC_ObjCToPython(@encode(SCNetworkConnectionRef), &result);
	if (result != NULL) {
		CFRelease(result);
	}
	return rv;
}

static PyObject*
mod_SCNetworkReachabilitySetCallback(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_target;
	PyObject* callout;
	PyObject* context;
	SCNetworkReachabilityRef target;

	if (!PyArg_ParseTuple(args, "OOO", &py_target, &callout, &context)) {
		return NULL;
	}
	
	if (PyObjC_PythonToObjC(@encode(SCNetworkReachabilityRef), py_target, &target) < 0) {
		return NULL;
	}

	PyObject* real_info = Py_BuildValue("OO", callout, context);
	if (real_info == NULL) {
		return NULL;
	}

	SCNetworkReachabilityContext real_context;
	real_context = mod_SCNetworkReachabilityContext;
	real_context.info = real_info;

	Boolean result = FALSE;
	PyObjC_DURING
		result = SCNetworkReachabilitySetCallback(
				target,
				mod_SCNetworkReachabilityCallBack,
				&real_context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = FALSE;

	PyObjC_ENDHANDLER
	Py_DECREF(real_info);

	if (!result) {
		if (PyErr_Occurred()) {
			return NULL;
		}
	}
	
	return PyBool_FromLong(result);
}


PyDoc_STRVAR(mod_doc, "");

static PyMethodDef mod_methods[] = {
	{ 
		"SCDynamicStoreCreate", 
		(PyCFunction)mod_SCDynamicStoreCreate, 
		METH_VARARGS, 
		NULL,
	},
	{ 
		"SCDynamicStoreCreateWithOptions", 
		(PyCFunction)mod_SCDynamicStoreCreateWithOptions, 
		METH_VARARGS, 
		NULL,
	},
	{ 
		"SCPreferencesSetCallback", 
		(PyCFunction)mod_SCPreferencesSetCallback, 
		METH_VARARGS, 
		NULL,
	},
	{ 
		"SCNetworkConnectionCreateWithServiceID", 
		(PyCFunction)mod_SCNetworkConnectionCreateWithServiceID, 
		METH_VARARGS, 
		NULL,
	},
	{ 
		"SCNetworkReachabilitySetCallback", 
		(PyCFunction)mod_SCNetworkReachabilitySetCallback, 
		METH_VARARGS, 
		NULL,
	},
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_manual(void);

void
init_manual(void)
{
	PyObject* m = Py_InitModule4("_manual", mod_methods,
			mod_doc, NULL, PYTHON_API_VERSION);

	if (PyObjC_ImportAPI(m) < 0) { return; }
}
