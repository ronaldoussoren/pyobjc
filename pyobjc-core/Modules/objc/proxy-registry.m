#include "pyobjc.h"

#include <objc/runtime.h>
#include <objc/objc.h>

extern id objc_loadWeakRetained(id* value);
extern void objc_release(id value);
extern id objc_retain(id value);

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
static PyMutex proxy_mutex = { 0 };
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

static void weak_value_retain(NSMapTable* table __attribute__((__unused__)), const void* _Nonnull _value)
{
    struct weak_value* value = (struct weak_value*)_value;

    value->refcnt++;
}

static void weak_value_release(NSMapTable* table __attribute__((__unused__)), void* _value)
{
    struct weak_value* value = (struct weak_value*)_value;

    if (--(value->refcnt) == 0) {
        objc_storeWeak(&value->value, nil);
        free(value);
    }
}

static NSString* _Nullable weak_value_describe(NSMapTable* table __attribute__((__unused__)), const void* _value)
{
    struct weak_value* value = (struct weak_value*)_value;
    id ptr = objc_loadWeakRetained(&value->value);

    NSString* result =  [NSString stringWithFormat:@"<weak_value %p refcnt %d>", ptr, value->refcnt];
    objc_release(ptr);
    return result;
}
static struct weak_value* _Nullable weak_value_alloc(id value)
{
    struct weak_value* result = malloc(sizeof(struct weak_value));
    if (result == NULL) {
        return NULL;
    }
    result->refcnt = 1;
    result->value = nil;
    objc_storeWeak(&result->value, value);
    return result;
}

static NSMapTableValueCallBacks weak_value_callbacks = {
    .describe = weak_value_describe,
    .retain = weak_value_retain,
    .release = weak_value_release,
};



int
PyObjC_InitProxyRegistry(PyObject* module __attribute__((__unused__)))
{
    python_proxies = NSCreateMapTable(PyObjCUtil_PointerKeyCallBacks,
                                      PyObjCUtil_PointerValueCallBacks, 0);

    if (python_proxies == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot create NSMapTable for python_proxies");
        return -1;
        // LCOV_EXCL_STOP
    }

    objc_proxies = NSCreateMapTable(PyObjCUtil_PointerKeyCallBacks,
                                    weak_value_callbacks, 0);
    if (objc_proxies == NULL) { // LCOV_BR_EXCL_LINE
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

    PyObject* current = NSMapGet(python_proxies, original);
    if (current != NULL) {
        Py_INCREF(current);
        proxy = current;
    } else {
        NSMapInsert(python_proxies, original, proxy);
        Py_INCREF(proxy);
    }

#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&proxy_mutex);
#endif

    return proxy;
}

id NS_RETURNS_RETAINED _Nullable
PyObjC_RegisterObjCProxy(PyObject* original, id proxy)
{
    id _Nullable result;
#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif
    struct weak_value* weak = NSMapGet(objc_proxies, original);
   if (weak != NULL) {
        id current = objc_loadWeakRetained(&weak->value);
        if (current != nil) {
            result = current;
        } else {
            objc_retain(proxy);
            objc_storeWeak(&weak->value, proxy);
            result = proxy;
        }
    } else {
        weak = weak_value_alloc(proxy);
        if (weak == NULL) {
            result = nil;
        } else {
            NSMapInsert(objc_proxies, original, weak);
            objc_retain(proxy);
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
    PyObject* v;

    if (original == nil)
        return;

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif

    v = NSMapGet(python_proxies, original);
    if (v == proxy) {
        NSMapRemove(python_proxies, original);
    }

#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&proxy_mutex);
#endif

}

void
PyObjC_UnregisterObjCProxy(PyObject* original, id proxy)
{
    struct weak_value* record;
    id v;

    if (original == NULL)
        return;

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif
    record = NSMapGet(objc_proxies, original);
    if (record != NULL) {
        v = objc_loadWeakRetained(&record->value);
        if (v == proxy) {
            NSMapRemove(objc_proxies, original);
        }
        if (v != nil) {
            objc_release(v);
        }
     }
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&proxy_mutex);
#endif

}

PyObject* _Nullable PyObjC_FindPythonProxy(id original)
{
    PyObject* v;

    if (original == nil)           // LCOV_BR_EXCL_LINE
        PyObjCErr_InternalError(); // LCOV_EXCL_LINE

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif

    v = NSMapGet(python_proxies, original);
    Py_XINCREF(v);

#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&proxy_mutex);
#endif

    return v;
}

id _Nullable NS_RETURNS_RETAINED PyObjC_FindObjCProxy(PyObject* original)
{
    if (original == Py_None)       // LCOV_BR_EXCL_LINE
        PyObjCErr_InternalError(); // LCOV_EXCL_LINE

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&proxy_mutex);
#endif

    struct weak_value* record  = NSMapGet(objc_proxies, original);
    if (record == NULL) {
        return nil;
    }

    id result =  objc_loadWeakRetained(&record->value);
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&proxy_mutex);
#endif

    return result;
}

NS_ASSUME_NONNULL_END
