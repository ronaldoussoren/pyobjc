#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OCTestClasses : NSObject {
}
+ (Class)classForObject:(id)object;
@end

@implementation OCTestClasses

+ (Class)classForObject:(id)object
{
    return object_getClass(object);
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "classes", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_classes(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_classes(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OCTestClasses", PyObjC_IdToPython([OCTestClasses class]))
        < 0) {
        return NULL;
    }

    return m;
}
