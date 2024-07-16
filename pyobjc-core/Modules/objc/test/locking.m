/*
 * Helper methods opaque-pointer tests (objc.test.test_opaque)
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

typedef struct _Foo* FooHandle;
typedef struct _Bar* BarHandle;

@interface
NSObject (OC_LockingTest)
- (void)setLocked:(NSObject*)value;
- (NSObject*)isLocked;
- (void)appendToList:(NSObject*)value;
@end

@interface OC_LockTest : NSObject
- (void)threadFunc:(NSObject*)object;
@end

@implementation OC_LockTest
- (void)threadFunc:(NSObject*)object
{
    int i;
    for (i = 0; i < 6; i++) {
        usleep(500000);
        @synchronized(object) {
            NSNumber* isLocked = (NSNumber*)[object isLocked];
            if ([isLocked boolValue]) {
                [object appendToList:@"LOCK FOUND"];
            }
            [object setLocked:[NSNumber numberWithBool:YES]];
            [object appendToList:@"threading a"];
            usleep(5000000);
            [object appendToList:@"threading b"];
            [object setLocked:[NSNumber numberWithBool:NO]];
        }
    }
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "OC_LockTest", PyObjC_IdToPython([OC_LockTest class]))
        < 0) {
        return -1;
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
    .m_name = "locking",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_locking(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_locking(void)
{
    return PyModuleDef_Init(&mod_module);
}
