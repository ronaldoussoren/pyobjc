/*
 * NSGraphicsContext mappings for difficult methods:
 *
 * Unsupported:
 * -focusStack
 * -setFocusStack
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

#ifdef MACOSX

#include <ApplicationServices/ApplicationServices.h>

static int
py_to_CG(PyObject* obj __attribute__((__unused__)), void* output __attribute__((__unused__)))
{
	PyErr_SetString(PyExc_TypeError,  "cannot convert to CGContextRef yet");
	return -1;
}

static PyObject*
CG_to_py(void* cgValue)
{
static	PyObject* pyCGContextPtr = NULL;
	PyObject* pyCoreGraphicsModule;
	PyObject* sillySwigThing;
	char ptrString[9];
	PyObject* retVal;

	if (pyCGContextPtr == NULL) {
		if ((pyCoreGraphicsModule = PyImport_ImportModule("CoreGraphics")) == NULL ) {
			return NULL;
		}
		pyCGContextPtr = PyObject_GetAttrString(pyCoreGraphicsModule, "CGContextPtr");
		Py_DECREF(pyCoreGraphicsModule);
		if (pyCGContextPtr == NULL) {
			return NULL;
		}
	}

	sprintf(ptrString, "%08x", (unsigned int)cgValue);
	sillySwigThing = PyString_FromFormat("_%s_CGContextRef", ptrString);
	retVal = PyObject_CallFunctionObjArgs(
			pyCGContextPtr, sillySwigThing, NULL);
	Py_DECREF(sillySwigThing);
	return retVal;
}

#endif

static int 
_pyobjc_install_NSGraphicsContext(void)
{
	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSGraphicsContext"), 
		@selector(focusStack),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSGraphicsContext"), 
		@selector(setFocusStack:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

#ifdef MACOSX
	if (PyObjCPointerWrapper_Register(
		@encode(CGContextRef),
		CG_to_py,
		py_to_CG) == -1) {

		return -1;
	}
#else
	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSGraphicsContext"), 
		@selector(graphicsPort),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}
#endif

	return 0;
}
