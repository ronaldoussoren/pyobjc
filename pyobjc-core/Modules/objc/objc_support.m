/* Copyright (c) 1996,97,98 by Lele Gaifax. All Rights Reserved
 * Copyright (c) 2002-2021 Ronald Oussoren
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: objc_support.m,v
 * Revision: 1.24
 * Date: 1998/08/18 15:35:58
 *
 * Created Tue Sep 10 14:16:02 1996.
 */

#include "pyobjc.h"
#include <objc/Protocol.h>
#include <simd/simd.h>

#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

#import <Foundation/NSData.h>
#import <Foundation/NSDecimalNumber.h>
#import <Foundation/NSInvocation.h>
#import <Foundation/NSValue.h>

#include <CoreFoundation/CFNumber.h>

#ifndef __LP64__
#error "Requires LP64"
#endif

NS_ASSUME_NONNULL_BEGIN

/*
 * Category on NSObject to make sure that every object supports
 * the method  __pyobjc_PythonObject__, this helps to simplify
 * pythonify_c_value.
 *
 * XXX: Are these categories really necessary? Check if
 *      hardcoding the result (including the various OC_.. classes
 *      leads to faster code)
 */
@interface
NSObject (PyObjCSupport)
- (PyObject* _Nullable)__pyobjc_PythonObject__;
+ (PyObject* _Nullable)__pyobjc_PythonObject__;

- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie;
+ (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie;
@end /* PyObjCSupport */

@implementation
NSObject (PyObjCSupport)

- (PyObject* _Nullable)__pyobjc_PythonObject__
{
    PyObject* rval;

    rval = PyObjC_FindPythonProxy(self);
    if (rval == NULL) {
        rval = PyObjC_TryCreateCFProxy(self);
        if (rval == NULL && PyErr_Occurred()) {
            return NULL;
        }
    }

    if (rval == NULL) {
        rval = (PyObject*)PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
        if (rval == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;    // LCOV_EXCL_LINE
        }
    }

    PyObjC_RegisterPythonProxy(self, rval);
    return rval;
}

+ (PyObject* _Nullable)__pyobjc_PythonObject__
{
    return (PyObject*)PyObjCClass_New(self);
}

- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie
{
    PyObject* result = PyObjC_FindPythonProxy(self);
    if (result) {
        *cookie = 0;
        return result;
    }

    *cookie = 1;
    return PyObjCObject_New(self, PyObjCObject_kSHOULD_NOT_RELEASE, NO);
}

+ (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    return (PyObject*)PyObjCClass_New(self);
}

@end /* PyObjCSupport */

@interface
NSProxy (PyObjCSupport)
- (PyObject* _Nullable)__pyobjc_PythonObject__;
+ (PyObject* _Nullable)__pyobjc_PythonObject__;

- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie;
+ (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie;
@end /* PyObjCSupport */

@implementation
NSProxy (PyObjCSupport)

- (PyObject* _Nullable)__pyobjc_PythonObject__
{
    PyObject* rval;

    rval = PyObjC_FindPythonProxy(self);
    if (rval == NULL) {
        rval = (PyObject*)PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
        if (rval != NULL) {
            PyObjC_RegisterPythonProxy(self, rval);
        }
    }
    return rval;
}

+ (PyObject* _Nullable)__pyobjc_PythonObject__
{
    PyObject* rval;

    rval = NULL;
    if (rval == NULL) {
        rval = (PyObject*)PyObjCClass_New(self);
    }
    return rval;
}

- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie
{
    PyObject* result = PyObjC_FindPythonProxy(self);
    if (result) {
        *cookie = 0;
        return result;
    }

    *cookie = 1;
    return PyObjCObject_New(self, PyObjCObject_kSHOULD_NOT_RELEASE, NO);
}

+ (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    return (PyObject*)PyObjCClass_New(self);
}
@end /* PyObjCSupport */

@interface
Protocol (PyObjCSupport)
- (PyObject* _Nullable)__pyobjc_PythonObject__;
- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie;
@end /* PyObjCSupport */

@implementation
Protocol (PyObjCSupport)

- (PyObject* _Nullable)__pyobjc_PythonObject__
{
    PyObject* rval;

    rval = PyObjC_FindPythonProxy(self);
    if (rval == NULL) {
        rval = PyObjCFormalProtocol_ForProtocol(self);
    }
    return rval;
}

- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie
{
    PyObject* rval;

    *cookie = 0;
    rval    = PyObjC_FindPythonProxy(self);
    if (rval == NULL) {
        rval = PyObjCFormalProtocol_ForProtocol(self);
    }
    return rval;
}

@end /* PyObjCSupport */

@interface
NSString (PyObjCSupport)
- (PyObject* _Nullable)__pyobjc_PythonObject__;
- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie;
@end /* NSString (PyObjCSupport) */

@implementation
NSString (PyObjCSupport)

- (PyObject* _Nullable)__pyobjc_PythonObject__
{
    /* This creates a new proxy every time a string
     * value is proxied to Python. That ensures that
     * changes to mutable strings get reflected in
     * the python value sooner.
     *
     * This means that the 'is' operator won't work
     * for string proxies.
     *
     * Current behaviour has been here for a long time
     * and changing this likely breaks code.
     */
    return (PyObject*)PyObjCUnicode_New(self);
}

- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    return (PyObject*)PyObjCUnicode_New(self);
}

@end /* NSString (PyObjCSupport) */

@interface
NSNumber (PyObjCSupport)
- (PyObject* _Nullable)__pyobjc_PythonObject__;
- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie;
@end /* NSNumber (PyObjCSupport) */

@implementation
NSNumber (PyObjCSupport)
- (PyObject* _Nullable)__pyobjc_PythonObject__
{
    PyObject* rval;

    /* shortcut for booleans */
    if (kCFBooleanTrue == (CFBooleanRef)self) {
        Py_INCREF(Py_True);
        return Py_True;

    } else if (kCFBooleanFalse == (CFBooleanRef)self) {
        Py_INCREF(Py_False);
        return Py_False;
    }

    rval = PyObjC_FindPythonProxy(self);
    if (rval == NULL) {
        rval = PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);

        if (PyObjC_NSNumberWrapper && rval) {
            PyObject* val = rval;

            PyObject* args[2] = {NULL, val};
            rval              = PyObject_Vectorcall(PyObjC_NSNumberWrapper, args + 1,
                                                    1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
            Py_DECREF(val);
        }
    }
    return rval;
}

- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    return [self __pyobjc_PythonObject__];
}
@end

@interface
NSDecimalNumber (PyObjCSupport)
- (PyObject* _Nullable)__pyobjc_PythonObject__;
- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie;
@end /* NSDecimalNumber (PyObjCSupport) */

@implementation
NSDecimalNumber (PyObjCSupport)
- (PyObject* _Nullable)__pyobjc_PythonObject__
{
    PyObject* rval;

    rval = PyObjC_FindPythonProxy(self);
    if (rval == NULL) {
        rval = (PyObject*)PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
        if (rval != NULL) {
            PyObjC_RegisterPythonProxy(self, rval);
        }
    }

    return rval;
}

- (PyObject* _Nullable)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    return [self __pyobjc_PythonObject__];
}
@end

#ifdef MAX
#undef MAX
#endif

static inline Py_ssize_t
MAX(Py_ssize_t x, Py_ssize_t y)
{
    return x > y ? x : y;
}

static inline Py_ssize_t
ROUND(Py_ssize_t v, Py_ssize_t a)
{
    if (v % a == 0) {
        return v;

    } else {
        return v + a - (v % a);
    }
}

#define VECTOR_TO_PYTHON(ctype, elemcount, convertelem)                                  \
    static PyObject* _Nullable ctype##_as_tuple(const void* _pvalue)                     \
    {                                                                                    \
        const ctype value;                                     \
        memcpy((void*)&value, _pvalue, sizeof(ctype)); \
        PyObject*    rv     = PyTuple_New(elemcount);                                    \
        if (rv == NULL) {                                                                \
            return NULL;                                                                 \
        }                                                                                \
                                                                                         \
        for (Py_ssize_t i = 0; i < elemcount; i++) {                                     \
            PyObject* elem = convertelem(value[i]);                                  \
            if (elem == NULL) {                                                          \
                Py_DECREF(rv);                                                           \
                return NULL;                                                             \
            }                                                                            \
            PyTuple_SET_ITEM(rv, i, elem);                                               \
        }                                                                                \
                                                                                         \
        return rv;                                                                       \
    }

#define VECTOR_FROM_PYTHON(ctype, elemcount, convertelem)                                \
    static int ctype##_from_python(PyObject* py, void* _pvalue)                          \
    {                                                                                    \
        ctype value;                                                 \
                                                                                         \
        if (!PySequence_Check(py) || PySequence_Length(py) != elemcount) {               \
            PyErr_SetString(PyExc_ValueError,                                            \
                            "Expecting value with " #elemcount " elements");             \
            return -1;                                                                   \
        }                                                                                \
                                                                                         \
        for (Py_ssize_t i = 0; i < elemcount; i++) {                                     \
            PyObject* e = PySequence_GetItem(py, i);                                     \
            if (e == NULL) {                                                             \
                return -1;                                                               \
            }                                                                            \
            value[i] = convertelem(e);                                               \
            Py_DECREF(e);                                                                \
            if (PyErr_Occurred()) {                                                      \
                return -1;                                                               \
            }                                                                            \
        }                                                                                \
        memcpy(_pvalue, (void*)&value, sizeof(ctype)); \
        return 0;                                                                        \
    }

VECTOR_TO_PYTHON(vector_uchar16, 16, PyLong_FromLong)
VECTOR_TO_PYTHON(vector_short2, 2, PyLong_FromLong)
VECTOR_TO_PYTHON(vector_ushort2, 2, PyLong_FromLong)
VECTOR_TO_PYTHON(vector_ushort3, 3, PyLong_FromLong)
VECTOR_TO_PYTHON(vector_ushort4, 4, PyLong_FromLong)
VECTOR_TO_PYTHON(vector_int2, 2, PyLong_FromLong)
VECTOR_TO_PYTHON(vector_int3, 3, PyLong_FromLong)
VECTOR_TO_PYTHON(vector_int4, 4, PyLong_FromLong)
VECTOR_TO_PYTHON(vector_uint2, 2, PyLong_FromLong)
VECTOR_TO_PYTHON(vector_uint3, 3, PyLong_FromLong)
VECTOR_TO_PYTHON(vector_float2, 2, PyFloat_FromDouble)
VECTOR_TO_PYTHON(vector_float3, 3, PyFloat_FromDouble)
VECTOR_TO_PYTHON(vector_float4, 4, PyFloat_FromDouble)
VECTOR_TO_PYTHON(vector_double2, 2, PyFloat_FromDouble)
VECTOR_TO_PYTHON(vector_double3, 3, PyFloat_FromDouble)
VECTOR_TO_PYTHON(vector_double4, 4, PyFloat_FromDouble)

VECTOR_FROM_PYTHON(vector_uchar16, 16, PyLong_AsLong)
VECTOR_FROM_PYTHON(vector_short2, 2, PyLong_AsLong)
VECTOR_FROM_PYTHON(vector_ushort2, 2, PyLong_AsLong)
VECTOR_FROM_PYTHON(vector_ushort3, 3, PyLong_AsLong)
VECTOR_FROM_PYTHON(vector_ushort4, 4, PyLong_AsLong)
VECTOR_FROM_PYTHON(vector_int2, 2, (int)PyLong_AsLong)
VECTOR_FROM_PYTHON(vector_int3, 3, (int)PyLong_AsLong)
VECTOR_FROM_PYTHON(vector_int4, 4, (int)PyLong_AsLong)
VECTOR_FROM_PYTHON(vector_uint2, 2, (unsigned int)PyLong_AsLong)
VECTOR_FROM_PYTHON(vector_uint3, 3, (unsigned int)PyLong_AsLong)
VECTOR_FROM_PYTHON(vector_float2, 2, PyFloat_AsDouble)
VECTOR_FROM_PYTHON(vector_float3, 3, PyFloat_AsDouble)
VECTOR_FROM_PYTHON(vector_float4, 4, PyFloat_AsDouble)
VECTOR_FROM_PYTHON(vector_double2, 2, PyFloat_AsDouble)
VECTOR_FROM_PYTHON(vector_double3, 3, PyFloat_AsDouble)
VECTOR_FROM_PYTHON(vector_double4, 4, PyFloat_AsDouble)

static struct vector_info {
    char*      encoding;
    Py_ssize_t size;
    Py_ssize_t align;
    PyObject* _Nullable pytype;
    PyObject* _Nullable (*as_tuple)(const void*);
    int (*from_python)(PyObject*, void*);
} gVectorInfo[] = {{
                       .encoding    = "<16C>",
                       .size        = sizeof(vector_uchar16),
                       .align       = __alignof__(vector_uchar16),
                       .pytype      = NULL,
                       .as_tuple    = vector_uchar16_as_tuple,
                       .from_python = vector_uchar16_from_python,
                   },
                   {
                       .encoding    = "<2s>",
                       .size        = sizeof(vector_short2),
                       .align       = __alignof__(vector_short2),
                       .pytype      = NULL,
                       .as_tuple    = vector_short2_as_tuple,
                       .from_python = vector_short2_from_python,
                   },
                   {
                       .encoding    = "<2S>",
                       .size        = sizeof(vector_ushort2),
                       .align       = __alignof__(vector_ushort2),
                       .pytype      = NULL,
                       .as_tuple    = vector_ushort2_as_tuple,
                       .from_python = vector_ushort2_from_python,
                   },
                   {
                       .encoding    = "<3S>",
                       .size        = sizeof(vector_ushort3),
                       .align       = __alignof__(vector_ushort3),
                       .pytype      = NULL,
                       .as_tuple    = vector_ushort3_as_tuple,
                       .from_python = vector_ushort3_from_python,
                   },
                   {
                       .encoding    = "<4S>",
                       .size        = sizeof(vector_ushort4),
                       .align       = __alignof__(vector_ushort4),
                       .pytype      = NULL,
                       .as_tuple    = vector_ushort4_as_tuple,
                       .from_python = vector_ushort4_from_python,
                   },
                   {
                       .encoding    = "<2i>",
                       .size        = sizeof(vector_int2),
                       .align       = __alignof__(vector_int2),
                       .pytype      = NULL,
                       .as_tuple    = vector_int2_as_tuple,
                       .from_python = vector_int2_from_python,
                   },
                   {
                       .encoding    = "<3i>",
                       .size        = sizeof(vector_int3),
                       .align       = __alignof__(vector_int3),
                       .pytype      = NULL,
                       .as_tuple    = vector_int3_as_tuple,
                       .from_python = vector_int3_from_python,
                   },
                   {
                       .encoding    = "<4i>",
                       .size        = sizeof(vector_int4),
                       .align       = __alignof__(vector_int4),
                       .pytype      = NULL,
                       .as_tuple    = vector_int4_as_tuple,
                       .from_python = vector_int4_from_python,
                   },
                   {
                       .encoding    = "<2I>",
                       .size        = sizeof(vector_uint2),
                       .align       = __alignof__(vector_uint2),
                       .pytype      = NULL,
                       .as_tuple    = vector_uint2_as_tuple,
                       .from_python = vector_uint2_from_python,
                   },
                   {
                       .encoding    = "<3I>",
                       .size        = sizeof(vector_uint3),
                       .align       = __alignof__(vector_uint3),
                       .pytype      = NULL,
                       .as_tuple    = vector_uint3_as_tuple,
                       .from_python = vector_uint3_from_python,
                   },
                   {
                       .encoding    = "<2f>",
                       .size        = sizeof(vector_float2),
                       .align       = __alignof__(vector_float2),
                       .pytype      = NULL,
                       .as_tuple    = vector_float2_as_tuple,
                       .from_python = vector_float2_from_python,
                   },
                   {
                       .encoding    = "<3f>",
                       .size        = sizeof(vector_float3),
                       .align       = __alignof__(vector_float3),
                       .pytype      = NULL,
                       .as_tuple    = vector_float3_as_tuple,
                       .from_python = vector_float3_from_python,
                   },
                   {
                       .encoding    = "<4f>",
                       .size        = sizeof(vector_float4),
                       .align       = __alignof__(vector_float4),
                       .pytype      = NULL,
                       .as_tuple    = vector_float4_as_tuple,
                       .from_python = vector_float4_from_python,
                   },
                   {
                       .encoding    = "<2d>",
                       .size        = sizeof(vector_double2),
                       .align       = __alignof__(vector_double2),
                       .pytype      = NULL,
                       .as_tuple    = vector_double2_as_tuple,
                       .from_python = vector_double2_from_python,
                   },
                   {
                       .encoding    = "<3d>",
                       .size        = sizeof(vector_double3),
                       .align       = __alignof__(vector_double3),
                       .pytype      = NULL,
                       .as_tuple    = vector_double3_as_tuple,
                       .from_python = vector_double3_from_python,
                   },
                   {
                       .encoding    = "<4d>",
                       .size        = sizeof(vector_double4),
                       .align       = __alignof__(vector_double4),
                       .pytype      = NULL,
                       .as_tuple    = vector_double4_as_tuple,
                       .from_python = vector_double4_from_python,
                   },
                   {
                       NULL, -1, -1, NULL, NULL, NULL /* Sentinel */
                   }};

/* XXX: This lookup function is fairly inefficient */
static struct vector_info*
vector_lookup(const char* type)
{
    const char* end = type;
    while (*end && *end != _C_VECTOR_E)
        end++;
    end++;

    struct vector_info* cur = gVectorInfo;
    while (cur->encoding != NULL) {
        if (strncmp(cur->encoding, type, end - type) == 0) {
            return cur;
        }
        cur++;
    }

    PyErr_Format(PyObjCExc_InternalError, "Unsupported SIMD encoding: %s", type);
    return cur;
}

int
PyObjCRT_RegisterVectorType(const char* typestr, PyObject* pytype)
{
    struct vector_info* info = vector_lookup(typestr);
    if (PyErr_Occurred()) {
        return -1;
    }

    if (info->pytype) {
        Py_CLEAR(info->pytype);
    }
    info->pytype = pytype;
    Py_INCREF(pytype);
    return 0;
}

const char*
PyObjCRT_SkipTypeQualifiers(const char* type)
{
    while (*type == _C_CONST || *type == _C_IN || *type == _C_INOUT || *type == _C_OUT
           || *type == _C_BYCOPY || *type == _C_BYREF || *type == _C_ONEWAY
           || *type == 'O' || *type == _C_ATOMIC) {
        type++;
    }
    while (*type && isdigit(*type)) { // LCOV_BR_EXCL_LINE
        /* XXX: There are no digits in after type qualifiers!. */
        type++; // LCOV_EXCL_LINE
    }
    return type;
}

const char* _Nullable PyObjCRT_SkipTypeSpec(const char* start_type)
{
    PyObjC_Assert(start_type != NULL, NULL);
    const char* type = start_type;

    type = PyObjCRT_SkipTypeQualifiers(type);

    switch (*type) {
    case '"':
        /* Embedded name in ivar or compound type */
        type++;
        while (*type != '\0' && *type != '"')
            type++;
        break;

    /* The following are one character type codes */
    case _C_UNDEF:
    case _C_CLASS:
    case _C_SEL:
    case _C_CHR:
    case _C_UCHR:
    case _C_CHARPTR:
#ifdef _C_ATOM
    case _C_ATOM:
#endif
    case _C_BOOL:
    case _C_NSBOOL:
    case _C_SHT:
    case _C_USHT:
    case _C_INT:
    case _C_UINT:
    case _C_LNG:
    case _C_ULNG:
    case _C_FLT:
    case _C_DBL:
    case _C_VOID:
    case _C_LNG_LNG:
    case _C_ULNG_LNG:
    case _C_UNICHAR:
    case _C_CHAR_AS_TEXT:
    case _C_CHAR_AS_INT:
        ++type;
        break;

    case _C_BFLD:
        while (isdigit(*++type))
            ;
        break;

    case _C_ID:
        ++type;
        if (*type == '?') {
            /* Block pointer */
            type++;
        }
        break;

    case _C_VECTOR_B:
        /* Skip length specifier,  type and _C_VECTOR_E */
        while (isdigit(*++type))
            ;
        type = PyObjCRT_SkipTypeSpec(type);
        if (type && *type != _C_VECTOR_E) {
            PyErr_Format(PyObjCExc_InternalError,
                         "Invalid SIMD definition in type signature: %s", start_type);
            return NULL;
        }
        if (type)
            type++;
        break;

    case _C_ARY_B:
        /* skip digits, typespec and closing ']' */

        while (isdigit(*++type))
            ;
        type = PyObjCRT_SkipTypeSpec(type);
        if (type && *type != _C_ARY_E) {
            PyErr_Format(PyObjCExc_InternalError,
                         "Invalid array definition in type signature: %s", start_type);
            return NULL;
        }
        if (type)
            type++;
        break;

    case _C_STRUCT_B:
        /* skip name, and elements until closing '}'  */
        while (*type && *type != _C_STRUCT_E && *type++ != '=')
            ;
        while (type && *type && *type != _C_STRUCT_E) {
            if (*type == '"') {
                /* embedded field names */
                type = strchr(type + 1, '"');
                if (type != NULL) {
                    type++;
                } else {
                    PyErr_Format(PyExc_ValueError,
                                 "Invalid struct definition in type signature: %s",
                                 start_type);
                    return NULL;
                }
            }
            type = PyObjCRT_SkipTypeSpec(type);
        }
        if (type && *type != _C_STRUCT_E) {
            PyErr_Format(PyExc_ValueError,
                         "Invalid struct definition in type signature: %s", start_type);
            return NULL;
        }
        if (type)
            type++;
        break;

    case _C_UNION_B:
        /* skip name, and elements until closing ')'  */
        while (*type && *type != _C_UNION_E && *type++ != '=')
            ;
        while (type && *type && *type != _C_UNION_E) {
            if (*type == '"') {
                /* embedded field names */
                type = strchr(type + 1, '"');
                if (type != NULL) {
                    type++;
                } else {
                    PyErr_Format(PyObjCExc_InternalError,
                                 "Invalid union definition in type signature: '%s'",
                                 start_type);
                    return NULL;
                }
            }
            type = PyObjCRT_SkipTypeSpec(type);
        }
        if (type && *type != _C_UNION_E) {
            PyErr_Format(PyObjCExc_InternalError,
                         "Invalid union definition in type signature: '%s'", start_type);
            return NULL;
        }
        if (type)
            type++;
        break;

    case _C_PTR:
    case _C_CONST:
    case _C_IN:
    case _C_INOUT:
    case _C_OUT:
    case _C_BYCOPY:
    case _C_BYREF:
    case _C_ONEWAY:
        if (type[1] == '\0') {
            PyErr_Format(PyObjCExc_InternalError, "Incomplete type signature: '%s'",
                         start_type);
            return NULL;
        }

        /* Just skip the following typespec */
        type = PyObjCRT_SkipTypeSpec(type + 1);
        break;

    case '\0':
        return type;

    default:
        PyErr_Format(PyObjCExc_InternalError,
                     "PyObjCRT_SkipTypeSpec: Unhandled type '0x%x' %s", *type, type);
        return NULL;
    }

    /* The compiler inserts a number after the actual signature,
     * this number may or may not be useful depending on the compiler
     * version. We never use it.
     */
    while (type && *type && isdigit(*type))
        type++;
    return type;
}

/* XXX: How is this different from SKipTypeSpec (prev. function) */
const char* _Nullable PyObjCRT_NextField(const char* start_type)
{
    PyObjC_Assert(start_type != NULL, NULL);

    const char* type = start_type;

    type = PyObjCRT_SkipTypeQualifiers(type);

    switch (*type) {
    /* The following are one character type codes */
    case _C_UNDEF:
    case _C_CLASS:
    case _C_SEL:
    case _C_CHR:
    case _C_UCHR:
    case _C_CHARPTR:
#ifdef _C_ATOM
    case _C_ATOM:
#endif
    case _C_BOOL:
    case _C_NSBOOL:
    case _C_SHT:
    case _C_USHT:
    case _C_INT:
    case _C_UINT:
    case _C_LNG:
    case _C_ULNG:
    case _C_FLT:
    case _C_DBL:
    case _C_VOID:
    case _C_LNG_LNG:
    case _C_ULNG_LNG:
    case _C_UNICHAR:
    case _C_CHAR_AS_TEXT:
    case _C_CHAR_AS_INT:
    case _C_BFLD: /* Not really 1 character, but close enough  */
        ++type;
        break;

    case _C_ID:
        ++type;
        break;

    case _C_ARY_B:
        /* skip digits, typespec and closing ']' */

        while (isdigit(*++type))
            ;
        type = (const char* _Nonnull)PyObjCRT_SkipTypeSpec(type);
        if (unlikely(type == NULL)) {
            if (!PyErr_Occurred()) {
                /* XXX: Can this happen? */
                PyErr_SetString(PyObjCExc_InternalError,
                                "Unexpected NULL while parsing array encoding type");
            }
            return NULL;
        } else if (unlikely(*type != _C_ARY_E)) {
            PyErr_Format(PyObjCExc_InternalError,
                         "PyObjCRT_SkipTypeSpec: Got '0x%x' at end of array encoding, "
                         "expecting '0x%x'",
                         *type, _C_ARY_E);
            return NULL;
        }
        if (type)
            type++;
        break;

    case _C_STRUCT_B:
        /* skip name, and elements until closing '}'  */
        while (*type && *type != _C_STRUCT_E && *type++ != '=')
            ;
        while (type && *type && *type != _C_STRUCT_E) {
            if (*type == '"') {
                /* embedded field names */
                type = strchr(type + 1, '"');
                if (type != NULL) {
                    type++;
                } else {
                    PyErr_SetString(PyObjCExc_InternalError,
                                    "Struct with invalid embedded field name");
                    return NULL;
                }
            }
            type = PyObjCRT_SkipTypeSpec(type);
        }
        if (unlikely(type == NULL)) {
            if (!PyErr_Occurred()) {
                PyErr_SetString(PyObjCExc_InternalError,
                                "Unexpected NULL while parsing struct encoding type");
            }
            return NULL;
        } else if (unlikely(*type != _C_STRUCT_E)) {
            PyErr_Format(PyObjCExc_InternalError,
                         "PyObjCRT_SkipTypeSpec: Got '0x%x' at end of struct encoding, "
                         "expecting '0x%x'",
                         *type, _C_STRUCT_E);
            return NULL;
        }
        type++;
        break;

    case _C_UNION_B:
        /* skip name, and elements until closing ')'  */
        while (*type && *type != _C_UNION_E && *type++ != '=')
            ;
        while (type && *type && *type != _C_UNION_E) {
            if (*type == '"') {
                /* embedded field names */
                type = strchr(type + 1, '"');
                if (type != NULL) {
                    type++;
                } else {
                    return NULL;
                }
            }
            type = PyObjCRT_SkipTypeSpec(type);
        }
        if (unlikely(type == NULL)) {
            if (!PyErr_Occurred()) {
                PyErr_SetString(PyObjCExc_InternalError,
                                "Unexpected NULL while parsing union encoding type");
            }
            return NULL;
        } else if (unlikely(*type != _C_UNION_E)) {
            PyErr_Format(PyObjCExc_InternalError,
                         "PyObjCRT_SkipTypeSpec: Got '0x%x' at end of union encoding, "
                         "expecting '0x%x'",
                         *type, _C_UNION_E);
            return NULL;
        }
        break;

    case _C_PTR:
    case _C_CONST:
    case _C_IN:
    case _C_INOUT:
    case _C_OUT:
    case _C_BYCOPY:
    case _C_BYREF:
    case _C_ONEWAY:

        /* Just skip the following typespec */
        type = PyObjCRT_NextField(type + 1);
        if (type == NULL) {
            return NULL;
        }
        break;

    default:
        PyErr_Format(PyExc_ValueError, "invalid signature: unknown type coding 0x%x",
                     (int)*type);
        return NULL;
    }

    /* The compiler inserts a number after the actual signature,
     * this number may or may not be useful depending on the compiler
     * version. We never use it.
     */
    while (type && *type && isdigit(*type))
        type++;
    return type;
}

/*
Return the alignment of an object specified by type

XXX: The embedded align function is used for the first
member of a struct, and is no longer necessary.
*/

#define PyObjC_EmbeddedAlignOfType PyObjCRT_AlignOfType

Py_ssize_t
PyObjCRT_AlignOfType(const char* start_type)
{
    const char* _Nullable type = start_type;
    PyObjC_Assert(type != NULL, -1);

    switch (*type) {
    case _C_VOID:
        return __alignof__(char);
    case _C_ID:
        return __alignof__(id);
    case _C_CLASS:
        return __alignof__(Class);
    case _C_SEL:
        return __alignof__(SEL);
    case _C_CHR:
        return __alignof__(char);
    case _C_UCHR:
        return __alignof__(unsigned char);
    case _C_SHT:
        return __alignof__(short);
    case _C_USHT:
        return __alignof__(unsigned short);
    case _C_BOOL:
    case _C_NSBOOL:
        return __alignof__(bool);
    case _C_UNICHAR:
        return __alignof__(UniChar);
    case _C_CHAR_AS_TEXT:
        return __alignof__(char);
    case _C_CHAR_AS_INT:
        return __alignof__(char);
    case _C_INT:
        return __alignof__(int);
    case _C_UINT:
        return __alignof__(unsigned int);
    case _C_LNG:
    case _C_LNG_LNG:
        return __alignof__(long);
    case _C_ULNG:
    case _C_ULNG_LNG:
        return __alignof__(unsigned long);
    case _C_FLT:
        return __alignof__(float);
    case _C_DBL:
        return __alignof__(double);
    case _C_CHARPTR:
        return __alignof__(char*);
#ifdef _C_ATOM
    case _C_ATOM:
        return __alignof__(char*);
#endif
    case _C_PTR:
        return __alignof__(void*);

    case _C_VECTOR_B:
        return vector_lookup(type)->align;

    case _C_ARY_B:
        while (isdigit(*++type)) /* do nothing */
            ;
        return PyObjCRT_AlignOfType(type);

    case _C_STRUCT_B: {
        struct {
            int    x;
            double y;
        } fooalign;
        while (*type != _C_STRUCT_E && *type++ != '=') /* do nothing */
            ;
        if (*type != _C_STRUCT_E) {
            int        have_align = 0;
            Py_ssize_t align      = 0;

            while (type != NULL && *type != _C_STRUCT_E) {
                if (*type == '"') {
                    type = strchr(type + 1, '"');
                    if (type == NULL) {
                        PyErr_SetString(
                            PyObjCExc_InternalError,
                            "Struct encoding with invalid embedded field name");
                        return -1;
                    }
                    type++;
                }

                if (have_align) {
                    align = MAX(align, PyObjC_EmbeddedAlignOfType(type));

                } else {
                    align      = PyObjCRT_AlignOfType(type);
                    have_align = 1;
                }
                type = PyObjCRT_SkipTypeSpec(type);
            }

            if (type == NULL)
                return -1;
            return align;

        } else {
            return __alignof__(fooalign);
        }
    }

    case _C_UNION_B: {
        Py_ssize_t maxalign = 0;
        type++;
        while (*type != _C_STRUCT_E && *type++ != '=') /* do nothing */
            ;
        while (*type != _C_UNION_E) {
            Py_ssize_t item_align = PyObjCRT_AlignOfType(type);
            if (item_align == -1) {
                return -1;
            }
            maxalign = MAX(maxalign, item_align);
            type     = PyObjCRT_SkipTypeSpec(type);
            if (type == NULL) {
                return -1;
            }
        }
        return maxalign;
    }

    case _C_CONST:
    case _C_IN:
    case _C_INOUT:
    case _C_OUT:
    case _C_BYCOPY:
    case _C_BYREF:
    case _C_ONEWAY:
        return PyObjCRT_AlignOfType(type + 1);

    case _C_BFLD:
        /* Calculating the alignment of bitfields appears to need information
         * that's not present here. This hack is good enough for now.
         */
        return 4;

    case _C_UNDEF:
        return __alignof__(void*);

    default:
        PyErr_Format(PyObjCExc_InternalError,
                     "PyObjCRT_AlignOfType: Unhandled type '0x%x' %s", *type, type);
        return -1;
    }
}

/*
The aligned size if the size rounded up to the nearest alignment.
*/

Py_ssize_t
PyObjCRT_AlignedSize(const char* type)
{
    PyObjC_Assert(type != NULL, -1);

    Py_ssize_t size  = PyObjCRT_SizeOfType(type);
    Py_ssize_t align = PyObjCRT_AlignOfType(type);

    if (size == -1 || align == -1)
        return -1;
    return ROUND(size, align);
}

/*
return the size of an object specified by type
*/

Py_ssize_t
PyObjCRT_SizeOfType(const char* start_type)
{
    PyObjC_Assert(start_type != NULL, -1);

    const char* _Nullable type = start_type;

    Py_ssize_t itemSize;
    switch (*type) {
    case _C_VOID:
        return 1; // More convenient than the correct value.
    case _C_ID:
        return sizeof(id);
    case _C_CLASS:
        return sizeof(Class);
    case _C_SEL:
        return sizeof(SEL);
    case _C_CHR:
        return sizeof(char);
    case _C_UCHR:
        return sizeof(unsigned char);
    case _C_SHT:
        return sizeof(short);
    case _C_USHT:
        return sizeof(unsigned short);
    case _C_BOOL:
    case _C_NSBOOL:
        return sizeof(bool);
    case _C_INT:
        return sizeof(int);
    case _C_UINT:
        return sizeof(unsigned int);
    case _C_LNG:
    case _C_LNG_LNG:
        return sizeof(long);
    case _C_ULNG:
    case _C_ULNG_LNG:
        return sizeof(unsigned long);
    case _C_FLT:
        return sizeof(float);
    case _C_DBL:
        return sizeof(double);
    case _C_UNICHAR:
        return sizeof(UniChar);
    case _C_CHAR_AS_TEXT:
        return sizeof(char);
    case _C_CHAR_AS_INT:
        return sizeof(char);

    case _C_PTR:
    case _C_CHARPTR:
#ifdef _C_ATOM
    case _C_ATOM:
#endif
        return sizeof(char*);

    case _C_VECTOR_B:
        return vector_lookup(type)->size;

    case _C_ARY_B: {
        Py_ssize_t len = atoi(type + 1);
        Py_ssize_t item_align;
        while (isdigit(*++type))
            ;
        item_align = PyObjCRT_AlignedSize(type);
        if (item_align == -1)
            return -1;
        return len * item_align;
    } break;

    case _C_STRUCT_B: {
        Py_ssize_t acc_size   = 0;
        int        have_align = 0;
        Py_ssize_t align;
        Py_ssize_t max_align = 0;

        /* This is an awfull hack... */
        /*   struct sockaddr is a generic type with several supported
         *   specific types. Annoyingly enough not all of those have the
         *   same size.
         *   This file has crude support for this scheme as its almost
         *   impossible to implement this nicely using our C/Python
         *   API.
         */
        if (strncmp(type, @encode(struct sockaddr), sizeof(@encode(struct sockaddr)) - 1)
            == 0) {

            /* XXX: What about struct sockaddr_un? */
            return sizeof(struct sockaddr_storage);
        }

        if (unlikely(IS_DECIMAL(type))) {
            /* NSDecimal contains embedded bitfields and those
             * aren't handled properly by this code.
             */
            return sizeof(NSDecimal);
        }

        while (*type != _C_STRUCT_E && *type++ != '=')
            ; /* skip "<name>=" */

        while (*type != _C_STRUCT_E) {
            if (*type == '"') {
                type = strchr(type + 1, '"');
                if (type == NULL) {
                    PyErr_Format(PyObjCExc_InternalError,
                                 "Struct with invalid embedded field name: %s",
                                 start_type);
                    return -1;
                }
                type++;
            }

            if (have_align) {
                align = PyObjC_EmbeddedAlignOfType(type);
                if (align == -1)
                    return -1;

            } else {
                align = PyObjCRT_AlignOfType(type);
                if (align == -1)
                    return -1;
                have_align = 1;
            }

            max_align = MAX(align, max_align);
            acc_size  = ROUND(acc_size, align);

            itemSize = PyObjCRT_SizeOfType(type);
            if (itemSize == -1)
                return -1;
            acc_size += itemSize;
            type = PyObjCRT_SkipTypeSpec(type);
            if (type == NULL) {
                return -1;
            }
        }

        if (max_align) {
            acc_size = ROUND(acc_size, max_align);
        }
        return acc_size;
    }

    case _C_UNION_B: {
        Py_ssize_t max_size = 0;
        type++;
        /* Skip name part: */
        while (*type != _C_UNION_E && *type++ != '=')
            ;

        /* Calculate size: */
        while (*type != _C_UNION_E) {
            itemSize = PyObjCRT_SizeOfType(type);
            if (itemSize == -1)
                return -1;
            max_size = MAX(max_size, itemSize);
            type     = PyObjCRT_SkipTypeSpec(type);
            if (type == NULL) {
                return -1;
            }
        }

        return max_size;
    }

    case _C_CONST:
    case _C_IN:
    case _C_INOUT:
    case _C_OUT:
    case _C_BYCOPY:
    case _C_BYREF:
    case _C_ONEWAY:
        return PyObjCRT_SizeOfType(type + 1);

    case _C_BFLD: {
        long i = strtol(type + 1, NULL, 10);
        return (i + 7) / 8;
    } break;

    case _C_UNDEF:
        return sizeof(void*);

    default:
        PyErr_Format(PyObjCExc_InternalError,
                     "PyObjCRT_SizeOfType: Unhandled type '0x%x', %s", *type, type);
        return -1;
    }
}

extern bool
PyObjCRT_IsValidEncoding(const char* _type, Py_ssize_t type_length)
{
    const char* type     = _type; /* Strip "_Nonnull" */
    const char* end_type = type + type_length;
    if (type_length == 0) {
        return false;
    }

    switch (*type) {
    case _C_UNDEF:
    case _C_VOID:
    case _C_ID:
    case _C_CLASS:
    case _C_SEL:
    case _C_CHR:
    case _C_UCHR:
    case _C_SHT:
    case _C_USHT:
    case _C_BOOL:
    case _C_NSBOOL:
    case _C_INT:
    case _C_UINT:
    case _C_LNG:
    case _C_LNG_LNG:
    case _C_ULNG:
    case _C_ULNG_LNG:
    case _C_FLT:
    case _C_DBL:
    case _C_UNICHAR:
    case _C_CHAR_AS_TEXT:
    case _C_CHAR_AS_INT:
    case _C_CHARPTR:
#ifdef _C_ATOM
    case _C_ATOM:
#endif
        return true;

    case _C_VECTOR_B:
        type++;
        /* Digits */
        while (type < end_type && isdigit(*type)) {
            type++;
        }

        /* Check if there is space for a format char
         * and the closing '>'
         */
        if (type + 1 >= end_type) {
            return false;
        }
        if (type[1] != _C_VECTOR_E) {
            return false;
        }
        return PyObjCRT_IsValidEncoding(type, 1);

    case _C_ARY_B:
        type++;
        type_length--;

        /* Digits */
        while (type < end_type && isdigit(*type)) {
            type++;
        }

        /* Type encoding */
        if (!PyObjCRT_IsValidEncoding(type, end_type - type)) {
            return false;
        }
        type = PyObjCRT_SkipTypeSpec(type);
        if (type == NULL) {
            PyErr_Clear();
            return false;
        }
        if (type >= end_type) {
            return false;
        }
        return *type == _C_ARY_E;

    case _C_STRUCT_B:
        while (type < end_type && *type != _C_STRUCT_E && *type++ != '=') {
            /* skip "<name>=" */
        }

        if (type >= end_type) {
            return false;
        }

        while (type < end_type && *type != _C_STRUCT_E) {
            if (*type == '"') {
                /* XXX: Struct encodings with embedded field names
                 *      are not supported by the only user of this
                 *      API.
                 */
                return false;
            }

            if (!PyObjCRT_IsValidEncoding(type, end_type - type)) {
                return false;
            }

            type = PyObjCRT_SkipTypeSpec(type);
            if (type == NULL) {
                PyErr_Clear();
                return false;
            }
        }
        if (type >= end_type) {
            return false;
        }
        return *type == _C_STRUCT_E;

    case _C_BFLD:
    case _C_UNION_B:
        /* XXX:  The only user of this API does not support
         * bitfields and unions in the first place.
         */
        return false;

    case _C_PTR:
    case _C_CONST:
    case _C_IN:
    case _C_INOUT:
    case _C_OUT:
    case _C_BYCOPY:
    case _C_BYREF:
    case _C_ONEWAY:
        return PyObjCRT_IsValidEncoding(type + 1, type_length - 1);

    default:
        return false;
    }
}

PyObject* _Nullable pythonify_c_array_nullterminated(const char* type, const void* datum,
                                                     BOOL alreadyRetained,
                                                     BOOL alreadyCFRetained)
{
    PyObjC_Assert(type != NULL, NULL);
    PyObjC_Assert(datum != NULL, NULL);

    Py_ssize_t           count      = 0;
    Py_ssize_t           sizeofitem = PyObjCRT_SizeOfType(type);
    const unsigned char* curdatum   = datum;

    type = PyObjCRT_SkipTypeQualifiers(type);

    switch (*type) {
    case _C_CHARPTR:
        while (*(const char**)curdatum != NULL) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    case _C_ID:
        while (*(const id*)curdatum != NULL) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    case _C_PTR:
        while (*(const void**)curdatum != NULL) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    case _C_UCHR:
        while (*(const unsigned char*)curdatum != 0) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    case _C_VOID:
    case _C_CHR:
        return PyBytes_FromString((const char*)curdatum);
        break;

    case _C_CHAR_AS_TEXT:
        return PyBytes_FromString((const char*)curdatum);
        break;

    case _C_USHT:
        while (*(const unsigned short*)curdatum != 0) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    case _C_SHT:
        while (*(const short*)curdatum != 0) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    case _C_UINT:
        while (*(const unsigned int*)curdatum != 0) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    case _C_INT:
        while (*(const int*)curdatum != 0) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    case _C_ULNG:
    case _C_ULNG_LNG:
        while (*(const unsigned long*)curdatum != 0) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    case _C_LNG:
    case _C_LNG_LNG:
        while (*(const long*)curdatum != 0) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    case _C_UNICHAR:
        while (*(const UniChar*)curdatum != 0) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    case _C_CHAR_AS_INT:
        while (*(const char*)curdatum != 0) {
            count++;
            curdatum += sizeofitem;
        }
        break;

    default:
        PyErr_Format(PyExc_TypeError, "Cannot deal with NULL-terminated array of %s",
                     type);
        return NULL;
    }

    if (*type == _C_UNICHAR) {
        int byteorder = 0;
        return PyUnicode_DecodeUTF16((const char*)datum, count * 2, NULL, &byteorder);
    }

    return PyObjC_CArrayToPython2(type, datum, count, alreadyRetained, alreadyCFRetained);
}

/*#F Returns a tuple of objects representing the content of a C array
of type @var{type} pointed by @var{datum}. */
static PyObject* _Nullable pythonify_c_array(const char* type, const void* datum)
{
    PyObjC_Assert(type != NULL, NULL);
    PyObjC_Assert(datum != NULL, NULL);

    PyObject*            ret;
    Py_ssize_t           nitems, itemidx, sizeofitem;
    const unsigned char* curdatum;

    nitems = atoi(type + 1);
    while (isdigit(*++type))
        ;
    sizeofitem = PyObjCRT_SizeOfType(type);
    if (sizeofitem == -1)
        return NULL;

    ret = PyTuple_New(nitems);
    if (!ret)        // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE

    curdatum = datum;
    for (itemidx = 0; itemidx < nitems; itemidx++) {
        PyObject* pyitem = NULL;

        pyitem = pythonify_c_value(type, curdatum);

        if (pyitem) {
            PyTuple_SET_ITEM(ret, itemidx, pyitem);

        } else {
            Py_DECREF(ret);
            return NULL;
        }

        curdatum += sizeofitem;
    }

    return ret;
}

/*#F Returns a tuple of objects representing the content of a C structure
of type @var{type} pointed by @var{datum}. */
static PyObject* _Nullable pythonify_c_struct(const char* type, const void* datum)
{
    PyObjC_Assert(type != NULL, NULL);
    PyObjC_Assert(datum != NULL, NULL);

    PyObject*   ret;
    Py_ssize_t  offset, itemidx;
    const char* item;
    int         have_align = 0;
    Py_ssize_t  align;
    int         haveTuple;
    const char* type_start = type;
    const char* type_end   = PyObjCRT_SkipTypeSpec(type);
    Py_ssize_t  pack       = -1;

    if (type_end == NULL) {
        return NULL;
    }

    /* Hacked up support for socket addresses */
    if (strncmp(type, @encode(struct sockaddr), sizeof(@encode(struct sockaddr)) - 1)
        == 0) {
        return PyObjC_SockAddrToPython(datum);
    }

    if (IS_FSREF(type)) {
        return PyObjC_decode_fsref(datum);
    }

    if (IS_DECIMAL(type)) {
        return pythonify_nsdecimal(datum);
    }
    if (IS_AUTHORIZATIONITEM(type)) {
        return pythonify_authorizationitem(datum);
    }

    /* The compiler adds useless digits at the end of the signature */
    while (type_end != type_start + 1 && type_end[-1] != _C_STRUCT_E) {
        type_end--;
    }

    while (*type != _C_STRUCT_E && *type++ != '=') {
        /* skip "<name>=" */
    }

    haveTuple              = 0;
    const char* oc_typestr = NULL;
    ret = PyObjC_CreateRegisteredStruct(type_start, type_end - type_start, &oc_typestr,
                                        &pack);
    if (ret == NULL) {
        int nitems;

        nitems = 0;
        item   = type;
        while (*item != _C_STRUCT_E) {
            nitems++;
            if (*item == '"') {
                item = strchr(item + 1, '"');
                if (item == NULL) {
                    PyErr_SetString(PyObjCExc_InternalError,
                                    "Struct encoding with invalid embedded field");
                    return NULL;
                }
                item++;
            }
            item = PyObjCRT_SkipTypeSpec(item);
            if (item == NULL) {
                return NULL;
            }
        }

        haveTuple = 1;
        ret       = PyTuple_New(nitems);
        if (!ret)        // LCOV_BR_EXCL_LINE
            return NULL; // LCOV_EXCL_LINE

        item = type;

    } else {
        item = type;

        if (oc_typestr != NULL) {
            item = oc_typestr + 1;
            while (*item && *item != '=') {
                item++;
            }
            if (*item) {
                item++;
            }
        }
    }

    offset = itemidx = 0;
    while (*item != _C_STRUCT_E) {
        PyObject* pyitem;

        if (*item == '"') {
            item = strchr(item + 1, '"');
            if (item == NULL) {
                /* Invalid emmbedded name */
                PyErr_Format(PyObjCExc_InternalError,
                             "Encoding with invalid embedded name");
                Py_DECREF(ret);
                return NULL;
            } else {
                item++;
            }
        }

        if (!have_align) {
            align      = PyObjCRT_AlignOfType(item);
            have_align = 1;

        } else {
            align = PyObjC_EmbeddedAlignOfType(item);
        }

        if (pack != -1 && pack < align) {
            align = pack;
        }

        offset = ROUND(offset, align);

        pyitem = pythonify_c_value(item, ((char*)datum) + offset);

        if (pyitem) {
            if (haveTuple) {
                PyTuple_SET_ITEM(ret, itemidx, pyitem);

            } else {
                int r;
                r = PyObjC_SetStructField(ret, itemidx, pyitem);
                Py_DECREF(pyitem);

                if (r == -1) {
                    Py_DECREF(ret);
                    return NULL;
                }
            }

        } else {
            Py_DECREF(ret);
            return NULL;
        }

        itemidx++;
        offset += PyObjCRT_SizeOfType(item);
        item = PyObjCRT_SkipTypeSpec(item);
        if (item == NULL) {
            Py_DECREF(ret);
            return NULL;
        }
    }

    return ret;
}

int
depythonify_c_return_array_count(const char* rettype, Py_ssize_t count, PyObject* arg,
                                 void* resp, BOOL already_retained,
                                 BOOL already_cfretained)
{
    PyObjC_Assert(rettype != NULL, -1);
    PyObjC_Assert(arg != NULL, -1);
    PyObjC_Assert(resp != NULL, -1);

    /* Use an NSMutableData object to store the bytes, that way we can autorelease the
     * data because we cannot free it otherwise.
     */
    PyObject* seq = PySequence_Fast(arg, "Sequence required");
    if (seq == NULL) {
        return -1;
    }

    if (count == -1) {
        count = PySequence_Fast_GET_SIZE(seq);
    }

    NSMutableData* data =
        [NSMutableData dataWithLength:count * PyObjCRT_SizeOfType(rettype)];
    *(void**)resp = [data mutableBytes];
    int r = depythonify_c_array_count(rettype, count, YES, seq, [data mutableBytes],
                                      already_retained, already_cfretained);
    Py_DECREF(seq);

    return r;
}

int
depythonify_c_return_array_nullterminated(const char* rettype, PyObject* arg, void* resp,
                                          BOOL already_retained, BOOL already_cfretained)
{
    PyObjC_Assert(rettype != NULL, -1);
    PyObjC_Assert(arg != NULL, -1);
    PyObjC_Assert(resp != NULL, -1);

    /* Use an NSMutableData object to store the bytes, that way we can autorelease the
     * data because we cannot free it otherwise.
     */
    if (*rettype == _C_CHR || *rettype == _C_CHAR_AS_TEXT || *rettype == _C_VOID) {
        if (PyBytes_Check(arg)) {
            NSMutableData* data = [NSMutableData dataWithBytes:PyBytes_AsString(arg)
                                                        length:PyBytes_Size(arg)];
            *(void**)resp       = [data mutableBytes];
            return 0;

#ifdef PyByteArray_Check
        } else if (PyByteArray_Check(arg)) {
            NSMutableData* data = [NSMutableData dataWithBytes:PyByteArray_AsString(arg)
                                                        length:PyByteArray_Size(arg)];
            *(void**)resp       = [data mutableBytes];
            return 0;
#endif
        }
    }

    PyObject* seq = PySequence_Fast(arg, "Sequence required");
    if (seq == NULL) {
        return -1;
    }

    Py_ssize_t count = PySequence_Fast_GET_SIZE(seq);

    /* The data is 0-filled, which means we won't have to add the terminated ourselves */
    NSMutableData* data =
        [NSMutableData dataWithLength:(count + 1) * PyObjCRT_SizeOfType(rettype)];
    *(void**)resp = [data mutableBytes];
    int result = depythonify_c_array_count(rettype, count, YES, seq, [data mutableBytes],
                                           already_retained, already_cfretained);
    Py_DECREF(seq);
    return result;
}

int
depythonify_c_array_count(const char* type, Py_ssize_t nitems, BOOL strict,
                          PyObject* value, void* datum, BOOL already_retained,
                          BOOL already_cfretained)
{
    PyObjC_Assert(type != NULL, -1);
    PyObjC_Assert(value != NULL, -1);
    PyObjC_Assert(datum != NULL, -1);

    Py_ssize_t     itemidx, sizeofitem;
    unsigned char* curdatum;
    PyObject*      seq;

    sizeofitem = PyObjCRT_AlignedSize(type);
    if (sizeofitem == -1) {
        PyErr_Format(PyExc_ValueError, "cannot depythonify array of unknown type");
        return -1;
    }

    if (sizeofitem == 1 && PyBytes_Check(value)) {
        /* Special casing for strings */
        if (strict) {
            if (PyBytes_Size(value) != nitems) {
                PyErr_Format(PyExc_ValueError,
                             "depythonifying array of %" PY_FORMAT_SIZE_T
                             "d items, got one of %" PY_FORMAT_SIZE_T "d",
                             nitems, PyBytes_Size(value));
                return -1;
            }

        } else {
            if (PyBytes_Size(value) < nitems) {
                PyErr_Format(PyExc_ValueError,
                             "depythonifying array of %" PY_FORMAT_SIZE_T
                             "d items, got one of %" PY_FORMAT_SIZE_T "d",
                             nitems, PyBytes_Size(value));
                return -1;
            }
        }

        memcpy(datum, PyBytes_AS_STRING(value), nitems);
        return 0;
    }

    seq = PySequence_Fast(value, "depythonifying array, got no sequence");
    if (seq == NULL) {
        return -1;
    }

    if (strict) {
        if (PySequence_Fast_GET_SIZE(seq) != nitems) {
            PyErr_Format(PyExc_ValueError,
                         "depythonifying array of %" PY_FORMAT_SIZE_T
                         "d items, got one of %" PY_FORMAT_SIZE_T "d",
                         nitems, PySequence_Fast_GET_SIZE(seq));
            Py_DECREF(seq);
            return -1;
        }

    } else {
        if (PySequence_Fast_GET_SIZE(seq) < nitems) {
            PyErr_Format(PyExc_ValueError,
                         "depythonifying array of %" PY_FORMAT_SIZE_T
                         "d items, got one of %" PY_FORMAT_SIZE_T "d",
                         nitems, PySequence_Fast_GET_SIZE(seq));
            Py_DECREF(seq);
            return -1;
        }
    }

    curdatum = datum;
    for (itemidx = 0; itemidx < nitems; itemidx++) {
        PyObject* pyarg = PySequence_Fast_GET_ITEM(seq, itemidx);
        int       err;

        err = depythonify_c_value(type, pyarg, curdatum);
        if (err == -1) {
            Py_DECREF(seq);
            return err;
        }

        if (already_retained) {
            [*(NSObject**)curdatum retain];

        } else if (already_cfretained) {
            CFRetain(*(NSObject**)curdatum);
        }

        curdatum += sizeofitem;
    }

    if (*type == _C_CHARPTR) {
        /* We're depythonifying a list of strings, make sure the originals stay
         * around long enough.
         */
        [[[OC_PythonObject alloc] initWithPyObject:seq] autorelease];
    }
    Py_DECREF(seq);
    return 0;
}

Py_ssize_t
c_array_nullterminated_size(PyObject* object, PyObject** seq)
{
    PyObjC_Assert(object != NULL, -1);
    PyObjC_Assert(seq != NULL, -1);

    *seq = PySequence_Fast(object, "depythonifying array, got no sequence");
    if (*seq == NULL) {
        return -1;
    }

    return PySequence_Fast_GET_SIZE(*seq) + 1;
}

int
depythonify_c_array_nullterminated(const char* type, Py_ssize_t count, PyObject* value,
                                   void* datum, BOOL already_retained,
                                   BOOL already_cfretained)
{
    PyObjC_Assert(count >= 0, -1);
    PyObjC_Assert(type != NULL, -1);
    PyObjC_Assert(value != NULL, -1);
    PyObjC_Assert(datum != NULL, -1);

    /* Ensure that the list will be NULL terminated */
    if (count > 0) {
        Py_ssize_t sz = PyObjCRT_SizeOfType(type);
        memset(((unsigned char*)datum) + ((count - 1) * sz), 0, sz);
    }

    /* Shortcut: empty list */
    if (count == 1) {
        return 0;
    }

    /* Then copy the actual values */
    return depythonify_c_array_count(type, count - 1, YES, value, datum, already_retained,
                                     already_cfretained);
}

/*#F Extracts the elements from the tuple @var{arg} and fills a C array
of type @var{type} pointed by @var{datum}. Returns an error message, or
NULL on success. */
static int
depythonify_c_array(const char* type, PyObject* arg, void* datum)
{
    PyObjC_Assert(type != NULL, -1);
    PyObjC_Assert(arg != NULL, -1);
    PyObjC_Assert(datum != NULL, -1);

    Py_ssize_t     nitems, itemidx, sizeofitem;
    unsigned char* curdatum;
    PyObject*      seq;

    nitems = atoi(type + 1);
    while (isdigit(*++type))
        ;
    sizeofitem = PyObjCRT_AlignedSize(type);
    if (sizeofitem == -1) {
        PyErr_Format(PyExc_ValueError, "cannot depythonify array of unknown type");
        return -1;
    }

    seq = PySequence_Fast(arg, "depythonifying array, got no sequence");
    if (seq == NULL) {
        return -1;
    }

    if (nitems != PySequence_Fast_GET_SIZE(seq)) {
        PyErr_Format(PyExc_ValueError,
                     "depythonifying array of %" PY_FORMAT_SIZE_T
                     "d items, got one of %" PY_FORMAT_SIZE_T "d",
                     nitems, PySequence_Fast_GET_SIZE(seq));
        Py_DECREF(seq);
        return -1;
    }

    curdatum = datum;
    for (itemidx = 0; itemidx < nitems; itemidx++) {
        PyObject* pyarg = PySequence_Fast_GET_ITEM(seq, itemidx);
        int       err;

        err = depythonify_c_value(type, pyarg, curdatum);
        if (err == -1) {
            Py_DECREF(seq);
            return err;
        }

        curdatum += sizeofitem;
    }

    Py_DECREF(seq);
    return 0;
}

/*#F Extracts the elements from the tuple @var{arg} and fills a C structure
of type @var{type} pointed by @var{datum}. Returns an error message, or
NULL on success. */
static int
depythonify_c_struct(const char* types, PyObject* arg, void* datum)
{
    PyObjC_Assert(types != NULL, -1);
    PyObjC_Assert(arg != NULL, -1);
    PyObjC_Assert(datum != NULL, -1);

    Py_ssize_t  nitems, offset, itemidx;
    int         have_align = 0;
    Py_ssize_t  align;
    const char* type;
    PyObject*   seq;
    Py_ssize_t  pack;

    /* Hacked in support for sockaddr structs */
    if (strncmp(types, @encode(struct sockaddr), sizeof(@encode(struct sockaddr)) - 1)
        == 0) {
        return PyObjC_SockAddrFromPython(arg, datum);
    }
    if (IS_AUTHORIZATIONITEM(types)) {
        return depythonify_authorizationitem(arg, datum);
    }

    /* Extract struck packing value, need better way to fetch this */
    pack = -1;
    if (!PyList_Check(arg) && !PyTuple_Check(arg)) {
        seq = PyObject_GetAttrString(arg, "__struct_pack__");
        if (seq == NULL) {
            PyErr_Clear();

        } else {
            pack = PyNumber_AsSsize_t(seq, NULL);
            if (PyErr_Occurred()) {
                return -1;
            }
            Py_DECREF(seq);
        }
    }

    if (IS_FSREF(types)) {
        return PyObjC_encode_fsref(arg, datum);
    }

    if (IS_DECIMAL(types)) {
        return depythonify_nsdecimal(arg, datum);
    }

    while (*types != _C_STRUCT_E && *types++ != '=')
        ; /* skip "<name>=" */

    type   = types;
    nitems = 0;
    while (*type != _C_STRUCT_E) {
        if (*type == '"') {
            type = strchr(type + 1, '"');
            type++;
        }
        nitems++;
        type = PyObjCRT_SkipTypeSpec(type);
        if (type == NULL) {
            return -1;
        }
    }

    if (PyObjCStruct_Check(arg)) {
        seq = StructAsTuple(arg);
    } else {
        seq = PySequence_Fast(arg, "depythonifying struct, got no sequence");
    }
    if (seq == NULL) {
        return -1;
    }

    if (nitems != PySequence_Fast_GET_SIZE(seq)) {
        PyErr_Format(PyExc_ValueError,
                     "depythonifying struct of %" PY_FORMAT_SIZE_T
                     "d members, got tuple of %" PY_FORMAT_SIZE_T "d",
                     nitems, PySequence_Fast_GET_SIZE(seq));
        Py_DECREF(seq);
        return -1;
    }

    type   = types;
    offset = itemidx = 0;

    while (*type != _C_STRUCT_E) {
        PyObject* argument;

        if (*type == '"') {
            type = strchr(type + 1, '"');
            type++;
        }

        argument = PySequence_Fast_GET_ITEM(seq, itemidx);
        int error;
        if (!have_align) {
            align      = PyObjCRT_AlignOfType(type);
            have_align = 1;

        } else {
            align = PyObjC_EmbeddedAlignOfType(type);
        }

        if (pack != -1 && pack < align) {
            align = pack;
        }

        offset = ROUND(offset, align);

        error = depythonify_c_value(type, argument, ((char*)datum) + offset);
        if (error == -1) {
            Py_DECREF(seq);
            return -1;
        }

        itemidx++;
        offset += PyObjCRT_SizeOfType(type);
        type = PyObjCRT_SkipTypeSpec(type);
        if (type == NULL) {
            return -1;
        }
    }
    Py_DECREF(seq);
    return 0;
}

PyObject*
pythonify_c_value(const char* type, const void* datum)
{
    PyObjC_Assert(type != NULL, NULL);
    PyObjC_Assert(datum != NULL, NULL);

    PyObject* retobject = NULL;

    type = PyObjCRT_SkipTypeQualifiers(type);

    switch (*type) {
    case _C_UNICHAR: {
        int byteorder = 0;
        retobject     = PyUnicode_DecodeUTF16((const char*)datum, 2, NULL, &byteorder);
    } break;

    case _C_CHAR_AS_TEXT:
        retobject = PyBytes_FromStringAndSize((char*)datum, 1);
        break;

    case _C_CHR:
    case _C_CHAR_AS_INT:
        /*
         * We don't return a string because BOOL is an alias for
         * char (at least on MacOS X)
         */
        retobject = (PyObject*)PyLong_FromLong((int)(*(char*)datum));
        break;

    case _C_UCHR:
        retobject = (PyObject*)PyLong_FromLong((long)(*(unsigned char*)datum));
        break;

    case _C_CHARPTR:
#ifdef _C_ATOM
    case _C_ATOM:
#endif
    {
        char* cp;
        memcpy((void*)&cp, datum, sizeof(char*));

        if (cp == NULL) {
            Py_INCREF(Py_None);
            retobject = Py_None;

        } else {
            retobject = (PyObject*)PyBytes_FromString(cp);
        }
        break;
    }

    case _C_BOOL:
    case _C_NSBOOL:
        retobject = (PyObject*)PyBool_FromLong(*(bool*)datum);
        break;

    case _C_INT:
        {
            int v;
            memcpy((void*)&v, datum, sizeof(int));
            retobject = (PyObject*)PyLong_FromLong(v);
        }
        break;

    case _C_UINT:
        {
            unsigned int v;
            memcpy((void*)&v, datum, sizeof(unsigned int));
            retobject = (PyObject*)PyLong_FromLong(v);
        }
        break;

    case _C_SHT:
        {
            short v;
            memcpy((void*)&v, datum, sizeof(short));
            retobject = (PyObject*)PyLong_FromLong(v);
        }
        break;

    case _C_USHT:
        {
            unsigned short v;
            memcpy((void*)&v, datum, sizeof(unsigned short));
            retobject = (PyObject*)PyLong_FromLong(v);
        }
        break;

    case _C_LNG_LNG:
    case _C_LNG:
        {
            long v;
            memcpy((void*)&v, datum, sizeof(long));
            retobject = (PyObject*)PyLong_FromLong(v);
        }
        break;

    case _C_ULNG_LNG:
    case _C_ULNG:
        {
            unsigned long v;
            memcpy((void*)&v, datum, sizeof(unsigned long));
            retobject = (PyObject*)PyLong_FromUnsignedLong(v);
        }
        break;

    case _C_FLT:
        {
            float v;
            memcpy((void*)&v, datum, sizeof(float));
            retobject = (PyObject*)PyFloat_FromDouble(v);
        }
        break;

    case _C_DBL:
        {
            double v;
            memcpy((void*)&v, datum, sizeof(double));
            retobject = (PyObject*)PyFloat_FromDouble(v);
        }
        break;

    case _C_ID:
        {
            id v;
            memcpy((void*)&v, datum, sizeof(id));
            retobject = id_to_python(v);
        }
        break;

    case _C_SEL:
        if (*(SEL*)datum == NULL) {
            retobject = Py_None;
            Py_INCREF(retobject);

        } else {
            SEL s;
            memcpy((void*)&s, datum, sizeof(SEL));
            retobject = PyUnicode_FromString(sel_getName(s));
        }
        break;

    case _C_CLASS: {
        Class c;
        memcpy((void*)&c, datum, sizeof(Class));

        if (c == Nil) {
            retobject = Py_None;
            Py_INCREF(retobject);

        } else {
            retobject = (PyObject*)PyObjCClass_New(c);
        }
        break;
    }

    case _C_PTR:
     {
        void* v;
        memcpy((void*)&v, datum, sizeof(void*));

        if (type[1] == _C_VOID) {
            /* A void*. These are treated like unsigned integers. */
            retobject = (PyObject*)PyLong_FromVoidPtr(v);

        } else if (v == NULL) {
            retobject = Py_None;
            Py_INCREF(retobject);

        } else {
            retobject = PyObjCPointerWrapper_ToPython(type, datum);
            if (retobject == NULL && !PyErr_Occurred()) {
                retobject = (PyObject*)PyObjCPointer_New(v, type);
            }
        }
     }
     break;

    case _C_UNION_B: {
        Py_ssize_t size = PyObjCRT_SizeOfType(type);
        if (size == -1)
            return NULL;
        retobject = PyBytes_FromStringAndSize((void*)datum, size);
        break;
    }

    case _C_STRUCT_B:
        retobject = pythonify_c_struct(type, datum);
        break;

    case _C_ARY_B:
        retobject = pythonify_c_array(type, datum);
        break;

    case _C_VOID:
        retobject = Py_None;
        Py_INCREF(retobject);
        break;

    case _C_VECTOR_B: {
        struct vector_info* info = vector_lookup(type);
        if (info->size == -1) {
            return NULL;
        }
        PyObject* args = info->as_tuple(datum);
        if (args == NULL) {
            return NULL;
        }
        if (info->pytype == NULL) {
            return args;
        } else {
            PyObject* retval = PyObject_Call(info->pytype, args, NULL);
            Py_DECREF(args);
            return retval;
        }
    } break;

    default:
        PyErr_Format(PyObjCExc_Error,
                     "pythonify_c_value: unhandled value type (%c|%d|%s)", *type, *type,
                     type);
        break;
    }

    return retobject;
}

Py_ssize_t
PyObjCRT_SizeOfReturnType(const char* type)
{
    PyObjC_Assert(type != NULL, -1);

#if defined(__x86_64__) /* XXX */
    switch (*type) {
    case _C_CHR:
    case _C_BOOL:
    case _C_NSBOOL:
    case _C_UCHR:
    case _C_SHT:
    case _C_USHT:
    case _C_UNICHAR:
    case _C_CHAR_AS_TEXT:
    case _C_CHAR_AS_INT:
        return sizeof(long);
    default:
        return PyObjCRT_SizeOfType(type);
    }
#else
    return PyObjCRT_SizeOfType(type);
#endif
}

/*
 * Convert a python value to a basic C unsigned integer value.
 */
static int
depythonify_unsigned_int_value(PyObject* argument, char* descr, unsigned long long* out,
                               unsigned long long max)
{
    PyObjC_Assert(argument != NULL, -1);
    PyObjC_Assert(descr != NULL, -1);
    PyObjC_Assert(out != NULL, -1);

    if (PyLong_Check(argument)) {
        *out = PyLong_AsUnsignedLongLong(argument);
        if (*out == (unsigned long long)-1 && PyErr_Occurred()) {
            PyErr_Clear();

            *out = (unsigned long long)PyLong_AsLongLong(argument);
            if (*out == (unsigned long long)-1 && PyErr_Occurred()) {
                PyErr_Format(PyExc_ValueError,
                             "depythonifying '%s', got '%s' of "
                             "wrong magnitude (max %llu, value %llu)",
                             descr, Py_TYPE(argument)->tp_name, max, *out);
                return -1;
            }

            if ((long long)*out < 0) {
                if (PyErr_WarnEx(PyExc_DeprecationWarning,
                                 "converting negative value to unsigned integer", 1)
                    < 0) {

                    return -1;
                }
            }
        }

        if (*out > max) {
            PyErr_Format(PyExc_ValueError,
                         "depythonifying '%s', got '%s' of "
                         "wrong magnitude (max %llu, value %llu)",
                         descr, Py_TYPE(argument)->tp_name, max, *out);
            return -1;
        }
        return 0;

    } else {
        PyObject* tmp;

        if (PyBytes_Check(argument) ||
#ifdef PyByteArray_Check
            PyByteArray_Check(argument) ||
#endif
            PyUnicode_Check(argument)) {

            PyErr_Format(PyExc_ValueError, "depythonifying '%s', got '%s'", descr,
                         Py_TYPE(argument)->tp_name);
            return -1;
        }

        tmp = PyNumber_Long(argument);
        if (tmp != NULL) {
            *out = PyLong_AsUnsignedLongLong(tmp);
            if (*out == (unsigned long long)-1 && PyErr_Occurred()) {
                PyErr_Clear();

                *out = PyLong_AsLong(tmp);
                if (*out == (unsigned long long)-1 && PyErr_Occurred()) {
                    Py_DECREF(tmp);
                    return -1;
                }

                if ((long long)*out < 0) {
                    if (PyErr_WarnEx(PyExc_DeprecationWarning,
                                     "converting negative value to unsigned integer", 1)
                        < 0) {
                        Py_DECREF(tmp);

                        return -1;
                    }
                }
            }
            Py_DECREF(tmp);

            if (*out <= max) {
                return 0;
            }
        }

        PyErr_Format(PyExc_ValueError, "depythonifying '%s', got '%s'", descr,
                     Py_TYPE(argument)->tp_name);
        return -1;
    }
}

/*
 * Convert a python value to a basic C signed integer value.
 */
static int
depythonify_signed_int_value(PyObject* argument, char* descr, long long* out,
                             long long min, long long max)
{
    PyObjC_Assert(argument != NULL, -1);
    PyObjC_Assert(descr != NULL, -1);
    PyObjC_Assert(out != NULL, -1);

    if (PyLong_Check(argument)) {
        *out = PyLong_AsLongLong(argument);
        if (PyErr_Occurred()) {
            PyErr_Format(PyExc_ValueError,
                         "depythonifying '%s', got '%s' of "
                         "wrong magnitude",
                         descr, Py_TYPE(argument)->tp_name);
            return -1;
        }

        if (*out < min || *out > max) {
            PyErr_Format(PyExc_ValueError,
                         "depythonifying '%s', got '%s' of "
                         "wrong magnitude",
                         descr, Py_TYPE(argument)->tp_name);
            return -1;
        }
        return 0;

    } else {
        PyObject* tmp;

        if (PyBytes_Check(argument) ||
#ifdef PyByteArray_Check
            PyByteArray_Check(argument) ||
#endif
            PyUnicode_Check(argument)) {

            PyErr_Format(PyExc_ValueError,
                         "depythonifying '%s', got '%s' of %" PY_FORMAT_SIZE_T "d", descr,
                         Py_TYPE(argument)->tp_name, PyObject_Size(argument));
            return -1;
        }

        tmp = PyNumber_Long(argument);
        if (tmp != NULL) {
            *out = PyLong_AsLongLong(tmp);
            Py_DECREF(tmp);

            if (PyErr_Occurred()) {
                return -1;
            }

            if (*out >= min && *out <= max) {
                return 0;
            }
        }

        PyErr_Format(PyExc_ValueError, "depythonifying '%s', got '%s'", descr,
                     Py_TYPE(argument)->tp_name);
        return -1;
    }
}

int /* XXX: No longer necessary */
depythonify_c_return_value(const char* type, PyObject* argument, void* datum)
{
    PyObjC_Assert(type != NULL, -1);
    PyObjC_Assert(argument != NULL, -1);
    PyObjC_Assert(datum != NULL, -1);

    return depythonify_c_value(type, argument, datum);
}

PyObject* _Nullable /*  XXX: No longer necessary */
    pythonify_c_return_value(const char* type, const void* datum) /* XXX */
{
    PyObjC_Assert(type != NULL, NULL);
    PyObjC_Assert(datum != NULL, NULL);

    return pythonify_c_value(type, datum);
}

int
depythonify_python_object(PyObject* argument, id* datum)
{
    PyObject* anObject;

    if (argument == Py_None) {
        *datum = nil;
        return 0;
    }

    *datum = PyObjC_FindObjCProxy(argument);
    if (*datum != nil) {
        [[(*datum) retain] autorelease];
        return 0;
    }

    if (PyObjCObject_Check(argument)) {
        *datum = PyObjCObject_GetObject(argument);
        return 0;
    }

    if (PyObjCClass_Check(argument)) {
        *datum = PyObjCClass_GetClass(argument);
        return 0;
    }

    anObject = PyObject_GetAttrString(argument, "__pyobjc_object__");
    if (anObject != NULL) {
        if (anObject != argument) {
            int r = depythonify_python_object(anObject, datum);
            Py_DECREF(anObject);
            return r;
        } else {
            Py_DECREF(anObject);
        }
    } else {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError)) {
            return -1;
        }
        PyErr_Clear();
    }

    if (PyUnicode_CheckExact(argument)) {
        *datum = [OC_BuiltinPythonUnicode unicodeWithPythonObject:argument];

    } else if (PyUnicode_Check(argument)) {
        *datum = [OC_PythonUnicode unicodeWithPythonObject:argument];

    } else if (PyBool_Check(argument)) {
        if (argument == Py_True) {
            *datum = [NSNumber numberWithBool:YES];
        } else {
            *datum = [NSNumber numberWithBool:NO];
        }

    } else if (PyFloat_CheckExact(argument) || PyLong_CheckExact(argument)) {
        *datum = [OC_BuiltinPythonNumber numberWithPythonObject:argument];

    } else if (PyFloat_Check(argument) || PyLong_Check(argument)) {
        *datum = [OC_PythonNumber numberWithPythonObject:argument];

    } else if (PyList_CheckExact(argument) || PyTuple_CheckExact(argument)) {
        *datum = [OC_BuiltinPythonArray arrayWithPythonObject:argument];

    } else if (PyList_Check(argument) || PyTuple_Check(argument)) {
        *datum = [OC_PythonArray arrayWithPythonObject:argument];

    } else if (PyDict_CheckExact(argument)) {
        *datum = [OC_BuiltinPythonDictionary dictionaryWithPythonObject:argument];

    } else if (PyDict_Check(argument)) {
        *datum = [OC_PythonDictionary dictionaryWithPythonObject:argument];

    } else if (PyBytes_CheckExact(argument) || PyByteArray_CheckExact(argument)) {
        *datum = [OC_BuiltinPythonData dataWithPythonObject:argument];

    } else if (PyObject_CheckBuffer(argument)) {
        *datum = [OC_PythonData dataWithPythonObject:argument];

    } else if (PyAnySet_CheckExact(argument)) {
        *datum = [OC_BuiltinPythonSet setWithPythonObject:argument];

    } else if (PyAnySet_Check(argument)) {
        *datum = [OC_PythonSet setWithPythonObject:argument];

    } else if (PyObjCFormalProtocol_Check(argument)) {
        *datum = PyObjCFormalProtocol_GetProtocol(argument);
        return 0;

    } else {

        if (*datum == nil && PyObjC_ListLikeTypes != NULL) {
            int r;

            r = PyObject_IsInstance(argument, PyObjC_ListLikeTypes);
            if (r == -1) {
                return -1;
            }

            if (r) {
                *datum = [OC_PythonArray arrayWithPythonObject:argument];
                if (*datum == nil) {
                    return -1;
                }
            }
        }

        if (*datum == nil && PyObjC_DictLikeTypes != NULL) {
            int r;

            r = PyObject_IsInstance(argument, PyObjC_DictLikeTypes);
            if (r == -1) {
                return -1;
            }

            if (r) {
                *datum = [OC_PythonDictionary dictionaryWithPythonObject:argument];
                if (*datum == nil) {
                    return -1;
                }
            }
        }

        if (*datum == nil && PyObjC_SetLikeTypes != NULL) {
            int r;

            r = PyObject_IsInstance(argument, PyObjC_SetLikeTypes);
            if (r == -1) {
                return -1;
            }

            if (r) {
                *datum = [OC_PythonSet setWithPythonObject:argument];
                if (*datum == nil) {
                    return -1;
                }
            }
        }

        if (*datum == nil && PyObjC_DateTime_Date_Type != NULL
            && PyObjC_DateTime_Date_Type != Py_None) {
            if ((PyObject*)Py_TYPE(argument) == PyObjC_DateTime_Date_Type) {
                *datum = [OC_BuiltinPythonDate dateWithPythonObject:argument];
                if (*datum == nil) {
                    return -1;
                }
            }
        }

        if (*datum == nil && PyObjC_DateTime_DateTime_Type != NULL
            && PyObjC_DateTime_DateTime_Type != Py_None) {
            if ((PyObject*)Py_TYPE(argument) == PyObjC_DateTime_DateTime_Type) {
                *datum = [OC_BuiltinPythonDate dateWithPythonObject:argument];
                if (*datum == nil) {
                    return -1;
                }
            }
        }

        if (*datum == nil && PyObjC_DateLikeTypes != NULL) {
            int r;

            r = PyObject_IsInstance(argument, PyObjC_DateLikeTypes);
            if (r == -1) {
                return -1;
            }

            if (r) {
                *datum = [OC_PythonDate dateWithPythonObject:argument];
                if (*datum == nil) {
                    return -1;
                }
            }
        }

        if (*datum == nil && PyObjC_PathLikeTypes != NULL) {
            int r;

            r = PyObject_IsInstance(argument, PyObjC_PathLikeTypes);
            if (r == -1) {
                return -1;
            }

            if (r) {
                *datum = [OC_PythonURL URLWithPythonObject:argument];
                if (*datum == nil) {
                    /* XXX: Datum can be nil due to `argument` not being
                     *      pathlike after all or because NSURL construction
                     *      failed.
                     */
                    return -1;
                }
            }
        }

        if (*datum == nil) {
            PyObjC_Assert(!PyObjCObject_Check(argument), -1);
            *datum = [OC_PythonObject objectWithPythonObject:argument];
        }
    }

    if (*datum) {
        PyObjC_RegisterObjCProxy(argument, *datum);
        return 0;
    } else {
        return -1;
    }
}

int
depythonify_c_value(const char* type, PyObject* argument, void* datum)
{
    PyObjC_Assert(type != NULL, -1);
    PyObjC_Assert(argument != NULL, -1);
    PyObjC_Assert(datum != NULL, -1);

    if (argument == NULL)
        abort();

    /* Pass by reference output arguments are sometimes passed a NULL
     * pointer, this suppresses a core dump.
     */
    long long          temp;
    unsigned long long utemp;
    int                r;

    if (!datum)
        return 0;

    type = PyObjCRT_SkipTypeQualifiers(type);

    switch (*type) {
#ifdef _C_ATOM
    case _C_ATOM:
#endif
    case _C_CHARPTR:

        if (PyBytes_Check(argument)) {
            char* v = PyBytes_AsString(argument);
            memcpy(datum, (void*)&v, sizeof(char*));
            if (v == NULL) {
                return -1;
            }
#ifdef PyByteArray_Check
        } else if (PyByteArray_Check(argument)) {
            char* v = PyByteArray_AsString(argument);
            memcpy(datum, (void*)&v, sizeof(char*));
            if (v == NULL) {
                return -1;
            }
#endif
        } else if (argument == Py_None) {
            char* v = NULL;
            memcpy(datum, (void*)&v, sizeof(char*));

        } else {
            PyErr_Format(PyExc_ValueError, "depythonifying 'charptr', got '%s'",
                         Py_TYPE(argument)->tp_name);
            return -1;
        }
        break;

    case _C_CHR:
        if (PyBytes_Check(argument) && PyBytes_Size(argument) == 1) {
            *(char*)datum = PyBytes_AsString(argument)[0];
            return 0;
        } else if (PyByteArray_Check(argument) && PyByteArray_Size(argument) == 1) {
            *(char*)datum = PyByteArray_AsString(argument)[0];
            return 0;
        }

        r = depythonify_signed_int_value(argument, "char", &temp, CHAR_MIN, CHAR_MAX);
        if (r == 0) {
            *(char*)datum = temp;
        }
        return r;

    case _C_CHAR_AS_INT:
        r = depythonify_signed_int_value(argument, "char", &temp, CHAR_MIN, CHAR_MAX);
        if (r == 0) {
            *(char*)datum = temp;
        }
        return r;

    case _C_CHAR_AS_TEXT:
        if (PyBytes_Check(argument) && PyBytes_Size(argument) == 1) {
            *(char*)datum = PyBytes_AsString(argument)[0];
            return 0;

#ifdef PyByteArray_Check
        } else if (PyByteArray_Check(argument) && PyByteArray_Size(argument) == 1) {
            *(char*)datum = PyByteArray_AsString(argument)[0];
            return 0;
#endif

        } else {
            PyErr_Format(PyExc_ValueError,
                         "Expecting byte string of length 1, got a '%s'",
                         Py_TYPE(argument)->tp_name);
            return -1;
        }

    case _C_UCHR:
        if (PyBytes_Check(argument) && PyBytes_Size(argument) == 1) {
            *(unsigned char*)datum = PyBytes_AsString(argument)[0];
            return 0;

#ifdef PyByteArray_Check
        } else if (PyByteArray_Check(argument) && PyByteArray_Size(argument) == 1) {
            *(unsigned char*)datum = PyByteArray_AsString(argument)[0];
            return 0;
#endif
        }

        r = depythonify_unsigned_int_value(argument, "unsigned char", &utemp, UCHAR_MAX);
        if (r == 0) {
            *(unsigned char*)datum = utemp;
        }
        return r;

    case _C_SHT:
        r = depythonify_signed_int_value(argument, "short", &temp, SHRT_MIN, SHRT_MAX);
        if (r == 0) {
            short v = temp;
            memcpy(datum, (void*)&v, sizeof(short));
        }
        return r;

    case _C_USHT:
        r = depythonify_unsigned_int_value(argument, "unsigned short", &utemp, USHRT_MAX);
        if (r == 0) {
            unsigned short v = utemp;
            memcpy(datum, (void*)&v, sizeof(unsigned short));
        }
        return r;

    case _C_BOOL:
    case _C_NSBOOL:
        r = PyObject_IsTrue(argument);
        if (r == -1) {
            return -1;
        }
        *(bool*)datum = (bool)r;
        return 0;

    case _C_UNICHAR:
        if (PyUnicode_Check(argument) && PyUnicode_GetLength(argument) == 1) {

            /* Need to guard against values outside of the BMP, which cannot be
             * converted to UniChar
             */
            switch (PyUnicode_KIND(argument)) {
            case PyUnicode_1BYTE_KIND:
            case PyUnicode_2BYTE_KIND:
                break;

            default:
                PyErr_Format(PyExc_ValueError, "Expecting string of length 1, got a '%s'",
                             Py_TYPE(argument)->tp_name);
                return -1;
            }
            UniChar v = (UniChar)PyUnicode_ReadChar(argument, 0);
            memcpy(datum, (void*)&v, sizeof(UniChar));
            return 0;
        }
        PyErr_Format(PyExc_ValueError, "Expecting unicode string of length 1, got a '%s'",
                     Py_TYPE(argument)->tp_name);
        return -1;

    case _C_INT:
        r = depythonify_signed_int_value(argument, "int", &temp, INT_MIN, INT_MAX);
        if (r == 0) {
            int v = (int)temp;
            memcpy(datum, &v, sizeof(int));
        }
        return r;

    case _C_UINT:
        r = depythonify_unsigned_int_value(argument, "unsigned int", &utemp, UINT_MAX);
        if (r == 0) {
            unsigned int v = (unsigned int)utemp;
            memcpy(datum, &v, sizeof(unsigned int));
        }
        return r;

    case _C_LNG:
        r = depythonify_signed_int_value(argument, "long", &temp, LONG_MIN, LONG_MAX);
        if (r == 0) {
            long v = (long)temp;
            memcpy(datum, &v, sizeof(long));
        }
        return r;

    case _C_ULNG:
        r = depythonify_unsigned_int_value(argument, "unsigned long", &utemp, ULONG_MAX);
        if (r == 0) {
            unsigned long v = (unsigned long)utemp;
            memcpy(datum, &v, sizeof(unsigned long));
        }
        return r;

    case _C_LNG_LNG:
        r = depythonify_signed_int_value(argument, "long long", &temp, LLONG_MIN,
                                         LLONG_MAX);
        if (r == 0) {
            long long v = temp;
            memcpy(datum, &v, sizeof(long long));
        }
        return r;

    case _C_ULNG_LNG:
        r = depythonify_unsigned_int_value(argument, "unsigned long long", &utemp,
                                           ULLONG_MAX);
        if (r == 0) {
            unsigned long long v = utemp;
            memcpy(datum, &v, sizeof(unsigned long long));
        }
        return r;

    case _C_ID:
        {
            id v;
            r = depythonify_python_object(argument, &v);
            memcpy(datum, (void*)&v, sizeof(id));
            return r;
        }

    case _C_CLASS:
        if (PyObjCClass_Check(argument)) {
            *(Class*)datum = PyObjCClass_GetClass(argument);

        } else if (argument == Py_None) {
            *(Class*)datum = nil;

        } else if (PyType_Check(argument)
                   && PyType_IsSubtype((PyTypeObject*)argument, &PyObjCClass_Type)) {
            PyObject* class_object = PyObjCClass_ClassForMetaClass(argument);
            if (class_object == NULL) {
                PyErr_Format(PyObjCExc_Error, "Cannot locate class for metaclass %R",
                             argument);
                return -1;
            }
            *(Class*)datum = PyObjCClass_GetClass(class_object);

        } else {
            PyErr_Format(PyExc_ValueError, "depythonifying 'Class', got '%s'",
                         Py_TYPE(argument)->tp_name);
            return -1;
        }
        break;

    case _C_SEL:
        if (argument == Py_None) {
            *(SEL*)datum = NULL;

        } else if (PyObjCSelector_Check(argument)) {
            *(SEL*)datum = PyObjCSelector_GetSelector(argument);

        } else if (PyUnicode_Check(argument)) {
            PyObject* bytes = PyUnicode_AsEncodedString(argument, NULL, NULL);
            if (bytes == NULL) {
                return -1;
            }
            char* selname = PyBytes_AsString(bytes);
            SEL   sel;

            if (*selname == '\0') {
                *(SEL*)datum = NULL;
                Py_DECREF(bytes);

            } else {
                sel = sel_getUid(selname);
                Py_DECREF(bytes);

                if (sel) {
                    *(SEL*)datum = sel;

                } else {
                    PyErr_Format(PyExc_ValueError, "depythonifying 'SEL', cannot "
                                                   "register string with runtime");
                    return -1;
                }
            }

        } else if (PyBytes_Check(argument)) {
            char* selname = PyBytes_AsString(argument);
            SEL   sel;

            if (*selname == '\0') {
                *(SEL*)datum = NULL;

            } else {
                sel = sel_getUid(selname);

                if (sel) {
                    *(SEL*)datum = sel;

                } else {
                    PyErr_Format(PyExc_ValueError, "depythonifying 'SEL', cannot "
                                                   "register string with runtime");
                    return -1;
                }
            }
#ifdef PyByteArray_Check
        } else if (PyByteArray_Check(argument)) {
            char* selname = PyByteArray_AsString(argument);
            SEL   sel;

            if (*selname == '\0') {
                *(SEL*)datum = NULL;

            } else {
                sel = sel_getUid(selname);

                if (sel) {
                    *(SEL*)datum = sel;

                } else {
                    PyErr_Format(PyExc_ValueError, "depythonifying 'SEL', cannot "
                                                   "register string with runtime");
                    return -1;
                }
            }
#endif
        } else {
            PyErr_Format(PyExc_ValueError, "depythonifying 'SEL', got '%s'",
                         Py_TYPE(argument)->tp_name);
            return -1;
        }
        break;

    case _C_PTR:
        if (argument == Py_None) {
            *(void**)datum = NULL;
            return 0;
        }

        if (type[1] == _C_VOID) {
            r = depythonify_unsigned_int_value(argument, "unsigned long", &utemp,
                                               ULONG_MAX);
            if (r == 0) {
                *(void**)datum = (void*)(unsigned long)utemp;
            }
            return r;
        }

        r = PyObjCPointerWrapper_FromPython(type, argument, datum);
        if (r == -1) {
            if (PyErr_Occurred()) {
                return -1;

            } else if (PyObjCPointer_Check(argument)) {
                *(void**)datum = PyObjCPointer_Ptr(argument);

            } else {
                PyErr_Format(PyExc_ValueError, "depythonifying 'pointer', got '%s'",
                             Py_TYPE(argument)->tp_name);
                return -1;
            }
        }
        break;

    case _C_FLT:
        if (PyFloat_Check(argument)) {
            float v = (float)PyFloat_AsDouble(argument);
            memcpy(datum, (void*)&v, sizeof(float));

        } else if (PyLong_Check(argument)) {
            float v = (float)PyLong_AsDouble(argument);
            if (v == -1 && PyErr_Occurred()) {
                return -1;
            }
            memcpy(datum, (void*)&v, sizeof(float));

        } else if (PyBytes_Check(argument) ||
                   PyByteArray_Check(argument) ||
                   PyUnicode_Check(argument)) {
            PyErr_Format(PyExc_ValueError, "depythonifying 'float', got '%s'",
                         Py_TYPE(argument)->tp_name);
            return -1;

        } else {
            PyObject* tmp = PyNumber_Float(argument);
            if (tmp != NULL) {
                float dblval = (float)PyFloat_AsDouble(tmp);
                Py_DECREF(tmp);
                memcpy(datum, (void*)&dblval, sizeof(float));
                return 0;
            }

            PyErr_Format(PyExc_ValueError, "depythonifying 'float', got '%s'",
                         Py_TYPE(argument)->tp_name);
            return -1;
        }
        break;

    case _C_DBL:
        if (PyFloat_Check(argument)) {
            double v = PyFloat_AsDouble(argument);
            memcpy(datum, (void*)&v, sizeof(double));

        } else if (PyLong_Check(argument)) {
            double v = PyLong_AsDouble(argument);
            if (v == -1 && PyErr_Occurred()) {
                return -1;
            }
            memcpy(datum, (void*)&v, sizeof(double));

        } else if (PyBytes_Check(argument) ||
                   PyByteArray_Check(argument) ||
                   PyUnicode_Check(argument)) {
            PyErr_Format(PyExc_ValueError, "depythonifying 'double', got '%s'",
                         Py_TYPE(argument)->tp_name);
            return -1;

        } else {
            PyObject* tmp = PyNumber_Float(argument);
            if (tmp != NULL) {
                double dblval = PyFloat_AsDouble(tmp);
                Py_DECREF(tmp);
                memcpy(datum, (void*)&dblval, sizeof(double));
                return 0;
            }

            PyErr_Format(PyExc_ValueError, "depythonifying 'double', got '%s'",
                         Py_TYPE(argument)->tp_name);
            return -1;
        }
        break;

    case _C_UNION_B:
        if (PyBytes_Check(argument)) {
            Py_ssize_t expected_size = PyObjCRT_SizeOfType(type);

            if (expected_size == -1) {
                PyErr_Format(PyExc_ValueError, "depythonifying 'union' of "
                                               "unknown size");
                return -1;

            } else if (expected_size != PyBytes_Size(argument)) {
                PyErr_Format(PyExc_ValueError,
                             "depythonifying 'union' of size %" PY_FORMAT_SIZE_T "d, "
                             "got byte string of %" PY_FORMAT_SIZE_T "d",
                             expected_size, PyBytes_Size(argument));
                return -1;

            } else {
                memcpy((void*)datum, PyBytes_AS_STRING(argument), expected_size);
            }

        } else {
            PyErr_Format(PyExc_ValueError, "depythonifying 'union', got '%s'",
                         Py_TYPE(argument)->tp_name);
            return -1;
        }
        break;

    case _C_STRUCT_B:
        return depythonify_c_struct(type, argument, datum);

    case _C_ARY_B:
        return depythonify_c_array(type, argument, datum);

    case _C_VECTOR_B: {
        struct vector_info* info = vector_lookup(type);
        if (info->size == -1) {
            return -1;
        }
        return info->from_python(argument, datum);
    } break;

    default:
        PyErr_Format(PyExc_ValueError, "depythonifying unknown typespec 0x%x", *type);
        return -1;
    }
    return 0;
}

const char* _Nullable PyObjCRT_RemoveFieldNames(char* buf, const char* type)
{
    PyObjC_Assert(buf != NULL, NULL);
    PyObjC_Assert(type != NULL, NULL);

    const char* end;
    if (*type == '"') {
        type++;
        while (*type && *type++ != '"') {
        }
    }

    end = PyObjCRT_SkipTypeQualifiers(type);

    switch (*end) {
    case _C_STRUCT_B:
        /* copy struct header */
        while (*end && *end != '=' && *end != _C_STRUCT_E) {
            end++;
        }

        if (*end == '\0') {
            PyErr_SetString(PyExc_ValueError, "Bad type string");
            return NULL;
        }

        if (*end == _C_STRUCT_E) {
            end++;
            memcpy(buf, type, end - type);
            buf[end - type] = '\0';
            return end;
        }

        end++;
        memcpy(buf, type, end - type);
        buf += end - type;
        type = end;

        /* RemoveFieldNames until reaching end of struct */
        while (*type && *type != _C_STRUCT_E) {
            end = PyObjCRT_RemoveFieldNames(buf, type);
            if (end == NULL)
                return NULL;
            buf += strlen(buf);
            type = end;
        }
        if (*type != _C_STRUCT_E) {
            PyErr_SetString(PyExc_ValueError, "Bad type string");
            return NULL;
        }

        buf[0] = _C_STRUCT_E;
        buf[1] = '\0';
        return type + 1;

    case _C_ARY_B:
        /* copy array header */
        end++;
        while (isdigit(*end)) {
            end++;
        }

        memcpy(buf, type, end - type);
        buf += end - type;
        type = end;
        if (*type == _C_ARY_E) {
            buf[0] = _C_ARY_E;
            buf[1] = '\0';
            return type;
        }

        /* RemoveFieldName until reaching end of array */
        end = PyObjCRT_RemoveFieldNames(buf, type);
        if (end == NULL)
            return NULL;

        if (*end != _C_ARY_E) {
            PyErr_SetString(PyExc_ValueError, "bad type string");
            return NULL;
        }

        buf += strlen(buf);
        /*type += end - type;*/
        buf[0] = _C_ARY_E;
        buf[1] = '\0';
        return end + 1;
        break;

    default:
        end = PyObjCRT_SkipTypeSpec(end);
        if (end == NULL)
            return NULL;

        memcpy(buf, type, end - type);
        buf[end - type] = '\0';
        return end;
    }
}

PyObject* _Nullable PyObjCObject_NewTransient(id objc_object, int* cookie)
{
    return [(NSObject*)objc_object __pyobjc_PythonTransient__:cookie];
}

void
PyObjCObject_ReleaseTransient(PyObject* proxy, int cookie)
{
    if (cookie && Py_REFCNT(proxy) != 1) {
        Py_BEGIN_ALLOW_THREADS
            CFRetain(PyObjCObject_GetObject(proxy));
        Py_END_ALLOW_THREADS((PyObjCObject*)proxy)->flags &=
            ~PyObjCObject_kSHOULD_NOT_RELEASE;
    }
    Py_DECREF(proxy);
}

BOOL
PyObjC_signatures_compatible(const char* type1, const char* type2)
{
    /* Ignore type modifiers */
    type1 = PyObjCRT_SkipTypeQualifiers(type1);
    type2 = PyObjCRT_SkipTypeQualifiers(type2);

    if (*type1 == _C_ARY_B) {
        if (type2[0] == _C_PTR) {
            type1++;
            while (isdigit(*type1))
                type1++;
            return PyObjC_signatures_compatible(type1, type2 + 1);

        } else if (type2[0] == _C_ARY_B) {
            type1++;
            while (isdigit(*type1))
                type1++;
            type2++;
            while (isdigit(*type2))
                type2++;
            return PyObjC_signatures_compatible(type1, type2);
        }
        return NO;
    }

    if (PyObjCRT_SizeOfType(type1) != PyObjCRT_SizeOfType(type2)) {
        return NO;
    }

    switch (*type1) {
    case _C_FLT:
    case _C_DBL:
        switch (*type2) {
        case _C_FLT:
        case _C_DBL:
            return YES;

        default:
            return NO;
        }

    case _C_ID:
        if (*type2 == _C_ID) {
            return YES;
        }

        if (type2[0] == _C_PTR && type2[1] == _C_VOID) {
            return YES;
        }

        return NO;

    case _C_CHARPTR:
        if (*type2 == _C_CHARPTR) {
            return YES;

        } else if (*type2 == _C_PTR) {
            return PyObjC_signatures_compatible("c", type2 + 1);

        } else {
            return NO;
        }

    case _C_PTR:
        if (type1[1] == _C_VOID && type2[0] == _C_ID) {
            return YES;
        }

        if (*type2 == _C_CHARPTR) {
            return PyObjC_signatures_compatible(type1 + 1, "c");
        }

        if (*type2 != _C_PTR) {
            return NO;
        }

        if (type1[1] == _C_VOID || type2[1] == _C_VOID) {
            return YES;
        }

        return PyObjC_signatures_compatible(type1 + 1, type2 + 1);

    default:
        switch (*type2) {
        case _C_ID:
        case _C_PTR:
            return NO;
        case _C_FLT:
        case _C_DBL:
            return NO;
        default:
            return YES;
        }
    }
}

PyObject* _Nullable id_to_python(id _Nullable obj)
{
    PyObject* retobject;
#if 1
    /* In theory this is a no-op, in practice this gives us EOF 4.5
     * support.
     *
     * EOF can return references to 'to-be-restored' objects,
     * calling any method on them fully restores them, 'self' is
     * the safest method to call.
     *
     * XXX: Is this still necessary?
     */
    obj = [obj self];
#endif

    if (obj == nil) {
        retobject = Py_None;
        Py_INCREF(retobject);

    } else {
        retobject = PyObjC_FindPythonProxy(obj);
        if (retobject == NULL) {
            retobject = [obj __pyobjc_PythonObject__];
        }
    }
    return retobject;
}

NS_ASSUME_NONNULL_END
