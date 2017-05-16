#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OCTestDeprecations : NSObject {}
-(int)method1;
-(int)method2;
-(int)method3;
-(int)method4;
-(int)method5;
-(int)method6;
-(int)method7;
-(int)method8;
-(int)method9;
@end

@implementation OCTestDeprecations

-(int)method1 { return 1; }
-(int)method2 { return 2; }
-(int)method3 { return 3; }
-(int)method4 { return 4; }
-(int)method5 { return 5; }
-(int)method6 { return 6; }
-(int)method7 { return 7; }
-(int)method8 { return 8; }
-(int)method9 { return 9; }

@end


static int func1(void) { return 1; }
static int func2(void) { return 2; }
static int func3(void) { return 3; }
static int func4(void) { return 4; }
static int func5(void) { return 5; }
static int func6(void) { return 6; }
static int func7(void) { return 7; }
static int func8(void) { return 8; }
static int func9(void) { return 9; }

typedef void (*F)(void);
static struct function {
    char* name;
    F function;
} gFunctionMap[] = {
    { "func1", (F)func1 },
    { "func2", (F)func2 },
    { "func3", (F)func3 },
    { "func4", (F)func4 },
    { "func5", (F)func5 },
    { "func6", (F)func6 },
    { "func7", (F)func7 },
    { "func8", (F)func8 },
    { "func9", (F)func9 },
    { NULL, NULL }
};


static PyMethodDef mod_methods[] = {
            { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT,
    "deprecations",
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

PyObject* PyInit_deprecations(void);

PyObject* __attribute__((__visibility__("default")))
PyInit_deprecations(void)

#else

#define INITERROR() return
#define INITDONE() return

void initdeprecations(void);

void __attribute__((__visibility__("default")))
initdeprecations(void)
#endif
{
    PyObject* m;
    PyObject* v;

#if PY_VERSION_HEX >= 0x03000000
    m = PyModule_Create(&mod_module);
#else
    m = Py_InitModule4("deprecations", mod_methods,
        NULL, NULL, PYTHON_API_VERSION);
#endif
    if (!m) {
        INITERROR();
    }

    if (PyObjC_ImportAPI(m) < 0) {
        INITERROR();
    }

    if (PyModule_AddObject(m, "OCTestDeprecations",
        PyObjC_IdToPython([OCTestDeprecations class])) < 0) {
        INITERROR();
    }

#if PY_VERSION_MAJOR == 2 && PY_VERSION_MINOR < 7
    v = PyCObject_FromVoidPtr(gFunctionMap, NULL);
#else
    v = PyCapsule_New(gFunctionMap, "objc.__inline__", NULL);
#endif
    if (v == NULL) {
        INITERROR();
    }
    if (PyModule_AddObject(m, "function_list", v) < 0) {
        INITERROR();
    }
    INITDONE();
}
