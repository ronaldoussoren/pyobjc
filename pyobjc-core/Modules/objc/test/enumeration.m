#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_Enumeration : NSObject {
}
@end

@implementation OC_Enumeration
+ (NSArray*)consumeDictKeyIteratorPlusOne:(NSDictionary*)argValue
{
    NSMutableArray* array = [NSMutableArray array];

    NSEnumerator* enumValue = [argValue keyEnumerator];

    for (NSObject* value = [enumValue nextObject]; value != nil;
         value           = [enumValue nextObject]) {
        [array addObject:value];
    }

    if ([enumValue nextObject] != nil) {
        return nil;
    }

    return array;
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "enumeration", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_enumeration(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_enumeration(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_Enumeration", PyObjC_IdToPython([OC_Enumeration class]))
        < 0) {
        return NULL;
    }

    return m;
}
