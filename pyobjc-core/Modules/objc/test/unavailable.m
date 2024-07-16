#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_NSUnavailable : NSObject {
}
@end

@interface OC_NSUnavailableChild : OC_NSUnavailable {
}
@end

@implementation OC_NSUnavailable
- (id)instmeth1
{
    return @"objc-inst";
}

+ (id)clsmeth1
{
    return @"objc-cls";
}


+(id)invokeInst:(OC_NSUnavailable*)inst
{
   return [inst instmeth1];
}

+(id)invokeCls
{
   return [self clsmeth1];
}

@end

@implementation OC_NSUnavailableChild
- (id)instmeth1
{
    return @"objc-inst child";
}

+ (id)clsmeth1
{
    return @"objc-cls child";
}
@end


static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "OC_NSUnavailable", PyObjC_IdToPython([OC_NSUnavailable class]))
        < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "OC_NSUnavailableChild", PyObjC_IdToPython([OC_NSUnavailableChild class]))
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
    .m_name = "unavailable",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_unavailable(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_unavailable(void)
{
    return PyModuleDef_Init(&mod_module);
}
