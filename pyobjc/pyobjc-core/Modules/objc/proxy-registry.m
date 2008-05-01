#include "pyobjc.h"

static NSMapTable* python_proxies = NULL;
static NSMapTable* objc_proxies = NULL;

int PyObjC_InitProxyRegistry(void)
{
	python_proxies = NSCreateMapTable(
			PyObjCUtil_PointerKeyCallBacks,
			PyObjCUtil_PointerValueCallBacks,
			0);
	if (python_proxies == NULL) {
		PyErr_SetString(PyExc_RuntimeError,
			"Cannot create NSMapTable for python_proxies");
		return -1;
	}

	objc_proxies = NSCreateMapTable(
			PyObjCUtil_PointerKeyCallBacks,
			PyObjCUtil_PointerValueCallBacks,
			0);
	if (objc_proxies == NULL) {
		PyErr_SetString(PyExc_RuntimeError,
			"Cannot create NSMapTable for objc_proxies");
		return -1;
	}
	return 0;
}

int PyObjC_RegisterPythonProxy(id original, PyObject* proxy)
{
	NSMapInsert(python_proxies, original, proxy);
	return 0;
}

int PyObjC_RegisterObjCProxy(PyObject* original, id proxy)
{
	NSMapInsert(objc_proxies, original, proxy);
	return 0;
}

void PyObjC_UnregisterPythonProxy(id original, PyObject* proxy)
{
	PyObject* v;

	if (original == nil) return;

	v = NSMapGet(python_proxies, original);
	if (v == proxy) {
		NSMapRemove(python_proxies, original);
	}
}

void PyObjC_UnregisterObjCProxy(PyObject* original, id proxy)
{
	id v;

	if (original == NULL) return;

	v = NSMapGet(objc_proxies, original);
	if (v == proxy) {
		NSMapRemove(objc_proxies, original);
	}
}

PyObject* PyObjC_FindPythonProxy(id original)
{
	PyObject* v;
	
	if (original == nil) {
		v = Py_None;
	} else {
		v = NSMapGet(python_proxies, original);
	}
	Py_XINCREF(v);
	return v;
}

id PyObjC_FindObjCProxy(PyObject* original)
{
    if (original == Py_None) {
        return nil;
    } else {
        return NSMapGet(objc_proxies, original);
    }
}
