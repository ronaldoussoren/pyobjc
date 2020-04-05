/*
 * Helper classes for test_clinmeth
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface PyObjC_ClsInst1 : NSObject {
}
- (int)instance;
- (int)both;
+ (int)both;
+ (int)clsmeth;
@end

@implementation PyObjC_ClsInst1

- (int)instance
{
    return 1;
}

- (int)both
{
    return 2;
}

+ (int)both
{
    return 3;
}

+ (int)clsmeth
{
    return 4;
}
@end

@interface PyObjC_ClsInst2 : PyObjC_ClsInst1 {
}
- (int)instance;
- (int)both;
+ (int)both;
+ (int)clsmeth;
@end

@implementation PyObjC_ClsInst2

- (int)instance
{
    return 10;
}

- (int)both
{
    return 20;
}

+ (int)both
{
    return 30;
}

+ (int)clsmeth
{
    return 40;
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "clinmeth", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_clinmeth(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_clinmeth(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "PyObjC_ClsInst1",
                           PyObjC_IdToPython([PyObjC_ClsInst1 class]))
        < 0) {
        return NULL;
    }
    if (PyModule_AddObject(m, "PyObjC_ClsInst2",
                           PyObjC_IdToPython([PyObjC_ClsInst2 class]))
        < 0) {
        return NULL;
    }

    return m;
}
