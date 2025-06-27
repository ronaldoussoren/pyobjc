#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OCTestNULL : NSObject {
}
- (int)callList:(NSMutableArray*)list andInOut:(int*)pval;
- (int)callList:(NSMutableArray*)list andInOut2:(int*)pval;
- (int)callList:(NSMutableArray*)list andIn:(int*)pval;
- (int)callList:(NSMutableArray*)list andOut:(int*)pval;
- (void)callOut:(int*)pval;
@end

@implementation OCTestNULL

- (int)callList:(NSMutableArray*)list andInOut:(int*)pval
{
    if (pval == NULL) {
        [list addObject:@"NULL"];
    } else {
        [list addObject:[NSString stringWithFormat:@"%d", *pval]];
        *pval = *pval / 2;
    }
    return 12;
}

/* This is the same implementation as callList:andInOut:, the python code
 * uses a different type string for this one.
 */
- (int)callList:(NSMutableArray*)list andInOut2:(int*)pval
{
    if (pval == NULL) {
        [list addObject:@"NULL"];
    } else {
        [list addObject:[NSString stringWithFormat:@"%d", *pval]];
        *pval = *pval / 2;
    }
    return 12;
}

- (int)callList:(NSMutableArray*)list andIn:(int*)pval
{
    if (pval == NULL) {
        [list addObject:@"NULL"];
    } else {
        [list addObject:[NSString stringWithFormat:@"%d", *pval]];
    }
    return 24;
}

- (int)callList:(NSMutableArray*)list andOut:(int*)pval
{
    if (pval == NULL) {
        [list addObject:@"NULL"];
    } else {
        [list addObject:@"POINTER"];
        *pval = 99;
    }

    return 24;
}

- (int)on:(OCTestNULL*)object callList:(NSMutableArray*)list andInOut:(int*)pval
{
    return [object callList:list andInOut:pval];
}

- (int)on:(OCTestNULL*)object callList:(NSMutableArray*)list andIn:(int*)pval
{
    return [object callList:list andIn:pval];
}

- (int)on:(OCTestNULL*)object callList:(NSMutableArray*)list andOut:(int*)pval
{
    return [object callList:list andOut:pval];
}

- (void)callOut:(int*)pval
{
    *pval = 144;
}

- (void)on:(OCTestNULL*)object callOut:(int*)pval
{
    [object callOut:pval];
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
                           "OCTestNULL", PyObjC_IdToPython([OCTestNULL class]))
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
    .m_name     = "NULL",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_NULL(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_NULL(void)
{
    return PyModuleDef_Init(&mod_module);
}
