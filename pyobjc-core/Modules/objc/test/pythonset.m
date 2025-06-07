#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

#ifndef NSINTEGER_DEFINED

typedef unsigned int NSUInteger;

#endif

@interface OC_TestSet : NSObject {
}
@end

@implementation OC_TestSet

+ (id)setWithInstanceOfClass:(Class)aClass
{
    NSInvocation*        inv;
    NSMutableSet*        set = [[NSMutableSet alloc] init];
    NSObject<NSCopying>* value;

    inv = [NSInvocation
        invocationWithMethodSignature:[NSObject
                                          methodSignatureForSelector:@selector(new)]];
    if (inv == nil) {
        [set release];
        return nil;
    }
    inv.target   = aClass;
    inv.selector = @selector(new);

    [inv invoke];
    [inv getReturnValue:&value];
    [set addObject:value];
    return [set autorelease];
}

+ (Class)classOf:(NSObject*)value
{
    return [value class];
}

/* copying */
+ (id)set:(NSSet*)set copyWithZone:(NSZone*)zone
{
    return [[set copyWithZone:zone] autorelease];
}

+ (id)set:(NSSet*)set mutableCopyWithZone:(NSZone*)zone
{
    return [[set mutableCopyWithZone:zone] autorelease];
}

/* Base set */

+ (NSArray*)allObjectsOfSet:(NSSet*)set
{
    return [set allObjects];
}

+ (id)anyObjectOfSet:(NSSet*)set
{
    return [set anyObject];
}

+ (BOOL)set:(NSSet*)set containsObject:(id)anObject
{
    return [set containsObject:anObject];
}

+ (BOOL)set:(NSSet*)set containsInstanceOf:(Class)cls
{
    id anObject = [[cls alloc] init];
    BOOL result = [set containsObject:anObject];
    [anObject release];
    return result;
}

+ (NSUInteger)countOfSet:(NSSet*)set
{
    return [set count];
}

+ (NSString*)descriptionOfSet:(NSSet*)set
{
    return [set description];
}

+ (NSString*)set:(NSSet*)set descriptionWithLocale:(id)locale
{
    return [set descriptionWithLocale:locale];
}

+ (NSSet*)set:(NSSet*)set filteredSetUsingPredicate:(NSPredicate*)predicate
{
    return [set filteredSetUsingPredicate:predicate];
}

+ (BOOL)set:(NSMutableSet*)set intersectsSet:(NSSet*)otherSet
{
    return [set intersectsSet:otherSet];
}

+ (BOOL)set:(NSSet*)set isEqualToSet:(NSSet*)otherSet
{
    return [set isEqualToSet:otherSet];
}

+ (BOOL)set:(NSSet*)set isSubsetOfSet:(NSSet*)otherSet
{
    return [set isSubsetOfSet:otherSet];
}

+ (void)set:(NSSet*)set makeObjectsPerformSelector:(SEL)aSelector
{
    [set makeObjectsPerformSelector:aSelector];
}

+ (void)set:(NSSet*)set makeObjectsPerformSelector:(SEL)aSelector withObject:(id)anObject
{
    [set makeObjectsPerformSelector:aSelector withObject:anObject];
}

+ (id)set:(NSSet*)set member:(id)anObject
{
    return [set member:anObject];
}

+ (id)set:(NSSet*)set memberInstanceOf:(Class)cls
{
    id anObject = [[cls alloc] init];
    id result = [set member:anObject];
    [anObject release];
    return result;
}

+ (NSEnumerator*)objectEnumeratorOfSet:(NSSet*)set
{
    return [set objectEnumerator];
}

+ (NSSet*)set:(NSSet*)set setByAddingObject:(id)anObject
{
    return [set setByAddingObject:anObject];
}

+ (NSSet*)set:(NSSet*)set setByAddingObjectsFromArray:(NSArray*)anObject
{
    return [set setByAddingObjectsFromArray:anObject];
}

+ (NSSet*)set:(NSSet*)set setByAddingObjectsFromSet:(NSSet*)anObject
{
    return [set setByAddingObjectsFromSet:anObject];
}

+ (void)set:(NSSet*)set setValue:(id)value forKey:(id)key
{
    [set setValue:value forKey:key];
}

+ (id)set:(NSSet*)set valueForKey:(id)key
{
    return [set valueForKey:key];
}

/* Mutable set */

+ (void)set:(NSMutableSet*)set addObject:(id)anObject
{
    [set addObject:anObject];
}

+ (void)set:(NSMutableSet*)set addInstanceOf:(Class)cls
{
    id anObject = [[cls alloc] init];
    [set addObject:anObject];
    [anObject release];
}

+ (void)set:(NSMutableSet*)set addObjectsFromArray:(NSArray*)anArray
{
    [set addObjectsFromArray:anArray];
}

+ (void)set:(NSMutableSet*)set filterUsingPredicate:(NSPredicate*)predicate
{
    [set filterUsingPredicate:predicate];
}

+ (void)set:(NSMutableSet*)set intersectSet:(NSSet*)otherSet
{
    [set intersectSet:otherSet];
}

+ (void)set:(NSMutableSet*)set minusSet:(NSSet*)otherSet
{
    [set minusSet:otherSet];
}

+ (void)removeAllObjecsFromSet:(NSMutableSet*)set
{
    [set removeAllObjects];
}

+ (void)set:(NSMutableSet*)set removeObject:(id)anObject
{
    [set removeObject:anObject];
}

+ (void)set:(NSMutableSet*)set removeInstanceOf:(Class)cls
{
    id anObject = [[cls alloc] init];
    [set removeObject:anObject];
    [anObject release];
}

+ (void)set:(NSMutableSet*)set setSet:(NSSet*)otherSet
{
    [set setSet:otherSet];
}

+ (void)set:(NSMutableSet*)set unionSet:(NSSet*)otherSet
{
    [set unionSet:otherSet];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_TestSet", PyObjC_IdToPython([OC_TestSet class])) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {
        .slot = Py_mod_exec,
        .value = (void*)mod_exec_module
    },
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        .slot = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "pythonset",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_pythonset(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_pythonset(void)
{
    return PyModuleDef_Init(&mod_module);
}
