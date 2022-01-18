#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_DateInt : NSObject {
}
@end

@implementation OC_DateInt
+ (NSTimeInterval)timeIntervalSinceReferenceDateFor:(NSDate*)date
{
    return [date timeIntervalSinceReferenceDate];
}

+ (NSTimeInterval)timeIntervalSince1970For:(NSDate*)date
{
    return [date timeIntervalSince1970];
}

+ (NSTimeInterval)timeIntervalSinceNowFor:(NSDate*)date
{
    return [date timeIntervalSinceNow];
}

+ (NSDate*)date:(NSDate*)date byAddingInterval:(NSTimeInterval)seconds
{
    return [date dateByAddingTimeInterval:seconds];
}

+ (NSComparisonResult)compare:(NSDate*)first and:(NSDate*)second
{
    return [first compare:second];
}

+ (NSDate*)earlierOf:(NSDate*)first and:(NSDate*)second
{
    return [first earlierDate:second];
}

+ (NSDate*)laterOf:(NSDate*)first and:(NSDate*)second
{
    return [first laterDate:second];
}

+ (BOOL)date:(NSDate*)first equalToDate:(NSDate*)second
{
    return [first isEqualToDate:second];
}

+ (NSString*)descriptionFor:(NSDate*)date
{
    return [date description];
}

+ (NSString*)descriptionFor:(NSDate*)date withLocale:(NSLocale*)locale
{
    return [date descriptionWithLocale:locale];
}

/* Deprecated methods used by current implementation */

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

+ (id)date2:(NSDate*)date byAddingInterval:(NSTimeInterval)seconds
{
    return [date addTimeInterval:seconds];
}

+ (NSCalendarDate*)date:(NSDate*)date
    dateWithCalendarFormat:(NSString*)format
                  timeZone:(NSTimeZone*)zone
{
    return [date dateWithCalendarFormat:format timeZone:zone];
}

+ (NSString*)date:(NSDate*)date
    descriptionWithCalendarFormat:(NSString*)formatString
                         timeZone:(NSTimeZone*)aTimeZone
                           locale:(NSLocale*)locale
{
    return [date descriptionWithCalendarFormat:formatString
                                      timeZone:aTimeZone
                                        locale:locale];
}

#pragma clang diagnostic pop

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "dateint", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_dateint(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_dateint(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_DateInt", PyObjC_IdToPython([OC_DateInt class])) < 0) {
        return NULL;
    }

    return m;
}
