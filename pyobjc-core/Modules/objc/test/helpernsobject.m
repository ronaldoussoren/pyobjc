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

@interface OC_RefcountRaises : NSObject {
    int scenario;
}
@end

@implementation OC_RefcountRaises
- (instancetype)init
{
    self = [super init];
    if (!self)
        return self;
    scenario = 0;
    return self;
}
- (void)setScenario:(int)value
{
    scenario = value;
}

- (instancetype)retain
{
    if (scenario == 1) {
        scenario = 0;
        @throw [NSException exceptionWithName:@"SomeException"
                                       reason:@"Some Reason"
                                     userInfo:nil];
    }
    return [super retain];
}

- (oneway void)release
{
    if (scenario == 2) {
        scenario = 0;
        @throw [NSException exceptionWithName:@"SomeException"
                                       reason:@"Some Reason"
                                     userInfo:nil];
    }
    [super release];
}

- (void)dealloc
{
    if (scenario == 3) {
        scenario = 0;
        @throw [NSException exceptionWithName:@"SomeException"
                                       reason:@"Some Reason"
                                     userInfo:nil];
    }
    if (self == nil)
        [super dealloc];
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
    if (PyModule_AddObject(m, "OC_RefcountRaises",
                           PyObjC_IdToPython([OC_RefcountRaises class]))
        < 0) {
        return NULL;
    }

    return m;
}

NS_ASSUME_NONNULL_END
