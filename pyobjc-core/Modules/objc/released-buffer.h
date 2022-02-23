NS_ASSUME_NONNULL_BEGIN
/*
 * OCReleasedBuffer is a wrapper for a Py_buffer
 * that will release the buffer when the
 * OCReleasedBuffer object is deallocated.
 *
 * This will keep the Py_buffer alive while
 * Objective-C might use the data pointer.
 *
 * In particular, OCReleasedBuffer  is required
 * for objects like bytearray() where the data
 * pointer might change during the lifetime of
 * the object.
 *
 * NOTE: Methods other than dealloc assume that
 *       the GIL is held.
 */
@interface OCReleasedBuffer : NSObject {
    BOOL      have_buffer;
    Py_buffer buffer;
}
- (instancetype)initWithPythonBuffer:(PyObject*)object writable:(BOOL)writable;

- (void)dealloc;
- (void*)buffer;
- (NSUInteger)length;
@end
NS_ASSUME_NONNULL_END
