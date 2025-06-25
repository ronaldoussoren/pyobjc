#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface NSNumber ()
- (void)getValue:(void*)buffer forType:(const char*)type;
@end

@interface OC_NumberInt : NSObject {
}
+ (Class)numberClass:(NSNumber*)number;
+ (BOOL)numberAsBOOL:(NSNumber*)number;
+ (char)numberAsChar:(NSNumber*)number;
+ (short)numberAsShort:(NSNumber*)number;
+ (int)numberAsInt:(NSNumber*)number;
+ (long)numberAsLong:(NSNumber*)number;
+ (long long)numberAsLongLong:(NSNumber*)number;
+ (unsigned char)numberAsUnsignedChar:(NSNumber*)number;
+ (unsigned short)numberAsUnsignedShort:(NSNumber*)number;
+ (unsigned int)numberAsUnsignedInt:(NSNumber*)number;
+ (unsigned long)numberAsUnsignedLong:(NSNumber*)number;
+ (unsigned long long)numberAsUnsignedLongLong:(NSNumber*)number;
+ (NSDecimalNumber*)numberAsDecimal:(NSNumber*)number;
+ (float)numberAsFloat:(NSNumber*)number;
+ (double)numberAsDouble:(NSNumber*)number;

+ (const char*)objCTypeOf:(NSNumber*)number;
+ (NSComparisonResult)compareA:(NSNumber*)a andB:(NSNumber*)b;
+ (NSString*)numberDescription:(NSNumber*)number;
+ (NSString*)numberDescription:(NSNumber*)number withLocale:(id)aLocale;
+ (NSComparisonResult)compareA:(NSNumber*)a instanceOf:(Class)b;

+ (bool)number:(NSNumber*)left isEqualTo:(NSNumber*)right;
+ (bool)number:(NSNumber*)left isNotEqualTo:(NSNumber*)right;
+ (bool)number:(NSNumber*)left isGreaterThan:(NSNumber*)right;
+ (bool)number:(NSNumber*)left isGreaterThanOrEqualTo:(NSNumber*)right;
+ (bool)number:(NSNumber*)left isLessThan:(NSNumber*)right;
+ (bool)number:(NSNumber*)left isLessThanOrEqualTo:(NSNumber*)right;

+ (NSData*)getValueOf:(NSNumber*)value;
+ (NSData*)getValueOf:(NSNumber*)value forType:(char*)encoding;
@end

@implementation OC_NumberInt

+ (Class)numberClass:(NSNumber*)number
{
    return [number class];
}

+ (const char*)objCTypeOf:(NSNumber*)number
{
    return [number objCType];
}

+ (NSComparisonResult)compareA:(NSNumber*)a andB:(NSNumber*)b
{
    return [a compare:b];
}

+ (NSComparisonResult)compareA:(NSNumber*)a instanceOf:(Class)b
{
    id                 value  = [[b alloc] init];
    NSComparisonResult result = [a compare:value];
    [value release];
    return result;
}

+ (BOOL)number:(NSNumber*)a isEqualToValue:(NSNumber*)b
{
    return [a isEqualToValue:b];
}

+ (NSString*)numberDescription:(NSNumber*)number
{
    return [number description];
}

+ (NSString*)numberAsString:(NSNumber*)number
{
    return [number stringValue];
}

+ (NSString*)numberDescription:(NSNumber*)number withLocale:(id)aLocale
{
    return [number descriptionWithLocale:aLocale];
}

+ (BOOL)numberAsBOOL:(NSNumber*)number
{
    return [number boolValue];
}

+ (char)numberAsChar:(NSNumber*)number
{
    return [number charValue];
}

+ (short)numberAsShort:(NSNumber*)number
{
    return [number shortValue];
}

+ (int)numberAsInt:(NSNumber*)number
{
    return [number intValue];
}

+ (NSInteger)numberAsInteger:(NSNumber*)number
{
    return [number integerValue];
}

+ (NSUInteger)numberAsUnsignedInteger:(NSNumber*)number
{
    return [number unsignedIntegerValue];
}

+ (long)numberAsLong:(NSNumber*)number
{
    return [number longValue];
}

+ (long long)numberAsLongLong:(NSNumber*)number
{
    return [number longLongValue];
}

+ (unsigned char)numberAsUnsignedChar:(NSNumber*)number
{
    return [number unsignedCharValue];
}

+ (unsigned short)numberAsUnsignedShort:(NSNumber*)number
{
    return [number unsignedShortValue];
}

+ (unsigned int)numberAsUnsignedInt:(NSNumber*)number
{
    return [number unsignedIntValue];
}

+ (unsigned long)numberAsUnsignedLong:(NSNumber*)number
{
    return [number unsignedLongValue];
}

+ (unsigned long long)numberAsUnsignedLongLong:(NSNumber*)number
{
    return [number unsignedLongLongValue];
}

+ (NSDecimalNumber*)numberAsDecimal:(NSNumber*)number
{
    return [NSDecimalNumber decimalNumberWithDecimal:[number decimalValue]];
}

+ (float)numberAsFloat:(NSNumber*)number
{
    return [number floatValue];
}

+ (double)numberAsDouble:(NSNumber*)number
{
    return [number doubleValue];
}

+ (bool)number:(NSNumber*)a isEqualTo:(NSNumber*)b
{
    return [a isEqualToNumber:b];
}
+ (bool)number:(NSNumber*)a isEqualToInstanceOf:(Class)b
{
    id   value  = [[b alloc] init];
    BOOL result = [a isEqualTo:value];
    [value release];
    return result;
}

+ (bool)number:(NSNumber*)left isNotEqualTo:(NSNumber*)right
{
    return [left isNotEqualTo:right];
}
+ (BOOL)number:(NSNumber*)a isNotEqualToInstanceOf:(Class)b
{
    id   value  = [[b alloc] init];
    BOOL result = [a isNotEqualTo:value];
    [value release];
    return result;
}

+ (bool)number:(NSNumber*)left isGreaterThan:(NSNumber*)right
{
    return [left isGreaterThan:right];
}
+ (BOOL)number:(NSNumber*)a isGreaterThanInstanceOf:(Class)b
{
    id   value  = [[b alloc] init];
    BOOL result = [a isGreaterThan:value];
    [value release];
    return result;
}

+ (bool)number:(NSNumber*)left isGreaterThanOrEqualTo:(NSNumber*)right
{
    return [left isGreaterThanOrEqualTo:right];
}
+ (BOOL)number:(NSNumber*)a isGreaterThanOrEqualToInstanceOf:(Class)b
{
    id   value  = [[b alloc] init];
    BOOL result = [a isGreaterThanOrEqualTo:value];
    [value release];
    return result;
}

+ (bool)number:(NSNumber*)left isLessThan:(NSNumber*)right
{
    return [left isLessThan:right];
}
+ (BOOL)number:(NSNumber*)a isLessThanInstanceOf:(Class)b
{
    id   value  = [[b alloc] init];
    BOOL result = [a isLessThan:value];
    [value release];
    return result;
}

+ (bool)number:(NSNumber*)left isLessThanOrEqualTo:(NSNumber*)right
{
    return [left isLessThanOrEqualTo:right];
}
+ (BOOL)number:(NSNumber*)a isLessThanOrEqualToInstanceOf:(Class)b
{
    id   value  = [[b alloc] init];
    BOOL result = [a isLessThanOrEqualTo:value];
    [value release];
    return result;
}

+ (NSData*)getValueOf:(NSNumber*)value
{
    char buffer[32];
    [value getValue:buffer];
    return [NSData dataWithBytes:buffer length:32];
}

+ (NSData*)getValueOf:(NSNumber*)value forType:(char*)encoding
{
    char buffer[32];
    [value getValue:buffer forType:encoding];
    return [NSData dataWithBytes:buffer length:32];
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
                           "OC_NumberInt", PyObjC_IdToPython([OC_NumberInt class]))
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
    .m_name     = "pythonnumber",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_pythonnumber(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_pythonnumber(void)
{
    return PyModuleDef_Init(&mod_module);
}
