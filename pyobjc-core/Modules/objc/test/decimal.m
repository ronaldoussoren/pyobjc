#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_TestDecimal : NSObject
{
}
-(int)getDecimal:(out NSDecimal*)value;
-(id)stringFromDecimal:(in NSDecimal*)value;
-(void)doubleDecimal:(inout NSDecimal*)value;

@end

@implementation OC_TestDecimal

-(int)getDecimal:(out NSDecimal*)value
{
    NSDecimalNumber* num = [NSDecimalNumber decimalNumberWithString:@"2.5"];
    *value = [num decimalValue];
    return 1;
}

-(id)stringFromDecimal:(in NSDecimal*)value
{
    return NSDecimalString(value, nil);
}

-(void)doubleDecimal:(inout NSDecimal*)value
{
    NSDecimal tmp;
    NSDecimalAdd(&tmp, value, value, NSRoundPlain);
    *value = tmp;
}

@end


static PyMethodDef mod_methods[] = {
            { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT,
    "decimal",
    NULL,
    0,
    mod_methods,
    NULL,
    NULL,
    NULL,
    NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit_decimal(void);

PyObject* __attribute__((__visibility__("default")))
PyInit_decimal(void)

#else

#define INITERROR() return
#define INITDONE() return

void initdecimal(void);

void __attribute__((__visibility__("default")))
initdecimal(void)
#endif
{
    PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
    m = PyModule_Create(&mod_module);
#else
    m = Py_InitModule4("decimal", mod_methods,
        NULL, NULL, PYTHON_API_VERSION);
#endif
    if (!m) {
        INITERROR();
    }

    if (PyObjC_ImportAPI(m) < 0) {
        INITERROR();
    }

    if (PyModule_AddObject(m, "OC_TestDecimal",
        PyObjC_IdToPython([OC_TestDecimal class])) < 0) {
        INITERROR();
    }

    INITDONE();
}
