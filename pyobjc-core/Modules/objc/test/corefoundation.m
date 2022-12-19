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

static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "corefoundation",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit_corefoundation(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_corefoundation(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_TestCoreFoundation",
                           PyObjC_IdToPython([OC_TestCoreFoundation class]))
        < 0) {
        return NULL;
    }

    return m;
}
