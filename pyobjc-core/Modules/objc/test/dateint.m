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

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_DateInt", PyObjC_IdToPython([OC_DateInt class]))
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
    .m_name     = "dateint",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_dateint(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_dateint(void)
{
    return PyModuleDef_Init(&mod_module);
}
