/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_TestIdentity : NSObject {
    NSObject* storedObject;
    int       isClassic;
}

- (NSObject*)storedObject;
- (void)setStoredClassicObject:(NSObject*)object;
- (void)setStoredObject:(NSObject*)object;
- (void)dealloc;

- (void)setStoredObjectToResultOf:(SEL)aSelector on:(NSObject*)object;
- (void)setStoredObjectToInteger:(int)value;
- (void)setStoredObjectToUnsignedInteger:(unsigned int)value;
- (void)setStoredObjectToLongLong:(long long)value;
- (void)setStoredObjectToUnsignedLongLong:(unsigned long long)value;
- (void)setStoredObjectToDouble:(double)value;
- (void)setStoredObjectToFloat:(float)value;

- (int)isSameObjectAsStored:(NSObject*)value;
- (void)setStoredObjectToAProtocol;
- (void)setStoredObjectAnInstanceOf:(Class)cls;
- (void)setStoredObjectAnInstanceOfClassic:(Class)cls;

- (void)writeStoredObjectToFile:(NSString*)fname;

@end

@implementation OC_TestIdentity
- (void)dealloc
{
    if (isClassic) {
        /* pass, we could call free but why bother? */
    } else {
        [storedObject release];
    }
    [super dealloc];
}

- (NSObject*)storedObject
{
    if (isClassic) {
        return storedObject;
    } else {
        return [[storedObject retain] autorelease];
    }
}

- (void)setStoredObject:(NSObject*)object
{
    if (!isClassic) {
        [storedObject release];
    }
    [object retain];
    storedObject = object;
    isClassic    = 0;
}

- (void)setStoredClassicObject:(NSObject*)object
{
    if (!isClassic) {
        [storedObject release];
    }
    storedObject = object;
    isClassic    = 1;
}

- (void)setStoredObjectToResultOf:(SEL)aSelector on:(NSObject*)object
{
    [self setStoredObject:[object performSelector:aSelector]];
}

- (void)setStoredObjectToInteger:(int)value
{
    [self setStoredObject:[NSNumber numberWithInt:value]];
}

- (void)setStoredObjectToUnsignedInteger:(unsigned int)value
{
    [self setStoredObject:[NSNumber numberWithUnsignedInt:value]];
}

- (void)setStoredObjectToLongLong:(long long)value
{
    [self setStoredObject:[NSNumber numberWithLongLong:value]];
}

- (void)setStoredObjectToUnsignedLongLong:(unsigned long long)value
{
    [self setStoredObject:[NSNumber numberWithUnsignedLongLong:value]];
}

- (void)setStoredObjectToDouble:(double)value
{
    [self setStoredObject:[NSNumber numberWithDouble:value]];
}

- (void)setStoredObjectToFloat:(float)value
{
    [self setStoredObject:[NSNumber numberWithFloat:value]];
}

- (int)isSameObjectAsStored:(NSObject*)value
{
    return value == storedObject;
}

- (void)setStoredObjectToAProtocol
{
    [self setStoredClassicObject:(NSObject*)@protocol(NSObject)];
}

- (void)setStoredObjectAnInstanceOf:(Class)cls
{
    [self setStoredObject:[[[cls alloc] init] autorelease]];
}
- (void)setStoredObjectAnInstanceOfClassic:(Class)cls
{
    [self setStoredClassicObject:[[cls alloc] init]];
}

- (void)writeStoredObjectToFile:(NSString*)fname
{
    [(NSArray*)storedObject writeToFile:fname atomically:YES];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_TestIdentity",
                           PyObjC_IdToPython([OC_TestIdentity class]))
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
    .m_name = "identity",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_identity(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_identity(void)
{
    return PyModuleDef_Init(&mod_module);
}
