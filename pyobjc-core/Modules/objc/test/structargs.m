/*
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Cocoa/Cocoa.h>

struct BufferStruct {
    char* buffer;
    int   buffer_size;
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

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "structargs", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_structargs(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_structargs(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "StructArgClass", PyObjC_IdToPython([StructArgClass class]))
        < 0) {
        return NULL;
    }

    return m;
}
