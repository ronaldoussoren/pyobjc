/*
 * NOTE: PyObjC_TestClassAndInstance is a class that can't be created
 *      from Python but ends up in some fun places like NSWindow
 */

#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

#ifndef GNU_RUNTIME
#include <objc/objc-runtime.h>
#endif

@interface PyObjC_TestUnallocatable : NSObject {
}
@end

@implementation PyObjC_TestUnallocatable
+ (id)allocWithZone:(NSZone*)zone
{
    (void)&zone; /* Force use */
    return nil;
}
@end

@interface PyObjC_TestClassAndInstance : NSObject {
}

+ (BOOL)isInstance;
- (BOOL)isInstance;
@end

@implementation PyObjC_TestClassAndInstance
+ (BOOL)isInstance
{
    return NO;
}
- (BOOL)isInstance
{
    return YES;
}
@end

/* Python glue */
static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "testclassandinst",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit_testclassandinst(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_testclassandinst(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "PyObjC_TestClassAndInstance",
                           PyObjC_IdToPython([PyObjC_TestClassAndInstance class]))
        < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "PyObjC_TestUnallocatable",
                           PyObjC_IdToPython([PyObjC_TestUnallocatable class]))
        < 0) {
        return NULL;
    }

    return m;
}
