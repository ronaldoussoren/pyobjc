#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_GenericNew : NSObject {
    NSObject* value;
}
@end
@interface OC_GenericNewChild : OC_GenericNew {
}
@end
@interface OC_GenericNewChild2 : OC_GenericNewChild {
}
@end

@implementation OC_GenericNew
-(NSObject*)value
{
    return value;
}

-(instancetype)init
{
    self = [super init];
    if (!self) return nil;

    value = nil;
    return self;
}

-(instancetype)initWithValue:(NSObject*)v
{
    self = [super init];
    if (!self) return nil;

    value = [v retain];
    return self;
}

-(instancetype)initWithURL:(NSObject*)v
{
    self = [super init];
    if (!self) return nil;

    value = [v retain];
    return self;
}

-(instancetype)initWithFirst:(NSObject*)first second:(NSObject*)second
{
    self = [super init];
    if (!self) return nil;

    value = [[NSArray alloc] initWithObjects:@"first-second", first,second,nil];
    return self;
}
@end

@implementation OC_GenericNewChild

-(instancetype)initWithX:(NSObject*)x y:(NSObject*)y
{
    self = [super init];
    if (!self) return nil;

    value = [[NSArray alloc] initWithObjects:@"x-y", x,y,nil];
    return self;
}
@end

@implementation OC_GenericNewChild2

-(instancetype)initWithX:(NSObject*)x y:(NSObject*)y z:(NSObject*)z
{
    self = [super init];
    if (!self) return nil;

    value = [[NSArray alloc] initWithObjects:@"x-y-z", x,y,z,nil];
    return self;
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "genericnew", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_genericnew(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_genericnew(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_GenericNew", PyObjC_IdToPython([OC_GenericNew class]))
        < 0) {
        return NULL;
    }
    if (PyModule_AddObject(m, "OC_GenericNewChild", PyObjC_IdToPython([OC_GenericNewChild class]))
        < 0) {
        return NULL;
    }
    if (PyModule_AddObject(m, "OC_GenericNewChild2", PyObjC_IdToPython([OC_GenericNewChild2 class]))
        < 0) {
        return NULL;
    }

    return m;
}
