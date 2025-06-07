
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_ArrayInt : NSObject {
}
@end

@implementation OC_ArrayInt

+ (id)getNthElement:(NSArray*)array offset:(NSUInteger)offset
{
    @try {
        return [array objectAtIndex:offset];
    } @catch (NSException* exc) {
        return exc;
    }
}

+ (id)getSub:(NSArray*)array range:(NSRange)range
{
    static id buf[100];

    if (range.length > 100) { // LCOV_BR_EXCL_LINE
        return @"too many items"; // LCOV_EXCL_LINE
    }

    [array getObjects:buf range:range];
    return [NSArray arrayWithObjects:buf count:range.length];
}

+ (id)setNthElement:(NSMutableArray*)array offset:(NSUInteger)offset replacement:(id)value
{
    @try {
        [array replaceObjectAtIndex:offset withObject:value];
        return nil;
    } @catch (NSException* exc) {
        return exc;
    }
}

+ (id _Nullable)setNthElement:(NSMutableArray*)array offset:(NSUInteger)offset from:(Class)value
{
    @try {
        id ref = [[value alloc] init];
        [array replaceObjectAtIndex:offset withObject:ref];
        [ref release];
        return nil;
    } @catch (NSException* exc) {
        return exc;
    }
}

+ (id _Nullable)addToArray:(NSMutableArray*)array from:(Class)value
{
    @try {
        id ref = [[value alloc] init];
        [array addObject:ref];
        [ref release];
        return nil;
    } @catch (NSException* exc) {
        return exc;
    }
}

+ (id _Nullable)addToArray:(NSMutableArray*)array value:(id)value
{
    @try {
        [array addObject:value];
        return nil;
    } @catch (NSException* exc) {
        return exc;
    }
}

+ (id _Nullable)insertIntoArray:(NSMutableArray*)array offset:(NSUInteger)offset from:(Class)value
{
    @try {
        id ref = [[value alloc] init];
        [array insertObject:ref atIndex:offset];
        [ref release];
        return nil;
    } @catch (NSException* exc) {
        return exc;
    }
}

+ (id)insertIntoArray:(NSMutableArray*)array offset:(NSUInteger)offset value:(id)value
{
    @try {
        [array insertObject:value atIndex:offset];
        return nil;
    } @catch (NSException* exc) {
        return exc;
    }
}

+ (id)removeLast:(NSMutableArray*)array
{
    @try {
        [array removeLastObject];
        return nil;
    } @catch (NSException* exc) {
        return exc;
    }
}
+ (id)remove:(NSMutableArray*)array offset:(NSUInteger)offset
{
    @try {
        [array removeObjectAtIndex:offset];
        return nil;
    } @catch (NSException* exc) {
        return exc;
    }
}

+ (id)countOf:(NSArray*)array
{
    @try {
        NSUInteger result = [array count];
        return [NSNumber numberWithUnsignedLongLong:result];
    } @catch (NSException* exc) {
        return exc;
    }
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject( // LCOV_BR_EXCL_LINE
                m, "OC_ArrayInt", PyObjC_IdToPython([OC_ArrayInt class]))
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
    .m_name = "arrayint",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_arrayint(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_arrayint(void)
{
    return PyModuleDef_Init(&mod_module);
}
