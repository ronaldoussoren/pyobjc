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
- (PyObject* _Nullable)__pyobjc_PythonObject__;
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
    return [object copyWithZone:zone];
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

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

+ (id)replacementObjectForArchiver:(NSArchiver*)archiver of:(NSObject*)object
{
    return [object replacementObjectForArchiver:archiver];
}

+ (id)replacementObjectForKeyedArchiver:(NSKeyedArchiver*)archiver of:(NSObject*)object
{
    return [object replacementObjectForKeyedArchiver:archiver];
}

#pragma clang diagnostic pop

+ (id)replacementObjectForCoder:(NSCoder*)archiver of:(NSObject*)object
{
    return [object replacementObjectForCoder:archiver];
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
    [object takeStoredValue:value forKey:key];
}

+ (void)takeValue:(id)value forKey:(NSString*)key of:(NSObject*)object
{
    [object takeValue:value forKey:key];
}

+ (void)takeValue:(id)value forKeyPath:(NSString*)keypath of:(NSObject*)object
{
    [object takeValue:value forKeyPath:keypath];
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

+ (CFTypeID)directCfTypeIDOf:(NSObject*)object
{
    return [object _cfTypeID];
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

+ (Class)invokeClassForCoderOf:(NSObject*)object
{
    Class              result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(classForCoder)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(classForCoder);

    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (Class)invokeClassForPortCoderOf:(NSObject*)object
{
    Class              result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(classForPortCoder)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(classForPortCoder);

    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (Class)invokeClassForArchiverOf:(NSObject*)object
{
    Class              result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(classForArchiver)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(classForArchiver);

    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (Class)invokeClassForKeyedArchiverOf:(NSObject*)object
{
    Class              result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(classForKeyedArchiver)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(classForKeyedArchiver);

    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (NSObject*)invokeReplacementObjectForCoder:(id)arg of:(NSObject*)object
{
    NSObject*          result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(replacementObjectForCoder:)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(replacementObjectForCoder:);
    [inv setArgument:&arg atIndex:2];

    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (NSObject*)invokeReplacementObjectForPortCoder:(id)arg of:(NSObject*)object
{
    NSObject*          result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(replacementObjectForPortCoder:)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(replacementObjectForPortCoder:);
    [inv setArgument:&arg atIndex:2];

    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (NSObject*)invokeReplacementObjectForArchiver:(id)arg of:(NSObject*)object
{
    NSObject*          result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(replacementObjectForArchiver:)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(replacementObjectForArchiver:);
    [inv setArgument:&arg atIndex:2];

    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (NSObject*)invokeReplacementObjectForKeyedArchiver:(id)arg of:(NSObject*)object
{
    NSObject*          result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(replacementObjectForKeyedArchiver:)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(replacementObjectForKeyedArchiver:);
    [inv setArgument:&arg atIndex:2];

    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (NSObject*)invokeDescriptionOf:(NSObject*)object
{
    NSObject*          result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(description)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(description);

    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (NSObject*)invokeCopyDescriptionOf:(NSObject*)object
{
    NSObject*          result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(_copyDescription)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(_copyDescription);
    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (NSObject*)invokeCopyOf:(NSObject*)object
{
    NSObject*          result;
    NSMethodSignature* signature = [object methodSignatureForSelector:@selector(copy)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(copy);
    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (NSObject*)invokeCopyWithZoneOf:(NSObject*)object
{
    NSObject*          result;
    NSZone*            zone = nil;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(copyWithZone:)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(copyWithZone:);
    [inv setArgument:&zone atIndex:2];
    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (void)invokeDoesNotRecognizeSelector:(SEL)selector of:(NSObject*)object
{
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(doesNotRecognizeSelector:)];
    if (signature == nil) {
        return;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return;
    }
    inv.target   = object;
    inv.selector = @selector(doesNotRecognizeSelector:);
    [inv setArgument:&selector atIndex:2];
    [object forwardInvocation:inv];
}

+ (NSObject*)invokeMethodSignatureForSelector:(SEL)selector of:(NSObject*)object
{
    NSObject*          result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(methodSignatureForSelector:)];
    if (signature == nil) {
        return nil;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return nil;
    }
    inv.target   = object;
    inv.selector = @selector(methodSignatureForSelector:);
    [inv setArgument:&selector atIndex:2];
    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (NSUInteger)invokeHashOf:(NSObject*)object
{
    NSUInteger         result;
    NSMethodSignature* signature = [object methodSignatureForSelector:@selector(hash)];
    if (signature == nil) {
        return 0;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return 0;
    }
    inv.target   = object;
    inv.selector = @selector(hash);
    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (bool)invokeRespondsToSelector:(SEL)sel of:(NSObject*)object
{
    BOOL               result;
    NSMethodSignature* signature =
        [object methodSignatureForSelector:@selector(respondsToSelector:)];
    if (signature == nil) {
        return 0;
    }
    NSInvocation* inv = [NSInvocation invocationWithMethodSignature:signature];
    if (inv == nil) {
        return 0;
    }
    inv.target   = object;
    inv.selector = @selector(respondsToSelector:);
    [inv setArgument:&sel atIndex:2];
    [object forwardInvocation:inv];
    [inv getReturnValue:&result];
    return result;
}

+ (bool)useStoredAccessorForClassOf:(NSObject*)object
{
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
    return [[object class] useStoredAccessor];
#pragma clang diagnostic pop
}

+ (bool)accessInstanceVariablesDirectlyForClassOf:(NSObject*)object
{
    return [[object class] accessInstanceVariablesDirectly];
}

@end

@interface OC_NoPythonRepresentation : NSObject <NSCopying>
/*
 * Helper class that can be used to test error paths
 * in creating a proxy for an ObjC object.
 */
{
    bool _allowPython;
}
@end

@implementation OC_NoPythonRepresentation
- (instancetype _Nullable)init
{
    self = [super init];
    if (!self)
        return nil;

    _allowPython = false;
    return self;
}

- (instancetype)copyWithZone:(NSZone*)__attribute__((__unused__))zone
{
    return [self retain];
}

- (instancetype)copy
{
    return [self retain];
}

- (instancetype _Nullable)initAllowPython:(bool)allowPython
{
    self = [super init];
    if (!self)
        return nil;

    _allowPython = allowPython;
    return self;
}

- (void)setAllowPython:(bool)allow
{
    _allowPython = allow;
}
- (bool)allowPython
{
    return _allowPython;
}
- (PyObject* _Nullable)__pyobjc_PythonObject__
{
    if (_allowPython) {
        return [super __pyobjc_PythonObject__];
    } else {
        PyErr_SetString(PyExc_ValueError, "cannot have Python representation");
        return NULL;
    }
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

    if (PyModule_AddObject(m, "OC_NoPythonRepresentation",
                           PyObjC_IdToPython([OC_NoPythonRepresentation class]))
        < 0) {
        return NULL;
    }

    return m;
}
