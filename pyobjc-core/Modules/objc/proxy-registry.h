/*!
 * @header   proxy-registry.h
 * @abstract Maintain a registry of proxied objects
 * @discussion
 * 	Object-identity is important in several Cocoa API's. For that
 * 	reason we need to make sure that at most one proxy object is 
 * 	alive for every Python or Objective-C object.
 */
#ifndef PyObjC_PROXY_REGISTRY_H
#define PyObjC_PROXY_REGISTRY_H

int PyObjC_InitProxyRegistry(void);

int PyObjC_RegisterPythonProxy(id original, PyObject* proxy);
int PyObjC_RegisterObjCProxy(PyObject* original, id proxy);

void PyObjC_UnregisterPythonProxy(id original, PyObject* proxy);
void PyObjC_UnregisterObjCProxy(PyObject* original, id proxy);

id PyObjC_FindObjCProxy(PyObject* original);
PyObject* PyObjC_FindPythonProxy(id original);

#endif /* PyObjC_PROXY_REGISTRY_H */
