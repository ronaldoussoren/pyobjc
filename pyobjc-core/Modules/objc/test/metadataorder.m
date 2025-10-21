#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@protocol OC_MetaDataProto
@optional
- (BOOL)metaProtoValue;
@end

@interface OC_MetadataOrder : NSObject {
}
@end

@interface OC_MetadataOrderChild1 : OC_MetadataOrder {
}
@end

@interface OC_MetadataOrderChild2 : OC_MetadataOrder {
}
@end

@interface OC_MetadataOrderGrandchild : OC_MetadataOrderChild1 {
}
@end

@implementation OC_MetadataOrder
- (char)metadataorder1
{
    return 1;
}
- (char)metadataorder2
{
    return 2;
}
- (char)metadataorder3
{
    return 3;
}
- (char)metadataorder4
{
    return 4;
}
- (char)metadataorder5
{
    return 5;
}
@end

@implementation OC_MetadataOrderChild1
- (char)metadataorder1
{
    return 11;
}
- (char)metadataorder2
{
    return 12;
}
- (char)metadataorder3
{
    return 13;
}
- (char)metadataorder4
{
    return 14;
}
- (char)metadataorder5
{
    return 15;
}
@end

@implementation OC_MetadataOrderChild2
- (char)metadataorder1
{
    return 21;
}
- (char)metadataorder2
{
    return 22;
}
- (char)metadataorder3
{
    return 23;
}
- (char)metadataorder4
{
    return 24;
}
- (char)metadataorder5
{
    return 25;
}
@end

@implementation OC_MetadataOrderGrandchild
- (char)metadataorder1
{
    return 111;
}
- (char)metadataorder2
{
    return 112;
}
- (char)metadataorder3
{
    return 113;
}
- (char)metadataorder4
{
    return 114;
}
- (char)metadataorder5
{
    return 115;
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
                           "OC_MetadataOrder",
                           PyObjC_IdToPython([OC_MetadataOrder class]))
        < 0) {

        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_MetadataOrderChild1",
                           PyObjC_IdToPython([OC_MetadataOrderChild1 class]))
        < 0) {

        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_MetadataOrderChild2",
                           PyObjC_IdToPython([OC_MetadataOrderChild2 class]))
        < 0) {

        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_MetadataOrderGrandchild",
                           PyObjC_IdToPython([OC_MetadataOrderGrandchild class]))
        < 0) {

        return -1; // LCOV_EXCL_LINE
    }

    PyObject* p = PyObjC_IdToPython(@protocol(OC_MetaDataProto));
    Py_CLEAR(p);

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
    .m_name     = "metadataorder",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_metadataorder(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_metadataorder(void)
{
    return PyModuleDef_Init(&mod_module);
}
