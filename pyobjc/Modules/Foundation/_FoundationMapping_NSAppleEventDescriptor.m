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

/* 
	WARNING: this is a major hack, you have to be careful using this!

	Should I use AEDuplicateDesc instead?

*/
#ifndef AEDescObject
typedef struct AEDescObject {
	PyObject_HEAD
	AEDesc ob_itself;
	int ob_owned;
} AEDescObject;
#endif

#ifndef AEDesc_Type
#define PYOBJC_LOCAL_AEDESC 1
PyObject *AEDesc_TypeObject;
#define AEDesc_TypePtr ((PyTypeObject *)AEDesc_TypeObject)
#else
#define AEDesc_TypePtr (&AEDesc_Type)
#endif

#ifndef AEDesc_Check
#define AEDesc_Check(x) ((x)->ob_type == AEDesc_TypePtr || PyObject_TypeCheck((x), AEDesc_TypePtr))
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

	PyObjC_DURING
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
		 * Apparently the original self is recycled during the init.
		 */
		if (self != result) {
			PyObjCObject_ClearObject(self);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	PyObjC_ENDHANDLER

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

	PyObjC_DURING
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

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	PyObjC_ENDHANDLER

	/* XXX Ronald: If you try to use the result of 
	 * PyObjCObject_GetObject(self) after the call to objc_msgSend 
	 * it will crash with large enough values of len (>=32). 
	 * Apparently the original self is recycled during the init.
	 */
	if (self != result) {
		PyObjCObject_ClearObject(self);
	}

	return result;
}

static int
PyAEDescPtr_Convert(PyObject *obj, void *output)
{
	AEDescObject *desc = (AEDescObject*)obj;
	if (!AEDesc_Check(obj)) {
		PyErr_SetString(PyExc_TypeError, "AEDesc required");
		return -1;
	}
	*(AEDesc **)output = &desc->ob_itself;
	desc->ob_owned = 0;
	return 0;
}

static PyObject*
PyAEDescPtr_New(void *obj)
{
	return AEDesc_NewBorrowed((AppleEvent*)obj);
}

static int 
_pyobjc_install_NSAppleEventDescriptor(void)
{
	int r;
	Class classNSAppleEventDescriptor = objc_lookUpClass("NSAppleEventDescriptor");
	if (classNSAppleEventDescriptor == NULL) return 0;
    
#ifdef PYOBJC_LOCAL_AEDESC
    PyObject *AEModule;
    PyObject *AEModuleDict;
    AEModule = PyImport_ImportModule("_AE");
    if (AEModule == NULL) {
        PyErr_Clear();
        return 0;
    }
    AEModuleDict = PyModule_GetDict(AEModule);
    AEDesc_TypeObject = PyMapping_GetItemString(AEModuleDict, "AEDesc");
    if (AEDesc_TypeObject == NULL) return -1;
#endif

	r = PyObjC_RegisterMethodMapping(
		classNSAppleEventDescriptor,
        @selector(initWithDescriptorType:bytes:length:),
		call_NSAppleEventDescriptor_initWithDescriptorType_bytes_length_,
		PyObjCUnsupportedMethod_IMP);
	if (r == -1) return -1;

	r = PyObjC_RegisterMethodMapping(
		classNSAppleEventDescriptor,
        @selector(descriptorWithDescriptorType:bytes:length:),
		call_NSAppleEventDescriptor_descriptorWithDescriptorType_bytes_length_,
		PyObjCUnsupportedMethod_IMP);
	if (r == -1) return -1;

	r = PyObjCPointerWrapper_Register(@encode(AEDesc*),
		PyAEDescPtr_New, PyAEDescPtr_Convert);
	if (r == -1) return -1;
	
	return 0;
}
