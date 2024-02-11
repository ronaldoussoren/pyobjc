#include "pyobjc.h"
NS_ASSUME_NONNULL_BEGIN

@implementation OC_PythonURL

+ (instancetype _Nullable)URLWithPythonObject:(PyObject*)object
{
    return [[[self alloc] initWithPythonObject:object] autorelease];
}

- (id _Nullable)initWithPythonObject:(PyObject*)object
{
    PyObject* fspath = PyOS_FSPath(object);
    if (fspath == NULL) {
        return nil;
    }
    if (!PyUnicode_Check(fspath)) {
        Py_DECREF(fspath);
        PyErr_Format(PyExc_ValueError, "os.fspath(%R) did not return a string", object);
        return nil;
    }

    const char* utf8;
    Py_ssize_t utf8_size;

    utf8 = PyUnicode_AsUTF8AndSize(fspath, &utf8_size);
    if (utf8 == NULL) {
        Py_DECREF(fspath);
        return nil;
    }
    if (utf8_size != (Py_ssize_t)strlen(utf8)) {
        Py_DECREF(fspath);
        PyErr_Format(PyExc_ValueError, "os.fspath(%R) result has embedded NULs", object);
        return nil;
    }

    NSString* path = [[NSString alloc] initWithUTF8String:utf8];
    Py_DECREF(fspath);
    if (path == nil) {
        return nil;
    }

    self = [super initFileURLWithPath:path];
    [path release];
    if (self == nil) {
        return nil;
    }

    SET_FIELD_INCREF(value, object);
    return self;
}

- (oneway void)release
{
    /* See comment in OC_PythonUnicode */
    if (unlikely(!Py_IsInitialized())) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        [super release];
        return;
        // LCOV_EXCL_STOP
    }

    PyObjC_BEGIN_WITH_GIL
        @try {
            [super release];
            // LCOV_EXCL_START
        } @catch (NSObject* exc) {
            /* I'm 99% sure this path cannot be hit,
             * this class cannot be subclassesed and
             * -dealloc cannot raise.
             */
            PyObjC_LEAVE_GIL;
            @throw;
        }
        // LCOV_EXCL_STOP

    PyObjC_END_WITH_GIL
}

- (void)dealloc
{
    if (unlikely(!Py_IsInitialized())) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        [super dealloc];
        return;
        // LCOV_EXCL_STOP
    }

    PyObjC_BEGIN_WITH_GIL
        Py_XDECREF(value);
    PyObjC_END_WITH_GIL

    [super dealloc];
}

/*
 * NSURL implements safe coding, that's something we cannot
 * do for arbitrary python objects. Therefore punt and encode
 * as a regular NSURL.
 */
- (Class)classForCoder
{
    return [NSURL class];
}

- (Class _Nullable)classForKeyedArchiver
{
    return [NSURL class];
}


- (PyObject*)__pyobjc_PythonObject__
{
    Py_XINCREF(value);
    return value;
}

- (PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    Py_XINCREF(value);
    return value;
}
@end



NS_ASSUME_NONNULL_END
