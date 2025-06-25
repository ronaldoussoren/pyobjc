/*
 * This module is used in the unittests for the sequence API
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_TestSequence : NSObject {
    NSObject*  objects[128];
    NSUInteger len;
}
- (id)initWithArray:(NSArray*)array;
- (NSUInteger)count;
- (id)objectAtIndex:(NSUInteger)idx;

@end

@implementation OC_TestSequence

- (id)initWithArray:(NSArray*)array
{
    NSUInteger i;

    self = [super init];
    if (!self)
        return nil;

    len = [array count];
    if (len > 128) {
        len = 128;
    }
    for (i = 0; i < len; i++) {
        objects[i] = [[array objectAtIndex:i] retain];
    }
    return self;
}

- (void)dealloc
{
    NSUInteger i;
    for (i = 0; i < len; i++) {
        [objects[i] release];
    }
    [super dealloc];
}

- (NSUInteger)count
{
    return len;
}

- (id)objectAtIndex:(NSUInteger)idx
{
    if (idx >= len) {
        [NSException raise:NSRangeException
                    format:@"Index %ld is out of range", (long)idx];
    }
    return [[objects[idx] retain] autorelease];
}

@end

@interface OC_TestMutableSequence : OC_TestSequence {
}
- (void)setObject:(id)value atIndex:(NSUInteger)idx;
@end

@implementation OC_TestMutableSequence
- (void)setObject:(id)value atIndex:(NSUInteger)idx
{
    if (idx >= len) {
        [NSException raise:NSRangeException
                    format:@"Index %ld is out of range", (long)idx];
    }
    [value retain];
    [objects[idx] release];
    objects[idx] = value;
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
                           "OC_TestSequence", PyObjC_IdToPython([OC_TestSequence class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_TestMutableSequence",
                           PyObjC_IdToPython([OC_TestMutableSequence class]))
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
    .m_name     = "sequence",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_sequence(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_sequence(void)
{
    return PyModuleDef_Init(&mod_module);
}
