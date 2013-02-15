#ifndef PyObjC_COMPAT_H
#define PyObjC_COMPAT_H

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
#define unlikely(x)  __builtin_expect (!!(x), 0)
#define likely(x)    __builtin_expect (!!(x), 1)
#else
#define likely(x)    x
#define likely(x)    x
#endif



#ifndef __has_feature
#  define __has_feature(x) 0
#endif

#if !__has_feature(objc_instancetype)
#  define instancetype id
#endif

/* On some versions of GCC <limits.h> defines LONG_LONG_MAX but not LLONG_MAX, compensate.  */
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

#   define PyErr_Format PyObjCErr_Format

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


#endif /* PyObjC_COMPAT_H */
