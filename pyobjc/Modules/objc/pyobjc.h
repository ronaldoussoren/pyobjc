#ifndef PyObjC_H
#define PyObjC_H

/*
 * Central include file for PyObjC. 
 */

#define OBJC_VERSION "1.3.1"

// Loading in AppKit on Mac OS X 10.3 results in
// a bit less than 1500 classes.
#define PYOBJC_EXPECTED_CLASS_COUNT 2048

#include <Python.h>
#include "structmember.h"
#include "pyobjc-compat.h"


#ifdef GNU_RUNTIME
//#include <objc/runtime.h>
#include <objc/objc.h>
#else
#include <objc/objc-runtime.h>
#include <objc/objc.h>
#endif

// how do we make this dependent on sizeof(unichar)??
#if Py_UNICODE_SIZE == 2
#define PyObjC_UNICODE_FAST_PATH
#endif

#include "proxy-registry.h"
#include "objc_support.h"
#include "pointer-support.h"
#include "OC_PythonObject.h"
#include "OC_PythonArray.h"
#include "OC_PythonData.h"
#include "OC_PythonDictionary.h"
#include "OC_PythonUnicode.h"
#include "OC_PythonString.h"
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


/*
 * XXX: All definitions below here should be moved to different/new 
 * headers
 */

#ifdef MACOSX

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

#endif

extern int PyObjC_VerboseLevel;
extern int PyObjC_StrBridgeEnabled;
extern PyObject *PyObjCStrBridgeWarning;
extern PyObject *PyObjC_NSNumberWrapper;


int PyObjCAPI_Register(PyObject* module);
#define PYOBJC_BUILD
#include "pyobjc-api.h"

extern PyObject* PyObjCMethodAccessor_New(PyObject* base, int class_method);

/* Needed by method-accessor, name will be changed soon */
extern PyTypeObject PyObjCMethodAccessor_Type;
char* PyObjC_SELToPythonName(SEL, char*, size_t);


#ifdef MACOSX

/* toll-free-bridging.m */
id PyObjC_CFTypeToID(PyObject* argument);
PyObject* PyObjC_IDToCFType(id argument);

/* opaque-pointer.m */
PyObject* PyObjCCreateOpaquePointerType(const char* name, 
		const char* typestr, const char* docstr);

#endif

#define PyObjCErr_InternalError() \
	PyErr_Format(PyObjCExc_InternalError, \
	   "PyObjC: internal error in %s at %s:%d", \
	   __FUNCTION__, __FILE__, __LINE__)
#define PyObjC_Assert(expr, retval) \
	if (!(expr)) { PyObjCErr_InternalError(); return (retval); }


#endif /* PyObjC_H */
