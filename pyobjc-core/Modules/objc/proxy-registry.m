#include "pyobjc.h"

#include <objc/objc.h>
#include <objc/runtime.h>

extern id   objc_loadWeakRetained(id* value);
extern void objc_release(id value);
extern id   objc_retain(id value);

NS_ASSUME_NONNULL_BEGIN

#ifdef Py_GIL_DISABLED
/*
 * NSMapTable is not thread safe when using the functional interface.
 *
 * Furthermore the code does some actions in multiple calls to the
 * NSMapTable API.
 *
 * For the traditional build this API is protected
 * by the GIL, for the free threaded build use a separate lock.
 *
 * XXX:
 * - Investigate another data structure
 * - Consider using two locks for the two maps.
 */
static PyMutex proxy_mutex = {0};
#endif

static NSMapTable* _Nonnull python_proxies;
static NSMapTable* _Nonnull objc_proxies;

/*
 * Using weak references to store the ObjC proxy values,
 * that way the cached value is cleanup atomaticly when
 * the proxy value is deallocated.
 */
struct weak_value {
    int refcnt;
    id _Nullable value;
};

static void
weak_value_retain(NSMapTable* table __attribute__((__unused__)),
                  const void* _Nonnull _value)
{
    struct weak_value* value = (struct weak_value*)_value;

    value->refcnt++;
}

static void
weak_value_release(NSMapTable* table __attribute__((__unused__)), void* _value)
{
    struct weak_value* value = (struct weak_value*)_value;

    if (--(value->refcnt) == 0) {
        objc_storeWeak(&value->value, nil);
        free(value);
    }
}

// LCOV_EXCL_START
/* Only used for debugging, won't be used in normal operation */
static NSString* _Nullable weak_value_describe(NSMapTable* table
                                               __attribute__((__unused__)),
                                               const void* _value)
{
    struct weak_value* value = (struct weak_value*)_value;
    id                 ptr   = objc_loadWeakRetained(&value->value);

    NSString* result =
        [NSString stringWithFormat:@"<weak_value %p refcnt %d>", ptr, value->refcnt];
    objc_release(ptr);
    return result;
}
// LCOV_EXCL_STOP

static struct weak_value* _Nullable weak_value_alloc(id value)
{
    struct weak_value* result = malloc(sizeof(struct weak_value));
    if (unlikely(result == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;                // LCOV_EXCL_LINE
    }
    result->refcnt = 1;
    result->value  = nil;
    objc_storeWeak(&result->value, value);
    return result;
}

static NSMapTableValueCallBacks weak_value_callbacks = {
    .describe = weak_value_describe,
    .retain   = weak_value_retain,
    .release  = weak_value_release,
};

int
PyObjC_InitProxyRegistry(PyObject* module __attribute__((__unused__)))
{
    python_proxies = NSCreateMapTable(PyObjCUtil_PointerKeyCallBacks,
                                      PyObjCUtil_PointerValueCallBacks, 0);

    if (unlikely(python_proxies == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot create NSMapTable for python_proxies");
        return -1;
        // LCOV_EXCL_STOP
    }

    objc_proxies =
        NSCreateMapTable(PyObjCUtil_PointerKeyCallBacks, weak_value_callbacks, 0);
    if (unlikely(objc_proxies == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_RuntimeError, "Cannot create NSMapTable for objc_proxies");
        return -1;
        // LCOV_EXCL_STOP
    }
    return 0;
}

PyObject*
PyObjC_RegisterPythonProxy(id original, PyObject* proxy)
{
#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif

    PyObject* current = NSMapInsertIfAbsent(python_proxies, original, proxy);
#ifdef Py_GIL_DISABLED
    if (current != NULL) {
        if (PyUnstable_TryIncRef(current)) {
            PyMutex_Unlock(&proxy_mutex);
            return current;
        } else {
            PyUnstable_EnableTryIncRef(proxy);
            NSMapInsert(python_proxies, original, proxy);
            Py_INCREF(proxy);
            PyMutex_Unlock(&proxy_mutex);
            return proxy;
        }

    } else {
        Py_INCREF(proxy);
        PyUnstable_EnableTryIncRef(proxy);
        PyMutex_Unlock(&proxy_mutex);
        return proxy;
    }
#else  /* ! Py_GIL_DISABLED */
    if (current != NULL) {
        Py_INCREF(current);
        return current;
    } else {
        Py_INCREF(proxy);
        return proxy;
    }
#endif /* ! Py_GIL_DISABLED */
}

/*
 * This function is used to release a "transient" proxy value.
 *
 * It converts a transient proxy value into a full proxy with a
 * strong reference to the value when the proxy will stay alive
 * (refcount > 1 in the GIL build).
 *
 * This has some challenges in the free threaded build.
 */
void
PyObjC_MaybeKeepAlivePythonProxy(PyObject* proxy)
{
    assert(PyObjCObject_Check(proxy));
#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif

#if 0
        printf("\nRT %#x %d %#x %#x %p %p\n", PyObjCObject_FLAGS(proxy) & PyObjCObject_kSHOULD_NOT_RELEASE,
            _Py_IsOwnedByCurrentThread(proxy),
            _Py_atomic_load_uint32_relaxed(&proxy->ob_ref_local),
            _Py_atomic_load_uint32_relaxed(&proxy->ob_ref_shared),
            PyObjC_FindPythonProxy(PyObjCObject_OBJECT(proxy)),
            proxy
            );
#endif

#ifdef Py_GIL_DISABLED
    /* XXX: This is needs work: relies on private Python API and its not clear if the code
     * is race free.
     *
     *      ``PyUnstable_Object_IsUniquelyReferenced`` returns false
     *      for objects that were used with ``PyUnstable_EnableTryIncRef``, even if the
     *      value has only one reference.
     *
     *      The code below open codes a variant on
     * ``!PyUnstable_Object_IsUniquelyReferenced()``, and tries to avoid race conditions
     * that could result in a long living proxy object only has a weak reference to the
     * Objective-C value.
     *
     *      Notes:
     *      - Current thread should own 'proxy', it was created locally in
     * __pyobjc_PythonTransient__
     *      - The WEAKREF flag is set due to using PyUnstable_EnableTryIncRef()
     *      - I'm not convinced yet that this code is race-free. Probably:
     *        * ob_ref_shared going from 1 to 0 while this runs should be fine, value is
     * still alive
     *        * ob_ref_shared going from 0 to 1 would be problematic, but shouldn't happen
     *          as we're not doing anything that passes a reference to a different thread
     * (????) and other threads cannot fetch a reference from the mapping because we own
     * proxy_mutex.
     */

    assert(_Py_IsOwnedByCurrentThread(proxy));
    assert(_Py_atomic_load_uint32_relaxed(&proxy->ob_ref_local) >= 1);
    if ((PyObjCObject_FLAGS(proxy) & PyObjCObject_kSHOULD_NOT_RELEASE) != 0
        && (!_Py_IsOwnedByCurrentThread(proxy)
            || _Py_atomic_load_uint32_relaxed(&proxy->ob_ref_local) != 1
            || (_Py_atomic_load_ssize_relaxed(&proxy->ob_ref_shared)
                & ~_Py_REF_SHARED_FLAG_MASK)
                   != 0))
#else
    if ((PyObjCObject_FLAGS(proxy) & PyObjCObject_kSHOULD_NOT_RELEASE) != 0
        && Py_REFCNT(proxy) != 1)
#endif
    {
        /* Proxy value will stay alive, convert to a strong reference
         *
         * The mutex is unlocked before calling -retain to avoid reentry issues
         * when there's a Python implementation for that method.
         *
         * This is safe because out caller owns a reference to proxy, it
         * cannot deallocate behind our back.
         */
#ifdef Py_GIL_DISABLED
        PyMutex_Unlock(&proxy_mutex);
#endif
        @try {
            [PyObjCObject_OBJECT(proxy) retain];
        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            return;
        }
        PyObjCObject_FLAGS(proxy) &= ~PyObjCObject_kSHOULD_NOT_RELEASE;
    } else {
        /* Make sure that 'proxy' doesn't get used while deallocating the weak reference
         */
        PyObject* current = NSMapGet(python_proxies, PyObjCObject_OBJECT(proxy));
        if (current == proxy) {
            NSMapRemove(python_proxies, PyObjCObject_OBJECT(proxy));
        }
#ifdef Py_GIL_DISABLED
        PyMutex_Unlock(&proxy_mutex);
#endif
    }
}

id NS_RETURNS_RETAINED _Nullable PyObjC_RegisterObjCProxy(PyObject* original, id proxy)
{
    id _Nullable result;
#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif
    struct weak_value* weak = NSMapGet(objc_proxies, original);
    if (weak != NULL) {
        id current = objc_loadWeakRetained(&weak->value);
        if (likely(current != nil)) { // LCOV_BR_EXCL_LINE
            result = current;
        } else {
            // LCOV_EXCL_START
            //
            // XXX: Spent more time on trying to hit this path.
            //
            // Regular code pattern is PyObjC_FindObjCProxy is
            // used before creating a proxy and calling this
            // function.
            //
            // There still is a race, but it is very small.
            objc_retain(proxy);
            objc_storeWeak(&weak->value, proxy);
            result = proxy;
            // LCOV_EXCL_STOP
        }
    } else {
        weak = weak_value_alloc(proxy);
        if (unlikely(weak == NULL)) { // LCOV_BR_EXCL_LINE
            result = nil;             // LCOV_EXCL_LINE
        } else {                      // LCOV_EXCL_LINE
            NSMapInsert(objc_proxies, original, weak);
            objc_retain(proxy);
            weak_value_release(objc_proxies, weak);
            result = proxy;
        }
    }

#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&proxy_mutex);
#endif

    return result;
}

void
PyObjC_UnregisterPythonProxy(id original, PyObject* proxy)
{
    PyObject* current;
    assert(original != nil);

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif

    current = NSMapGet(python_proxies, original);
    if (current == proxy) {
        NSMapRemove(python_proxies, original);
    }

#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&proxy_mutex);
#endif

} // LCOV_BR_EXCL_LINE

void
PyObjC_UnregisterObjCProxy(PyObject* original, id proxy)
{
    struct weak_value* record;
    id                 v;

    if (original == NULL)
        return;

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif
    record = NSMapGet(objc_proxies, original);
    if (record != NULL) {
        v = objc_loadWeak(&record->value);
        if (v == proxy || v == nil) { // LCOV_BR_EXCL_LINE
            NSMapRemove(objc_proxies, original);
        }
    }
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&proxy_mutex);
#endif

} // LCOV_BR_EXCL_LINE

PyObject* _Nullable PyObjC_FindPythonProxy(id original)
{
    PyObject* current;

    assert(original != nil);

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif

    current = NSMapGet(python_proxies, original);
    if (current == NULL) {
#ifdef Py_GIL_DISABLED
        PyMutex_Unlock(&proxy_mutex);
#endif
        return NULL;
    }

#ifdef Py_GIL_DISABLED
    if (PyUnstable_TryIncRef(current)) {
        PyMutex_Unlock(&proxy_mutex);
        return current;
    }
    PyMutex_Unlock(&proxy_mutex);
    return NULL;
#else
    Py_INCREF(current);
    return current;
#endif
}

id _Nullable NS_RETURNS_RETAINED
PyObjC_FindObjCProxy(PyObject* original)
{
    id result;

    assert(original != Py_None);

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif

    struct weak_value* record = NSMapGet(objc_proxies, original);
    if (record == NULL) {
        result = nil;
    } else {
        result = objc_loadWeakRetained(&record->value);
    }
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&proxy_mutex);
#endif

    return result;
}

NS_ASSUME_NONNULL_END
