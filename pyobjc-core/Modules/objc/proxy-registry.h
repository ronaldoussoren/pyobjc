/*!
 * @header   proxy-registry.h
 * @abstract Maintain a registry of proxied objects
 * @discussion
 *     Object-identity is important in several Cocoa API's. For that
 *     reason we need to make sure that at most one proxy object is
 *     alive for every Python or Objective-C object.
 */
#ifndef PyObjC_PROXY_REGISTRY_H
#define PyObjC_PROXY_REGISTRY_H

NS_ASSUME_NONNULL_BEGIN

/*
 * Locking patterns for the proxy registry
 *
 * The patterns are needed for both the regular and
 * free-threading build. PyObjC calls back into Python
 * at a number of places, which means that we cannot
 * fully rely on the GIL to maintain consistency without
 * following these patterns.
 *
 * * For the Objective-C to Python registry:
 *
 *   + The Python proxy is removed from the registry in ``tp_dealloc``,
 *     this can race against a different thread fetching from
 *     the registry.
 *
 *     Code pattern:
 *     - Lock the registry when fetching an item from the registry
 *     - Lock the registry in tp_dealloc before unregistering,
 *       and don't actually dealloc when object is revived once
 *       the lock is taken.
 *
 *   + There is a race between creating a new proxy object and
 *     registering it.
 *
 *     Code pattern:
 *     - Create a new proxy object
 *     - Lock registry
 *     - Try to fetch from registry, if ok: use that value
 *     - Insert new value in to registry
 *
 * * For the Python to Objective-C registry:
 *
 *   + The ObjC proxy is removed from the registry in ``-dealloc``,
 *     this can race against a different thread fetching from the
 *     registry.
 *
 *     A snag here is that reviving Objective-C values is not
 *     allowed. Because of this the race is also present while using
 *     the GIL and the GIL is taken in ``-release``.
 *
 *   + As with the other registry there is a race between creating a
 *     new proxy object and registering it.
 *
 *     After creating a new proxy:
 *     - Lock registry
 *     - Fetch from registry again, if success: use that value
 *     - Insert into registry
 */

extern int PyObjC_InitProxyRegistry(PyObject*);

extern PyObject* PyObjC_RegisterPythonProxy(id original, PyObject* proxy)
    __attribute__((warn_unused_result));
extern id NS_RETURNS_RETAINED _Nullable PyObjC_RegisterObjCProxy(PyObject* original,
                                                                 id        proxy)
    __attribute__((warn_unused_result));

extern void PyObjC_UnregisterPythonProxy(id original, PyObject* proxy);
extern void PyObjC_UnregisterObjCProxy(PyObject* original, id proxy);

extern id _Nullable NS_RETURNS_RETAINED PyObjC_FindObjCProxy(PyObject* original)
    __attribute__((warn_unused_result));
extern PyObject* _Nullable PyObjC_FindPythonProxy(id original)
    __attribute__((warn_unused_result));

extern void PyObjC_MaybeKeepAlivePythonProxy(PyObject* proxy);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_PROXY_REGISTRY_H */
