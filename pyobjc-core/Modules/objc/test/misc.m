/*
 * Helper classes for test_clinmeth
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_Misc : NSObject {
}
+ (NSComparisonResult)compare:(NSNumber*)x and:(NSNumber*)y;
@end

@implementation OC_Misc
+ (NSComparisonResult)compare:(NSNumber*)x and:(NSNumber*)y
{
    return [x compare:y];
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "misc", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_misc(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_misc(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_Misc", PyObjC_IdToPython([OC_Misc class])) < 0) {
        return NULL;
    }

    return m;
}
