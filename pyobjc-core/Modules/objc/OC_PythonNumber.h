#include "pyobjc.h"


@interface OC_PythonNumber : NSNumber {
    PyObject* value;
}

+ (instancetype _Nullable)numberWithPythonObject:(PyObject* _Nonnull)value;
- (instancetype _Nullable)initWithPythonObject:(PyObject* _Nonnull)value;
- (void)dealloc;
- (PyObject* _Nullable)__pyobjc_PythonObject__;
- (Class _Nonnull)classForArchiver;

@end
