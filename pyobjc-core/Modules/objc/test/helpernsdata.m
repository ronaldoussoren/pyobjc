#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface OC_MutableDataHelper : NSMutableData {
    int scenario;
}
@end

@implementation OC_MutableDataHelper
+ (NSData* _Nullable)fetchBytesOf:(NSMutableData*)input
{
    const void* bytes = [input bytes];
    if (bytes == NULL) {
        return NULL;
    }
    return [NSData dataWithBytes:bytes length:[input length]];
}

+ (NSData* _Nullable)fetchMutableBytesOf:(NSMutableData*)input
{
    void* bytes = [input mutableBytes];
    if (bytes == NULL) {
        return NULL;
    }
    return [NSData dataWithBytes:bytes length:[input length]];
}

- (instancetype)initWithScenario:(int)value
{
    self = [super init];
    if (!self) {
        return nil;
    }
    scenario = value;
    return self;
}
- (NSString*)description
{
    return [NSString stringWithFormat:@"<OC_MutableDataHelper scenario=%d>", scenario];
}

- (NSUInteger)length
{
    return 0;
}

- (const void*)bytes
{
    switch (scenario) {
    case 0:
        return (void* _Nonnull)NULL;
    case 1:
        @throw [NSException exceptionWithName:@"SomeException"
                                       reason:@"Some Reason"
                                     userInfo:nil];
    default:
        abort();
    }
}

- (void*)mutableBytes
{
    switch (scenario) {
    case 0:
        return (void* _Nonnull)NULL;
    case 1:
        @throw [NSException exceptionWithName:@"SomeException"
                                       reason:@"Some Reason"
                                     userInfo:nil];
    default:
        abort();
    }
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "helpernsdata", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* _Nullable PyInit_helpernsdata(void);

PyObject* _Nullable __attribute__((__visibility__("default"))) PyInit_helpernsdata(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_MutableDataHelper",
                           PyObjC_IdToPython([OC_MutableDataHelper class]))
        < 0) {
        return NULL;
    }

    return m;
}

NS_ASSUME_NONNULL_END
