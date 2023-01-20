/*
 * The class in this file is a helper that helps in
 * following the rules for Python's modern buffer protocol
 * without locking these buffers unnecessarity long.
 *
 * Users of this calls create an instance that's immediately
 * autoreleased and return the result of [instance buffer] to
 * Objective-C code.
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OCReleasedBuffer
- (instancetype)initWithPythonBuffer:(PyObject*)object writable:(BOOL)writable
{
    int r;

    /* -[NSObject init] is documented to not return nil */
    self = (id _Nonnull)[super init];

    self->have_buffer = NO;

    r = PyObject_GetBuffer(object, &self->buffer,
                           writable ? PyBUF_CONTIG : PyBUF_CONTIG_RO);
    if (r != 0) {
        [self release];
        return nil;
    }
    self->have_buffer = YES;

    return self;
}

- (void)dealloc
{
    PyObjC_BEGIN_WITH_GIL
        if (have_buffer) {
            PyBuffer_Release(&buffer);
            have_buffer = NO;
        }
    PyObjC_END_WITH_GIL
    [super dealloc];
}

- (void*)buffer
{
    return buffer.buf;
}

- (NSUInteger)length
{
    return (NSUInteger)buffer.len;
}

@end

NS_ASSUME_NONNULL_END
