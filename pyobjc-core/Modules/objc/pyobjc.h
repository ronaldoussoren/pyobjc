#ifndef PyObjC_H
#define PyObjC_H

/*
 * Central include file for PyObjC.
 */

#define OBJC_VERSION "3.0a1"


#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

#import <Foundation/Foundation.h>
#include <AvailabilityMacros.h>
#include <objc/objc-runtime.h>
#include <objc/objc.h>


#include "pyobjc-compat.h"

/*
 * Configuration block
 */

/* PyObjC_DEBUG: If defined the bridge will perform more internal checks */
#ifdef Py_DEBUG
   /* Enable when Python is compiled with internal checks enabled */
# ifndef PyObjC_DEBUG
#  define PyObjC_DEBUG
# endif
#endif

/* PyObjC_ERROR_ABORT: If defined an internal error will result in an abort() */
#define    PyObjC_ERROR_ABORT 1

/* PyObjC_FAST_BUT_INEXACT: If defined the method lookup will add a selector
 * to the __dict__ of the class of the object that you looked up the selector,
 * when it it is not defined the selector is added to the dict of the class that
 * actually defines the method.
 *
 * The latter is slightly more correct when using objc.super on arbitrary classes,
 * but does result in more calls to the objc runtime and appears to be slower.
 *
 * NOTE: Option is present for performance testing.
 */
/*#define PyObjC_FAST_BUT_INEXACT 1*/


/*
 * End of configuration block
 */


#include "objc_util.h"
#include "pyobjc-assert.h"
#include "arc-runtime.h"
#include "objc-runtime-compat.h"
#include "proxy-registry.h"
#include "objc_support.h"
#include "pointer-support.h"
#include "OC_PythonObject.h"
#include "OC_PythonArray.h"
#include "OC_PythonData.h"
#include "OC_PythonDictionary.h"
#include "OC_PythonUnicode.h"

#if PY_MAJOR_VERSION == 2
#include "OC_PythonString.h"
#endif

#include "OC_PythonEnumerator.h"
#include "OC_PythonDate.h"
#include "OC_PythonNumber.h"
#include "OC_PythonSet.h"
#include "method-signature.h"
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
#include "pyobjc_unicode.h"
#include "class-descriptor.h"
#include "class-list.h"
#include "struct-wrapper.h"
#include "struct-sockaddr.h"
#include "method-imp.h"
#include "bundle-variables.h"
#include "function.h"
#include "varlist.h"
#include "objc_super.h"
#include "fsref.h"
#include "fsspec.h"
#include "registry.h"
#include "corefoundation.h"
#include "closure_pool.h"
#include "block_support.h"
#include "helpers.h"
#include "opaque-pointer.h"
#include "objc-NULL.h"
#include "options.h"
#include "method-accessor.h"
#include "ivar-accessor.h"
#include "ctests.h"

#define PYOBJC_BUILD
#include "pyobjc-api.h"
#undef PyObjC_BUILD

#if __has_feature(objc_arc_weak)
#  error "It is not possible to compile PyObjC with ARC enabled"
#endif

/*
 * XXX: All definitions below here should be moved to different/new
 * headers
 */

/* module.m */
extern PyObject* PyObjC_TypeStr2CFTypeID;
extern PyObject* PyObjC_callable_docstr_get(PyObject* callable, void* closure);
#if PY_VERSION_HEX >= 0x03030000
extern PyObject* PyObjC_callable_signature_get(PyObject* callable, void* closure);
#endif

#if PY_MAJOR_VERSION == 2
extern PyObject* PyObjCStrBridgeWarning;
#endif

#endif /* PyObjC_H */
