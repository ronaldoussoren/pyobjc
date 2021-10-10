/*
 * This module is used for tests dealing with FSRef "objects"
 */
#include "Python.h"
#include "pyobjc-api.h"

#pragma GCC diagnostic   ignored "-Wdeprecated-declarations"
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

#import <CoreServices/CoreServices.h>

#import <Foundation/Foundation.h>

@interface OC_TestFSRefHelper : NSObject {
}

- (FSRef)fsrefForPath:(NSString*)path;
- (NSString*)pathForFSRef:(in FSRef*)fsref;
- (void)getFSRef:(out FSRef*)fsref forPath:(NSString*)path;
- (NSString*)stringForFSRef:(FSRef)fsref;

@end

@implementation OC_TestFSRefHelper

- (NSString*)stringForFSRef:(FSRef)fsref
{
    return [self pathForFSRef:&fsref];
}

- (FSRef)fsrefForPath:(NSString*)path
{
    FSRef    fsref;
    Boolean  isDirectory;
    OSStatus rc;

    rc = FSPathMakeRef((UInt8*)[path UTF8String], &fsref, &isDirectory);
    if (rc != 0) {
        [NSException raise:@"failure" format:@"status: %ld", (long)rc];
    }

    return fsref;
}

- (NSString*)pathForFSRef:(in FSRef*)fsref
{
    UInt8    buffer[256];
    OSStatus rc;

    rc = FSRefMakePath(fsref, buffer, sizeof(buffer));
    if (rc != 0) {
        [NSException raise:@"failure" format:@"status: %ld", (long)rc];
    }

    return [NSString stringWithUTF8String:(char*)buffer];
}

- (void)getFSRef:(out FSRef*)fsref forPath:(NSString*)path
{
    Boolean  isDirectory;
    OSStatus rc;

    rc = FSPathMakeRef((UInt8*)[path UTF8String], fsref, &isDirectory);
    if (rc != 0) {
        [NSException raise:@"failure" format:@"status: %ld", (long)rc];
    }
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "fsref", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_fsref(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_fsref(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_TestFSRefHelper",
                           PyObjC_IdToPython([OC_TestFSRefHelper class]))
        < 0) {
        return NULL;
    }

    return m;
}
