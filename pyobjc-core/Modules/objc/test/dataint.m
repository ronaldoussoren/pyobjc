#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_DataInt : NSObject {
}
@end

@implementation OC_DataInt
+ (NSData*)getBytes:(NSData*)data length:(NSUInteger)length
{
    const void* bytes = [data bytes];
    return [NSData dataWithBytes:bytes length:length];
}

+ (NSObject*)setBytes:(NSMutableData*)data new:(NSData*)newData length:(NSUInteger)length
{
    const void* bytes    = [newData bytes];
    void*       mutbytes = [data mutableBytes];
    memcpy(mutbytes, bytes, length);
    return nil;
}

+ (NSUInteger)lengthOf:(NSData*)data
{
    return [data length];
}

+ (Class)coderClassFor:(NSData*)data
{
    return [data classForCoder];
}

+ (Class)keyedArchiverClassFor:(NSData*)data
{
    return [data classForKeyedArchiver];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "dataint", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_dataint(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_dataint(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_DataInt", PyObjC_IdToPython([OC_DataInt class])) < 0) {
        return NULL;
    }

    return m;
}
