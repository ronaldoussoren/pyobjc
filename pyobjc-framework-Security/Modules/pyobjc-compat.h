#ifndef PyObjC_COMPAT_H
#define PyObjC_COMPAT_H

/*
 *
 * Start of compiler definitions
 *
 */
#ifndef __has_feature
#define __has_feature(x) 0
#endif
#ifndef __has_extension
#define __has_extension(x) __has_feature(x)
#endif

#if __has_extension(c_static_assert)
#define STATIC_ASSERT(test, message) _Static_assert(test, message)
#else
#define STATIC_ASSERT(test, message)                                                     \
    switch (0) {                                                                         \
    case 0:                                                                              \
    case test:;                                                                          \
    }
#endif

#if !__has_feature(objc_instancetype)
#define instancetype id
#endif

/*
 *
 * Start of Cocoa definitions
 *
 *
 * Ensure that CGFloat and NSInteger are always
 * available, even when compiling with ancient SDKs.
 *
 * Also ensure that MAC_OS_X_VERSION_... macros are available
 * for all existing OSX versions.
 */

/* On 10.1 there are no defines for the OS version. */
#ifndef MAC_OS_X_VERSION_10_1
#define MAC_OS_X_VERSION_10_1 1010
#define MAC_OS_X_VERSION_MAX_ALLOWED MAC_OS_X_VERSION_10_1

#error "MAC_OS_X_VERSION_10_1 not defined. You aren't running 10.1 are you?"

#endif

#ifndef MAC_OS_X_VERSION_10_2
#define MAC_OS_X_VERSION_10_2 1020
#endif

#ifndef MAC_OS_X_VERSION_10_3
#define MAC_OS_X_VERSION_10_3 1030
#endif

#ifndef MAC_OS_X_VERSION_10_4
#define MAC_OS_X_VERSION_10_4 1040
#endif

#ifndef MAC_OS_X_VERSION_10_5
#define MAC_OS_X_VERSION_10_5 1050
#endif

#ifndef MAC_OS_X_VERSION_10_6
#define MAC_OS_X_VERSION_10_6 1060
#endif

#ifndef MAC_OS_X_VERSION_10_7
#define MAC_OS_X_VERSION_10_7 1070
#endif

#ifndef MAC_OS_X_VERSION_10_8
#define MAC_OS_X_VERSION_10_8 1080
#endif

#ifndef MAC_OS_X_VERSION_10_9
#define MAC_OS_X_VERSION_10_9 1090
#endif

#ifndef MAC_OS_X_VERSION_10_10
#define MAC_OS_X_VERSION_10_10 101000
#endif

#ifndef MAC_OS_X_VERSION_10_10_2
#define MAC_OS_X_VERSION_10_10_2 101002
#endif

#ifndef MAC_OS_X_VERSION_10_10_3
#define MAC_OS_X_VERSION_10_10_3 101003
#endif

#ifndef MAC_OS_X_VERSION_10_11
#define MAC_OS_X_VERSION_10_11 101100
#endif

#ifndef MAC_OS_X_VERSION_10_11_1
#define MAC_OS_X_VERSION_10_11_1 101101
#endif

#ifndef MAC_OS_X_VERSION_10_11_2
#define MAC_OS_X_VERSION_10_11_2 101102
#endif

#ifndef MAC_OS_X_VERSION_10_11_3
#define MAC_OS_X_VERSION_10_11_3 101103
#endif

#ifndef MAC_OS_X_VERSION_10_11_4
#define MAC_OS_X_VERSION_10_11_4 101104
#endif

#ifndef MAC_OS_X_VERSION_10_12
#define MAC_OS_X_VERSION_10_12 101200
#endif

#ifndef MAC_OS_X_VERSION_10_12_1
#define MAC_OS_X_VERSION_10_12_1 101201
#endif

#ifndef MAC_OS_X_VERSION_10_12_2
#define MAC_OS_X_VERSION_10_12_2 101202
#endif

#ifndef MAC_OS_X_VERSION_10_12_4
#define MAC_OS_X_VERSION_10_12_4 101204
#endif

#ifndef MAC_OS_X_VERSION_10_13
#define MAC_OS_X_VERSION_10_13 101300
#endif

#ifndef MAC_OS_X_VERSION_10_13_1
#define MAC_OS_X_VERSION_10_13_1 101301
#endif

#ifndef MAC_OS_X_VERSION_10_13_2
#define MAC_OS_X_VERSION_10_13_2 101302
#endif

#ifndef MAC_OS_X_VERSION_10_13_3
#define MAC_OS_X_VERSION_10_13_3 101303
#endif

#ifndef MAC_OS_X_VERSION_10_13_4
#define MAC_OS_X_VERSION_10_13_4 101304
#endif

#ifndef MAC_OS_X_VERSION_10_13_5
#define MAC_OS_X_VERSION_10_13_5 101305
#endif

#ifndef MAC_OS_X_VERSION_10_13_6
#define MAC_OS_X_VERSION_10_13_6 101306
#endif

#ifndef MAC_OS_X_VERSION_10_14
#define MAC_OS_X_VERSION_10_14 101400
#endif

#ifndef MAC_OS_X_VERSION_10_14_1
#define MAC_OS_X_VERSION_10_14_1 101401
#endif

#ifndef MAC_OS_X_VERSION_10_14_2
#define MAC_OS_X_VERSION_10_14_2 101402
#endif

#ifndef MAC_OS_X_VERSION_10_14_3
#define MAC_OS_X_VERSION_10_14_3 101403
#endif

#ifndef MAC_OS_X_VERSION_10_14_4
#define MAC_OS_X_VERSION_10_14_4 101404
#endif

#ifndef MAC_OS_X_VERSION_10_14_5
#define MAC_OS_X_VERSION_10_14_5 101405
#endif

#ifndef MAC_OS_X_VERSION_10_14_6
#define MAC_OS_X_VERSION_10_14_6 101406
#endif

#ifndef MAC_OS_X_VERSION_10_15
#define MAC_OS_X_VERSION_10_15 101500
#endif

#ifndef MAC_OS_X_VERSION_10_15_1
#define MAC_OS_X_VERSION_10_15_1 101501
#endif

#ifndef MAC_OS_X_VERSION_10_15_2
#define MAC_OS_X_VERSION_10_15_2 101502
#endif

#ifndef MAC_OS_X_VERSION_10_15_3
#define MAC_OS_X_VERSION_10_15_3 101503
#endif

#ifndef MAC_OS_X_VERSION_10_15_4
#define MAC_OS_X_VERSION_10_15_4 101504
#endif

#ifndef MAC_OS_X_VERSION_10_15_5
#define MAC_OS_X_VERSION_10_15_5 101505
#endif

#ifndef MAC_OS_X_VERSION_10_15_6
#define MAC_OS_X_VERSION_10_15_6 101506
#endif

#ifndef MAC_OS_X_VERSION_10_16
#define MAC_OS_X_VERSION_10_16 101600
#endif

#ifndef MAC_OS_X_VERSION_11_0
#define MAC_OS_X_VERSION_11_0 110000
#endif

#ifndef MAC_OS_X_VERSION_11_1
#define MAC_OS_X_VERSION_11_1 110100
#endif

#ifndef MAC_OS_X_VERSION_11_2
#define MAC_OS_X_VERSION_11_2 110200
#endif

#ifndef MAC_OS_X_VERSION_11_3
#define MAC_OS_X_VERSION_11_3 110300
#endif

#ifndef MAC_OS_X_VERSION_11_4
#define MAC_OS_X_VERSION_11_4 110400
#endif

#ifndef MAC_OS_X_VERSION_11_5
#define MAC_OS_X_VERSION_11_5 110500
#endif

/*
 * Explicit support for weak-linking functions
 *
 * For some reason implicit weak-linking using '#pragma weak' and
 * '__attribute__((__weak__))' doesn't work (at least of some functions)
 * when building on 10.8 and deploying to * 10.5)
 *
 * The code below introduces infrastructure that makes it fairly
 * painless to do weak-linking anyway.
 *
 * Usage for function CFArrayCreate:
 * * Use 'WEAK_LINKED_NAME(CFArrayCreate)' at the start of a wrapper module
 * * Use 'USE(CFArrayCreate)' to actually call the function, don't use the
 *   actual function.
 * * Use 'CHECK_WEAK_LINK(module, CFArrayCreate)' in the module init function,
 *   this will remove "CFArrayCreate" from the module dictionary when the function
 *   cannot by found by dlsym.
 * * All access to function should be done through weak-refs like this.
 *
 * NOTE: When the version that introduced the function is known, that version number
 *       can be appended to the macros and the function will be hard-linked when
 *       the minimal deployment target is high enough.
 */
#include <dlfcn.h>

#define WEAK_LINKED_NAME(NAME) static __typeof__(&NAME) ptr_##NAME;
#define USE(NAME) ptr_##NAME
#define CHECK_WEAK_LINK(module, NAME)                                                    \
    do {                                                                                 \
        void* dl   = dlopen(NULL, RTLD_GLOBAL);                                          \
        ptr_##NAME = dlsym(dl, PyObjC_STR(NAME));                                        \
        dlclose(dl);                                                                     \
        if (ptr_##NAME == NULL) {                                                        \
            if (PyDict_DelItemString(PyModule_GetDict(module), PyObjC_STR(NAME)) < 0) {  \
                return NULL;                                                             \
            }                                                                            \
        }                                                                                \
    } while (0)

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_5
#define WEAK_LINKED_NAME_10_5(NAME)
#define USE_10_5(NAME) NAME
#define CHECK_WEAK_LINK_10_5(module, NAME)                                               \
    do {                                                                                 \
    } while (0)
#else
#define WEAK_LINKED_NAME_10_5(NAME) WEAK_LINKED_NAME(NAME)
#define USE_10_5(NAME) USE(NAME)
#define CHECK_WEAK_LINK_10_5(module, NAME) CHECK_WEAK_LINK(module, NAME)
#endif

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_6
#define WEAK_LINKED_NAME_10_6(NAME)
#define USE_10_6(NAME) NAME
#define CHECK_WEAK_LINK_10_6(module, NAME)                                               \
    do {                                                                                 \
    } while (0)
#else
#define WEAK_LINKED_NAME_10_6(NAME) WEAK_LINKED_NAME(NAME)
#define USE_10_6(NAME) USE(NAME)
#define CHECK_WEAK_LINK_10_6(module, NAME) CHECK_WEAK_LINK(module, NAME)
#endif

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_7
#define WEAK_LINKED_NAME_10_7(NAME)
#define USE_10_7(NAME) NAME
#define CHECK_WEAK_LINK_10_7(module, NAME)                                               \
    do {                                                                                 \
    } while (0)
#else
#define WEAK_LINKED_NAME_10_7(NAME) WEAK_LINKED_NAME(NAME)
#define USE_10_7(NAME) USE(NAME)
#define CHECK_WEAK_LINK_10_7(module, NAME) CHECK_WEAK_LINK(module, NAME)
#endif

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_8
#define WEAK_LINKED_NAME_10_8(NAME)
#define USE_10_8(NAME) NAME
#define CHECK_WEAK_LINK_10_8(module, NAME)                                               \
    do {                                                                                 \
    } while (0)
#else
#define WEAK_LINKED_NAME_10_8(NAME) WEAK_LINKED_NAME(NAME)
#define USE_10_8(NAME) USE(NAME)
#define CHECK_WEAK_LINK_10_8(module, NAME) CHECK_WEAK_LINK(module, NAME)
#endif

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_9
#define WEAK_LINKED_NAME_10_9(NAME)
#define USE_10_9(NAME) NAME
#define CHECK_WEAK_LINK_10_9(module, NAME)                                               \
    do {                                                                                 \
    } while (0)
#else
#define WEAK_LINKED_NAME_10_9(NAME) WEAK_LINKED_NAME(NAME)
#define USE_10_9(NAME) USE(NAME)
#define CHECK_WEAK_LINK_10_9(module, NAME) CHECK_WEAK_LINK(module, NAME)
#endif

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_10
#define WEAK_LINKED_NAME_10_10(NAME)
#define USE_10_10(NAME) NAME
#define CHECK_WEAK_LINK_10_10(module, NAME)                                              \
    do {                                                                                 \
    } while (0)
#else
#define WEAK_LINKED_NAME_10_10(NAME) WEAK_LINKED_NAME(NAME)
#define USE_10_10(NAME) USE(NAME)
#define CHECK_WEAK_LINK_10_10(module, NAME) CHECK_WEAK_LINK(module, NAME)
#endif

/*
 *
 * End of Cocoa definitions
 *
 */

/*
 *
 * Start of compiler support helpers
 *
 */

#ifdef __GNUC__
#define unlikely(x) __builtin_expect(!!(x), 0)
#define likely(x) __builtin_expect(!!(x), 1)
#else
#define likely(x) x
#define likely(x) x
#endif

/* On some versions of GCC <limits.h> defines LONG_LONG_MAX but not LLONG_MAX, compensate.
 */
#ifndef LLONG_MIN
#ifdef LONG_LONG_MIN
#define LLONG_MIN LONG_LONG_MIN
#define LLONG_MAX LONG_LONG_MAX
#define ULLONG_MAX ULONG_LONG_MAX
#endif
#endif

/*
 *
 * End of compiler support helpers
 *
 */

#if __LP64__
#define Py_ARG_NSInteger "l"
#define Py_ARG_NSUInteger "k"
#else
#define Py_ARG_NSInteger "i"
#define Py_ARG_NSUInteger "I"
#endif

#define PyObjC__STR(x) #x
#define PyObjC_STR(x) PyObjC__STR(x)

/*
 *
 * Python version compatibility
 *
 */

#ifndef Py_SET_TYPE
#define Py_SET_TYPE(obj, type) do { Py_TYPE((obj)) = (type); } while(0)
#endif

#ifndef Py_SET_SIZE
#define Py_SET_SIZE(obj, size) do { Py_SIZE((obj)) = (size); } while(0)
#endif

#ifndef Py_SET_REFCNT
#define Py_SET_REFCNT(obj, count) do { Py_REFCNT((obj)) = (count); } while(0)
#endif

/* Use CLINIC_SEP between the prototype and
 * description in doc strings, to get clean
 * docstrings.
 */
#define CLINIC_SEP "--\n"

/* Define PyObjC_UNICODE_FAST_PATH when
 * 1) We're before Python 3.3, and
 * 2) Py_UNICODE has the same size as unichar
 *
 * Python 3.3 has an optimized representation that
 * makes it impossible (and unnecessary) to use the
 * "fast path"
 */

extern int       PyObjC_Cmp(PyObject* o1, PyObject* o2, int* result);
extern PyObject* PyBytes_InternFromString(const char* v);
extern PyObject* PyBytes_InternFromStringAndSize(const char* v, Py_ssize_t l);

/*
 * A micro optimization: when using Python 3.3 or later it
 * is possible to access a 'char*' with an ASCII representation
 * of a unicode object without first converting it to a bytes
 * string (if the string can be encoded as ASCII in the first
 * place.
 *
 * This slightly reduces the object allocation rate during
 * attribute access.
 */
extern const char* PyObjC_Unicode_Fast_Bytes(PyObject* object);

#ifdef __clang__

#ifndef Py_LIMITED_API

/* This is a crude hack to disable a otherwise useful warning in the context of
 * PyTuple_SET_ITEM, without disabling it everywhere
 */
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Warray-bounds"
static inline void
_PyObjCTuple_SetItem(PyObject* tuple, Py_ssize_t idx, PyObject* value)
{
    PyTuple_SET_ITEM(tuple, idx, value);
}
#undef PyTuple_SET_ITEM
#define PyTuple_SET_ITEM(a, b, c) _PyObjCTuple_SetItem(a, b, c)

static inline PyObject*
_PyObjCTuple_GetItem(PyObject* tuple, Py_ssize_t idx)
{
    return PyTuple_GET_ITEM(tuple, idx);
}
#undef PyTuple_GET_ITEM
#define PyTuple_GET_ITEM(a, b) _PyObjCTuple_GetItem(a, b)

#pragma clang diagnostic pop

#endif /* !Py_LIMITED_API */

#endif /* __clang__ */

#define PyObjC_BEGIN_WITH_GIL                                                            \
    {                                                                                    \
        PyGILState_STATE _GILState;                                                      \
        _GILState = PyGILState_Ensure();

#define PyObjC_GIL_FORWARD_EXC()                                                         \
    do {                                                                                 \
        PyObjCErr_ToObjCWithGILState(&_GILState);                                        \
    } while (0)

#define PyObjC_GIL_RETURN(val)                                                           \
    do {                                                                                 \
        PyGILState_Release(_GILState);                                                   \
        return (val);                                                                    \
    } while (0)

#define PyObjC_GIL_RETURNVOID                                                            \
    do {                                                                                 \
        PyGILState_Release(_GILState);                                                   \
        return;                                                                          \
    } while (0)

#define PyObjC_END_WITH_GIL                                                              \
    PyGILState_Release(_GILState);                                                       \
    }

#endif /* PyObjC_COMPAT_H */
