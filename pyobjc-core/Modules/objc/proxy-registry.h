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
 * Locking in a free threaded build
 *
 * The GIL protects against a couple of races that can
 * cause problems in maintaining these registries. For the
 * free threaded build a mutex is used to protect against
 * these races.
 *
 * XXX: Need to rephrase this comment, the race is also present
 *      in regular builds due to invoking Python code while
 *      creating proxies. Also keeping the code patterns the same
 *      should result in cleaner code overall.
 *
 * Otherwise the GIL and no-GIL builds use the same code patterns to
 * protect against races due to giving up the GIL when calling back
 * into the interpreter (for the no-GIL build).
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
 *     TODO: Switch to a weak value mapping that removes the race in
 *     both build types, with at worse a need to lock the mapping itself
 *     while using it.
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

NS_ASSUME_NONNULL_END

#endif /* PyObjC_PROXY_REGISTRY_H */
