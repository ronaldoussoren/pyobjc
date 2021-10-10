NS_ASSUME_NONNULL_BEGIN
/* Methods assume the GIL is held */
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
