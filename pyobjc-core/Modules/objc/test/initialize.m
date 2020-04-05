/*
 * This module is used in the unittests for object initialize.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

static int numUninitialized = 0;

@interface OC_TestInitialize : NSObject {
    int isInitialized;
}
- (instancetype)init;
- (instancetype)retain;
- (void)release;
- (instancetype)autorelease;
- (int)isInitialized;
+ (int)numUninitialized;
- (id)dummy;
+ (id)makeInstance;

/* completely unrelated ... */
- (oneway void)onewayVoidMethod;

@end

@implementation OC_TestInitialize

- (instancetype)init
{
    self = [super init];
    if (!self)
        return self;

    isInitialized = 1;
    return self;
}

- (instancetype)retain
{
    if (!isInitialized) {
        numUninitialized++;
    }
    return [super retain];
}

- (void)release
{
    if (!isInitialized) {
        numUninitialized++;
    }
    [super release];
}

- (instancetype)autorelease
{
    if (!isInitialized) {
        numUninitialized++;
    }
    return [super autorelease];
}

- (int)isInitialized
{
    return isInitialized;
}

+ (int)numUninitialized
{
    return numUninitialized;
}

- (id)dummy
{
    return @"hello";
}

+ (id)makeInstance
{
    return [[[self alloc] init] autorelease];
}

- (oneway void)onewayVoidMethod
{
    isInitialized = -1;
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "initialize", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_initialize(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_initialize(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }
    if (PyModule_AddObject(m, "OC_TestInitialize",
                           PyObjC_IdToPython([OC_TestInitialize class]))
        < 0) {
        return NULL;
    }

    return m;
}
