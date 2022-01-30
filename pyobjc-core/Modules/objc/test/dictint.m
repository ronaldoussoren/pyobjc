#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_DictInt : NSObject {
}
@end

@implementation OC_DictInt
+ (id)dictWithKeyOfClass:(Class)keyClass valueOfClass:(Class)valueClass
{
    NSInvocation*        inv;
    NSMutableDictionary* dict = [[NSMutableDictionary alloc] init];
    NSObject<NSCopying>* key;
    NSObject*            value;

    inv = [NSInvocation
        invocationWithMethodSignature:[NSObject
                                          methodSignatureForSelector:@selector(new)]];
    if (inv == nil) {
        [dict release];
        return nil;
    }
    inv.selector = @selector(new);

    inv.target = keyClass;
    [inv invoke];
    [inv getReturnValue:&key];

    inv.target = valueClass;
    [inv invoke];
    [inv getReturnValue:&value];

    [dict setObject:value forKey:key];
    return [dict autorelease];
}

+ (NSArray*)allKeys:(NSDictionary*)dict
{
    return [[dict keyEnumerator] allObjects];
}

+ (NSArray*)allValues:(NSDictionary*)dict
{
    return [[dict objectEnumerator] allObjects];
}

+ (id)dict:(NSDictionary*)dict getItem:(id)key
{
    return [dict objectForKey:key];
}

+ (void)dict:(NSMutableDictionary*)dict set:(id)key value:(id)value
{
    [dict setObject:value forKey:key];
}

+ (void)dict:(NSMutableDictionary*)dict remove:(id)key
{
    [dict removeObjectForKey:key];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "dictint", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_dictint(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_dictint(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_DictInt", PyObjC_IdToPython([OC_DictInt class])) < 0) {
        return NULL;
    }

    return m;
}
