/*
 * NSDecimalNumber mapping for special methods:
 * - initWithDecimal: 			[call, imp]
 * - decimalValue			[call, imp]
 * + decimalNumberWithDecimal:		[call, imp]
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static PyObject* 
call_NSDecimalNumber_decimalWithDecimal_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	NSDecimal* aDecimal;
	id res;

	if  (!PyArg_ParseTuple(arguments, "O&", Decimal_Convert, &aDecimal)) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuperCls(&super,
			  PyObjCSelector_GetClass(method),
			  PyObjCClass_GetClass(self));

		res = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				*aDecimal);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	PyObjC_ENDHANDLER

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}

	return PyObjC_IdToPython(res);
}

static PyObject* 
call_NSDecimalNumber_initWithDecimal_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	NSDecimal* aDecimal;
	id res;

	if  (!PyArg_ParseTuple(arguments, "O&", Decimal_Convert, &aDecimal)) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		res = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				*aDecimal);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	PyObjC_ENDHANDLER

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}

	return PyObjC_IdToPython(res);
}

static void 
imp_NSDecimalNumber_initWithDecimal_(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	NSDecimal aDecimal = *(NSDecimal*)args[2];
	id* pretval  = (id*)resp;

	PyObject* result = NULL;
	PyObject* arglist = NULL;
	PyObject* v = NULL;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(2);
	if (arglist == NULL) goto error;
	
	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 0,  v);

	v = Decimal_New(&aDecimal);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	*pretval = PyObjC_PythonToId(result);
	Py_DECREF(result);
	PyGILState_Release(state);
	return;

error:
	*pretval = nil;
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
}

static PyObject* 
call_NSDecimalNumber_decimalValue(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	NSDecimal aDecimal;
	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));
#ifdef MACOSX
		objc_msgSendSuper_stret(&aDecimal, &super,
				PyObjCSelector_GetSelector(method));

#else /* GNUSTEP */
		/*  My hacked objc_msgSendSuper_stret doesn't work and it
		 *  is unlikely that anyone ever overrides this method.
		 */
		aDecimal = [super.self decimalValue];

#endif /* GNUSTEP */
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	return Decimal_New(&aDecimal);
}

#ifdef MACOSX /* See GNU comment above */
static void 
imp_NSDecimalNumber_decimalValue(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	NSDecimal* pretval = (NSDecimal*)resp;
	NSDecimal* res;

	PyObject* result = NULL;
	PyObject* arglist = NULL;
	PyObject* v = NULL;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) goto error;
	
	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 0,  v);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	Decimal_Convert(result, &res);
	*pretval = *res;
	Py_DECREF(result);
	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
}
#endif /* MACOSX */


static int 
_pyobjc_install_NSDecimalNumber(void)
{
	Class classNSDecimalNumber = objc_lookUpClass("NSDecimalNumber");
	if (classNSDecimalNumber == NULL) return 0;
  
	if (PyObjC_RegisterMethodMapping(
			classNSDecimalNumber,
			@selector(initWithDecimal:),
			call_NSDecimalNumber_initWithDecimal_,
			imp_NSDecimalNumber_initWithDecimal_) < 0) {
		return -1;
	}

#if defined(MACOSX) 
	{
		Class classNSDecimalNumberPlaceholder = objc_lookUpClass("NSDecimalNumberPlaceholder");
		if (classNSDecimalNumberPlaceholder != nil) {
			if (PyObjC_RegisterMethodMapping(
				classNSDecimalNumberPlaceholder,
				@selector(initWithDecimal:),
				call_NSDecimalNumber_initWithDecimal_,
				imp_NSDecimalNumber_initWithDecimal_) < 0) {

				return -1;
			}
		}
	}
#endif

	if (PyObjC_RegisterMethodMapping(
			classNSDecimalNumber,
			@selector(decimalNumberWithDecimal:),
			call_NSDecimalNumber_decimalWithDecimal_,
			imp_NSDecimalNumber_initWithDecimal_) < 0) {
		return -1;
	}

#ifdef MACOSX
	if (PyObjC_RegisterMethodMapping(
			classNSDecimalNumber,
			@selector(decimalValue),
			call_NSDecimalNumber_decimalValue,
			imp_NSDecimalNumber_decimalValue) < 0) {
		return -1;
	}


#else 
	/* Our objc_msgSendSuper_stret implementation for the GNU runtime
	 * doesn't work, because of the work-around we cannot allow overriding
	 * -decimalValue for now.
	 */
	if (PyObjC_RegisterMethodMapping(
			classNSDecimalNumber,
			@selector(decimalValue),
			call_NSDecimalNumber_decimalValue,
			PyObjCUnsupportedMethod_IMP) < 0) {
		return -1;
	}
#endif


	return 0;
}
