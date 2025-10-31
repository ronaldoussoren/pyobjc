#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@protocol OC_MetaDataProto
@optional
- (BOOL)metaProtoValue;
@end

@interface OC_CustomCaller : NSObject {
}
@end

@interface OC_CustomCallerChild1 : OC_CustomCaller {
}
@end

@interface OC_CustomCallerChild2 : OC_CustomCaller {
}
@end

@interface OC_CustomCallerGrandchild : OC_CustomCallerChild1 {
}
@end

@implementation OC_CustomCaller
- (int)customcallers1
{
    return 1;
}
- (int)customcallers2
{
    return 2;
}
- (int)customcallers3
{
    return 3;
}
- (int)customcallers4
{
    return 4;
}
- (int)customcallers5
{
    return 5;
}
- (int)customcallers6
{
    return 6;
}
- (int)customcallers7
{
    return 7;
}
- (int)customcallers8
{
    return 8;
}
- (int)customcallers8:(int*)pvalue
{
    return 8 + *pvalue;
}
@end

@implementation OC_CustomCallerChild1
- (int)customcallers1
{
    return 11;
}
- (int)customcallers2
{
    return 12;
}
- (int)customcallers3
{
    return 13;
}
- (int)customcallers4
{
    return 14;
}
- (int)customcallers5
{
    return 15;
}
- (int)customcallers6
{
    return 16;
}
- (int)customcallers7
{
    return 17;
}
@end

@implementation OC_CustomCallerChild2
- (int)customcallers1
{
    return 21;
}
- (int)customcallers2
{
    return 22;
}
- (int)customcallers3
{
    return 23;
}
- (int)customcallers4
{
    return 24;
}
- (int)customcallers5
{
    return 25;
}
- (int)customcallers6
{
    return 26;
}
- (int)customcallers7
{
    return 27;
}
@end

@implementation OC_CustomCallerGrandchild
- (int)customcallers1
{
    return 111;
}
- (int)customcallers2
{
    return 112;
}
- (int)customcallers3
{
    return 113;
}
- (int)customcallers4
{
    return 114;
}
- (int)customcallers5
{
    return 115;
}
- (int)customcallers6
{
    return 116;
}
- (int)customcallers7
{
    return 117;
}
@end

#define DEFINE_CALLER(NAME, VALUE)                                                       \
    static PyObject* _Nullable NAME(PyObject* _Nonnull meth __attribute__((__unused__)), \
                                    PyObject* _Nonnull self __attribute__((__unused__)), \
                                    PyObject* const _Nonnull* _Nonnull args              \
                                    __attribute__((__unused__)),                         \
                                    size_t nargs __attribute__((__unused__)))            \
    {                                                                                    \
        return PyLong_FromLong((VALUE));                                                 \
    }

#define REGISTER_CALLER(class, sel, name)                                                \
    do {                                                                                 \
        if (PyObjC_RegisterMethodMapping((class), (sel), (name),                         \
                                         PyObjCUnsupportedMethod_IMP)                    \
            < 0) {                                                                       \
            return -1;                                                                   \
        }                                                                                \
    } while (0)

DEFINE_CALLER(call_customcallers2, -2)
DEFINE_CALLER(call_customcallers2b, -20)
DEFINE_CALLER(call_customcallers3, -3)
DEFINE_CALLER(call_customcallers3b, -30)
DEFINE_CALLER(call_customcallers4, -4)
DEFINE_CALLER(call_customcallers4b, -40)
DEFINE_CALLER(call_customcallers5, -5)
DEFINE_CALLER(call_customcallers5b, -50)
DEFINE_CALLER(call_customcallers6, -6)
DEFINE_CALLER(call_customcallers7, -7)
DEFINE_CALLER(call_customcallers7b, -70)

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_CustomCaller", PyObjC_IdToPython([OC_CustomCaller class]))
        < 0) {

        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_CustomCallerChild1",
                           PyObjC_IdToPython([OC_CustomCallerChild1 class]))
        < 0) {

        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_CustomCallerChild2",
                           PyObjC_IdToPython([OC_CustomCallerChild2 class]))
        < 0) {

        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_CustomCallerGrandchild",
                           PyObjC_IdToPython([OC_CustomCallerGrandchild class]))
        < 0) {

        return -1; // LCOV_EXCL_LINE
    }

    REGISTER_CALLER(NULL, @selector(customcallers2), call_customcallers2);
    REGISTER_CALLER([OC_CustomCallerChild2 class], @selector(customcallers2),
                    call_customcallers2b);

    REGISTER_CALLER([OC_CustomCallerChild2 class], @selector(customcallers3),
                    call_customcallers3b);
    REGISTER_CALLER(NULL, @selector(customcallers3), call_customcallers3);

    REGISTER_CALLER([OC_CustomCaller class], @selector(customcallers4),
                    call_customcallers4);
    REGISTER_CALLER([OC_CustomCallerChild2 class], @selector(customcallers4),
                    call_customcallers4b);

    REGISTER_CALLER([OC_CustomCallerChild2 class], @selector(customcallers5),
                    call_customcallers5b);
    REGISTER_CALLER([OC_CustomCaller class], @selector(customcallers5),
                    call_customcallers5);

    REGISTER_CALLER([OC_CustomCallerChild2 class], @selector(customcallers6),
                    call_customcallers6);

    REGISTER_CALLER([OC_CustomCallerChild2 class], @selector(customcallers7),
                    call_customcallers7);
    REGISTER_CALLER([OC_CustomCallerChild2 class], @selector(customcallers7),
                    call_customcallers7b);

    REGISTER_CALLER([OC_CustomCaller class], @selector(customcallers8),
                    PyObjCUnsupportedMethod_Caller);
    REGISTER_CALLER([OC_CustomCaller class], @selector(customcallers8:),
                    PyObjCUnsupportedMethod_Caller);

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
    .m_name     = "customcallers",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_customcallers(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_customcallers(void)
{
    return PyModuleDef_Init(&mod_module);
}
