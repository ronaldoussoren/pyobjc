/*
 * This file defines the glue code that is needed to access the objc module
 * from other modules.
 *
 * Why would you want to do that?
 * - To wrap native functions that use Objective-C objects as arguments or
 *   return values
 * - To add custom wrappers for troublesome methods in specific classes
 * - To generic support for additional method signatures
 */
#include "pyobjc.h"
#include "objc_support.h"

#define PYOBJC_BUILD
#include "pyobjc-api.h"

#ifdef ObjCObject_GetObject
#undef ObjCObject_GetObject
#endif

static id python_to_id(PyObject* object)
{
	id    result;
	const char* errstr;

	errstr = depythonify_c_value("@", object, &result);
	if (errstr) {
		ObjCErr_Set(PyExc_TypeError, "Building <id>: %s", errstr);
		return nil;
	}

	return result;
}

static PyObject* id_to_python(id object)
{
	PyObject* result;

	result = pythonify_c_value("@", &object);
	return result;
}

static Class      sel_get_class(PyObject* sel)
{
	if (!ObjCNativeSelector_Check(sel)) {
		PyErr_SetString(PyExc_TypeError, "Expecting ObjCSelector");
	}
	return ((ObjCNativeSelector*)sel)->sel_class;
}

static SEL      sel_get_sel(PyObject* sel)
{
	if (!ObjCSelector_Check(sel)) {
		PyErr_SetString(PyExc_TypeError, "Expecting ObjCSelector");
	}
	return ((ObjCSelector*)sel)->sel_selector;
}



struct pyobjc_api objc_api = {
	PYOBJC_API_VERSION,		/* api_version */
	&ObjCClass_Type,		/* class_type */
	&ObjCObject_Type,		/* object_type */
	&ObjCSelector_Type,		/* select_type */
	ObjC_RegisterMethodMapping,	/* register_method_mapping */
	ObjC_RegisterSignatureMapping,	/* register_signature_mapping */
	ObjCObject_GetObject,		/* obj_get_object */
	ObjCObject_ClearObject,		/* obj_clear_object */
	ObjCClass_GetClass,		/* cls_get_class */
	ObjCClass_New,			/* cls_to_python */
	python_to_id,			/* python_to_id */
	id_to_python,			/* id_to_python */
	ObjCErr_FromObjC,		/* err_objc_to_python */
	ObjCErr_ToObjC,			/* err_python_to_objc */
	depythonify_c_value,		/* py_to_objc */
	pythonify_c_value,		/* objc_to_python */
	ObjC_call_to_python,		/* call_to_python */
	objc_sizeof_type,		/* sizeof_type */
	sel_get_class,			/* sel_get_class */
	sel_get_sel,			/* sel_get_sel */
};

int ObjCAPI_Register(PyObject* module_dict)
{
	PyObject* API = PyCObject_FromVoidPtr(&objc_api, NULL);

	if (API == NULL) return -1;

	if (PyDict_SetItemString(module_dict, PYOBJC_API_NAME, API) < 0) {
		Py_DECREF(API);
		return -1;
	}
	Py_DECREF(API); 
	return 0;
}
