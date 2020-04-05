#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_TestDecimal : NSObject {
}
- (int)getDecimal:(out NSDecimal*)value;
- (id)stringFromDecimal:(in NSDecimal*)value;
- (void)doubleDecimal:(inout NSDecimal*)value;

@end

@implementation OC_TestDecimal

- (int)getDecimal:(out NSDecimal*)value
{
    NSDecimalNumber* num = [NSDecimalNumber decimalNumberWithString:@"2.5"];
    *value               = [num decimalValue];
    return 1;
}

- (id)stringFromDecimal:(in NSDecimal*)value
{
    return NSDecimalString(value, nil);
}

- (void)doubleDecimal:(inout NSDecimal*)value
{
    NSDecimal tmp;
    NSDecimalAdd(&tmp, value, value, NSRoundPlain);
    *value = tmp;
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "decimal", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_decimal(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_decimal(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_TestDecimal", PyObjC_IdToPython([OC_TestDecimal class]))
        < 0) {
        return NULL;
    }

    return m;
}
