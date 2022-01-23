#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
#include <objc/objc.h>

@interface
NSObject ()
- (NSString*)_copyDescription;
- (BOOL)isNSArray__;
- (BOOL)isNSDictionary__;
- (BOOL)isNSSet__;
- (BOOL)isNSNumber__;
- (BOOL)isNSData__;
- (BOOL)isNSDate__;
- (BOOL)isNSString__;
- (BOOL)isNSValue__;
- (CFTypeID)_cfTypeID;
- (NSComparisonResult)compare:(NSObject*)other;
@end

@interface
NSObject (TestMethods)
- (void)nosuchSelector;
- (void)voidSelector;
- (id)idSelector;
- (id)selectorWithArg:(id)arg1 andArg:(id)arg2;
@end

@interface OC_ObjectInt : NSObject {
}
@end

@implementation OC_ObjectInt

+ (id)invokeSelector:(SEL)sel of:(NSObject*)object
{
    return ((id(*)(id, SEL))objc_msgSend)(object, sel);
}

+ (bool)respondsToSelector:(SEL)sel classOf:(NSObject*)object
{
    return [[object class] respondsToSelector:sel];
}

+ (bool)respondsToSelector:(SEL)sel of:(NSObject*)object
{
    return [object respondsToSelector:sel];
}

+ (NSMethodSignature*)methodSignatureForSelector:(SEL)selector of:(NSObject*)object
{
    return [object methodSignatureForSelector:selector];
}

+ (NSMethodSignature*)methodSignatureForSelector:(SEL)selector classOf:(NSObject*)object
{
    return [[object class] methodSignatureForSelector:selector];
}

+ (Class)classOf:(NSObject*)value
{
    return [value class];
}

/* copying */
+ (id)copyObject:(NSObject<NSCopying>*)object withZone:(NSZone*)zone
{
    return [[object copyWithZone:zone] autorelease];
}

+ (id)copyObject:(NSObject<NSCopying>*)object
{
    return [object copy];
}

+ (NSString*)descriptionOf:(NSObject*)object
{
    return [object description];
}

+ (id)valueForKey:(NSString*)key of:(NSObject*)object
{
    return [object valueForKey:key];
}

+ (id)valueForKeyPath:(NSString*)keypath of:(NSObject*)object
{
    return [object valueForKeyPath:keypath];
}

+ (void)setValue:(id)value forKey:(NSString*)key of:(NSObject*)object
{
    [object setValue:value forKey:key];
}

+ (void)setValue:(id)value forKeyPath:(NSString*)keypath of:(NSObject*)object
{
    [object setValue:value forKeyPath:keypath];
}

+ (void)setValuesForKeysWithDictionary:(NSDictionary*)dict of:(NSObject*)object
{
    [object setValuesForKeysWithDictionary:dict];
}

+ (NSUInteger)hashOf:(NSObject*)object
{
    return [object hash];
}

+ (bool)object:(NSObject*)first equalTo:(NSObject*)second
{
    return [first isEqual:second];
}

+ (NSComparisonResult)object:(NSObject*)first compareTo:(NSObject*)second
{
    return [first compare:second];
}

+ (id)replacementObjectForArchiver:(NSArchiver*)archiver of:(NSObject*)object
{
    return [object replacementObjectForArchiver:archiver];
}

+ (id)replacementObjectForKeyedArchiver:(NSKeyedArchiver*)archiver of:(NSObject*)object
{
    return [object replacementObjectForKeyedArchiver:archiver];
}

+ (Class)classForArchiverOf:(NSObject*)object
{
    return [object classForArchiver];
}

+ (Class)classForKeyedArchiverOf:(NSObject*)object
{
    return [object classForKeyedArchiver];
}

+ (Class)classForKeyedUnarchiverOf:(NSObject*)object
{
    return [[object class] classForKeyedUnarchiver];
}

+ (Class)classForCoderOf:(NSObject*)object
{
    return [object classForCoder];
}

+ (bool)isKindOfClass:(Class)aClass of:(NSObject*)value
{
    return [value isKindOfClass:aClass];
}

+ (NSArray*)classFallbacksForKeyedArchiverOf:(NSObject<NSCopying>*)object
{
    return [[object class] classFallbacksForKeyedArchiver];
}

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

+ (id)storedValueForKey:(NSString*)key of:(NSObject*)object
{
    return [object storedValueForKey:key];
}

+ (void)takeStoredValue:(id)value forKey:(NSString*)key of:(NSObject*)object
{
    return [object takeStoredValue:value forKey:key];
}

+ (void)takeValue:(id)value forKey:(NSString*)key of:(NSObject*)object
{
    return [object takeValue:value forKey:key];
}

+ (void)takeValue:(id)value forKeyPath:(NSString*)keypath of:(NSObject*)object
{
    return [object takeValue:value forKeyPath:keypath];
}

+ (NSDictionary*)valuesForKeys:(NSArray*)keys of:(NSObject*)object
{
    return [object valuesForKeys:keys];
}

+ (void)takeValuesFromDictionary:(NSDictionary*)dict of:(NSObject*)object
{
    [object takeValuesFromDictionary:dict];
}

+ (id)replacementObjectForPortCoder:(NSPortCoder*)coder of:(NSObject*)object
{
    return [object replacementObjectForPortCoder:coder];
}

+ (Class)classForPortCoderOf:(NSObject*)object
{
    return [object classForPortCoder];
}

+ (void)unableToSetNilForKey:(NSString*)key of:(NSObject*)object
{
    [object unableToSetNilForKey:key];
}

+ (void)handleQueryWithUnboundKey:(NSString*)key of:(NSObject*)object
{
    [object handleQueryWithUnboundKey:key];
}

+ (void)valueForUndefinedKey:(NSString*)key of:(NSObject*)object
{
    [object valueForUndefinedKey:key];
}

+ (void)setValue:(id)value forUndefinedKey:(NSString*)key of:(NSObject*)object
{
    [object setValue:value forUndefinedKey:key];
}

#pragma clang diagnostic pop

/* XXX: Some private methods that need to be implemented to be compabitible
 * with NSObject
 */
+ (NSString*)copyDescriptionOf:(NSObject*)object
{
    return [object _copyDescription];
}

+ (bool)isNSArrayOf:(NSObject*)object
{
    return [object isNSArray__];
}

+ (bool)isNSDictionaryOf:(NSObject*)object
{
    return [object isNSDictionary__];
}

+ (bool)isNSSetOf:(NSObject*)object
{
    return [object isNSSet__];
}

+ (bool)isNSNumberOf:(NSObject*)object
{
    return [object isNSNumber__];
}

+ (bool)isNSDataOf:(NSObject*)object
{
    return [object isNSData__];
}

+ (bool)isNSDateOf:(NSObject*)object
{
    return [object isNSDate__];
}

+ (bool)isNSStringOf:(NSObject*)object
{
    return [object isNSString__];
}

+ (bool)isNSValueOf:(NSObject*)object
{
    return [object isNSValue__];
}

+ (CFTypeID)cfTypeIDOf:(NSObject*)object
{
    return CFGetTypeID((CFTypeRef)object);
}

+ (void)nosuchSelectorOf:(NSObject*)object
{
    [object nosuchSelector];
}

+ (void)voidSelectorOf:(NSObject*)object
{
    [object voidSelector];
}

+ (id)idSelectorOf:(NSObject*)object
{
    return [object idSelector];
}

+ (id)selectorWithArg:(id)arg1 andArg:(id)arg2 of:(NSObject*)object
{
    return [object selectorWithArg:arg1 andArg:arg2];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "objectint", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_objectint(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_objectint(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_ObjectInt", PyObjC_IdToPython([OC_ObjectInt class]))
        < 0) {
        return NULL;
    }

    return m;
}
