/*
 * Special wrappers for NSAppleEventDescriptor methods with 'difficult' 
 * arguments.
 *
 * - aeDesc
 * - initWithAEDescNoCopy:
 *
 * XXX - should also do these
 * + descriptorWithDescriptorType:bytes:length:
 * - initWithDescriptorType:bytes:length:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"
#include "pymactoolbox.h"

static PyObject*
call_NSAppleEventDescriptor_initWithAEDescNoCopy_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
    AEDesc *theEvent;
	id res;
	struct objc_super super;
	PyObject* retVal;

    if ( (theEvent = PyMem_NEW(AEDesc, 1)) == NULL ) {
        PyErr_NoMemory();
        return 0;
    }
	if (!PyArg_ParseTuple(arguments, "O&", AEDesc_Convert, theEvent)) { 
        PyMem_DEL(theEvent);
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		res = (id)objc_msgSendSuper(&super,
		    @selector(initWithAEDescNoCopy:), theEvent);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		res = NULL;
	NS_ENDHANDLER

	if (res == NULL && PyErr_Occurred()) {
		return NULL;
	}

	retVal = PyObjC_IdToPython(res);
	return retVal;
}

static PyObject*
call_NSAppleEventDescriptor_aeDesc(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	AppleEvent* res;
	struct objc_super super;
	PyObject* retVal;

	if (!PyArg_ParseTuple(arguments, "")) { 
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		res = (AppleEvent*)objc_msgSendSuper(&super,
		    @selector(aeDesc));
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		res = NULL;
	NS_ENDHANDLER

	if (res == NULL && PyErr_Occurred()) {
		return NULL;
	}

	retVal = AEDesc_NewBorrowed(res);
	return retVal;
}

static int 
_pyobjc_install_NSAppleEventDescriptor(void)
{
	Class classNSAppleEventDescriptor = objc_lookUpClass("NSAppleEventDescriptor");
	if (classNSAppleEventDescriptor == NULL) return 0;

	if (PyObjC_RegisterMethodMapping(
		classNSAppleEventDescriptor,
		@selector(aeDesc),
		call_NSAppleEventDescriptor_aeDesc,
		PyObjCUnsupportedMethod_IMP) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSAppleEventDescriptor,
		@selector(initWithAEDescNoCopy:),
		call_NSAppleEventDescriptor_initWithAEDescNoCopy_,
		PyObjCUnsupportedMethod_IMP) < 0) {
		return -1;
	}
	return 0;
}
