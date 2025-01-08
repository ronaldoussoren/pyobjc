/*
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Cocoa/Cocoa.h>

struct BufferStruct {
    char* buffer;
    int   buffer_size;
};

struct empty {
};

@interface StructArgClass : NSObject {
}
- (NSString*)compP:(NSPoint)aPoint aRect:(NSRect)aRect anOp:(int)op;
- (size_t)stackPtr;
- (NSRect)someRect;
- (NSRect)someRectWithRect:(NSRect)rect;
- (NSRect)someRectWithX:(int)x Y:(int)y H:(int)h W:(int)w;
- (NSRect)someRectWithObject:(StructArgClass*)o X:(int)x Y:(int)y H:(int)h W:(int)w;
- (NSData*)dataFromBuffer:(struct BufferStruct*)buf;
- (int)callWithEmpty:(struct empty)empty;
@end

@implementation StructArgClass
- (NSRect)someRectWithRect:(NSRect)rect
{
    return rect;
}

- (NSRect)someRectWithX:(int)x Y:(int)y H:(int)h W:(int)w
{
    return NSMakeRect(x, y, h, w);
}

- (NSRect)someRectWithObject:(StructArgClass*)o X:(int)x Y:(int)y H:(int)h W:(int)w
{
    return [o someRectWithRect:NSMakeRect(x, y, h, w)];
}

- (NSRect)someRect
{
    NSRect retval = NSMakeRect(1, 2, 3, 4);
    return retval;
}

- (NSString*)compP:(NSPoint)aPoint aRect:(NSRect)aRect anOp:(int)op
{
    return [NSString stringWithFormat:@"aP:%@ aR:%@ anO:%d", NSStringFromPoint(aPoint),
                                      NSStringFromRect(aRect), op];
}

static size_t
ident(size_t v)
{
    return v;
}
- (size_t)stackPtr
{
    char c;

    return ident(((size_t)&c) + 1);
}

- (NSData*)dataFromBuffer:(in struct BufferStruct*)buf
{
    return [NSData dataWithBytes:buf->buffer length:buf->buffer_size];
}

- (int)callWithEmpty:(struct empty)empty
{
    return 99;
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "StructArgClass", PyObjC_IdToPython([StructArgClass class]))
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
    .m_name = "structargs",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_structargs(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_structargs(void)
{
    return PyModuleDef_Init(&mod_module);
}
