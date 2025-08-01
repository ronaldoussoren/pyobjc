#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_Authorization : NSObject {
}
@end

@implementation OC_Authorization

+ (NSDictionary*)dictWithAuthorizationItem:(AuthorizationItem*)item
{
    NSObject* name_value =
        item->name != NULL ? [NSString stringWithUTF8String:item->name] : nil;
    if (item->value) {
        return @{
            @"flags" : @(item->flags),
            @"value" : [NSData dataWithBytes:item->value length:item->valueLength],
            @"name" : name_value ? name_value : [NSNull null],
        };
    } else {
        return @{
            @"flags" : @(item->flags),
            @"value" : [NSNull null],
            @"valueLength" : @(item->valueLength),
            @"name" : name_value ? name_value : [NSNull null],
        };
    }
}

+ (void)getAuthorizationItem:(AuthorizationItem*)item kind:(int)kind
{
    switch (kind) {
    case 0:
        /* The _Nonnull cast is required because the name
         * cannot be NULL according to Apple's headers. For
         * testing we want to set it to a NULL value anyway.
         */
        item->name        = (char* _Nonnull)NULL;
        item->value       = NULL;
        item->valueLength = 32;
        item->flags       = 0;
        break;
    case 1:
        item->name        = "name-value";
        item->value       = "value buffer";
        item->valueLength = 12;
        item->flags       = 14356;
        break;
    }
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject( // LCOV_BR_EXCL_LINE
            m, "OC_Authorization", PyObjC_IdToPython([OC_Authorization class]))
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
    .m_name     = "authorizationitem",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_authorizationitem(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_authorizationitem(
    void)
{
    return PyModuleDef_Init(&mod_module);
}
