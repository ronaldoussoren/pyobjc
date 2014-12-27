#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface NSURL (MethodResolution2)
-(id)oc_method1;
-(id)ocmethod2;
@end

@implementation NSURL (MethodResolution2)

-(id)oc_method1
{
    return @"NSURL.oc_method1";
}

-(id)ocmethod2
{
    return @"NSURL.ocmethod2";
}

@end


static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT,
    "methres2",
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

PyObject* PyInit_methres2(void);

PyObject* __attribute__((__visibility__("default")))
PyInit_methres2(void)

#else

#define INITERROR() return
#define INITDONE() return

void initmethres2(void);

void __attribute__((__visibility__("default")))
initmethres2(void)
#endif
{
    PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
    m = PyModule_Create(&mod_module);
#else
    m = Py_InitModule4("methres2", mod_methods,
        NULL, NULL, PYTHON_API_VERSION);
#endif
    if (!m) {
        INITERROR();
    }

    INITDONE();
}
