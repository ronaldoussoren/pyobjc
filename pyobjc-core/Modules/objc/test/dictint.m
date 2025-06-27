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

+ (id)dict:(NSDictionary*)dict getItemInstanceOf:(Class)cls
{
    id key    = [[cls alloc] init];
    id result = [dict objectForKey:key];
    [key release];
    return result;
}

+ (void)dict:(NSMutableDictionary*)dict set:(id)key value:(id)value
{
    [dict setObject:value forKey:key];
}

+ (void)dict:(NSMutableDictionary*)dict setInstanceOf:(Class)cls value:(id)value
{
    id key = [[cls alloc] init];
    [dict setObject:value forKey:key];
    [key release];
}

+ (void)dict:(NSMutableDictionary*)dict set:(id)key valueInstanceOf:(Class)cls
{
    id value = [[cls alloc] init];
    [dict setObject:value forKey:key];
    [value release];
}

+ (void)dict:(NSMutableDictionary*)dict remove:(id)key
{
    [dict removeObjectForKey:key];
}

+ (void)dict:(NSMutableDictionary*)dict removeInstanceOf:(Class)cls
{
    id key = [[cls alloc] init];
    [dict removeObjectForKey:key];
    [key release];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_DictInt", PyObjC_IdToPython([OC_DictInt class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot  = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "dictint",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_dictint(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_dictint(void)
{
    return PyModuleDef_Init(&mod_module);
}
