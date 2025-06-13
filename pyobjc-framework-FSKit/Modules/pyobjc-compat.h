#ifndef PyObjC_COMPAT_H
#define PyObjC_COMPAT_H

#ifndef NS_ASSUME_NONNULL_BEGIN
/* Old compiler without the Nullability attributes */
#define NS_ASSUME_NONNULL_BEGIN
#define NS_ASSUME_NONNULL_END
#define _Nullable
#define _Nonnull
#endif

NS_ASSUME_NONNULL_BEGIN

#ifdef USE_STATIC_ANALYZER
#define CLANG_SUPPRESS [[clang::suppress]]
#else
#define CLANG_SUPPRESS
#endif

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

#ifdef __has_attribute
#if __has_attribute(objc_subclassing_restricted)
#define PyObjC_FINAL_CLASS __attribute__((__objc_subclassing_restricted__))
#endif
#endif
#ifndef PyObjC_FINAL_CLASS
#define PyObjC_FINAL_CLASS
#endif

/*
 *
 * Start of compiler support helpers
 *
 * XXX: Are these needed?
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
 * XXX: These two are no longer needed, all supported platforms
 *      are 64-bit
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
#define Py_SET_TYPE(obj, type)                                                           \
    do {                                                                                 \
        Py_TYPE((obj)) = (type);                                                         \
    } while (0)
#endif

#ifndef Py_SET_SIZE
#define Py_SET_SIZE(obj, size)                                                           \
    do {                                                                                 \
        Py_SIZE((obj)) = (size);                                                         \
    } while (0)
#endif

#ifndef Py_SET_REFCNT
#define Py_SET_REFCNT(obj, count)                                                        \
    do {                                                                                 \
        Py_REFCNT((obj)) = (count);                                                      \
    } while (0)
#endif

#if PY_VERSION_HEX < 0x03090000

/* For use on Python 3.8 and earlier. PyObjC doesn't use the
 * "flag" bit internally.
 */

#ifndef PY_VECTORCALL_ARGUMENTS_OFFSET
#define PY_VECTORCALL_ARGUMENTS_OFFSET ((size_t)1 << (8 * sizeof(size_t) - 1))
#endif

#define PyVectorcall_NARGS(nargsf) ((nargsf) & ~PY_VECTORCALL_ARGUMENTS_OFFSET)

#ifdef OBJC_VERSION
/* Don't use PyObject prefixed symbols in our binaries */
#define PyObject_Vectorcall PyObjC_Vectorcall
#define PyObject_VectorcallMethod PyObjC_VectorcallMethod

extern PyObject* _Nullable PyObject_Vectorcall(PyObject* callable,
                                               PyObject* _Nonnull const* _Nonnull args,
                                               size_t nargsf,
                                               PyObject* _Nullable kwnames);
extern PyObject* _Nullable PyObject_VectorcallMethod(
    PyObject* name, PyObject* _Nonnull const* _Nonnull args, size_t nargsf,
    PyObject* _Nullable kwnames);
#endif

#endif /* Python < 3.9 */

/* Use CLINIC_SEP between the prototype and
 * description in doc strings, to get clean
 * docstrings.
 */
#define CLINIC_SEP "--\n"

extern int PyObjC_Cmp(PyObject* o1, PyObject* o2, int* result);

/*
 * A micro optimization: when using Python 3.3 or later it
 * is possible to access a 'char*' with an ASCII representation
 * of a unicode object without first converting it to a bytes
 * string (if the string can be encoded as ASCII in the first
 * place.
 *
 * This slightly reduces the object allocation rate during
 * attribute access.
 *
 * XXX: Use PyUnicode_AsUTF8 instead.
 */
extern const char* _Nullable PyObjC_Unicode_Fast_Bytes(PyObject* object);

#ifdef __clang__

#ifndef Py_LIMITED_API

static inline PyObject* _Nullable* _Nonnull PyTuple_ITEMS(PyObject* tuple)
{
    return &PyTuple_GET_ITEM(tuple, 0); // LCOV_BR_EXCL_LINE
}

/* This is a crude hack to disable a otherwise useful warning in the context of
 * PyTuple_SET_ITEM, without disabling it everywhere
 */
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Warray-bounds"
static inline void
_PyObjCTuple_SetItem(PyObject* tuple, Py_ssize_t idx, PyObject* _Nullable value)
{
    PyTuple_SET_ITEM(tuple, idx, value);
}
#undef PyTuple_SET_ITEM
#define PyTuple_SET_ITEM(a, b, c) _PyObjCTuple_SetItem(a, b, c)

static inline PyObject*
_PyObjCTuple_GetItem(PyObject* tuple, Py_ssize_t idx)
{
    return PyTuple_GET_ITEM(tuple, idx); // LCOV_BR_EXCL_LINE
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

#define PyObjC_LEAVE_GIL                                                                 \
    do {                                                                                 \
        PyGILState_Release(_GILState);                                                   \
    } while (0)

#if PY_VERSION_HEX < 0x030a0000

static inline PyObject* Py_NewRef(PyObject* o)
{
    Py_INCREF(o);
    return o;
}

static inline PyObject* Py_XNewRef(PyObject* o)
{
    Py_XINCREF(o);
    return o;
}

#endif /* PY_VERSION_HEX < 0x030a0000 */

#if PY_VERSION_HEX < 0x030d0000
#define Py_BEGIN_CRITICAL_SECTION(value) { (void)(value);
#define Py_END_CRITICAL_SECTION() }
#define Py_EXIT_CRITICAL_SECTION() ((void)0)

#define Py_BEGIN_CRITICAL_SECTION2(value1, value2) { (void)(value1); (void)(value2);
#define Py_END_CRITICAL_SECTION2() }
#define Py_EXIT_CRITICAL_SECTION2() ((void)0)

#define PyObjC_ATOMIC

#else

#ifdef Py_GIL_DISABLED
#define Py_EXIT_CRITICAL_SECTION() PyCriticalSection_End(&_py_cs)
#define Py_EXIT_CRITICAL_SECTION2() PyCriticalSection2_End(&_py_cs2)
#define PyObjC_ATOMIC _Atomic
#else
#define Py_EXIT_CRITICAL_SECTION() ((void)0)
#define Py_EXIT_CRITICAL_SECTION2() ((void)0)
#define PyObjC_ATOMIC
#endif

#endif

#if PY_VERSION_HEX < 0x030d0000
static inline int PyDict_GetItemRef(PyObject *p, PyObject *key, PyObject * _Nonnull* _Nullable result)
{
    *result = PyDict_GetItemWithError(p, key);
    if (*result == NULL) {
        if (PyErr_Occurred()) {
            return -1;
        } else {
            return 0;
        }
    } else {
        Py_INCREF(*result);
        return 1;
    }
}

static inline PyObject* _Nullable PyList_GetItemRef(PyObject* l, Py_ssize_t i)
{
    PyObject* result = PyList_GetItem(l, i);
    Py_XINCREF(result);
    return result;
}
#endif

#if PY_VERSION_HEX < 0x030c0000
static inline PyObject* PyType_GetDict(PyTypeObject* type)
{
    PyObject* result = type->tp_dict;
    Py_INCREF(result);
    return result;
}
#endif

#if PY_VERSION_HEX >= 0x030c0000 && PY_VERSION_HEX < 0x030e0000
/*
 * These are available in 3.14 and above, the definitions below
 * mirror the private implementation in 3.13.
 */
static inline int PyUnstable_Object_IsUniquelyReferenced(PyObject* ob)
{
#ifdef Py_GIL_DISABLED
    return (_Py_IsOwnedByCurrentThread(ob) &&
            _Py_atomic_load_uint32_relaxed(&ob->ob_ref_local) == 1 &&
            _Py_atomic_load_ssize_relaxed(&ob->ob_ref_shared) == 0);
#else
    return Py_REFCNT(ob) == 1;
#endif
}

static inline void
PyUnstable_EnableTryIncRef(PyObject* op __attribute__((__unused__)))
{
#ifdef Py_GIL_DISABLED
    for (;;) {
        Py_ssize_t shared = _Py_atomic_load_ssize_relaxed(&op->ob_ref_shared);
        if ((shared & _Py_REF_SHARED_FLAG_MASK) != 0) {
            // Nothing to do if it's in WEAKREFS, QUEUED, or MERGED states.
            return;
        }
        if (_Py_atomic_compare_exchange_ssize(
                &op->ob_ref_shared, &shared, shared | _Py_REF_MAYBE_WEAKREF)) {
            return;
        }
    }
#endif
}

#ifdef Py_GIL_DISABLED
static inline int
_Py_TryIncrefFast(PyObject *op) {
    uint32_t local = _Py_atomic_load_uint32_relaxed(&op->ob_ref_local);
    local += 1;
    if (local == 0) {
        // immortal
        return 1;
    }
    if (_Py_IsOwnedByCurrentThread(op)) {
        _Py_INCREF_STAT_INC();
        _Py_atomic_store_uint32_relaxed(&op->ob_ref_local, local);
#ifdef Py_REF_DEBUG
        _Py_IncRefTotal(_PyThreadState_GET());
#endif
        return 1;
    }
    return 0;
}

static inline int
_Py_TryIncRefShared(PyObject *op)
{
    Py_ssize_t shared = _Py_atomic_load_ssize_relaxed(&op->ob_ref_shared);
    for (;;) {
        // If the shared refcount is zero and the object is either merged
        // or may not have weak references, then we cannot incref it.
        if (shared == 0 || shared == _Py_REF_MERGED) {
            return 0;
        }

        if (_Py_atomic_compare_exchange_ssize(
                &op->ob_ref_shared,
                &shared,
                shared + (1 << _Py_REF_SHARED_SHIFT))) {
#ifdef Py_REF_DEBUG
            _Py_IncRefTotal(_PyThreadState_GET());
#endif
            _Py_INCREF_STAT_INC();
            return 1;
        }
    }
}
#endif

static inline int
PyUnstable_TryIncRef(PyObject *op __attribute__((__unused__)))
{
#ifdef Py_GIL_DISABLED
    return _Py_TryIncrefFast(op) || _Py_TryIncRefShared(op);
#else
    if (Py_REFCNT(op) > 0) {
        Py_INCREF(op);
        return 1;
    }
    return 0;
#endif
}
#endif

NS_ASSUME_NONNULL_END

#endif /* PyObjC_COMPAT_H */
