#ifndef PyObjC_H
#define PyObjC_H

/*
 * Central include file for PyObjC. 
 */

#define OBJC_VERSION "2.0"

// Loading in AppKit on Mac OS X 10.3 results in
// a bit less than 1500 classes.
#define PYOBJC_EXPECTED_CLASS_COUNT 2048
#define PY_SSIZE_T_CLEAN

#include <Python.h>
#include "structmember.h"
#include "pyobjc-compat.h"


#include <objc/objc-runtime.h>
#include <objc/objc.h>

// how do we make this dependent on sizeof(unichar)??
#if Py_UNICODE_SIZE == 2
#define PyObjC_UNICODE_FAST_PATH
#endif

#include "objc-runtime-compat.h"
#include "proxy-registry.h"
#include "objc_support.h"
#include "pointer-support.h"
#include "OC_PythonObject.h"
#include "OC_PythonArray.h"
#include "OC_PythonData.h"
#include "OC_PythonDictionary.h"
#include "OC_PythonUnicode.h"
#include "OC_PythonString.h"
#include "OC_PythonEnumerator.h"
#include "method-signature.h"
#include "objc_util.h"
#include "objc-class.h"
#include "objc-object.h"
#include "selector.h"
#include "libffi_support.h"
#include "super-call.h"
#include "instance-var.h"
#include "class-builder.h" 
#include "ObjCPointer.h"
#include "informal-protocol.h"
#include "formal-protocol.h"
#include "alloc_hack.h"
#include "unicode-object.h"
#include "class-descriptor.h"
#include "class-list.h"
#include "struct-wrapper.h"
#include "method-imp.h"
#include "bundle-variables.h"
#include "function.h"
#include "varlist.h"
#include "parsexml.h"
#include "objc_super.h"


/*
 * XXX: All definitions below here should be moved to different/new 
 * headers
 */

/* On MacOS X, +signatureWithObjCTypes: is a method of NSMethodSignature,
 * but that method is not present in the header files. We add the definition
 * here to avoid warnings.
 * 
 * XXX: We use an undocumented API, but we also don't have much choice: we
 * must create the things and this is the only way to do it...
 */
@interface NSMethodSignature (WarningKiller)
	+signatureWithObjCTypes:(const char*)types;
@end /* interface NSMethodSignature */


extern int PyObjC_VerboseLevel;
extern int PyObjC_HideProtected;
extern int PyObjC_StrBridgeEnabled;
extern PyObject *PyObjCStrBridgeWarning;
extern PyObject *PyObjC_NSNumberWrapper;


int PyObjCAPI_Register(PyObject* module);
#define PYOBJC_BUILD
#include "pyobjc-api.h"
#include "registry.h"
#include "corefoundation.h"

extern PyObject* PyObjCMethodAccessor_New(PyObject* base, int class_method);

/* Needed by method-accessor, name will be changed soon */
extern PyTypeObject PyObjCMethodAccessor_Type;
char* PyObjC_SELToPythonName(SEL, char*, size_t);


/* toll-free-bridging.m */
id PyObjC_CFTypeToID(PyObject* argument);
PyObject* PyObjC_IDToCFType(id argument);

/* opaque-pointer.m */
PyObject* PyObjCCreateOpaquePointerType(const char* name, 
		const char* typestr, const char* docstr);

/* objc-NULL.m */
extern PyObject* PyObjC_NULL;
extern PyObject* PyObjCInitNULL(void);

/* socketsupport.m */
int PyObjC_SockAddrFromPython(PyObject*, void*);
PyObject* PyObjC_SockAddrToPython(void*);

/* module.m */
extern PyObject* PyObjC_TypeStr2CFTypeID;
extern PyObject* PyObjC_AdjustSelf(PyObject* self);




//#ifdef Py_DEBUG
#if 1

#define PyObjCErr_InternalError() \
	PyErr_Format(PyObjCExc_InternalError, \
	   "PyObjC: internal error in %s at %s:%d", \
	   __FUNCTION__, __FILE__, __LINE__)
#define PyObjC_Assert(expr, retval) \
	if (!(expr)) { PyObjCErr_InternalError(); return (retval); }

#else

#define PyObjC_Assert(expr, retval)	((void)0)

#endif

#endif /* PyObjC_H */
