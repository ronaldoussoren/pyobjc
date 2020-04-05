/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#include <CoreFoundation/CoreFoundation.h>

@interface OC_TestCFSocket : NSObject
- (id)newSocket;
@end

@implementation OC_TestCFSocket
- (id)newSocket
{
    CFSocketRef sock;

    sock = CFSocketCreate(NULL, 0, 0, 0, 0, 0, 0);
    return (id)sock;
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "cfsocket", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_cfsocket(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_cfsocket(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_TestCFSocket",
                           PyObjC_IdToPython([OC_TestCFSocket class]))
        < 0) {
        return NULL;
    }

    return m;
}
