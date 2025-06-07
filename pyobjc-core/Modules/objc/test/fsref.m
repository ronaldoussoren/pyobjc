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

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_TestFSRefHelper",
                           PyObjC_IdToPython([OC_TestFSRefHelper class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {
        .slot = Py_mod_exec,
        .value = (void*)mod_exec_module
    },
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        .slot = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "fsref",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_fsref(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_fsref(void)
{
    return PyModuleDef_Init(&mod_module);
}
