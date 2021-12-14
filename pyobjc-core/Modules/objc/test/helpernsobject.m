#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface OC_AllocRaises : NSObject {
}
@end

@implementation OC_AllocRaises
+ (instancetype)alloc
{
    @throw [NSException exceptionWithName:@"SomeException"
                                   reason:@"Some Reason"
                                 userInfo:nil];
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "helpernsobject",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* _Nullable PyInit_helpernsobject(void);

PyObject* _Nullable __attribute__((__visibility__("default"))) PyInit_helpernsobject(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_AllocRaises", PyObjC_IdToPython([OC_AllocRaises class]))
        < 0) {
        return NULL;
    }

    return m;
}

NS_ASSUME_NONNULL_END
