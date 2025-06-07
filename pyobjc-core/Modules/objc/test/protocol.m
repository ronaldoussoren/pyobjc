#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@protocol OC_NSObjectBased <NSObject>
@optional
- (int)optionalmethod;
@end

@protocol OC_TestProtocol
- (int)method1;
- (void)method2:(int)v;
@end

@protocol OC_TestProtocol2
- (id)description;
- (void)method;
+ (id)alloc;
+ (id)classMethod;
@end

@protocol OC_TestProtocolT1
+ (int)classMethod1;
@end

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wprotocol"
#pragma clang diagnostic ignored "-Wincomplete-implementation"
@interface OC_TestProtocolClass : NSObject <OC_TestProtocol, OC_TestProtocol2> {
}
@end

@implementation OC_TestProtocolClass
@end
#pragma clang diagnostic pop

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    Protocol* p              = @protocol(OC_TestProtocol);
    PyObject* prot = PyObjC_ObjCToPython("@", &p);
    if (!prot) {
        return -1;
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_TestProtocol", prot) < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    p    = @protocol(OC_NSObjectBased);
    prot = PyObjC_ObjCToPython("@", &p);
    if (!prot) {
        return -1;
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_NSObjectBased", prot) < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    p    = @protocol(OC_TestProtocolT1);
    prot = PyObjC_ObjCToPython("@", &p);
    if (!prot) {
        return -1;
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_TestProtocolT1", prot) < 0) {
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
    .m_name = "protocol",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_protocol(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_protocol(void)
{
    return PyModuleDef_Init(&mod_module);
}
