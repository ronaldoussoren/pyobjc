/*
 * NSAppleEventDescriptor mappings for difficult methods:
 *
 * + descriptorWithDescriptorType:bytes:length:
 * - initWithDescriptorType:bytes:length:
 * - initWithAEDescNoCopy:
 * - aeDesc
 * 
 * TODO:
 * + appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:
 * + descriptorWithDescriptorType:data:
 * + descriptorWithEnumCode:
 * + descriptorWithTypeCode:
 * - initWithDescriptorType:data:
 * - initWithEventClass:eventID:targetDescriptor:returnID:transactionID:
 * - descriptorType
 * - coerceToDescriptorType
 * - enumCodeValue
 * - typeCodeValue
 * - descriptorForKeyword:
 * - keywordForDescriptorAtIndex:
 * - removeDescriptorWithKeyword:
 * - removeParamDescriptorWithKeyword:
 * - setDescriptor:forKeyword:
 * - attributeDescriptorForKeyword:
 * - setAttributeDescriptor:forKeyword:
 * - eventClass
 * - eventID
 * - keywordForDescriptorAtIndex:
 * 
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"
#include "pymactoolbox.h"

#if PY_VERSION_HEX >= 0x0203000A

#define HAVE_AEDESC_NEWBORROWED

#endif

static PyObject* 
call_NSAppleEventDescriptor_initWithDescriptorType_bytes_length_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char*     bytes;
	int       bytes_len;
	int       len;
	PyObject* result;
	struct objc_super super;
	id        objc_result;
	OSType    descriptorType;

	/* mostly copied from similar NSData mapping */
	if  (!PyArg_ParseTuple(arguments, "O&t#i", PyMac_GetOSType, &descriptorType, &bytes, &bytes_len, &len)) {
		return NULL;
	}

	if (bytes_len < len) {
		PyErr_SetString(PyExc_ValueError, "Not enough bytes in data");
		return NULL;
	}

	NS_DURING
		if (PyObjCIMP_Check(method)) {
			objc_result = ((id(*)(id,SEL,char*,int))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					bytes, len);
		} else {
			PyObjC_InitSuper(&super,
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			objc_result = objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method),
					bytes, len);
		}

		result = PyObjC_IdToPython(objc_result);

		/* XXX Ronald: If you try to use the result of 
		 * PyObjCObject_GetObject(self) after the call to objc_msgSend 
		 * it will crash with large enough values of len (>=32). 
		 * Appearently the original self is recycled during the init.
		 */
		if (self != result) {
			PyObjCObject_ClearObject(self);
		}
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static PyObject* 
call_NSAppleEventDescriptor_descriptorWithDescriptorType_bytes_length_(
        PyObject* method, PyObject* self, PyObject* arguments)
{
	char*     bytes;
	int       bytes_len;
	int       len;
	PyObject* result;
	struct objc_super super;
	id        objc_result;
	OSType    descriptorType;

	/* mostly copied from similar NSData mapping */
	if  (!PyArg_ParseTuple(arguments, "O&t#i", PyMac_GetOSType, &descriptorType, &bytes, &bytes_len, &len)) {
		return NULL;
	}

	if (bytes_len < len) {
		PyErr_SetString(PyExc_ValueError, "Not enough bytes in data");
		return NULL;
	}

	NS_DURING
		if (PyObjCIMP_Check(method)) {
			objc_result = ((id(*)(id,SEL,char*,int))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCClass_GetClass(self),
					PyObjCIMP_GetSelector(method),
					bytes, len);
		} else {
			PyObjC_InitSuperCls(&super,
				PyObjCSelector_GetClass(method),
				PyObjCClass_GetClass(self));

			objc_result = objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method),
					descriptorType, bytes, len);
		}
		result = PyObjC_IdToPython(objc_result);

		/* XXX Ronald: If you try to use the result of 
		 * PyObjCObject_GetObject(self) after the call to objc_msgSend 
		 * it will crash with large enough values of len (>=32). 
		 * Appearently the original self is recycled during the init.
		 */
		if (self != result) {
			PyObjCObject_ClearObject(self);
		}
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

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
		if (PyObjCIMP_Check(method)) {
			res = ((id(*)(id,SEL,AEDesc*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					theEvent);
		} else {
			PyObjC_InitSuper(&super,
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			res = (id)objc_msgSendSuper(&super,
			    @selector(initWithAEDescNoCopy:), theEvent);
		}
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

#ifdef HAVE_AEDESC_NEWBORROWED
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
		if (PyObjCIMP_Check(method)) {
			res = ((AppleEvent*(*)(id,SEL))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method));
		} else {
			PyObjC_InitSuper(&super,
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			res = (AppleEvent*)objc_msgSendSuper(&super,
			    @selector(aeDesc));
		}
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
#endif

static int 
_pyobjc_install_NSAppleEventDescriptor(void)
{
	Class classNSAppleEventDescriptor = objc_lookUpClass("NSAppleEventDescriptor");
	if (classNSAppleEventDescriptor == NULL) return 0;

	if (PyObjC_RegisterMethodMapping(
		classNSAppleEventDescriptor,
        @selector(initWithDescriptorType:bytes:length:),
		call_NSAppleEventDescriptor_initWithDescriptorType_bytes_length_,
		PyObjCUnsupportedMethod_IMP) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSAppleEventDescriptor,
        @selector(descriptorWithDescriptorType:bytes:length:),
		call_NSAppleEventDescriptor_descriptorWithDescriptorType_bytes_length_,
		PyObjCUnsupportedMethod_IMP) < 0) {
		return -1;
	}

#ifdef HAVE_AEDESC_NEWBORROWED
	if (PyObjC_RegisterMethodMapping(
		classNSAppleEventDescriptor,
		@selector(aeDesc),
		call_NSAppleEventDescriptor_aeDesc,
		PyObjCUnsupportedMethod_IMP) < 0) {
		return -1;
	}
#endif

	if (PyObjC_RegisterMethodMapping(
		classNSAppleEventDescriptor,
		@selector(initWithAEDescNoCopy:),
		call_NSAppleEventDescriptor_initWithAEDescNoCopy_,
		PyObjCUnsupportedMethod_IMP) < 0) {
		return -1;
	}
	return 0;
}
