#ifndef PyObjC_COMPAT_H
#define PyObjC_COMPAT_H

/*
 *
 * Start of compiler definitions
 *
 */
#ifndef __has_feature
#  define __has_feature(x) 0
#endif
#ifndef __has_extension
#  define __has_extension(x) __has_feature(x)
#endif

#if !__has_feature(objc_instancetype)
#  define instancetype id
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
#ifndef CGFLOAT_DEFINED

#ifdef __LP64__
# error "Huh? 64-bit but no CFFloat available???"
#endif

typedef float CGFloat;
#define CGFLOAT_MIN FLT_MIN
#define CGFLOAT_MAX FLT_MAX
#define CGFLOAT_IS_DOUBLE 0
#define CGFLOAT_DEFINED

#endif /* CGFLOAT_DEFINED */

#ifndef NSINTEGER_DEFINED

#ifdef __LP64__
# error "Huh? 64-bit but no NSINTEGER available???"
#endif

typedef int NSInteger;
typedef unsigned int NSUInteger;

#define NSIntegerMax    LONG_MAX
#define NSIntegerMin    LONG_MIN
#define NSUIntegerMax   ULONG_MAX

#define NSINTEGER_DEFINED

#endif

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

#ifndef MAC_OS_X_VERSION_10_11
#define MAC_OS_X_VERSION_10_11 101100
#endif

#ifndef MAC_OS_X_VERSION_10_12
#define MAC_OS_X_VERSION_10_12 101200
#endif

#if PyObjC_BUILD_RELEASE <= 1005

/* On MacOS X, +signatureWithObjCTypes: is a method of NSMethodSignature,
 * but that method is not present in the header files until Mac OS X 10.5.
 *
 * Add a definition of the method when compiling on ancient OSX releases
 * to ensure that the code gets compiled without warnings.
 */
@interface NSMethodSignature (WarningKiller)
    +(instancetype)signatureWithObjCTypes:(const char*)types;
    @end /* interface NSMethodSignature */

#endif /* PyObjC_BUILD_RELEASE <= 1005 */

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

#define WEAK_LINKED_NAME(NAME)    static __typeof__(&NAME) ptr_ ## NAME;
#define USE(NAME)        ptr_ ## NAME
#define CHECK_WEAK_LINK(module, NAME) \
    do {                                            \
        void* dl = dlopen(NULL, RTLD_GLOBAL);                        \
        ptr_ ## NAME = dlsym(dl, PyObjC_STR(NAME));                    \
        dlclose(dl);                                    \
        if (ptr_ ## NAME == NULL) {                            \
            if (PyDict_DelItemString(PyModule_GetDict(module), PyObjC_STR(NAME)) < 0) {    \
                PyObjC_INITERROR();                        \
            }                                    \
        }                                        \
    } while(0)

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_5
#define WEAK_LINKED_NAME_10_5(NAME)
#define USE_10_5(NAME)                NAME
#define CHECK_WEAK_LINK_10_5(module, NAME) do {} while(0)
#else
#define WEAK_LINKED_NAME_10_5(NAME)         WEAK_LINKED_NAME(NAME)
#define USE_10_5(NAME)                USE(NAME)
#define CHECK_WEAK_LINK_10_5(module, NAME) CHECK_WEAK_LINK(module, NAME)
#endif

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_6
#define WEAK_LINKED_NAME_10_6(NAME)
#define USE_10_6(NAME)                NAME
#define CHECK_WEAK_LINK_10_6(module, NAME) do {} while(0)
#else
#define WEAK_LINKED_NAME_10_6(NAME)         WEAK_LINKED_NAME(NAME)
#define USE_10_6(NAME)                USE(NAME)
#define CHECK_WEAK_LINK_10_6(module, NAME) CHECK_WEAK_LINK(module, NAME)
#endif

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_7
#define WEAK_LINKED_NAME_10_7(NAME)
#define USE_10_7(NAME)                NAME
#define CHECK_WEAK_LINK_10_7(module, NAME) do {} while(0)
#else
#define WEAK_LINKED_NAME_10_7(NAME)         WEAK_LINKED_NAME(NAME)
#define USE_10_7(NAME)                USE(NAME)
#define CHECK_WEAK_LINK_10_7(module, NAME) CHECK_WEAK_LINK(module, NAME)
#endif

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_8
#define WEAK_LINKED_NAME_10_8(NAME)
#define USE_10_8(NAME)                NAME
#define CHECK_WEAK_LINK_10_8(module, NAME) do {} while(0)
#else
#define WEAK_LINKED_NAME_10_8(NAME)         WEAK_LINKED_NAME(NAME)
#define USE_10_8(NAME)                USE(NAME)
#define CHECK_WEAK_LINK_10_8(module, NAME) CHECK_WEAK_LINK(module, NAME)
#endif

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_9
#define WEAK_LINKED_NAME_10_9(NAME)
#define USE_10_9(NAME)                NAME
#define CHECK_WEAK_LINK_10_9(module, NAME) do {} while(0)
#else
#define WEAK_LINKED_NAME_10_9(NAME)         WEAK_LINKED_NAME(NAME)
#define USE_10_9(NAME)                USE(NAME)
#define CHECK_WEAK_LINK_10_9(module, NAME) CHECK_WEAK_LINK(module, NAME)
#endif

#if MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_10
#define WEAK_LINKED_NAME_10_10(NAME)
#define USE_10_10(NAME)                NAME
#define CHECK_WEAK_LINK_10_10(module, NAME) do {} while(0)
#else
#define WEAK_LINKED_NAME_10_10(NAME)         WEAK_LINKED_NAME(NAME)
#define USE_10_10(NAME)                USE(NAME)
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
#define unlikely(x) __builtin_expect (!!(x), 0)
#define likely(x) __builtin_expect (!!(x), 1)
#else
#define likely(x) x
#define likely(x) x
#endif




/* On some versions of GCC <limits.h> defines LONG_LONG_MAX but not LLONG_MAX, compensate. */
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


/*
 *
 * Python version compatibility
 *
 */


#define PyObjC__STR(x) #x
#define PyObjC_STR(x) PyObjC__STR(x)


/* Use CLINIC_SEP between the prototype and
 * description in doc strings, to get clean
 * docstrings.
 */
#if PY_VERSION_HEX >= 0x03040000

# define CLINIC_SEP "--\n"

#else

# define CLINIC_SEP ""

#endif

/* Define PyObjC_UNICODE_FAST_PATH when
 * 1) We're before Python 3.3, and
 * 2) Py_UNICODE has the same size as unichar
 *
 * Python 3.3 has an optimized representation that
 * makes it impossible (and unnecessary) to use the
 * "fast path"
 */
#if PY_VERSION_HEX >= 0x03030000

#undef PyObjC_UNICODE_FAST_PATH

#elif Py_UNICODE_SIZE == 2

#define PyObjC_UNICODE_FAST_PATH

#endif

#if PY_MAJOR_VERSION == 2

    typedef long Py_hash_t;

#   ifndef Py_ARG_BYTES
#       define Py_ARG_BYTES "z"
#   endif

    /* Cast a PyObject* to the type expected by the 2.x C API.
     * This is a macro because the cast is not necessary for the 3.x C API)
     */
#   define UNICODE_CAST(item)  ((PyUnicodeObject*)(item))
#   define SLICE_CAST(item)    ((PySliceObject*)(item))

#   define Py_REFCNT(ob)           (((PyObject*)(ob))->ob_refcnt)
#   define Py_TYPE(ob)             (((PyObject*)(ob))->ob_type)
#   define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)


    /* Source-level backward compatibility: use PyCapsule API in sources, fall back to
     * PyCObject when needed.
     */
#   if PY_MINOR_VERSION < 7
#       define PyCapsule_New(pointer, name, destructor) PyCObject_FromVoidPtr(pointer, destructor)
#       define PyCapsule_GetPointer(object, name) PyCObject_AsVoidPtr(object)
#       define PyCapsule_CheckExact(object)    PyCObject_Check(object)
#   endif /* Python < 2.7 */

#ifdef OBJC_VERSION
#   define PyErr_Format PyObjCErr_Format
#endif

    extern PyObject* PyObjCErr_Format(PyObject* exception, const char* format, ...);


#   define PyText_Check PyString_Check
#   define PyText_FromFormat PyString_FromFormat
#   define PyText_FromString PyString_FromString
#   define PyText_FromStringAndSize PyString_FromStringAndSize
#   define PyText_InternFromString PyString_InternFromString
#   define PyText_InternInPlace PyString_InternInPlace
#   define PyText_Append PyString_ConcatAndDel
#   define PyText_AsString    PyString_AsString

#   ifndef PyBytes_FromString
#       define PyBytes_AsString    PyString_AsString
#       define PyBytes_Size        PyString_Size
#       define PyBytes_FromString    PyString_FromString
#       define PyBytes_FromStringAndSize    PyString_FromStringAndSize
#       define PyBytes_AS_STRING    PyString_AS_STRING
#       define PyBytes_GET_SIZE    PyString_GET_SIZE
#   endif /* !PyBytes_FromString */

#   define PyBytes_InternFromString    PyString_InternFromString
#   define PyBytes_InternFromStringAndSize    PyObjCString_InternFromStringAndSize

    extern PyObject* PyObjCString_InternFromStringAndSize(const char* v, Py_ssize_t l);

#   define PyObjC_INITERROR() return
#   define PyObjC_INITDONE() return

#   define PyObjC_MODULE_INIT(name) \
        void init##name(void); \
        void __attribute__ ((__visibility__ ("default"))) init##name(void)

#   define PyObjC_MODULE_CREATE(name) \
        Py_InitModule4(PyObjC_STR(name), mod_methods, \
            NULL, NULL, PYTHON_API_VERSION);


# else /* Py_MAJOR_VERSION == 3 */

#   ifndef Py_ARG_BYTES
#       define Py_ARG_BYTES "y"
#   endif

#   define UNICODE_CAST(item) (item)
#   define SLICE_CAST(item) (item)


#   define PyText_Check PyUnicode_Check
#   define PyText_FromFormat PyUnicode_FromFormat
#   define PyText_FromString PyUnicode_FromString
#   define PyText_FromStringAndSize PyUnicode_FromStringAndSize
#   define PyText_InternFromString PyUnicode_InternFromString
#   define PyText_InternInPlace PyUnicode_InternInPlace
#   define PyText_Append PyUnicode_Append
#   define PyText_AsString _PyUnicode_AsString

#   define PyInt_FromLong PyLong_FromLong
#   define PyInt_FromString PyLong_FromString

    extern int PyObject_Cmp(PyObject *o1, PyObject *o2, int *result);
    extern PyObject* PyBytes_InternFromString(const char* v);
    extern PyObject* PyBytes_InternFromStringAndSize(const char* v, Py_ssize_t l);

#   define PyObjC_INITERROR() return NULL
#   define PyObjC_INITDONE() return m

#   define PyObjC_MODULE_INIT(name) \
        static struct PyModuleDef mod_module = { \
            PyModuleDef_HEAD_INIT, \
            PyObjC_STR(name), \
            NULL, \
            0, \
            mod_methods, \
            NULL, \
            NULL, \
            NULL, \
            NULL \
        }; \
        \
        PyObject* PyInit_##name(void); \
        PyObject* __attribute__ ((__visibility__ ("default"))) PyInit_##name(void)

#define PyObjC_MODULE_CREATE(name) \
    PyModule_Create(&mod_module);

#   if PY_MINOR_VERSION >= 3

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

#       define PyObjC_FAST_UNICODE_ASCII 1

        extern const char* PyObjC_Unicode_Fast_Bytes(PyObject* object);

#   endif /* Python >= 3.3 */

#endif /* PY_MAJOR_VERSION == 3 */




#ifdef __clang__

/* This is a crude hack to disable a otherwise useful warning in the context of
 * PyTuple_SET_ITEM, without disabling it everywhere
 */
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Warray-bounds"
static inline void _PyObjCTuple_SetItem(PyObject* tuple, Py_ssize_t idx, PyObject* value)
{
    PyTuple_SET_ITEM(tuple, idx, value);
}
#undef PyTuple_SET_ITEM
#define PyTuple_SET_ITEM(a, b, c) _PyObjCTuple_SetItem(a, b, c)

static inline PyObject* _PyObjCTuple_GetItem(PyObject* tuple, Py_ssize_t idx)
{
    return PyTuple_GET_ITEM(tuple, idx);
}
#undef PyTuple_GET_ITEM
#define PyTuple_GET_ITEM(a, b) _PyObjCTuple_GetItem(a, b)

#pragma clang diagnostic pop

#endif /* __clang__ */


/*
 *
 * Helper macros for Cocoa exceptions and the Python GIL
 *
 */

#ifdef NO_OBJC2_RUNTIME

#define PyObjC_DURING \
        Py_BEGIN_ALLOW_THREADS \
        NS_DURING

#define PyObjC_HANDLER NS_HANDLER

#define PyObjC_ENDHANDLER \
        NS_ENDHANDLER \
        Py_END_ALLOW_THREADS

#else /* !NO_OBJC2_RUNTIME */

#define    PyObjC_DURING \
        Py_BEGIN_ALLOW_THREADS \
        @try {

#define PyObjC_HANDLER } @catch(NSObject* _localException) { \
        NSException* localException __attribute__((__unused__))= (NSException*)_localException;

#define PyObjC_ENDHANDLER \
        } \
        Py_END_ALLOW_THREADS

#endif /* !NO_OBJC2_RUNTIME */

#define PyObjC_BEGIN_WITH_GIL \
    { \
        PyGILState_STATE _GILState; \
        _GILState = PyGILState_Ensure();

#define PyObjC_GIL_FORWARD_EXC() \
        do { \
            PyObjCErr_ToObjCWithGILState(&_GILState); \
        } while (0)


#define PyObjC_GIL_RETURN(val) \
        do { \
            PyGILState_Release(_GILState); \
            return (val); \
        } while (0)

#define PyObjC_GIL_RETURNVOID \
        do { \
            PyGILState_Release(_GILState); \
            return; \
        } while (0)


#define PyObjC_END_WITH_GIL \
        PyGILState_Release(_GILState); \
    }


#endif /* PyObjC_COMPAT_H */
