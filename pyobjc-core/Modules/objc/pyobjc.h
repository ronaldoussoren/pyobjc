#ifndef PyObjC_H
#define PyObjC_H

/*
 * Central include file for PyObjC.
 *
 */

#define OBJC_VERSION "10.3.2"

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include "structmember.h"

#include <AvailabilityMacros.h>
#import <Foundation/Foundation.h>
#include <objc/objc-runtime.h>

#include <objc/objc.h>

#ifndef __LP64__
#error "No in 64-bit mode"
#endif

#ifndef NS_ASSUME_NONNULL_BEGIN
/*
 * Old compiler without nullability support
 */
#define NS_ASSUME_NONNULL_BEGIN
#define NS_ASSUME_NONNULL_END
#define _Nullable
#define _Nonnull
#endif /* !NS_ASSUME_NONNULL_BEGIN */

/*
 * Configuration block
 */

/* PyObjC_DEBUG: If defined the bridge will perform more internal checks */
#ifdef Py_DEBUG
/* Enable when Python is compiled with internal checks enabled */
#ifndef PyObjC_DEBUG
#define PyObjC_DEBUG
#endif
#endif

#ifndef PyObjC_DEBUG
#define PyObjC_DEBUG 1
#endif

#ifdef USE_STATIC_ANALYZER
/* Add some annotations to the CPython API functions we use */
#import "python-api-used.h"
#endif

#import "pyobjc-assert.h"
#import "pyobjc-compat.h"

/* When this is defined the bridge adds a category to NSCFType (and known variants)
 * to help with the conversion to Python.
 *
 * This shouldn't be necessary anymore because the category on NSObject is sufficient,
 * but it is left here just in case someone decides that CFType's can be bridged to
 * a new root Objective-C class.
 */
#define PyObjC_ENABLE_CFTYPE_CATEGORY 1

/* PyObjC_ERROR_ABORT: If defined an internal error will result in an abort() */
#define PyObjC_ERROR_ABORT 1

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
/* #define PyObjC_FAST_BUT_INEXACT 1 */

/* PyObjC_ENABLE_LOOKUP_CACHE: If defined the _type_lookup will cache
 * found entries in leaf classes.
 *
 * A side effect of this is that methods introduced in categories might not
 * be seen in the Python proxy and as such suffers from the same issue as
 * PyObjC_FAST_BUT_INEXACT.
 *
 * NOTE: Option is present for performance testing.
 */
/* #define PyObjC_ENABLE_LOOKUP_CACHE 1 */

/*
 * End of configuration block
 */
#import "OC_PythonArray.h"
#import "OC_PythonData.h"
#import "OC_PythonDate.h"
#import "OC_PythonDictionary.h"
#import "OC_PythonEnumerator.h"
#import "OC_PythonNumber.h"
#import "OC_PythonObject.h"
#import "OC_PythonSet.h"
#import "OC_PythonUnicode.h"
#import "OC_PythonURL.h"

#import "OC_BuiltinPythonArray.h"
#import "OC_BuiltinPythonData.h"
#import "OC_BuiltinPythonDate.h"
#import "OC_BuiltinPythonDictionary.h"
#import "OC_BuiltinPythonNumber.h"
#import "OC_BuiltinPythonSet.h"
#import "OC_BuiltinPythonUnicode.h"

#import "OC_NSBundleHack.h"

#import "method-signature.h"

#import "selector.h"

#import "libffi_extra.h"
#import "libffi_support.h"

#import "ObjCPointer.h"
#import "block_support.h"
#import "bundle-variables.h"
#import "class-builder.h"
#import "class-list.h"
#import "corefoundation.h"
#import "ctests.h"
#import "file_wrapper.h"
#import "formal-protocol.h"
#import "fsref.h"
#import "function.h"
#import "helpers.h"
#import "instance-var.h"
#import "ivar-accessor.h"
#import "memview.h"
#import "meth-func.h"
#import "method-accessor.h"
#import "method-imp.h"
#import "objc-NULL.h"
#import "objc-class.h"
#import "objc-object.h"
#import "objc-runtime-compat.h"
#import "objc_super.h"
#import "objc_support.h"
#import "objc_util.h"
#import "opaque-pointer.h"
#import "options.h"
#import "pointer-support.h"
#import "proxy-registry.h"
#import "pyobjc_unicode.h"
#import "registry.h"
#import "released-buffer.h"
#import "struct-sockaddr.h"
#import "struct-wrapper.h"
#import "super-call.h"
#import "varlist.h"
#import "weakref.h"

#define PYOBJC_BUILD
#import "pyobjc-api.h"
#undef PyObjC_BUILD

#if __has_feature(objc_arc_weak)
#error "It is not possible to compile PyObjC with ARC enabled"
#endif

/*
 * XXX: All definitions below here should be moved to different/new
 * headers
 */

/* module.m */
NS_ASSUME_NONNULL_BEGIN
extern PyObject* _Nullable PyObjC_TypeStr2CFTypeID;
extern PyObject* _Nullable PyObjC_callable_docstr_get(PyObject* callable,
                                                      void* _Nullable closure);
extern PyObject* _Nullable PyObjC_callable_signature_get(PyObject* callable,
                                                         void* _Nullable closure);
extern PyObject* _Nullable PyInit__objc(void);
NS_ASSUME_NONNULL_END

#endif /* PyObjC_H */
