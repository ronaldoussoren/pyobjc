/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_TestFilePointer : NSObject {
}

- (FILE*)openFile:(char*)path withMode:(char*)mode;
- (FILE*)openNoFile;
- (NSString*)readline:(FILE*)fp;
@end

@implementation OC_TestFilePointer
+ (FILE* _Nullable)openFile:(char*)path withMode:(char*)mode on:(OC_TestFilePointer*)o
{
    return [o openFile:path withMode:mode];
}

- (FILE* _Nullable)openFile:(char*)path withMode:(char*)mode
{
    return fopen(path, mode);
}

+ (FILE* _Nullable)openNoFileOn:(OC_TestFilePointer*)o
{
    return [o openNoFile];
}

- (FILE* _Nullable)openNoFile
{
    return NULL;
}

- (FILE* _Nullable)openFileMode:(out char**)mode
{
    *mode = "w";
    return [self openFile:"/etc/resolve.conf" withMode:*mode];
}

+ (FILE* _Nullable)openFileMode:(out char**)mode on:(OC_TestFilePointer*)o
{
    return [o openFileMode:mode];
}

- (NSString*)readline:(FILE*)fp
{
    char buf[1024];

    if (!fp) {
        return nil;
    }

    return [NSString stringWithCString:fgets(buf, sizeof(buf), fp)
                              encoding:NSASCIIStringEncoding];
}

- (NSString*)readline2:(FILE*)fp
{
    return [self readline:fp];
}

- (NSString*)readline3:(FILE*)fp
{
    return [self readline:fp];
}

- (NSString*)readline4:(FILE*)fp
{
    return [self readline:fp];
}

- (void)printTo:(FILE*)fp format:(char*)fmt, ...
{
    va_list ap;

    va_start(ap, fmt);
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wformat-nonliteral"
    vfprintf(fp, fmt, ap);
#pragma clang diagnostic pop
    va_end(ap);
}

- (void)printTo2:(FILE*)fp format:(char*)fmt, ...
{
    va_list ap;

    va_start(ap, fmt);
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wformat-nonliteral"
    vfprintf(fp, fmt, ap);
#pragma clang diagnostic pop
    va_end(ap);
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_TestFilePointer",
                           PyObjC_IdToPython([OC_TestFilePointer class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot  = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "filepointer",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_filepointer(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_filepointer(void)
{
    return PyModuleDef_Init(&mod_module);
}
