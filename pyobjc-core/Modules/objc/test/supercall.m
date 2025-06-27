#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@implementation NSObject (supercallhelpers)
- (id)ocRegisterCallerFirst
{
    return @"native-first";
}

- (id)ocRegisterCallerLast
{
    return @"native-last";
}

- (id)ocRegisterCallerFirstNone1
{
    return @"native-first-none1";
}

- (id)ocRegisterCallerLastNone1
{
    return @"native-last-none1";
}

- (id)ocRegisterCallerFirstNone2
{
    return @"native-first-none2";
}

- (id)ocRegisterCallerLastNone2
{
    return @"native-last-none2";
}

- (id)ocRegisterSubClassOnly
{
    return @"native-subclass-only";
}

- (id)ocRegisterSubClassOnlyNone1
{
    return @"native-subclass-only-none1";
}
- (id)ocRegisterSubClassOnlyNone2
{
    return @"native-subclass-only-none2";
}

@end

@interface OCSuperCallHelper : NSObject {
}
@end

@implementation OCSuperCallHelper
- (id)ocRegisterCallerFirst
{
    return @"subclass-native-first";
}

- (id)ocRegisterCallerLast
{
    return @"subclass-native-last";
}

- (id)ocRegisterCallerFirstNone1
{
    return @"subclass-native-first-none1";
}

- (id)ocRegisterCallerLastNone1
{
    return @"subclass-native-last-none1";
}

- (id)ocRegisterCallerFirstNone2
{
    return @"subclass-native-first-none2";
}

- (id)ocRegisterCallerLastNone2
{
    return @"subclass-native-last-none2";
}

- (id)ocRegisterSubClassOnly
{
    return @"subclass-native-subclass-only";
}

- (id)ocRegisterSubClassOnlyNone1
{
    return @"subclass-native-subclass-only-none1";
}
- (id)ocRegisterSubClassOnlyNone2
{
    return @"subclass-native-subclass-only-none2";
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunused-parameter"

static PyObject*
call_ocRegisterCallerFirst_NSObject(PyObject* method, PyObject* self,
                                    PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-first-nsobject");
}

static PyObject*
call_ocRegisterCallerFirst_OCSuperCallHelper(PyObject* method, PyObject* self,
                                             PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-first-subclass");
}

static PyObject*
call_ocRegisterCallerLast_NSObject(PyObject* method, PyObject* self,
                                   PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-last-nsobject");
}

static PyObject*
call_ocRegisterCallerLast_OCSuperCallHelper(PyObject* method, PyObject* self,
                                            PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-last-subclass");
}

static PyObject*
call_ocRegisterCallerFirst_None1_NSObject(PyObject* method, PyObject* self,
                                          PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-first-none1-nsobject");
}

static PyObject*
call_ocRegisterCallerFirst_None1_OCSuperCallHelper(PyObject* method, PyObject* self,
                                                   PyObject* const* arguments,
                                                   size_t           nargs)
{
    return PyUnicode_FromString("overriden-first-none1-subclass");
}

static PyObject*
call_ocRegisterCallerFirst_None1_None(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-first-none1-none");
}

static PyObject*
call_ocRegisterCallerLast_None1_NSObject(PyObject* method, PyObject* self,
                                         PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-last-none1-nsobject");
}

static PyObject*
call_ocRegisterCallerLast_None1_OCSuperCallHelper(PyObject* method, PyObject* self,
                                                  PyObject* const* arguments,
                                                  size_t           nargs)
{
    return PyUnicode_FromString("overriden-last-none1-subclass");
}

static PyObject*
call_ocRegisterCallerLast_None1_None(PyObject* method, PyObject* self,
                                     PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-last-none1-none");
}

static PyObject*
call_ocRegisterCallerFirst_None2_NSObject(PyObject* method, PyObject* self,
                                          PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-first-none2-nsobject");
}

static PyObject*
call_ocRegisterCallerFirst_None2_OCSuperCallHelper(PyObject* method, PyObject* self,
                                                   PyObject* const* arguments,
                                                   size_t           nargs)
{
    return PyUnicode_FromString("overriden-first-none2-subclass");
}

static PyObject*
call_ocRegisterCallerFirst_None2_None(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-first-none2-none");
}

static PyObject*
call_ocRegisterCallerLast_None2_NSObject(PyObject* method, PyObject* self,
                                         PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-last-none2-nsobject");
}

static PyObject*
call_ocRegisterCallerLast_None2_OCSuperCallHelper(PyObject* method, PyObject* self,
                                                  PyObject* const* arguments,
                                                  size_t           nargs)
{
    return PyUnicode_FromString("overriden-last-none2-subclass");
}

static PyObject*
call_ocRegisterCallerLast_None2_None(PyObject* method, PyObject* self,
                                     PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-last-none2-none");
}

static PyObject*
call_ocRegisterSubClassOnly_OCSuperCallHelper(PyObject* method, PyObject* self,
                                              PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-subclass-only-subclass");
}

static PyObject*
call_ocRegisterSubClassOnly_None1_OCSuperCallHelper(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
{
    return PyUnicode_FromString("overriden-subclass-only-none1-subclass");
}

static PyObject*
call_ocRegisterSubClassOnly_None1_None(PyObject* method, PyObject* self,
                                       PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-subclass-only-none1-none");
}

static PyObject*
call_ocRegisterSubClassOnly_None2_OCSuperCallHelper(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
{
    return PyUnicode_FromString("overriden-subclass-only-none2-subclass");
}

static PyObject*
call_ocRegisterSubClassOnly_None2_None(PyObject* method, PyObject* self,
                                       PyObject* const* arguments, size_t nargs)
{
    return PyUnicode_FromString("overriden-subclass-only-none2-none");
}

#pragma clang diagnostic pop

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OCSuperCallHelper",
                           PyObjC_IdToPython([OCSuperCallHelper class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

#define REGISTER(CLASS, SELECTOR, CALLER)                                                \
    do {                                                                                 \
        if (PyObjC_RegisterMethodMapping(CLASS, @selector(SELECTOR), CALLER,             \
                                         PyObjCUnsupportedMethod_IMP)                    \
            < 0) {                                                                       \
            return -1;                                                                   \
        }                                                                                \
    } while (0)

    /* NSObject first */
    REGISTER([NSObject class], ocRegisterCallerFirst,
             call_ocRegisterCallerFirst_NSObject);
    REGISTER([OCSuperCallHelper class], ocRegisterCallerFirst,
             call_ocRegisterCallerFirst_OCSuperCallHelper);

    /* NSObject last */
    REGISTER([OCSuperCallHelper class], ocRegisterCallerLast,
             call_ocRegisterCallerLast_OCSuperCallHelper);
    REGISTER([NSObject class], ocRegisterCallerLast, call_ocRegisterCallerLast_NSObject);

    /* NSObject first, Nil before */
    REGISTER(Nil, ocRegisterCallerFirst, call_ocRegisterCallerFirst_None1_None);
    REGISTER([NSObject class], ocRegisterCallerFirstNone1,
             call_ocRegisterCallerFirst_None1_NSObject);
    REGISTER([OCSuperCallHelper class], ocRegisterCallerFirstNone1,
             call_ocRegisterCallerFirst_None1_OCSuperCallHelper);

    /* NSObject last, Nil before */
    REGISTER(Nil, ocRegisterCallerLastNone1, call_ocRegisterCallerLast_None1_None);
    REGISTER([OCSuperCallHelper class], ocRegisterCallerLastNone1,
             call_ocRegisterCallerLast_None1_OCSuperCallHelper);
    REGISTER([NSObject class], ocRegisterCallerLastNone1,
             call_ocRegisterCallerLast_None1_NSObject);

    /* NSObject first, Nil after */
    REGISTER([NSObject class], ocRegisterCallerFirstNone2,
             call_ocRegisterCallerFirst_None2_NSObject);
    REGISTER([OCSuperCallHelper class], ocRegisterCallerFirstNone2,
             call_ocRegisterCallerFirst_None2_OCSuperCallHelper);
    REGISTER(Nil, ocRegisterCallerFirstNone2, call_ocRegisterCallerFirst_None2_None);

    /* NSObject last, Nil after */
    REGISTER([OCSuperCallHelper class], ocRegisterCallerLastNone2,
             call_ocRegisterCallerLast_None2_OCSuperCallHelper);
    REGISTER([NSObject class], ocRegisterCallerLastNone2,
             call_ocRegisterCallerLast_None2_NSObject);
    REGISTER(Nil, ocRegisterCallerLastNone2, call_ocRegisterCallerLast_None2_None);

    /* Only on subclass */
    REGISTER([OCSuperCallHelper class], ocRegisterSubClassOnly,
             call_ocRegisterSubClassOnly_OCSuperCallHelper);

    /* Only in subclass, Nil before */
    REGISTER(Nil, ocRegisterSubClassOnlyNone1, call_ocRegisterSubClassOnly_None1_None);
    REGISTER([OCSuperCallHelper class], ocRegisterSubClassOnlyNone1,
             call_ocRegisterSubClassOnly_None1_OCSuperCallHelper);

    /* Only in subclass, Nil after */
    REGISTER(Nil, ocRegisterSubClassOnlyNone2, call_ocRegisterSubClassOnly_None2_None);
    REGISTER([OCSuperCallHelper class], ocRegisterSubClassOnlyNone2,
             call_ocRegisterSubClassOnly_None2_OCSuperCallHelper);

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
    .m_name     = "supercall",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_supercall(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_supercall(void)
{
    return PyModuleDef_Init(&mod_module);
}
