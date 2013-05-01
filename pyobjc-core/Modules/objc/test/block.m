#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

#if (PyObjC_BUILD_RELEASE >= 1006) && (__GNUC__ >= 4 && __GNUC_MINOR__ >= 2)
@interface NSObject (IndirectBlockTest)
-(double)processBlock:(double(^)(double, double))aBlock;
@end
#endif

@interface OCTestBlock : NSObject {}

#if (PyObjC_BUILD_RELEASE >= 1006) && (__GNUC__ >= 4 && __GNUC_MINOR__ >= 2)

-(int(^)(void))getIntBlock;
-(double(^)(double,double))getFloatBlock;
-(NSRect(^)(double, double, double, double))getStructBlock;
-(void)callIntBlock:(void(^)(int))block withValue:(int)value;
-(double)callDoubleBlock:(double(^)(double, double))block withValue:(double)v1 andValue:(double)v2;
#endif

@end

@implementation OCTestBlock

#if PyObjC_BUILD_RELEASE >= 1006 && (__GNUC__ >= 4 && __GNUC_MINOR__ >= 2)

-(NSRect(^)(double, double, double, double))getStructBlock
{
    return [[^(double a, double b, double c, double d) {
        return NSMakeRect(a, b, c, d);
    } copy] autorelease];
}

-(int(^)(void))getIntBlock
{
    return [[^{ return 42; } copy] autorelease];
}

-(double(^)(double,double))getFloatBlock
{
    return [[^(double a, double b) { return a + b; } copy] autorelease];
}

-(void)callIntBlock:(void(^)(int))block withValue:(int)value
{
    block(value);
}

-(double)callDoubleBlock: (double(^)(double, double))block withValue:(double)v1 andValue:(double)v2
{
    return block(v1, v2);
}

-(NSRect)callStructBlock: (NSRect(^)(double, double, double, double))block
                   withA:(double)a b:(double)b c:(double)c d:(double)d
{
    return block(a, b, c, d);
}

-(double)callProcessBlockOn:(NSObject*)testObject
{
    return [testObject processBlock:^(double a, double b) { return a*b; }];
}

#endif

@end


static PyMethodDef mod_methods[] = {
            { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT,
    "block",
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

PyObject* PyInit_block(void);

PyObject* __attribute__((__visibility__("default")))
PyInit_block(void)

#else

#define INITERROR() return
#define INITDONE() return

void initblock(void);

void __attribute__((__visibility__("default")))
initblock(void)
#endif
{
    PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
    m = PyModule_Create(&mod_module);
#else
    m = Py_InitModule4("block", mod_methods,
        NULL, NULL, PYTHON_API_VERSION);
#endif
    if (!m) {
        INITERROR();
    }

    if (PyObjC_ImportAPI(m) < 0) {
        INITERROR();
    }

    if (PyModule_AddObject(m, "OCTestBlock",
        PyObjC_IdToPython([OCTestBlock class])) < 0) {
        INITERROR();
    }

    INITDONE();
}
