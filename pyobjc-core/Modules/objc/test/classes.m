#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OCTestClasses : NSObject {}
+(Class)classForObject:(id)object;
@end

@implementation OCTestClasses

+(Class)classForObject:(id)object
{
    return object_getClass(object);
}

@end


static PyMethodDef mod_methods[] = {
            { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT,
    "classes",
    NULL,
    0,
    mod_methods,
    NULL,
    NULL,
    NULL,
    NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit_classes(void);

PyObject* __attribute__((__visibility__("default")))
PyInit_classes(void)

#else

#define INITERROR() return
#define INITDONE() return

void initclasses(void);

void __attribute__((__visibility__("default")))
initclasses(void)
#endif
{
    PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
    m = PyModule_Create(&mod_module);
#else
    m = Py_InitModule4("classes", mod_methods,
        NULL, NULL, PYTHON_API_VERSION);
#endif
    if (!m) {
        INITERROR();
    }

    if (PyObjC_ImportAPI(m) < 0) {
        INITERROR();
    }

    if (PyModule_AddObject(m, "OCTestClasses",
        PyObjC_IdToPython([OCTestClasses class])) < 0) {
        INITERROR();
    }

    INITDONE();
}
