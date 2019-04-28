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

@implementation OCReleasedBuffer
- (instancetype)initWithPythonBuffer:(PyObject*)object writable:(BOOL)writable
{
    int r;

    self = [super init];
    if (self == nil)
        return nil;

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
    if (self->have_buffer) {
        PyBuffer_Release(&self->buffer);
        self->have_buffer = NO;
    }
    [super dealloc];
}

- (void*)buffer
{
    return self->buffer.buf;
}

- (NSUInteger)length
{
    return (NSUInteger)self->buffer.len;
}

@end
