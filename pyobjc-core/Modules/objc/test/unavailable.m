#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_NSUnavailable : NSObject {
}
@end

@interface OC_NSUnavailableChild : OC_NSUnavailable {
}
@end

@implementation OC_NSUnavailable
- (id)instmeth1
{
    return @"objc-inst";
}

+ (id)clsmeth1
{
    return @"objc-cls";
}


+(id)invokeInst:(OC_NSUnavailable*)inst
{
   return [inst instmeth1];
}

+(id)invokeCls
{
   return [self clsmeth1];
}

@end

@implementation OC_NSUnavailableChild
- (id)instmeth1
{
    return @"objc-inst child";
}

+ (id)clsmeth1
{
    return @"objc-cls child";
}
@end


static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "unavailable", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_unavailable(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_unavailable(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_NSUnavailable", PyObjC_IdToPython([OC_NSUnavailable class]))
        < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_NSUnavailableChild", PyObjC_IdToPython([OC_NSUnavailableChild class]))
        < 0) {
        return NULL;
    }

    return m;
}
