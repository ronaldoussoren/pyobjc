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
#include <ApplicationServices/ApplicationServices.h>

static PyObject*
call_NSGraphicsContext_graphicsPort(
    PyObject* method, PyObject* self, PyObject* arguments)
{
    PyObject* pyCoreGraphicsModule;
    PyObject* pyCGContextPtr;
    PyObject* sillySwigThing;
    CGContextRef res;
    char ptrString[9];
    struct objc_super super;
    PyObject* retVal;

    if (!PyArg_ParseTuple(arguments, "")) {
        return NULL;
    }

    if ((pyCoreGraphicsModule = PyImport_ImportModule("CoreGraphics")) == NULL ) {
        return 0;
    }
    pyCGContextPtr = PyObject_GetAttrString(pyCoreGraphicsModule, "CGContextPtr");
    Py_DECREF(pyCoreGraphicsModule);
    if (pyCGContextPtr == NULL) {
        return 0;
    }

    NS_DURING
        PyObjC_InitSuper(&super,
            PyObjCSelector_GetClass(method),
            PyObjCObject_GetObject(self));

        res = (CGContextRef)objc_msgSendSuper(&super,
            @selector(graphicsPort));
    NS_HANDLER
        PyObjCErr_FromObjC(localException);
        res = NULL;
    NS_ENDHANDLER

    if (res == NULL && PyErr_Occurred()) {
        Py_DECREF(pyCGContextPtr);
        return NULL;
    }

    sprintf(ptrString, "%08x", (unsigned int)res);
    sillySwigThing = PyString_FromFormat("_%s_CGContextRef", ptrString);
    retVal = PyObject_CallFunctionObjArgs(pyCGContextPtr, sillySwigThing, NULL);
    Py_DECREF(sillySwigThing);
    Py_DECREF(pyCGContextPtr);
    return retVal;
}

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
	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSGraphicsContext"), 
		@selector(graphicsPort),
		call_NSGraphicsContext_graphicsPort,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

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
