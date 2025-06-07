/* Some testhelpers for CF-type support. */
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>
#import <Foundation/Foundation.h>

@interface OC_TestCoreFoundation : NSObject {
}
// not toll-free bridged.
+ (char*)signatureForCFUUIDRef;
+ (CFTypeID)typeidForCFUUIDRef;
+ (CFUUIDRef)createUUID;
+ (CFUUIDRef)createUUID;
+ (NSString*)formatUUID:(CFUUIDRef)uuid;
+ (NSString*)formatUUID2:(CFUUIDRef)uuid;
+ (NSObject*)anotherUUID;
+ (NSObject*)runloop;

// tollfree bridged:
+ (char*)signatureForCFDateRef;
+ (CFTypeID)typeidForCFDateRef;
+ (CFDateRef)today;
+ (NSString*)formatDate:(CFDateRef)date;
+ (int)shortStyle;
+ (int)noStyle;
@end

@implementation OC_TestCoreFoundation

+ (char*)signatureForCFUUIDRef
{
    return @encode(CFUUIDRef);
}

+ (CFTypeID)typeidForCFUUIDRef
{
    return CFUUIDGetTypeID();
}

+ (CFUUIDRef)createUUID
{
    CFUUIDRef result = CFUUIDCreate(NULL);

    /* We own a reference, but want to released a borrowed ref. */
    [(NSObject*)result retain];
    CFRelease(result);
    [(NSObject*)result autorelease];

    return result;
}

+ (NSObject*)anotherUUID
{
    CFUUIDRef result = CFUUIDCreate(NULL);

    /* We own a reference, but want to released a borrowed ref. */
    [(NSObject*)result autorelease];

    return (NSObject*)result;
}

+ (NSObject*)runloop
{
    return (NSObject*)CFRunLoopGetCurrent();
}

+ (NSString*)formatUUID:(CFUUIDRef)uuid
{
    NSString* result;

    result = (NSString*)CFUUIDCreateString(NULL, uuid);
    return [result autorelease];
}

+ (NSString*)formatUUID2:(CFUUIDRef)uuid
{
    NSString* result;

    result = (NSString*)CFUUIDCreateString(NULL, uuid);
    return [result autorelease];
}

+ (char*)signatureForCFDateRef
{
    return @encode(CFDateRef);
}

+ (CFTypeID)typeidForCFDateRef
{
    return CFDateGetTypeID();
}

+ (CFDateRef)today
{
    CFDateRef result;

    result = CFDateCreate(NULL, CFAbsoluteTimeGetCurrent());

    /* We own a reference, but want to released a borrowed ref. */
    [(NSDate*)result autorelease];

    return result;
}

+ (NSString*)formatDate:(CFDateRef)date
{
    CFLocaleRef        currentLocale = CFLocaleCopyCurrent();
    CFDateFormatterRef formatter     = CFDateFormatterCreate(
        NULL, currentLocale, kCFDateFormatterShortStyle, kCFDateFormatterNoStyle);

    if (currentLocale != NULL) {
        CFRelease(currentLocale);
    }

    NSString* result =
        (NSString*)CFDateFormatterCreateStringWithDate(NULL, formatter, date);

    CFRelease(formatter);
    return [result autorelease];
}

+ (int)shortStyle
{
    return kCFDateFormatterShortStyle;
}

+ (int)noStyle
{
    return kCFDateFormatterNoStyle;
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_TestCoreFoundation",
                           PyObjC_IdToPython([OC_TestCoreFoundation class]))
        < 0) {
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
    .m_name = "corefoundation",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_corefoundation(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_corefoundation(void)
{
    return PyModuleDef_Init(&mod_module);
}
