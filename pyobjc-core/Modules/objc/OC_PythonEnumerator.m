#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_PythonEnumerator

+ (instancetype)enumeratorWithPythonObject:(PyObject*)object
{
    return [[[self alloc] initWithPythonObject:object] autorelease];
}

- (id)initWithPythonObject:(PyObject*)object
{
    /* -[NSObject init] is documented as return self */
    self = (id _Nonnull)[super init];

    SET_FIELD_INCREF(value, object);
    valid = YES;

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

- (id _Nullable)nextObject
{
    if (!valid) {
        return nil;
    }

    NSObject* result;

    PyObjC_BEGIN_WITH_GIL
        PyObject* object = PyIter_Next(value);
        if (object == NULL) {
            if (!PyErr_Occurred()) {
                valid = NO;
                PyErr_Clear();
                PyObjC_GIL_RETURN(nil);
            } else {
                PyObjC_GIL_FORWARD_EXC();
            }
        }

        if (object == Py_None) {
            result = [NSNull null];
        } else {
            if (depythonify_python_object(object, &result) == -1) {
                PyObjC_GIL_FORWARD_EXC();
            }
        }
        Py_DECREF(object);

    PyObjC_END_WITH_GIL

    return result;
}

- (NSArray*)allObjects
{
    NSMutableArray* array;
    NSObject*       cur;

    array = [NSMutableArray array];
    if (array == nil) // LCOV_BR_EXCL_LINE
        return nil;   // LCOV_EXCL_LINE

    while ((cur = [self nextObject]) != nil) {
        [array addObject:cur];
    }

    return array;
}

@end

NS_ASSUME_NONNULL_END
