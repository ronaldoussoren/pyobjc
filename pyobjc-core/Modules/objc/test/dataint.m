#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_DataInt : NSObject {
}
@end

@implementation OC_DataInt
+ (NSData*)getBytes:(NSData*)data length:(NSUInteger)length
{
    const void* bytes = [data bytes];
    return [NSData dataWithBytes:bytes length:length];
}

+ (NSObject*)setBytes:(NSMutableData*)data new:(NSData*)newData length:(NSUInteger)length
{
    const void* bytes    = [newData bytes];
    void*       mutbytes = [data mutableBytes];
    memcpy(mutbytes, bytes, length);
    return nil;
}

+ (NSUInteger)lengthOf:(NSData*)data
{
    return [data length];
}

+ (Class)coderClassFor:(NSData*)data
{
    return [data classForCoder];
}

+ (Class)keyedArchiverClassFor:(NSData*)data
{
    return [data classForKeyedArchiver];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "OC_DataInt", PyObjC_IdToPython([OC_DataInt class])) < 0) {
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
    .m_name = "dataint",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_dataint(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_dataint(void)
{
    return PyModuleDef_Init(&mod_module);
}
