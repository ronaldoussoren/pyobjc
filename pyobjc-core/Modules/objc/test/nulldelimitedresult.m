#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_NullDelimitedResult : NSObject {
}
@end

@implementation OC_NullDelimitedResult

#define BODY(type)                                                                       \
    {                                                                                    \
        static type buffer[] = {1, 2, 3, 4, 0};                                          \
        return buffer;                                                                   \
    }

+ (char*)intchars
{
    static char buffer[] = {1, 2, 3, 4, 0};
    return buffer;
}

+ (void*)voids
{
    static char buffer[] = {1, 2, 3, 4, 0};
    return (void*)buffer;
}

+ (FILE**)files
{
    static FILE* buffer[3] = {0, 0, 0};
    if (buffer[0] == 0) {
        buffer[0] = stdin;
        buffer[1] = stdout;
    }
    return buffer;
}

+ (char*)chars BODY(char)

                   + (char*)chars2 BODY(char)

                   + (unsigned char*)uchars BODY(unsigned char)

                   + (unsigned char*)uchars2 BODY(unsigned char)

                   + (short*)shorts BODY(short)

                   + (unsigned short*)ushorts BODY(unsigned short)

                   + (int*)ints BODY(int)

                   + (unsigned int*)uints BODY(unsigned int)

                   + (long*)longs BODY(long)

                   + (unsigned long*)ulongs BODY(unsigned long)

                   + (long long*)longlongs BODY(long long)

                   + (unsigned long long*)ulonglongs BODY(unsigned long long)

                   + (float*)floats BODY(float)

                   + (id*)objects
{
    static id buf[] = {@"one", @"two", @"three", @"four", nil};
    return buf;
}

+ (id*)newrefsOfClass:(Class)aClass
{
    /* This leaks, but that's ok for a test */
    id* buf = malloc(sizeof(id) * 3);
    if (buf == NULL) {
        NSLog(@"Cannot allocate buffer");
        return NULL;
    }
    buf[0] = buf[1] = buf[2] = nil;
    buf[0]                   = [[aClass alloc] init];
    if (buf[0] == nil) {
        NSLog(@"Cannot allocate instance 0");
        return nil;
    }
    buf[1] = [[aClass alloc] init];
    if (buf[1] == nil) {
        NSLog(@"Cannot allocate instance 1");
        return nil;
    }
    return buf;
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
                           "OC_NullDelimitedResult",
                           PyObjC_IdToPython([OC_NullDelimitedResult class]))
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
    .m_name     = "nulldelimitedresult",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_nulldelimitedresult(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_nulldelimitedresult(
    void)
{
    return PyModuleDef_Init(&mod_module);
}
