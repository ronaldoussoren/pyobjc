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

#ifdef PyObjCObject_GetObject
#undef PyObjCObject_GetObject
#endif


static void do_weaklink(PyObject* module_dict, struct PyObjC_WeakLink* funcs)
{
	while (funcs->name) {
		if (!funcs->func) {
			if (PyDict_DelItemString(
					module_dict,
					funcs->name) == -1) {
				PyErr_Clear();
			}
		}
		funcs++;
	}
}

static int obj_is_uninitialized(PyObject* object)
{
	if (!PyObjCObject_Check(object)) {
		return -1;
	}
	return (PyObjCObject_GetFlags(object) & PyObjCObject_kUNINITIALIZED) != 0;
}

static id python_to_id(PyObject* object)
{
	id result;
	int err;

	err = depythonify_c_value(@encode(id), object, &result);
	if (err == -1) {
		return nil;
	}

	return result;
}

static PyObject* id_to_python(id object)
{
	PyObject* result;

	result = pythonify_c_value(@encode(id), &object);
	return result;
}

static Class      sel_get_class(PyObject* sel)
{
	if (!PyObjCNativeSelector_Check(sel)) {
		PyErr_SetString(PyExc_TypeError, "Expecting PyObjCSelector");
		return NULL;
	}
	return ((PyObjCNativeSelector*)sel)->sel_class;
}

static SEL      sel_get_sel(PyObject* sel)
{
	if (!PyObjCSelector_Check(sel)) {
		PyErr_SetString(PyExc_TypeError, "Expecting PyObjCSelector");
		return NULL;
	}
	return ((PyObjCSelector*)sel)->sel_selector;
}

static void 	fill_super(struct objc_super* super, Class cls, id receiver)
{
	objc_superSetReceiver(*super, receiver);
	objc_superSetClass(*super, cls);
}

static void 	fill_super_cls(struct objc_super* super, Class cls, Class self)
{
	objc_superSetReceiver(*super, self);
	objc_superSetClass(*super, object_getClass(cls));
}

static int depythonify_c_array_count2(const char* type, Py_ssize_t count, BOOL strict, PyObject* value, void* datum)
{
	return depythonify_c_array_count(type, count, strict, value, datum, NO, NO);
}




struct pyobjc_api objc_api = {
	PYOBJC_API_VERSION,		/* api_version */
	sizeof(struct pyobjc_api),	/* struct_size */
	&PyObjCClass_Type,		/* class_type */
	(PyTypeObject*)&PyObjCObject_Type, /* object_type */
	&PyObjCSelector_Type,		/* select_type */
	(RegisterMethodMappingFunctionType*)PyObjC_RegisterMethodMapping,	/* register_method_mapping */
	(int (*)(char*, PyObject *(*)(PyObject*, PyObject*, PyObject*), void (*)(void*, void*, void**, void*)))PyObjC_RegisterSignatureMapping,	/* register_signature_mapping */
	PyObjCObject_GetObject,		/* obj_get_object */
	PyObjCObject_ClearObject,		/* obj_clear_object */
	PyObjCClass_GetClass,		/* cls_get_class */
	PyObjCClass_New,			/* cls_to_python */
	python_to_id,			/* python_to_id */
	id_to_python,			/* id_to_python */
	PyObjCErr_FromObjC,		/* err_objc_to_python */
	PyObjCErr_ToObjC,			/* err_python_to_objc */
	depythonify_c_value,		/* py_to_objc */
	pythonify_c_value,		/* objc_to_python */
	PyObjCRT_SizeOfType,		/* sizeof_type */
	sel_get_class,			/* sel_get_class */
	sel_get_sel,			/* sel_get_sel */
	fill_super,			/* fill_super */
	fill_super_cls,			/* fill_super_cls*/
	PyObjCPointerWrapper_Register,	/* register_pointer_wrapper */
	(void(*)(void*,void*,void**,void*))PyObjCUnsupportedMethod_IMP,    /* unsupported_method_imp */
	PyObjCUnsupportedMethod_Caller, /* unsupported_method_caller */
	PyObjCErr_ToObjCWithGILState,	/* objc_err_to_objc_gil */
	PyObjCRT_AlignOfType,		/* alignof_type */
	sel_getName,			/* selname */
	PyObjCRT_SimplifySignature,	/* simplify_sig */
	PyObjC_FreeCArray,		/* free_c_array */
	PyObjC_PythonToCArray,		/* py_to_c_array */
	PyObjC_CArrayToPython,		/* c_array_to_py */
	PyObjC_RegisterStructType,	/* register_struct */
	&PyObjCIMP_Type,		/* imp_type */
	PyObjCIMP_GetIMP,		/* imp_get_imp */
	PyObjCIMP_GetSelector,		/* imp_get_sel */
	PyObjCErr_AsExc,		/* err_python_to_nsexception */
	PyGILState_Ensure,		/* gilstate_ensure */
	obj_is_uninitialized,   /* obj_is_uninitialized */
	PyObjCObject_New,		/* pyobjc_object_new */
	PyObjCCreateOpaquePointerType, /* pointer_type_new */
	PyObjCObject_NewTransient,	/* newtransient */
	PyObjCObject_ReleaseTransient,  /* releasetransient */
	do_weaklink,			/* doweaklink */
	PyObjCRT_RemoveFieldNames,	/* removefields */
	&PyObjC_NULL,			/* PyObjC_NULL */
	depythonify_c_array_count2,	/* PyObjC_DepythonifyCArray */
	PyObjC_VarList_New,		/* PyObjC_VarList_New */
	PyObjC_is_ascii_string,
	PyObjC_is_ascii_prefix,
	PyObjCObject_Convert,
};

int PyObjCAPI_Register(PyObject* module)
{
#if PY_MAJOR_VERSION == 2
	PyObject* API = PyCObject_FromVoidPtr(&objc_api, NULL);
#else
	PyObject* API = PyCapsule_New(&objc_api, "objc." PYOBJC_API_NAME, NULL);
#endif

	if (API == NULL) return -1;

	if (PyModule_AddObject(module, PYOBJC_API_NAME, API) < 0) {
		Py_DECREF(API);
		return -1;
	}
	return 0;
}
