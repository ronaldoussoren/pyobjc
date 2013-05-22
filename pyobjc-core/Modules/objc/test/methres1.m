#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface NSObject (MethodResolution1)
{
}
-(id)oc_method1;
-(id)ocmethod2;
@end

@implementation NSObject (MethodResolution1)

-(id)oc_method1
{
	return @"NSObject.oc_method1";
}

-(id)ocmethod2
{
	return @"NSObject.ocmethod2";
}

@end


static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT,
    "methres1",
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

PyObject* PyInit_methres1(void);

PyObject* __attribute__((__visibility__("default")))
PyInit_methres1(void)

#else

#define INITERROR() return
#define INITDONE() return

void initmethres1(void);

void __attribute__((__visibility__("default")))
initmethres1(void)
#endif
{
    PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
    m = PyModule_Create(&mod_module);
#else
    m = Py_InitModule4("methres1", mod_methods,
        NULL, NULL, PYTHON_API_VERSION);
#endif
    if (!m) {
        INITERROR();
    }

    INITDONE();
}
