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
        [self release];
        return nil;
    }
    if (!PyUnicode_Check(fspath)) {
        Py_DECREF(fspath);
        PyErr_Format(PyExc_ValueError, "os.fspath(%R) did not return a string", object);
        [self release];
        return nil;
    }

    const char* utf8;
    Py_ssize_t  utf8_size;

    utf8 = PyUnicode_AsUTF8AndSize(fspath, &utf8_size);
    if (unlikely(utf8 == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(fspath);
        [self release];
        return nil;
        // LCOV_EXCL_STOP
    }
    if (utf8_size != (Py_ssize_t)strlen(utf8)) {
        Py_DECREF(fspath);
        PyErr_Format(PyExc_ValueError, "os.fspath(%R) result has embedded NULs", object);
        [self release];
        return nil;
    }

    NSString* path = [[NSString alloc] initWithUTF8String:utf8];
    Py_DECREF(fspath);
    if (unlikely(path == nil)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        [self release];
        return nil;
        // LCOV_EXCL_STOP
    }

    self = [super initFileURLWithPath:path];
    [path release];
    if (self == nil) {
        return nil;
    }

    SET_FIELD_INCREF(value, object);
    return self;
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
        PyObjC_UnregisterObjCProxy(value, self);
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

// LCOV_EXCL_START
/* PythonTransient is used in the implementation of
 * methods written in Python, OC_Python* classes
 * don't have such methods.
 */
- (PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    Py_XINCREF(value);
    return value;
}
// LCOV_EXCL_STOP
@end

NS_ASSUME_NONNULL_END
